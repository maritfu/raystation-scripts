# encoding: utf8

# Import local files:
import beam_set_functions as BSF
import case_functions as CF
import region_codes as RC
import rois as ROIS
import structure_set_functions as SSF
#BSF.create_three_beams(beam_set, isocenter, energy = energy_name, name1 = 'LPO', name2 = 'LAO', name3 = 'RAO', gantry_angle1 = '110', gantry_angle2 = '35', gantry_angle3 = '350', collimator_angle1 = '343', collimator_angle2 = '17', collimator_angle3 = '17', iso_index=iso_index, beam_index=beam_index)


# Set up beams or arcs, based on region code (i.e. treatment site).
def setup_beams(ss, examination, beam_set, isocenter, region_code, fraction_dose, technique_name, energy_name, iso_index = 1, beam_index=1,beam_index2 = 2):
  if technique_name == '3D-CRT':
    #Two tangetial beams:
    if region_code in RC.breast_tang_r_codes:
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '54', gantry_angle2 = '231', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = 4)
      BSF.set_MU(beam_set,['54','231'], [110, 110] )
    elif region_code in RC.breast_tang_l_codes:
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '128', gantry_angle2 = '306', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = 4)
      BSF.set_MU(beam_set,['128','306'], [110, 110] )
    # Breast with regional lymph nodes:
    elif region_code in RC.breast_reg_l_codes: # Left
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '139', gantry_angle2 = '320', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = 6)
      BSF.set_MU(beam_set,['139','320'], [100, 100] )
    elif region_code in RC.breast_reg_r_codes: # Right
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '45', gantry_angle2 = '222', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = 6)
      BSF.set_MU(beam_set,['45','222'], [100, 100] )
    elif region_code in RC.brain_whole_codes:
      # Husk å legge inn 6 MV på kurative og 15 på palliative
      BSF.create_two_beams(beam_set, isocenter, energy = '15', gantry_angle1 = '270', gantry_angle2 = '90', collimator_angle1 = '295', collimator_angle2 = '63', iso_index=iso_index, beam_index=beam_index)
      BSF.set_MU(beam_set,['270','90'], [130, 130] )
  elif technique_name == 'VMAT':
    # Brain:
    if region_code in RC.brain_whole_codes: # Whole brain
      BSF.create_single_arc(beam_set, isocenter)
    elif region_code in RC.brain_partial_codes:
      if fraction_dose > 15:
        BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '5', collimator_angle2 = '355', iso_index=iso_index, beam_index=beam_index)
      elif fraction_dose > 6: # Stereotactic brain
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '5', iso_index=iso_index, beam_index=beam_index)
      else: # Partial brain
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '45', iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.head_neck_codes:
      BSF.create_single_arc(beam_set, isocenter)
    elif region_code in RC.breast_tang_l_codes:
      BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='100', gantry_stop_angle2='290', gantry_start_angle1='160', gantry_start_angle2='340', collimator_angle1='5', collimator_angle2='5',iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.breast_tang_r_codes:
      BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='20', gantry_stop_angle2='200', gantry_start_angle1='70', gantry_start_angle2='260', collimator_angle1='5', collimator_angle2='5',iso_index=iso_index, beam_index=beam_index)
    # Breast with regional lymph nodes:
    elif region_code in RC.breast_reg_l_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '280', gantry_start_angle = '178', iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.breast_reg_r_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '80', gantry_start_angle = '182', iso_index=iso_index, beam_index=beam_index)
    # Lung:
    elif region_code in RC.lung_and_mediastinum_codes:
      if region_code in RC.lung_r_codes: # Right
        #BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '30', gantry_stop_angle2 = '182', gantry_start_angle1 = '182', gantry_start_angle2 = '30', iso_index=iso_index, beam_index=beam_index)
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '182', gantry_start_angle = '30', iso_index=iso_index, beam_index=beam_index)
      elif region_code in RC.lung_l_codes: # Left
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '330', gantry_start_angle = '178', iso_index=iso_index, beam_index=beam_index)
        #BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '330', gantry_stop_angle2 = '178', gantry_start_angle1 = '178', gantry_start_angle2 = '330', iso_index=iso_index, beam_index=beam_index)
      else: # Mediastinum or both lungs
        BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Bladder:
    elif region_code in RC.bladder_codes:
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Prostate:
    elif region_code in RC.prostate_codes:
      # Set up beams (arcs). Two arcs if there is a lymph node volume and one arc if not.
      if SSF.has_roi_with_shape(ss, ROIS.ptv_56.name):
        BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '45', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
      else:
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Rectum:
    elif region_code in RC.rectum_codes:
      BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '45', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
    # Palliative:
    elif region_code in RC.palliative_codes:
      # Stereotactic palliative codes:
      if fraction_dose > 8:
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '5', iso_index=iso_index, beam_index=beam_index)
      else:
        if region_code in RC.whole_pelvis_codes:
          BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '45', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
        else:
          if region_code in RC.palliative_columna_codes:
             BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '138', gantry_stop_angle2 = '182', gantry_start_angle1 = '178', gantry_start_angle2 = '222', iso_index=iso_index, beam_index=beam_index)
          elif abs(isocenter.x) > 5:
            if isocenter.x > 5 and CF.is_head_first_supine(examination) or not CF.is_head_first_supine(examination) and isocenter.x < -5:
              BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '330', gantry_stop_angle2 = '178', gantry_start_angle1 = '178', gantry_start_angle2 = '330', iso_index=iso_index, beam_index=beam_index)
            else:
              BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '30', gantry_stop_angle2 = '182', gantry_start_angle1 = '182', gantry_start_angle2 = '30', iso_index=iso_index, beam_index=beam_index)
          elif abs(isocenter.y) +5 < abs(SSF.roi_center_y(ss, ROIS.external.name)):
            BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '240', gantry_stop_angle2 = '110', gantry_start_angle1 = '110', gantry_start_angle2 = '240', iso_index=iso_index, beam_index=beam_index)
          else:
            BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
  return len(list(beam_set.Beams))
