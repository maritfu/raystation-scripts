# encoding: utf8

# Import system libraries:
import math
from tkinter import *
from tkinter import messagebox
# Import local files:
import beam_functions as BF
import general_functions as GF
import objective_functions as OBJF
import plan_functions as PF
import region_codes as RC
import roi_functions as ROIF
import structure_set_functions as SSF
import colors as COLORS
import rois as ROIS

# Contains a collection of beam set functions.


# Set presciption (default is median dose, with dose at volume for stereotactic plans) HVA MED SKJELETTSTEREOTAKSI?
def add_prescription(beam_set, nr_fractions, fraction_dose, target, region_code, technique_name):
  total_dose = nr_fractions*fraction_dose
  if PF.is_stereotactic(nr_fractions, fraction_dose) and region_code in RC.brain_codes:
    beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'DoseAtVolume', DoseValue = total_dose*100, DoseVolume = 99)
  elif PF.is_stereotactic(nr_fractions, fraction_dose):
    beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'DoseAtVolume', DoseValue = total_dose*100, DoseVolume = 98)
  elif region_code in RC.breast_codes:
    if technique_name == 'VMAT':
      beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'MedianDose', DoseValue = total_dose*100)
    else:
      beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'NearMaximumDose', DoseValue = total_dose*100)
  elif region_code in RC.gyn_codes and total_dose > 50:
    beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'DoseAtVolume', DoseValue = total_dose*100, DoseVolume = 98)
  else:
    beam_set.AddDosePrescriptionToRoi(RoiName = target, PrescriptionType = 'MedianDose', DoseValue = total_dose*100)


# Creates two arcs, VMAT
def create_two_arcs(beam_set, isocenter, energy='6', gantry_stop_angle1='182', gantry_stop_angle2='178', gantry_start_angle1='178', gantry_start_angle2='182', collimator_angle1='5', collimator_angle2='355', couch_angle1='0', couch_angle2='0', iso_index=1, beam_index=1):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b1 = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle1,
    ArcRotationDirection = BF.rotation_direction(gantry_start_angle1, gantry_stop_angle1),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle1) + "-" + str(gantry_stop_angle1), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle1 ,
    CollimatorAngle = collimator_angle1,
    CouchRotationAngle = couch_angle1,
    CouchPitchAngle = couch_angle1,
    CouchRollAngle = couch_angle1 
  )
  b1.Number = beam_index
  b2 = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle2,
    ArcRotationDirection = BF.rotation_direction(gantry_start_angle2, gantry_stop_angle2),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle2) + "-" + str(gantry_stop_angle2), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle2,
    CollimatorAngle = collimator_angle2,
    CouchRotationAngle = couch_angle2,
    CouchPitchAngle = couch_angle2,
    CouchRollAngle = couch_angle2 
  )
  b2.Number = beam_index + 1



# Creates four beams, 3D-CRT
def create_four_beams(beam_set, isocenter, energy='6', gantry_angle1='182', gantry_angle2='178', gantry_angle3='182', gantry_angle4='178', collimator_angle1='0', collimator_angle2='0', collimator_angle3='0', collimator_angle4='0', couch_angle1='0', couch_angle2 = '0', couch_angle3 = '0', couch_angle4 = '0', iso_index = 1, beam_index=1):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b1 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle1),
    Description = '',
    GantryAngle = gantry_angle1 ,
    CollimatorAngle = collimator_angle1,
    CouchRotationAngle = couch_angle1,
    CouchPitchAngle = couch_angle1,
    CouchRollAngle = couch_angle1 
  )
  b1.Number = beam_index
  b2 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle2),
    Description = '',
    GantryAngle = gantry_angle2,
    CollimatorAngle = collimator_angle2,
    CouchRotationAngle = couch_angle2,
    CouchPitchAngle = couch_angle2,
    CouchRollAngle = couch_angle2 
  )
  b2.Number = beam_index + 1
  b3 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle3),
    Description = '',
    GantryAngle = gantry_angle3 ,
    CollimatorAngle = collimator_angle3,
    CouchRotationAngle = couch_angle3,
    CouchPitchAngle = couch_angle3,
    CouchRollAngle = couch_angle3 
  )
  b3.Number = beam_index + 2
  b4 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle4),
    Description = '',
    GantryAngle = gantry_angle4,
    CollimatorAngle = collimator_angle4,
    CouchRotationAngle = couch_angle4,
    CouchPitchAngle = couch_angle4,
    CouchRollAngle = couch_angle4 
  )
  b4.Number = beam_index + 3


# Adjusts leaf positions on the first segment of each beam for 3DCRT breast plans.
# Leafs (on anterior-lateral leaf bank) are pulled 2.5 cm out from their initial position.
# For locoregional plans, this is only done in the part of the field covering the breast.
def create_margin_air_for_3dcrt_breast(ss, beam_set, region_code):
  roi_dict = SSF.create_roi_dict(ss)
  for beam in beam_set.Beams:
    segment = beam.Segments[0]
    jaw = segment.JawPositions
    if beam.Name in ['45 seg','222 seg','139 seg','320 seg']:
      y2_iso = jaw[3] 
  for beam in beam_set.Beams:
    segment = beam.Segments[0]
    leaf_positions = segment.LeafPositions
    jaw = segment.JawPositions
    y1 = jaw[2]
    if region_code in RC.breast_reg_codes:
      if SSF.has_named_roi_with_contours(ss, ROIS.x_ptv_caud.name) and beam.Name in ['45','222','139','320']:
        breast = ss.RoiGeometries[ROIS.x_ptv_caud.name].GetBoundingBox()
        #y2 = jaw[3] - (breast[0].z-1)
        #y2 =  jaw[3] - (nodes[1].z - breast[1].z + 1)
        y2 = y2_iso
      elif SSF.has_named_roi_with_contours(ss, ROIS.x_ptv_caud.name) and beam.Name in ['45 seg','222 seg','139 seg','320 seg']:
        breast = ss.RoiGeometries[ROIS.x_ptv_caud.name].GetBoundingBox()
        y2 = jaw[3] 
      else:
        y2 = jaw[3]
    else:
      y2 = jaw[3]

    # don't forget that mlc 50 is index leafPositions[x][49]
    mlcY1 = int(math.floor((y1 + 20) * 2) + 1.0)
    mlcY2 = int(math.ceil ((y2 + 20) * 2))
    #['46','223','140','321']
    for leaf in range(mlcY1-1, mlcY2+1):
      if beam.Name in ['222','222 seg','320','320 seg','231','306']:#LEFT side
        leaf_positions[1][leaf] = leaf_positions[1][leaf] + 3
      elif beam.Name in ['45', '45 seg','139','139 seg','128','54']:
        leaf_positions[0][leaf] = leaf_positions[0][leaf] - 3

    segment.LeafPositions = leaf_positions


# Creates a single arc, VMAT
def create_single_arc(beam_set, isocenter, energy='6', gantry_stop_angle='182', gantry_start_angle='178', collimator_angle='5', couch_angle='0', iso_index = 1, beam_index=1):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle,
    ArcRotationDirection =BF.rotation_direction(gantry_start_angle, gantry_stop_angle),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle) + "-" + str(gantry_stop_angle), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle,
    CollimatorAngle = collimator_angle,
    CouchRotationAngle = couch_angle,
    CouchPitchAngle = couch_angle,
    CouchRollAngle = couch_angle 
  )
  b.Number = beam_index

# Creates two arcs, VMAT
def create_three_arcs(beam_set, isocenter, energy='6', gantry_stop_angle1='182', gantry_stop_angle2='178',gantry_stop_angle3='178', gantry_start_angle1='178', gantry_start_angle2='182', gantry_start_angle3='182', collimator_angle1='5', collimator_angle2='355', collimator_angle3='355', couch_angle1='0', couch_angle2='0',couch_angle3='0', iso_index=1, beam_index=1):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b1 = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle1,
    ArcRotationDirection = BF.rotation_direction(gantry_start_angle1, gantry_stop_angle1),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle1) + "-" + str(gantry_stop_angle1), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle1 ,
    CollimatorAngle = collimator_angle1,
    CouchRotationAngle = couch_angle1,
    CouchPitchAngle = couch_angle1,
    CouchRollAngle = couch_angle1 
  )
  b1.Number = beam_index
  b2 = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle2,
    ArcRotationDirection = BF.rotation_direction(gantry_start_angle2, gantry_stop_angle2),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle2) + "-" + str(gantry_stop_angle2), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle2,
    CollimatorAngle = collimator_angle2,
    CouchRotationAngle = couch_angle2,
    CouchPitchAngle = couch_angle2,
    CouchRollAngle = couch_angle2 
  )
  b2.Number = beam_index + 1

  b3 = beam_set.CreateArcBeam(
    ArcStopGantryAngle = gantry_stop_angle3,
    ArcRotationDirection = BF.rotation_direction(gantry_start_angle3, gantry_stop_angle3),
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_start_angle3) + "-" + str(gantry_stop_angle3), #TESTES
    Description = '',
    GantryAngle = gantry_start_angle3,
    CollimatorAngle = collimator_angle3,
    CouchRotationAngle = couch_angle3,
    CouchPitchAngle = couch_angle3,
    CouchRollAngle = couch_angle3 
  )
  b3.Number = beam_index + 2

# Creates three beams, 3D-CRT
def create_three_beams(beam_set, isocenter, energy='6', gantry_angle1='182', gantry_angle2='178', gantry_angle3='182', collimator_angle1='0', collimator_angle2='0', collimator_angle3='0', couch_angle1='0', couch_angle2 = '0', couch_angle3 = '0', iso_index = 1, beam_index=1):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b1 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle1),
    Description = '',
    GantryAngle = gantry_angle1 ,
    CollimatorAngle = collimator_angle1,
    CouchRotationAngle = couch_angle1,
    CouchPitchAngle = couch_angle1,
    CouchRollAngle = couch_angle1
  )
  b1.Number = beam_index
  b2 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle2),
    Description = '',
    GantryAngle = gantry_angle2,
    CollimatorAngle = collimator_angle2,
    CouchRotationAngle = couch_angle2,
    CouchPitchAngle = couch_angle2,
    CouchRollAngle = couch_angle2
  )
  b2.Number = beam_index + 1
  b3 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle3),
    Description = '',
    GantryAngle = gantry_angle3 ,
    CollimatorAngle = collimator_angle3,
    CouchRotationAngle = couch_angle3,
    CouchPitchAngle = couch_angle3,
    CouchRollAngle = couch_angle3 
  )
  b3.Number = beam_index + 2


# Creates two beams, 3D-CRT
def create_two_beams(beam_set, isocenter, energy='6', gantry_angle1='182', gantry_angle2='178', collimator_angle1='5', collimator_angle2='355', couch_angle1='0', couch_angle2='0', iso_index=1, beam_index=1,beam_index2=2):
  beam_set.ClearBeams(RemoveBeams = 'True')
  b1 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle1),
    Description = '',
    GantryAngle = gantry_angle1,
    CouchRotationAngle = couch_angle1,
    CouchPitchAngle = couch_angle1,
    CouchRollAngle = couch_angle1, 
    CollimatorAngle = collimator_angle1
  )
  b1.Number = beam_index
  b2 = beam_set.CreatePhotonBeam(
    BeamQualityId = energy,
    IsocenterData={ 'Position': { 'x': isocenter.x, 'y': isocenter.y, 'z': isocenter.z }, 'NameOfIsocenterToRef': "Iso"+str(iso_index), 'Name': "Iso"+str(iso_index), 'Color': COLORS.iso },
    Name= str(gantry_angle2),
    Description = '',
    GantryAngle = gantry_angle2,
    CouchRotationAngle = couch_angle2,
    CouchPitchAngle = couch_angle2,
    CouchRollAngle = couch_angle2,
    CollimatorAngle = collimator_angle2
  )
  b2.Number = beam_index2 


# Creates the label from region code, fraction dose, number of fractions and which technique (VMAT or 3D-CRT). Is used as beam set name.
def label(region_code, fraction_dose, nr_fractions, technique, background_dose=0):
  if technique == 'Conformal': # 3D-CRT
    if region_code in RC.breast_l_codes:
      technique = 'G'
    elif region_code in RC.breast_r_codes:
      technique ='M'
    t = ':' + str(background_dose) + '-'
  else:
    if PF.is_stereotactic(nr_fractions, fraction_dose):
      technique = 'S'
      t = ':' + str(background_dose) + '-' #Stereotactic
    else:
      technique = 'V'
      t = ':' + str(background_dose) + '-' #VMAT
  return technique + str(region_code) + t + GF.dynamic_round(background_dose + round(fraction_dose*nr_fractions,2)) + ':' + str(nr_fractions)


# Creates the label from region code, fraction dose, number of fractions and which technique (VMAT or 3D-CRT).
# Is used as beam set name for the addition beam sets for stereotactic brain with multiple targets
def label_s(region_code, fraction_dose, nr_fractions):
  technique = 'S'
  t = ':0-'
  return technique + str(region_code) + t + GF.dynamic_round(fraction_dose*nr_fractions) + ':' + str(nr_fractions)


# Sets the monitor units of the beams in a beam set based on a list of names and monitor units.
def set_MU(beam_set, names, mu):
  for i in range(len(names)):
    beam_set.Beams[names[i]].BeamMU = mu[i]

def set_up_treat_and_protect_for_stereotactic_lung(beam_set, protect_roi, margin):
    beam_set.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = protect_roi)
    for beam in beam_set.Beams:
        beam.SetTreatAndProtectMarginsForBeam(TopMargin = margin, BottomMargin = margin, LeftMargin = margin, RightMargin = margin, Roi = protect_roi)
    #beam_set.TreatAndProtect(ShowProgress=True)
		
def set_up_beams_and_optimization_for_tangential_breast(plan, beam_set, plan_optimization, protect_roi):
	beam_set.SetTreatmentTechnique(Technique = 'Conformal')
	beam_set.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = protect_roi)
	for beam in beam_set.Beams:
		beam.SetTreatAndProtectMarginsForBeam(TopMargin = 0.5, BottomMargin = 0.5, LeftMargin = 0.5, RightMargin = 0.5, Roi = protect_roi)
	beam_set.TreatAndProtect(ShowProgress=True)
	beam_set.CopyBeamsFromBeamSet(BeamSetToCopyFrom = beam_set)
	beam_set.SetTreatmentTechnique(Technique = 'SMLC')
	po = plan_optimization
	tss = po.OptimizationParameters.TreatmentSetupSettings[0]
	tss.SegmentConversion.UseConformalSequencing = False
	for bs in tss.BeamSettings:
		if bs.ForBeam.Name in ['RPO','LPO','LAO','RAO']:
			bs.EditBeamOptimizationSettings(OptimizationTypes=["None"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Automatic")
	po.ResetOptimization()
	po.AutoScaleToPrescription = False
	tss.SegmentConversion.UseConformalSequencing = False
	opt_param = po.OptimizationParameters.DoseCalculation.IterationsInPreparationsPhase = 7
	po.OptimizationParameters.DoseCalculation.ComputeFinalDose = True
	tss.SegmentConversion.MaxNumberOfSegments = 10
	tss.SegmentConversion.MinSegmentArea = 4
	tss.SegmentConversion.MinSegmentMUPerFraction = 4

def set_up_beams_for_tangential_breast(plan, beam_set, protect_roi):
        
  beam_set.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = protect_roi)
  for beam in beam_set.Beams:
    beam.SetTreatAndProtectMarginsForBeam(TopMargin = 0.5, BottomMargin = 0.5, LeftMargin = 0.5, RightMargin = 0.5, Roi = protect_roi)
    beam_set.TreatAndProtect(ShowProgress=True)	
	
	
def set_up_beams_for_regional_breast(plan, beam_set, protect_roi, region_code):
  if region_code in RC.breast_reg_codes:
    for beam in beam_set.Beams:
      if beam.Name in ['45','222','139','320']:
        beam_set.CopyBeam(BeamName = beam.Name)
        
  beam_set.SelectToUseROIasTreatOrProtectForAllBeams(RoiName = protect_roi)
  for beam in beam_set.Beams:
    beam.SetTreatAndProtectMarginsForBeam(TopMargin = 0.5, BottomMargin = 0.5, LeftMargin = 0.5, RightMargin = 0.5, Roi = protect_roi)
    beam_set.TreatAndProtect(ShowProgress=True)

  for beam in beam_set.Beams:
    segments = beam.Segments[0]
    jaw = segments.JawPositions
    new_beam_names = ['46','223','140','321']
    if beam.Name in new_beam_names:
      beam.Name = str(int(beam.Name)-1)+" seg"
      jaw[3] = 0
      if beam.Name in ['45 seg','139 seg']:
        beam.Number = 2
      elif beam.Name in ['222 seg','320 seg']:
        beam.Number = 7
    segments.JawPositions = jaw

      
def set_up_vmat_beams_and_optimization_for_regional_breast(plan, beam_set, protect_roi, region_code):
  beam_set.SetTreatmentTechnique(Technique = 'SMLC')
  po = plan.PlanOptimizations[0]
  tss = po.OptimizationParameters.TreatmentSetupSettings[0]

  for bs in tss.BeamSettings:
    if bs.ForBeam.Name in ['RPO','LPO','LAO','RAO','Høyre','Venstre','Forfra','RPO 1','LPO 1']:
      bs.EditBeamOptimizationSettings(OptimizationTypes=["None"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Automatic")
    elif bs.ForBeam.Name in ['RPO 2','LPO 2']:
      bs.EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt","SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Automatic")
    elif bs.ForBeam.Name in ['Høyre 1','Venstre 1','Forfra 1']:
      bs.EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt","SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Use limits as max", TopJaw = 0)
    elif bs.ForBeam.Name in ['LAO 1','RAO 1']:
      bs.EditBeamOptimizationSettings(OptimizationTypes=["SegmentOpt","SegmentMU"], SelectCollimatorAngle=False, AllowBeamSplit=False, JawMotion="Use limits as max", BottomJaw = 0)
  po.ResetOptimization()
  po.AutoScaleToPrescription = False
  tss.SegmentConversion.UseConformalSequencing = False
  opt_param = po.OptimizationParameters.DoseCalculation.IterationsInPreparationsPhase = 7
  po.OptimizationParameters.DoseCalculation.ComputeFinalDose = True
  tss.SegmentConversion.MaxNumberOfSegments = 15
  tss.SegmentConversion.MinSegmentArea = 4
  tss.SegmentConversion.MinSegmentMUPerFraction = 4



	
def close_leaves_behind_jaw_for_regional_breast(beam_set):
  for beam in beam_set.Beams:
    #messagebox.showinfo("close leaves",beam.Name)
    if beam.Name in ['45 seg','222 seg','139 seg','320 seg']:
      
      segments = beam.Segments[0]
      leaf_positions = segments.LeafPositions
      jaw = segments.JawPositions
      y1 = jaw[2]
      y2 = jaw[3]
      first_x1 = leaf_positions[0][1]
      last_x1 = leaf_positions[0][79]
      first_x2 = leaf_positions[1][1]
      last_x2 = leaf_positions[1][79]
      # get the last corresponding MLC that is in the field
      mlcY1 = math.floor((y1 + 20) * 2) + 1.0
      mlcY2 = math.ceil ((y2 + 20) * 2)

      # don't forget that mlc 50 is in spot leafPositions[0][49]
      for i in range(0, int(mlcY1 -2)):
        leaf_positions[0][i] = first_x1
        leaf_positions[1][i] = first_x2

      for j in range(int(mlcY2 +1), 80):
        leaf_positions[0][j] = last_x1
        leaf_positions[1][j] = last_x2
      if beam.Name in ['45 seg']: #'140','223'
        if abs(leaf_positions[1][int(mlcY2)-1]-leaf_positions[1][int(mlcY2)-2]) > 1:
          leaf_positions[1][int(mlcY2)-1] = leaf_positions[1][int(mlcY2)-2]
          leaf_positions[1][int(mlcY2)] = leaf_positions[1][int(mlcY2)-2]
        elif abs(leaf_positions[1][int(mlcY2)-1]-leaf_positions[1][int(mlcY2)])>1:
          leaf_positions[1][int(mlcY2)] = leaf_positions[1][int(mlcY2)-1]
      elif beam.Name in ['222 seg']:
        if abs(leaf_positions[0][int(mlcY2)-1]-leaf_positions[0][int(mlcY2)-2]) > 1:
          leaf_positions[0][int(mlcY2)-1] = leaf_positions[0][int(mlcY2)-2]
          leaf_positions[0][int(mlcY2)] = leaf_positions[0][int(mlcY2)-2]
        elif abs(leaf_positions[0][int(mlcY2)-1]-leaf_positions[0][int(mlcY2)])>1:
          leaf_positions[0][int(mlcY2)] = leaf_positions[0][int(mlcY2)-1]
                    
      segments.LeafPositions = leaf_positions
                          
