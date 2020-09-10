# encoding: utf8

# Import system libraries:
from connect import *
import clr, sys, os
from tkinter import *
from tkinter import messagebox

# Import local files:
import def_choices as DC
import def_site as DS
import gui_functions as GUIF
import patient_model_functions as PMF
import radio_button as RB
import roi_functions as ROIF
import structure_set_functions as SSF
import ts_case as TS_C
import ts_patient as TS_P
import rois as ROIS


class Definition(object):
  def __init__(self, patient_db, patient, case):
    self.patient_db = patient_db
    self.patient = patient
    self.case = case

    #messagebox.showinfo("Error.","hei")
    pm = case.PatientModel
    examination = get_current("Examination")
    ss = PMF.get_structure_set(pm, examination)

    # Check if the last CT has been set as primary, and display a warning if not.
    #success = TS_C.TSCase(case).last_examination_used_test()
    #if not success:
    #  GUIF.handle_primary_is_not_most_recent_ct()

    # Check if any ROIs exist, and if they have a contour in the current Structure Set.
    # If there is, ask to delete rois.
    if SSF.has_roi_with_contours(ss):
      delete = RB.RadioButton('Eksisterende ROIs oppdaget', 'Velg:', DC.delete)
      my_window = Tk()
      choice_d=[]
      delete_choice = GUIF.collect_delete_choice(delete, my_window, choice_d)
      for i in range(len(delete_choice)):
        # If the delete all rois choice was selected, delete rois.
        if delete_choice[i] == 'yes':
          PMF.delete_all_rois(pm)
        elif delete_choice[i] == 'some':
          PMF.delete_rois_except_manually_contoured(pm, ss)
      my_window = Toplevel()
    else:
      my_window = Tk()
      
      


    # Create initial radiobutton object, then recursively iterate it to collect all user choices:
    regions = RB.RadioButton('Behandlingsregion', 'Velg behandlingsregion:', DC.regions)

    choices = GUIF.collect_choices(regions, my_window, [])

    # Create site:
    site = DS.DefSite(patient_db, pm, examination, ss, choices, targets = [], oars = [])
    

    # Choice 1: Which region is going to be treated?
    region = choices[0]
    #if region == "breast":
    #  PMF.create_external_fripust(case, pm, ["Fripust","fripust"], choices, ROIS.x_body_fripust)
    #  PMF.create_ctv_L2_L4_and_external(pm, examination, ss, [ROIS.level2_l,ROIS.level3_l,ROIS.level4_l], ROIS.body, ROIS.box1, ROIS.x_l2_l4)

    if region == 'brain':
      import def_brain as DEF_BRAIN
      DEF_BRAIN.DefBrain(pm, examination, ss, choices, site)
    elif region == 'head_neck':
      import def_head_neck as DEF_HEAD_NECK
      DEF_HEAD_NECK.DefHeadNeck(pm, examination, ss, choices, site)
    elif region == 'lung':
      import def_lung as DEF_LUNG
      DEF_LUNG.DefLung(pm, examination, ss, choices, site)
    elif region == 'breast':
      import def_breast as DEF_BREAST
      DEF_BREAST.DefBreast(pm, examination, ss, choices, site)
    elif region == 'bladder':
      import def_bladder as DEF_BLADDER
      DEF_BLADDER.DefBladder(pm, examination, ss, choices, site)
    elif region == 'gyn':
      import def_gyn as DEF_GYN
      DEF_GYN.DefGyn(pm, examination, ss, choices, site)
    elif region == 'prostate':
      import def_prostate as DEF_PROSTATE
      DEF_PROSTATE.DefProstate(pm, examination, ss, choices, site)
    elif region == 'gi':
      diag = choices[1]
      if diag =='rectum': 
        import def_rectum as DEF_RECTUM
        DEF_RECTUM.DefRectum(pm, examination, ss, choices, site)
      elif diag == 'anus':
        import def_anus as DEF_ANUS
        DEF_ANUS.DefAnus(pm, examination, ss, choices, site)
      elif diag == 'esophagus':
        import def_esophagus as DEF_ESOPHAGUS
        DEF_ESOPHAGUS.DefEsophagus(pm, examination, ss, choices, site)
    elif region == 'other':
      import def_palliative as DEF_PALLIATIVE
      DEF_PALLIATIVE.DefPalliative(pm, examination, ss, choices, site)


    # Changes OrganType to "Other" for all ROIs in the given patient model which are of type "Undefined" or "Marker".
    if region != "breast":
      PMF.exclude_rois_from_export(pm)
    elif region == "breast":
      PMF.create_external_fripust(case, pm, examination, ["Fripust","fripust"], choices, ROIS.x_body_fripust)

    if region == 'head_neck':
      examination_names = ['ønh','ØNH','Ønh']
      PMF.create_external_body_and_couch_geometry_for_specified_examination(case, pm, examination_names, ss)  
    #if region == 'head_neck':
    #PMF.set_material(pm, ss,'xTetthetsvolum', 'Water')
    #PMF.create_external_outside_density_volume(pm, examination, ss, ROIS.x_tetthetsvolum)
    #PMF.set_all_undefined_to_organ_type_other(pm)
    #elif region == 'breast':
    #  PMF.create_external_outside_density_volume(pm, examination, ss, ROIS.z_match)
    #  #PMF.set_material(pm, ss,'xMatchingTetthetsvolum', 'Water')
    #else:
    PMF.set_all_undefined_to_organ_type_other(pm)
    
    
