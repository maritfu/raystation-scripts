# encoding: utf8
#!/usr/bin/python

# Import system libraries:
from connect import *
import clr, sys, os
from tkinter import *
from tkinter import messagebox
import math


# Import local files:
import beams as BEAMS
import beam_set_functions as BSF
import case_functions as CF
import clinical_goal as CG
import fractionation_frame as FORM
#import general_functions as GF
import gui_functions as GUIF
import margin as MARGIN
import objective_functions as OBJF
import patient_model_functions as PMF
import plan_functions as PF
import region_codes as RC
import region_list as REGIONS
import roi as ROI
import roi_functions as ROIF
import rois as ROIS
import site_functions as SF
import structure_set_functions as SSF
import ts_case as TS_C
import raystation_utilities as RSU


class Plan(object):
  def __init__(self, clinic_db, patient_db, patient, case):
    self.clinic_db = clinic_db
    self.patient_db = patient_db
    self.patient = patient
    self.case = case


    # Load patient model, examination and structure set:
    pm = case.PatientModel
    examination = get_current("Examination")
    ss = PMF.get_structure_set(pm, examination)


    # Determine if a target volume is present (raises error if not):
    if not PMF.has_defined_ctv_or_ptv(pm, examination):
      GUIF.handle_missing_ctv_or_ptv()


    # Check if the last CT has been set as primary, and display a warning if not.
    #success = TS_C.TSCase(case).last_examination_used_test()
    #if not success:
    #  GUIF.handle_primary_is_not_most_recent_ct()


    # Setup and run GUI:
    my_window = Tk()
    (region_code, fraction_dose, nr_fractions, initials, total_dose) = GUIF.collect_fractionation_choices(my_window)


    # Load list of region codes and corresponding region names and get the region name for our particular region code (raise error if a name is not retrieved):
    regions = REGIONS.RegionList("C:\\temp\\raystation-scripts\\settings\\regions.tsv")
    region_text = regions.get_text(region_code)
    assert region_text != None


    # For SBRT brain or lung, if there are multiple targets, an extra form appear where
    # the user has to type region code of the other targets.
    # FIXME: Bruke funksjon for test fx?
    # FIXME: Vurder hvor denne koden bør ligge.
    target = None
    palliative_choices = None
    nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
    if nr_targets > 1:
      if region_code in RC.palliative_codes:
        # For palliative cases with multiple targets:
        palliative_choices = GUIF.palliative_beamset_form(ss, Toplevel())
        if palliative_choices[0] in ['sep_beamset_iso', 'sep_beamset_sep_iso']:
          region_codes = GUIF.multiple_beamset_form(ss, Toplevel())
          GUIF.check_region_codes(region_code, region_codes)
          if SSF.has_roi_with_shape(ss, ROIS.ctv1.name):
            target = ROIS.ctv1.name
          elif SSF.has_roi_with_shape(ss, ROIS.ctv2.name):
            target = ROIS.ctv2.name
          elif SSF.has_roi_with_shape(ss, ROIS.ctv3.name):
            target = ROIS.ctv3.name
          elif SSF.has_roi_with_shape(ss, ROIS.ctv4.name):
            target = ROIS.ctv4.name
        elif palliative_choices[0] == 'sep_plan':
          target = palliative_choices[1]


    # Set up plan, making sure the plan name does not already exist. If the plan name exists, (1), (2), (3) etc is added behind the name.
    plan = CF.create_plan(case, examination, region_text)


    # Check that the number of fractions and fraction dose is among those expected for the given region code
    GUIF.check_input(ss, region_code, nr_fractions, fraction_dose)


    # Set planners initials
    plan.PlannedBy = initials


    # Set dose grid, 0.2x0.2x0.2 cm3 for stereotactic treatments and for prostate and 0.3x03x0.3 cm3 otherwise
    PF.set_dose_grid(plan, region_code, nr_fractions, fraction_dose)

    my_window = Toplevel()
    # Determine which technique and optimization choices which will appear in the form
    results = GUIF.determine_choices(region_code, nr_fractions, fraction_dose, my_window, [])
    # Chosen technique value, 'VMAT' or 'Conformal'
    technique = results[0]
    # Chosen technique name, 'VMAT' or '3D-CRT'
    technique_name = results[1]
    # Chosen optimization value
    opt = results[2]
    

    # Determine prescription target:
    if not target:
      roi_dict = SSF.create_roi_dict(ss)
      target = SSF.determine_target(ss, roi_dict, nr_fractions, fraction_dose)


    # Determine name of the body contour ('External' or 'Body'):
    external = SSF.body_roi_name(ss)
    if not external:
      GUIF.handle_missing_external()

    
    # Determine the machine name from the size of the target volume, only one target is taken into consideration here.
    # For those situations where you have two targets and you want to have separate isocenters, then you what to evaluate the targets separately.
    #if target in [ROIS.ctv1.name, ROIS.ctv2.name, ROIS.ctv3.name, ROIS.ctv4.name] and palliative_choices[0] in ['sep_beamset_sep_iso', 'sep_plan']:
      #energy_name = SSF.determine_energy_single_target(ss, target)
    #elif region_code in RC.breast_codes:
      #energy_name = '6'
    #else:
      # Determine the machine name from the size of the target volume:
      #energy_name = SSF.determine_energy(ss, target)
    energy_name = '6'
    if PF.is_stereotactic(nr_fractions, fraction_dose):
      machine_name = "Agility Trh FFF"
    else:
      machine_name = "Agility Trh"
    # Create the name of the beamset
    beam_set_name = BSF.label(region_code, fraction_dose, nr_fractions, technique)


    # Create primary beam set:
    beam_set = PF.create_beam_set(plan, beam_set_name, examination, technique, nr_fractions, machine_name = machine_name )
    # Add prescription:
    BSF.add_prescription(beam_set, nr_fractions, fraction_dose, target, region_code, technique_name)
    # Determine the point which will be our isocenter:
    if nr_targets > 1:
      if palliative_choices and palliative_choices[0] in ['sep_beamset_iso','beamset']:
        # Consider all targets when determining isocenter:
        isocenter = SSF.determine_isocenter(examination, ss, region_code, technique_name, target, external, multiple_targets = True)
      else:
        # Set isocenter for PTV1:
        isocenter = SSF.determine_isocenter(examination, ss, region_code, technique_name, target, external)
    else:
      # Consider all targets when determining isocenter:
      isocenter = SSF.determine_isocenter(examination, ss, region_code, technique_name, target, external, multiple_targets = True)
    # Setup beams or arcs
    nr_beams = BEAMS.setup_beams(ss, examination, beam_set, isocenter, region_code, fraction_dose, technique_name, energy_name)


    # For SBRT brain or lung, if there are multiple targets, create beam sets for all targets
    # FIXME: Bruke funksjon for test fx?
    if nr_targets > 1:
      if region_code in RC.palliative_codes:
        # Palliative cases with multiple targets:
        if palliative_choices[0] in ['sep_beamset_iso', 'sep_beamset_sep_iso']:
          if palliative_choices[0] == 'sep_beamset_iso':
            PF.create_additional_palliative_beamsets_prescriptions_and_beams(plan, examination, ss, region_codes, fraction_dose, nr_fractions, external, energy_name, nr_existing_beams = nr_beams, isocenter = isocenter)
          else:
            PF.create_additional_palliative_beamsets_prescriptions_and_beams(plan, examination, ss, region_codes, fraction_dose, nr_fractions, external, energy_name, nr_existing_beams = nr_beams)


    # If there is a 2Gy x 8 boost for breast patients
    #if SSF.has_roi_with_shape(ss, ROIS.ctv_sb.name) and SSF.has_roi_with_shape(ss, ROIS.ptv_c.name) and region_code in RC.breast_codes:
    #  PF.create_breast_boost_beamset(ss, plan, examination, isocenter, region_code, ROIS.ctv_sb.name, background_dose=int(round(fraction_dose*nr_fractions)))
    #  # Make sure that the original beam set (not this boost beam set) is loaded in the GUI:
    #  infos = plan.QueryBeamSetInfo(Filter={'Name':'^'+beam_set_name+'$'})
    #  plan.LoadBeamSet( BeamSetInfo=infos[0])


    # Determines and sets up isodoses based on region code and fractionation
    CF.determine_isodoses(case, ss, region_code, nr_fractions, fraction_dose)

    if region_code in RC.head_neck_codes:
      max_del_time = 150
      max_arc_mu = fraction_dose*200
      PMF.create_external_outside_density_volume(case, pm, ss, examination, ROIS.x_external, ROIS.external, ROIS.x_tetthetsvolum)
      PMF.set_material(patient_db, case, pm, ss, examination,  ROIS.x_tetthetsvolum, 'Water')
      
    elif region_code in RC.breast_codes:
      PMF.create_oars_for_breast(pm, examination,ss, region_code)
      if region_code in RC.breast_reg_codes:
        if technique_name == 'VMAT':
          new_examination_name = "CT-Robust"
          CF.export_and_import_ct_study(clinic_db, patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
          CF.compute_rigid_image_registration(case, examination, new_examination_name)
          OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])   
          PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, new_examination_name, ROIS.z_match,ROIS.x_tetthetsvolum,'Water')
          PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, ROIS.x_tetthetsvolum)
          PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case,pm,new_examination_name, region_code)
          PMF.set_up_volumes_for_breast_robust_optimization(case,pm,examination,ss, region_code)
          max_arc_mu = 650
          max_del_time = 150
          size = 0.3
          plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
          PF.expand_dose_grid(plan, expand_y=4)
        else:
          max_arc_mu = 40
          max_del_time = 20
          PMF.create_ptv_caudal_and_craniel(pm, examination, ss, isocenter, ROIS.x_ptv, ROIS.box, ROIS.x_ptv_cran,ROIS.x_ptv_caud)
          PMF.create_match_volume(pm, ss, examination, ROIS.z_match, ROIS.x_ptv_cran, ROIS.body)
          PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, examination.Name, ROIS.z_match, ROIS.x_tetthetsvolum, 'Water')
          PMF.create_external_outside_density_volume(case, pm, ss,examination,ROIS.x_external,ROIS.external, ROIS.x_tetthetsvolum)
          size = 0.3
          plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
          PF.expand_dose_grid(plan, expand_y=4)
        PMF.create_ctv_L2_L4_and_external(pm, examination, ss, [ROIS.level3_l,ROIS.level4_l], ROIS.body, ROIS.box1, ROIS.x_ctv_n_ring)
        PMF.exclude_rois_from_export(pm)
        PMF.set_all_undefined_to_organ_type_other(pm)
      elif region_code in RC.breast_tang_codes:
        if technique_name == 'VMAT':
          new_examination_name = "CT-Robust"
          CF.export_and_import_ct_study(clinic_db,patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
          CF.compute_rigid_image_registration(case, examination, new_examination_name)
          OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])   
          PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, new_examination_name, ROIS.z_match,ROIS.x_tetthetsvolum,'Water')
          PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, ROIS.x_tetthetsvolum)
          PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case,pm,new_examination_name, region_code)
          PMF.set_up_volumes_for_breast_robust_optimization(case,pm,examination,ss, region_code)
          max_arc_mu = 250
          max_del_time = 50
        else:
          max_arc_mu = 50
          max_del_time = 20
        size = 0.3
        plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
        PF.expand_dose_grid(plan, expand_y=4)
    else:
      max_arc_mu = fraction_dose*200
      max_del_time = 150
    


    if region_code in RC.breast_codes and technique == 'Conformal':
      second_beam_set_name = PF.create_breast_hybrid_vmat_beamset(ss, plan, examination, isocenter, region_code, target, beam_set_name,technique_name)
      if region_code in RC.breast_reg_codes: 
        BSF.set_up_beams_for_regional_breast(plan, beam_set, ROIS.x_ptv.name, region_code)
      elif region_code in RC.breast_tang_codes:
        BSF.set_up_beams_for_tangential_breast(plan, beam_set, ROIS.ptv_pc.name)
      #messagebox.showinfo("","")
      beam_set.ComputeDose(DoseAlgorithm = 'CCDose')

    # Determine site
    site = SF.site(pm, examination, ss, plan, nr_fractions, total_dose, region_code, target, technique_name)

    #if region_code in RC.breast_reg_codes:
    #  if SSF.has_named_roi_with_contours(ss, ROIS.external.name):
    #    ss.SimplifyContours(RoiNames = [ROIS.external.name], RemoveHoles3D = True, RemoveSmallContours = True, AreaThreshold = 1)
    #messagebox.showinfo("","")
    # Set up Clinical Goals:
    es = plan.TreatmentCourse.EvaluationSetup
    CG.setup_clinical_goals(ss, es, site, total_dose, nr_fractions, target)
    # Loads the plan, done after beam set is created, as this is the only way the CT-images appears in Plan Design and Plan Optimization when the plan is loaded
    patient.Save()
    CF.load_plan(case, plan)
      
    for beam_set in plan.BeamSets:
      for beam in beam_set.Beams:
        if beam.DeliveryTechnique != 'SMLC':
          #messagebox.showinfo("",beam.Name)
          beam_s = RSU.beam_settings(plan, beam_set, beam)
          beam_s.ArcConversionPropertiesPerBeam.FinalArcGantrySpacing = 2
          if beam_s.ForBeam.Name in ['109-350','10-257']:
            beam_s.EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt","SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Use limits as max", TopJaw = 0)

          if beam.Name in ['109-350','10-257']:
            max_arc_mu = 200
            max_del_time = 50
          elif beam.Name in ['45-10','257-222','139-109','350-320']:
            max_arc_mu = 40
            max_del_time = 20
          beam_s.ArcConversionPropertiesPerBeam.MaxArcMU = max_arc_mu
          beam_s.ArcConversionPropertiesPerBeam.MaxArcDeliveryTime = max_del_time
    
    # Run first optimization on each beam set:
    for po in plan.PlanOptimizations:
      po.OptimizationParameters.DoseCalculation.ComputeIntermediateDose = True
      po.OptimizationParameters.DoseCalculation.ComputeFinalDose = True
      #po.RunOptimization()
      if po.OptimizationParameters.TreatmentSetupSettings[0].ForTreatmentSetup.DeliveryTechnique != 'SMLC':
        acp = po.OptimizationParameters.TreatmentSetupSettings[0].SegmentConversion.ArcConversionProperties
        acp.UseMaxLeafTravelDistancePerDegree = True
        acp.MaxLeafTravelDistancePerDegree = 2
        acp.UseSlidingWindowSequencing = True
        CF.load_plan(case, plan)
        po.RunOptimization()
    #  # Set 'Constrain leaf motion' to 0.3 for stereotactic patients
    #  #if PF.is_stereotactic(nr_fractions, fraction_dose):
    #  acp = po.OptimizationParameters.TreatmentSetupSettings[0].SegmentConversion.ArcConversionProperties
    #  acp.UseMaxLeafTravelDistancePerDegree = True
    #  acp.MaxLeafTravelDistancePerDegree = 0.5
    #  po.RunOptimization()
    CF.load_plan(case, plan)

    # Start adaptive optimization if indicated 
    if opt == 'oar':
      OBJF.adapt_optimization_oar(ss, plan, site.oar_objectives, region_code)
    for beam_set in plan.BeamSets:
      if region_code in RC.breast_codes:
        if region_code in RC.breast_reg_codes:
          # Need to close leafs behind jaw for breast regional patients 
          BSF.close_leaves_behind_jaw_for_regional_breast(beam_set)
          PMF.set_roi_type_to_other(pm, ss, ROIS.x_ptv)
          PMF.exclude_roi_from_export(pm, ROIS.x_ptv.name)
        # # Create 2.5 cm margin to air for breast patient planned with a 3D-CRT technique for robustness purpuses
        BSF.create_margin_air_for_3dcrt_breast(ss, beam_set, region_code)
        # Compute dose
        beam_set.ComputeDose(DoseAlgorithm = 'CCDose')
      #Auto scale to prescription
    #for po in plan.PlanOptimizations:
      #po.AutoScaleToPrescription = True
    #Load plan
    CF.load_plan(case, plan)



    # Save
    patient.Save()


