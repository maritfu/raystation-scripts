# encoding: utf8

# encoding: utf8
#!/usr/bin/python

# Import system libraries:
from connect import *
import clr, sys

from tkinter import *
from tkinter import messagebox

from System.Windows import *
# Import local files:
import beams as BEAMS
import beam_set_functions as BSF
import case_functions as CF
import gui_functions as GUIF
import objectives as OBJ
import region_codes as RC
import roi_functions as ROIF
import structure_set_functions as SSF

# Contains a collection of plan functions.


# Creates additional palliative beamsets (if multiple targets exists).
def create_additional_palliative_beamsets_prescriptions_and_beams(plan, examination, ss, region_codes, fraction_dose, nr_fractions, external, energy_name, nr_existing_beams=1, isocenter=False):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  common_isocenter = False
  if isocenter:
    common_isocenter = True
  i = 1
  if nr_targets > 1:
    for r in region_codes:
      region_code = int(r)
      # Determine the point which will be our isocenter:
      if not isocenter:
        if SSF.has_named_roi_with_contours(ss, 'PTV' + str(i+1)):
          isocenter = SSF.determine_isocenter(examination, ss, region_code, 'VMAT', 'PTV' + str(i+1), external)
          energy_name = SSF.determine_energy_single_target(ss, 'PTV'+str(i+1))
        else:
          GUIF.handle_missing_ptv()
      # Set up beam set and prescription:
      beam_set = plan.AddNewBeamSet(
        Name=BSF.label(region_code, fraction_dose, nr_fractions, 'VMAT'),
        ExaminationName=examination.Name,
        MachineName= "Agility Trh",
        Modality='Photons',
        TreatmentTechnique='VMAT',
        PatientPosition=CF.determine_patient_position(examination),
        NumberOfFractions=nr_fractions
      )
      BSF.add_prescription(beam_set, nr_fractions, fraction_dose, 'CTV' + str(i+1))

      # Setup beams or arcs
      nr_beams = BEAMS.setup_beams(ss, examination, beam_set, isocenter, region_code, fraction_dose, 'VMAT', energy_name, iso_index=str(i+1), beam_index1=nr_existing_beams+1)
      nr_existing_beams += nr_beams
      OBJ.create_palliative_objectives_for_additional_beamsets(ss, plan, fraction_dose*nr_fractions, i)
      i += 1
      if not common_isocenter:
        isocenter=False

# Creates additional stereotactic beamsets (if multiple targets exists).
# (Used for brain or lung)
def create_additional_stereotactic_beamsets_prescriptions_and_beams(plan, examination, ss, region_codes, fraction_dose, nr_fractions, external, energy_name, nr_existing_beams=1):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  i = 1
  if nr_targets > 1:
    if int(region_codes[0]) in RC.brain_codes + RC.lung_codes:
      for r in region_codes:
        # Set up beam set and prescription:
        region_code = int(r)
        beam_set = plan.AddNewBeamSet(
          Name=BSF.label_s(region_code, fraction_dose, nr_fractions),
          ExaminationName=examination.Name,
          MachineName= "Agility Trh FFF",
          Modality='Photons',
          TreatmentTechnique='VMAT',
          PatientPosition='HeadFirstSupine',
          NumberOfFractions=nr_fractions
        )
        BSF.add_prescription(beam_set, nr_fractions, fraction_dose, 'PTV' + str(i+1))
        # Determine the point which will be our isocenter:
        isocenter = SSF.determine_isocenter(examination, ss, region_code, 'VMAT', 'PTV' + str(i+1), external)
        # Setup beams or arcs
        nr_beams = BEAMS.setup_beams(ss, examination, beam_set, isocenter, region_code, fraction_dose, 'VMAT', energy_name, iso_index=str(i+1), beam_index1=nr_existing_beams+1)
        nr_existing_beams += nr_beams
        i += 1


# Creates a beam set (the first beam set, if multiple beam sets are to me made):
def create_beam_set(plan, name, examination, treatment_technique, nr_fractions, machine_name = "Agility Trh", modality='Photons', patient_position="HeadFirstSupine"):
  beam_set = plan.AddNewBeamSet(
    Name=name,
    ExaminationName=examination.Name,
    MachineName=machine_name,
    Modality=modality,
    TreatmentTechnique=treatment_technique,
    PatientPosition=CF.determine_patient_position(examination),
    NumberOfFractions=nr_fractions
  )
  return beam_set

# Creates an additional beam set for breast patients with hybrid VMAT technique, prescription is set, two/three beams are set up and objectives are set:
def create_breast_hybrid_vmat_beamset(ss, plan, examination, isocenter, region_code, roi_name, beam_set_name, technique_name, background_dose=0):
  second_beam_set_name = BSF.label(region_code, 2.67, 15, 'VMAT', background_dose=background_dose)
  # Set up beam set and prescription:
  beam_set = plan.AddNewBeamSet(
    Name=second_beam_set_name,
    ExaminationName=examination.Name,
    MachineName= "Agility Trh",
    Modality='Photons',
    TreatmentTechnique='VMAT',
    PatientPosition='HeadFirstSupine',
    NumberOfFractions=15
  )
  plan.UpdateDependency(DependentBeamSetName = second_beam_set_name,BackgroundBeamSetName = beam_set_name,DependencyUpdate = 'CreateDependency')
  BSF.add_prescription(beam_set, 15, 2.67, roi_name, region_code,'VMAT')
  if region_code in RC.breast_tang_l_codes:
    BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='91', gantry_stop_angle2='300', gantry_start_angle1='121', gantry_start_angle2='330', collimator_angle1='5', collimator_angle2='5', iso_index=2, beam_index = 2)
  elif region_code in RC.breast_tang_r_codes:
    BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='24', gantry_stop_angle2='231', gantry_start_angle1='54', gantry_start_angle2='261', collimator_angle1='5', collimator_angle2='5', iso_index=2, beam_index = 2)
  elif region_code in RC.breast_reg_l_codes:
    BSF.create_three_arcs(beam_set, isocenter, gantry_stop_angle1='109', gantry_stop_angle2='350',gantry_stop_angle3='320', gantry_start_angle1='139', gantry_start_angle2='109', gantry_start_angle3='350', collimator_angle1='5', collimator_angle2='0', collimator_angle3='5', iso_index=2, beam_index = 3)
  elif region_code in RC.breast_reg_r_codes:
    BSF.create_three_arcs(beam_set, isocenter, gantry_stop_angle1='10', gantry_stop_angle2='257',gantry_stop_angle3='222', gantry_start_angle1='45', gantry_start_angle2='10', gantry_start_angle3='257', collimator_angle1='5', collimator_angle2='0', collimator_angle3='5', iso_index=2, beam_index = 3)
  
  #total_dose = 40.05
  #OBJ.create_breast_objectives(ss, plan, region_code, total_dose, '3D-CRT')
  return second_beam_set_name

# Creates an additional beam set for breast patients with a 2 Gy x 8 boost, prescription is set, two beams are set up and common objectives are set:
def create_breast_boost_beamset(ss, plan, examination, isocenter, region_code, roi_name, background_dose=0):
  # Set up beam set and prescription:
  beam_set = plan.AddNewBeamSet(
    Name=BSF.label(region_code, 2, 8, 'Conformal', background_dose=background_dose),
    ExaminationName=examination.Name,
    MachineName= "Agility Trh",
    Modality='Photons',
    TreatmentTechnique='Conformal',
    PatientPosition='HeadFirstSupine',
    NumberOfFractions=8
  )
  BSF.add_prescription(beam_set, 8, 2, roi_name, region_code)
  if region_code in RC.breast_l_codes:
    BSF.create_three_beams(beam_set, isocenter, gantry_angle1 = '110', gantry_angle2 = '35', gantry_angle3 = '350', collimator_angle1 = '343', collimator_angle2 = '17', collimator_angle3 = '17', iso_index=2)
    
  elif region_code in RC.breast_r_codes:
    BSF.create_three_beams(beam_set, isocenter, gantry_angle1 = '250', gantry_angle2 = '325', gantry_angle3 = '10', collimator_angle1 = '9', collimator_angle2 = '352', collimator_angle3 = '352', iso_index=2)
  total_dose = 16
  OBJ.create_breast_boost_objectives(ss, plan, total_dose)

def expand_dose_grid(plan, expand_x=0,expand_y=0,expand_z =0):
  c = plan.GetDoseGrid()
  corner = c.Corner
  corner.y = corner.y-expand_y
  nr_voxels = c.NrVoxels
  nr_voxels.y = nr_voxels.y+16
  plan.UpdateDoseGrid(
    Corner=corner,
    VoxelSize=c.VoxelSize,
    NumberOfVoxels = nr_voxels
  )


# Returns true if stereotactic fractionation is used
def is_stereotactic(nr_fractions, fraction_dose):
  if nr_fractions in [3, 5, 8] and fraction_dose in [15, 11, 7, 8, 9] or nr_fractions == 1 and fraction_dose > 14:
    return True
  else:
    return False


# Set dose grid, 0.2x0.2x0.2 cm3 for stereotactic treatments and 0.3x03x0.3 cm3 otherwise
def set_dose_grid(plan, region_code, nr_fractions, fraction_dose):
  # Default grid size:
  size = 0.3
  if is_stereotactic(nr_fractions, fraction_dose) or region_code in RC.prostate_codes or region_code in RC.brain_partial_codes or region_code in RC.head_neck_codes:
    size = 0.2
  plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
