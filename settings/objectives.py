# encoding: utf8

# Import system libraries:
from __future__ import division
import math
from connect import *
import clr, sys
from tkinter import messagebox

# Import local files:
import gui_functions as GUIF
import margins as MARGINS
import patient_model_functions as PMF
import rois as ROIS
import roi as ROI
import roi_functions as ROIF
import objective_functions as OF
import region_codes as RC
import structure_set_functions as SSF
import tolerance_doses as TOL

# OAR objectives:
# Brain
brain_oar_objectives = []
brain_whole_oar_objectives = [ROIS.lens_l, ROIS.lens_r, ROIS.nasal_cavity]
brain_stereotactic_oar_objectives = []
# Breast
breast_tang_oar_objectives = []
breast_reg_l_oar_objectives = []
breast_reg_r_oar_objectives = []
breast_reg_oar_objectives = []
# Head Neck
head_neck_objectives = []
# Esophagus
esophagus_objectives = []
# Lung
lung_objectives = []
# Palliative
palliative_head_oar_objectives = [ROIS.spinal_canal_head, ROIS.eye_l, ROIS.eye_r]
palliative_neck_oar_objectives = [ROIS.spinal_canal_head, ROIS.parotids]
palliative_thorax_oar_objectives =  [ROIS.spinal_canal, ROIS.heart, ROIS.lungs]
palliative_thorax_and_abdomen_oar_objectives =  [ROIS.spinal_canal, ROIS.heart, ROIS.lungs, ROIS.kidneys, ROIS.bowel_space]
palliative_abdomen_oar_objectives =  [ROIS.spinal_canal, ROIS.kidneys, ROIS.bowel_space]
palliative_abdomen_and_pelvis_objectives = [ROIS.spinal_canal, ROIS.kidneys, ROIS.bowel_space, ROIS.bladder, ROIS.rectum]
palliative_pelvis_oar_objectives =  [ROIS.bowel_space, ROIS.bladder, ROIS.rectum, ROIS.spinal_canal]
palliative_other_oar_objectives =  []
palliative_prostate_oar_objectives = [ROIS.bowel_space, ROIS.bladder, ROIS.rectum]
# Bladder
bladder_objectives = [ROIS.bowel_space, ROIS.rectum]
# Prostate
prostate_objectives = []
prostate_bed_objectives = []
#Gyn
gyn_objectives = []
# Rectum
rectum_objectives = []
anus_objectives = []

# Functions that creates objectives in the RayStation Plan Optimization module for various cases:

# Create common objectives.
def create_common_objectives(ss, plan, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)


# Create palliative objectives.
def create_palliative_objectives(ss, plan, total_dose, target):
  OF.uniform_dose(ss, plan, target, total_dose*100, 30)
  OF.min_dose(ss, plan, target.replace("C", "P"), total_dose*100*0.95, 150)
  OF.max_dose(ss, plan, target.replace("C", "P"), total_dose*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)


# Create objectives for palliative beam sets in cases of multiple beam sets.
def create_palliative_objectives_for_additional_beamsets(ss, plan, total_dose, beam_set_index):
  OF.uniform_dose(ss, plan, ROIS.ctv.name+str(beam_set_index+1), total_dose*100, 30, beam_set_index = beam_set_index)
  OF.min_dose(ss, plan, ROIS.ptv.name+str(beam_set_index+1), total_dose*100*0.95, 150, beam_set_index = beam_set_index)
  OF.max_dose(ss, plan, ROIS.ptv.name+str(beam_set_index+1), total_dose*100*1.05, 80, beam_set_index = beam_set_index)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30, beam_set_index = beam_set_index)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30, beam_set_index = beam_set_index)


# Create objectives for breast boost (2 Gy x 8)
def create_breast_boost_objectives(ss, plan, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv_sb.name, total_dose*100, 30, beam_set_index = 1)
  OF.min_dose(ss, plan, ROIS.ptv_sbc.name, total_dose*100*0.95, 150, beam_set_index = 1)
  OF.max_dose(ss, plan, ROIS.ptv_sbc.name, total_dose*100*1.05, 80, beam_set_index = 1)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30, beam_set_index = 1)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30, beam_set_index = 1)
  OF.max_eud(ss, plan, ROIS.heart.name, 0.5*100, 1, 1, beam_set_index = 1)


# Whole brain
def create_whole_brain_objectives(ss, plan, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.97, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.03, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)
  # These objectives are currently disabled and replaced with dynamic, adaptive optimization:
  #OF.max_eud(ss, plan, ROIS.eye_l.name, 0.3*total_dose*100, 1, 3)
  #OF.max_eud(ss, plan, ROIS.eye_r.name, 0.3*total_dose*100, 1, 3)
  #OF.max_eud(ss, plan, ROIS.lens_l.name, 0.13*total_dose*100, 1, 2)
  #OF.max_eud(ss, plan, ROIS.lens_r.name, 0.13*total_dose*100, 1, 2)
  #OF.max_eud(ss, plan, ROIS.nasal_cavity.name, 0.5*total_dose*100, 1, 2)


# Partial brain
def create_brain_objectives(pm, examination, ss, plan, total_dose, nr_fractions):
  if nr_fractions in [1, 3]: # Stereotactic brain
    if nr_fractions == 1: # One fraction
      nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
      
      if nr_targets == 1: # one target
        OF.min_dose(ss, plan, ROIS.gtv.name, 22*100, 200)
        OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 500)
        OF.max_dose(ss, plan, ROIS.ptv.name, 1.5*total_dose*100, 1)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 3, 1)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_05.name, total_dose*100, total_dose*100/2, 0.5, 1)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_2.name, total_dose*100/2, 4*100, 1.5, 1)
      else:
        for i in range(0, nr_targets):
          OF.min_dose(ss, plan, ROIS.gtv.name+str(i+1), 22*100, 200)
        for i in range(0, nr_targets):
          OF.min_dose(ss, plan, ROIS.ptv.name+str(i+1), total_dose*100, 500)
        for i in range(0, nr_targets):
          OF.max_dose(ss, plan, ROIS.ptv.name+str(i+1), 1.5*total_dose*100, 1)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 3, 1)
        for i in range(0, nr_targets):
          OF.fall_off(ss, plan, "xPTV"+str(i+1)+"_Ring0-0.5cm", total_dose*100, total_dose*100/2, 0.5, 1)
          OF.fall_off(ss, plan, "xPTV"+str(i+1)+"_Ring0.5-2cm", total_dose*100/2, 4*100, 1.5, 1)
    if nr_fractions == 3:# Three fractions
      nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
      if nr_targets == 1: # one target
        OF.min_dose(ss, plan, ROIS.gtv.name, 1.074*total_dose*100, 500)
        OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 1500)
        OF.max_dose(ss, plan, ROIS.ptv.name, 1.463*total_dose*100, 1)
        OF.max_dose(ss, plan, ROIS.body.name, 1.463*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 3, 1)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_05.name, total_dose*100, 12*100, 0.5, 1)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_2.name, 15*100, 3*100, 1.5, 1)
      else:
        for i in range(0, nr_targets):
          OF.min_dose(ss, plan, ROIS.gtv.name+str(i+1), 1.074*total_dose*100, 500)
        for i in range(0, nr_targets):
          OF.min_dose(ss, plan, ROIS.ptv.name+str(i+1), total_dose*100, 1500)
        for i in range(0, nr_targets):
          OF.max_dose(ss, plan, ROIS.ptv.name+str(i+1), 1.463*total_dose*100, 1)
        OF.max_dose(ss, plan, ROIS.body.name, 1.463*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 3, 1)
        for i in range(0, nr_targets):
          OF.fall_off(ss, plan, "xPTV"+str(i+1)+"_Ring0-0.5cm", total_dose*100, 12*100, 0.5, 1)
          OF.fall_off(ss, plan, "xPTV"+str(i+1)+"_Ring0.5-2cm", 15*100, 3*100, 1.5, 1)
  else: # Partial brain
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)
    # Objectives for prioritized OARs:
    OF.max_dose(ss, plan, ROIS.brainstem_surface.name, (TOL.brainstem_surface_v003_adx.equivalent(nr_fractions)*100)-50, 60)
    OF.max_dose(ss, plan, ROIS.brainstem_core.name, (TOL.brainstem_core_v003_adx.equivalent(nr_fractions)*100)-50, 80)
    OF.max_dose(ss, plan, ROIS.optic_chiasm.name, (TOL.optic_chiasm_v003_adx.equivalent(nr_fractions)*100)-50, 40)
    OF.max_dose(ss, plan, ROIS.optic_nrv_l.name, (TOL.optic_nrv_v003_adx.equivalent(nr_fractions)*100)-50, 20)
    OF.max_dose(ss, plan, ROIS.optic_nrv_r.name, (TOL.optic_nrv_v003_adx.equivalent(nr_fractions)*100)-50, 20)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, (TOL.spinalcord_v2_adx.equivalent(nr_fractions)*100)-50, 20)
    prioritized_oars = [ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.spinal_cord]
    tolerances = [TOL.brainstem_core_v003_adx, TOL.brainstem_surface_v003_adx, TOL.optic_chiasm_v003_adx, TOL.optic_nrv_v003_adx, TOL.optic_nrv_v003_adx, TOL.spinalcord_v2_adx]
    conflict_oars = []
    for i in range(len(prioritized_oars)):
      if tolerances[i].equivalent(nr_fractions) < total_dose*0.95:
        conflict_oars.append(prioritized_oars[i])
    # Setup of min and uniform doses depends on presence of critical overlaps or not:
    if len(conflict_oars) > 0:
      # Create subtraction and intersect ROIs for planning of conflicting sites:
      ctv_oars = ROI.ROIAlgebra(ROIS.ctv_oars.name, ROIS.ctv_oars.type, ROIS.ctv.color, sourcesA = [ROIS.ctv], sourcesB = conflict_oars, operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_2mm_expansion)
      ptv_oars = ROI.ROIAlgebra(ROIS.ptv_oars.name, ROIS.ptv_oars.type, ROIS.ptv.color, sourcesA = [ROIS.ptv], sourcesB = conflict_oars, operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_2mm_expansion)
      ptv_and_oars = ROI.ROIAlgebra(ROIS.ptv_and_oars.name, ROIS.ptv_and_oars.type, ROIS.other_ptv.color, sourcesA = [ROIS.ptv], sourcesB = conflict_oars, operator='Intersection')
      rois = [ctv_oars, ptv_oars, ptv_and_oars]
      PMF.delete_matching_rois(pm, rois)
      for i in range(len(rois)):
        PMF.create_algebra_roi(pm, examination, ss, rois[i])
        PMF.exclude_roi_from_export(pm, rois[i].name)
      # Create objectives for the subtraction/intersect ROIs:
      OF.uniform_dose(ss, plan, ROIS.ptv_and_oars.name, (tolerances[0].equivalent(nr_fractions)*100-50), 5) # (Note that this assumes our OARs have the same tolerance dose...)
      OF.uniform_dose(ss, plan, ROIS.ctv_oars.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv_oars.name, total_dose*100*0.95, 150)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
    # Setup of objectives for less prioritized OARs:
    other_oars = [ROIS.cochlea_l, ROIS.cochlea_r, ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.lens_l, ROIS.lens_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.retina_l, ROIS.retina_r, ROIS.cornea_r, ROIS.cornea_l, ROIS.pituitary]
    tolerances = [TOL.cochlea_mean_tinnitus, TOL.cochlea_mean_tinnitus, TOL.hippocampus_v40, TOL.hippocampus_v40, TOL.lens_v003_adx, TOL.lens_v003_adx, TOL.lacrimal_mean, TOL.lacrimal_mean, TOL.retina_v003_adx, TOL.retina_v003_adx, TOL.cornea_v003_adx, TOL.cornea_v003_adx, TOL.pituitary_mean]
    for i in range(len(other_oars)):
      if SSF.has_named_roi_with_contours(ss, other_oars[i].name):
        weight = None
        # Conflict with dose?
        if tolerances[i].equivalent(nr_fractions) < total_dose*0.95:
          # Conflict with dose:
          if not SSF.roi_overlap(pm, examination, ss, ROIS.ptv, other_oars[i], 2):
            if ROIF.roi_vicinity_approximate(SSF.rg(ss, ROIS.ptv.name), SSF.rg(ss, other_oars[i].name), 2):
              # OAR is close, but not overlapping:
              weight = 2
            else:
              weight = 20
        else:
          # No conflict with dose:
          weight = 20
        # Create objective if indicated:
        if weight:
          if other_oars[i].name in  [ROIS.cochlea_r.name, ROIS.cochlea_l.name, ROIS.lacrimal_l.name, ROIS.lacrimal_r.name, ROIS.hippocampus_l.name, ROIS.hippocampus_r.name]:
            OF.max_eud(ss, plan, other_oars[i].name, tolerances[i].equivalent(nr_fractions)*100-50, 1, weight)
          else:
            OF.max_dose(ss, plan, other_oars[i].name, (tolerances[i].equivalent(nr_fractions)*100)-50, weight)
      else:
        GUIF.handle_missing_roi_for_objective(other_oars[i].name)

def create_head_neck_objectives(ss, plan, total_dose):
  if total_dose == 60:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb_60.name, total_dose*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
      OF.uniform_dose(ss, plan, ROIS.x_ctv_54.name, 54*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_sb_60.name, 57*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_sb_60.name, 63*100, 100)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_54.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_54.name, 60*100, 54*100, 0.5, 10)
      elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_r_54.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_r_54.name, 60*100, 54*100, 0.5, 10)
      elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_l_54.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_l_54.name, 60*100, 54*100, 0.5, 10)
      OF.min_dose(ss, plan, ROIS.x_ptv_54.name, 51.3*100, 300)
      OF.max_dose(ss, plan, ROIS.x_ptv_54.name, 56.7*100, 100)
    elif SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
      OF.uniform_dose(ss, plan, ROIS.x_ctv_50.name, 50*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_sb_60.name, 57*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_sb_60.name, 63*100, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_50.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_50.name, 60*100, 50*100, 0.5, 10)
      elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_r_50.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_r_50.name, 60*100, 50*100, 0.5, 10)
      elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_l_50.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_l_50.name, 60*100, 50*100, 0.5, 10)
      OF.min_dose(ss, plan, ROIS.x_ptv_50.name, 47.5*100, 300)
      OF.max_dose(ss, plan, ROIS.x_ptv_50.name, 52.5*100, 300)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 3, 3)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.05*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 45*100, 100)
    OF.max_dose(ss, plan, ROIS.brainstem.name, 54*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 100)
    OF.max_eud(ss, plan, ROIS.parotid_l.name, 26*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.parotid_r.name, 26*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
      OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose*100, total_dose*100/2, 1.5, 3)
    elif SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
      OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose*100, total_dose*100/2, 2, 1)
    OF.max_eud(ss, plan, ROIS.x_skulder_h.name, 7*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.x_skulder_v.name, 7*100, 1, 10)
  elif total_dose == 66:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb_66.name, total_dose*100, 10)
    OF.min_dose(ss, plan, ROIS.ptv_sb_66.name, 62.7*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_sb_66.name, 69.3*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_sb_60.name, 57*100, 300)
    OF.uniform_dose(ss, plan, ROIS.x_ctv_54.name, 54*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_r_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_r_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_l_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_l_54.name, 60*100, 54*100, 0.5, 10)
    OF.min_dose(ss, plan, ROIS.x_ptv_54.name, 51.3*100, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_54.name, 56.7*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 3, 3)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.05*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 45*100, 100)
    OF.max_dose(ss, plan, ROIS.brainstem.name, 50*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 100)
    OF.max_eud(ss, plan, ROIS.parotid_l.name, 26*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.parotid_r.name, 26*100, 1, 10)
    OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose*100, total_dose*100/2, 1.5, 3)
    OF.max_eud(ss, plan, ROIS.x_skulder_h.name, 7*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.x_skulder_v.name, 7*100, 1, 10)
  elif total_dose == 68:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_68.name, total_dose*100, 10)
    ctv_n_68 = [ROIS.ctv_n_68.name, ROIS.ctv_n1_68.name,ROIS.ctv_n2_68.name,ROIS.ctv_n3_68.name]
    for c in ctv_n_68:
     if SSF.has_roi_with_shape(ss, c):
       OF.uniform_dose(ss, plan, c, total_dose*100, 10)
    OF.uniform_dose(ss, plan, ROIS.x_ctv_54.name, 54*100, 10)
    OF.min_dose(ss, plan, ROIS.ptv_p_68.name, 64.6*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p_68.name, 71.4*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_n_68.name, 64.6*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_n_68.name, 71.4*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_p_60.name, 57*100, 300)
    OF.min_dose(ss, plan, ROIS.ptv_n_60.name, 57*100, 300)
    OF.fall_off(ss, plan, ROIS.ptv_p_60.name, total_dose*100, 60*100, 0.5, 10)
    OF.fall_off(ss, plan, ROIS.ptv_n_60.name, total_dose*100, 60*100, 0.5, 10)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_r_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_r_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_l_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_l_54.name, 60*100, 54*100, 0.5, 10)
    OF.min_dose(ss, plan, ROIS.x_ptv_54.name, 51.3*100, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_54.name, 56.7*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 3, 3)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.05*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 45*100, 100)
    OF.max_dose(ss, plan, ROIS.brainstem.name, 54*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 100)
    OF.max_eud(ss, plan, ROIS.parotid_l.name, 26*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.parotid_r.name, 26*100, 1, 10)
    OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose*100, total_dose*100/2, 1.5, 3)
    OF.max_eud(ss, plan, ROIS.x_skulder_h.name, 7*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.x_skulder_v.name, 7*100, 1, 10)
  elif total_dose == 70:
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    OF.uniform_dose(ss, plan, ROIS.ctv_p_70.name, total_dose*100, 10)
    for c in ctv_n_70:
     if SSF.has_roi_with_shape(ss, c):
       OF.uniform_dose(ss, plan, c, total_dose*100, 10)
    OF.uniform_dose(ss, plan, ROIS.x_ctv_54.name, 54*100, 10)
    OF.min_dose(ss, plan, ROIS.ptv_p_70.name, 66.5*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p_70.name, 73.5*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.5*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73.5*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_p_60.name, 57*100, 300)
    OF.min_dose(ss, plan, ROIS.ptv_n_60.name, 57*100, 300)
    OF.fall_off(ss, plan, ROIS.ptv_p_60.name, total_dose*100, 60*100, 0.5, 10)
    OF.fall_off(ss, plan, ROIS.ptv_n_60.name, total_dose*100, 60*100, 0.5, 10)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_r_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_r_54.name, 60*100, 54*100, 0.5, 10)
    elif SSF.has_roi_with_shape(ss, ROIS.ptv_e_l_54.name):
      OF.fall_off(ss, plan, ROIS.ptv_e_l_54.name, 60*100, 54*100, 0.5, 10)
    OF.min_dose(ss, plan, ROIS.x_ptv_54.name, 51.3*100, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_54.name, 56.7*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 3, 3)
    OF.max_dose(ss, plan, ROIS.body.name, 1.05*total_dose*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 45*100, 100)
    OF.max_dose(ss, plan, ROIS.brainstem.name, 54*100, 100)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 100)
    OF.max_eud(ss, plan, ROIS.parotid_l.name, 26*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.parotid_r.name, 26*100, 1, 10)
    OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose*100, total_dose*100/2, 1.5, 3)
    OF.max_eud(ss, plan, ROIS.x_skulder_h.name, 7*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.x_skulder_v.name, 7*100, 1, 10)

# Esophagus

def create_esophagus_objectives(ss, plan, total_dose):
  if total_dose == 66:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_66.name, total_dose*100, 30)
    OF.uniform_dose(ss, plan, ROIS.ctv_n_66.name, total_dose*100, 30)
  elif total_dose == 60:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_60.name, total_dose*100, 30)
    OF.uniform_dose(ss, plan, ROIS.ctv_n_60.name, total_dose*100, 30)
  elif total_dose == 50:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_50.name, total_dose*100, 30)
    OF.uniform_dose(ss, plan, ROIS.ctv_n_50.name, total_dose*100, 30)
  elif total_dose == 41.4:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_41_4.name, total_dose*100, 30)
    OF.uniform_dose(ss, plan, ROIS.ctv_n_41_4.name, total_dose*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_46.name):
    OF.uniform_dose(ss, plan, ROIS.x_ctv_46.name, 46*100, 30)
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_e_41_4.name):
    OF.uniform_dose(ss, plan, ROIS.ctv_e_41_4.name, total_dose*100, 30)
  if total_dose == 66:
    OF.min_dose(ss, plan, ROIS.ptv_66.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv_66.name, total_dose*100*1.05, 80)
  elif total_dose == 60:
    OF.min_dose(ss, plan, ROIS.ptv_60.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv_60.name, total_dose*100*1.05, 80)
  elif total_dose == 50:
    OF.min_dose(ss, plan, ROIS.ptv_50.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv_50.name, total_dose*100*1.05, 80)
  elif total_dose == 41.4:
    OF.min_dose(ss, plan, ROIS.ptv_41_4.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv_41_4.name, total_dose*100*1.05, 80)
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_46.name):
    OF.min_dose(ss, plan, ROIS.ptv_e_46.name, 46*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv_e_46.name, 46*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)
  OF.max_eud(ss, plan, ROIS.heart.name, 20*100, 1, 10)
  OF.max_eud(ss, plan, ROIS.kidneys.name, 15*100, 1, 10)
  OF.max_eud(ss, plan, ROIS.lungs.name, 15*100, 1, 10)
  
# Lung
def create_lung_objectives(ss, plan, target, total_dose):
  if total_dose > 40: # Curative fractionation
    ictv_n = [ROIS.ictv_n1.name, ROIS.ictv_n2.name,ROIS.ictv_n3.name,ROIS.ictv_n4.name,ROIS.ictv_n5.name,ROIS.ictv_n6.name, ROIS.ictv_p]
    if SSF.has_roi_with_shape(ss, ROIS.ictv_n1.name):
      for c in ictv_n:
        if SSF.has_roi_with_shape(ss, c):
          OF.uniform_dose(ss, plan, c, total_dose*100, 20)
    else:
      OF.uniform_dose(ss, plan, ROIS.ictv_n.name, total_dose*100, 20)
    OF.uniform_dose(ss, plan, ROIS.ictv_p.name, total_dose*100, 20)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*0.95*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.02, 100)
    OF.min_dose(ss, plan, ROIS.x_ptv_vev.name, total_dose*0.95*100, 100)
    OF.min_dose(ss, plan, ROIS.x_ptv_lunge.name, total_dose*0.95*100, 100)
    
    match = False
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    OF.max_eud(ss, plan, l, 20*100, 1, 1) 
    OF.max_dvh(ss, plan, l, 5*100, 55, 1) 
    OF.max_dvh(ss, plan, l, 20*100, 35, 1)
    OF.max_dvh(ss, plan, ROIS.heart.name, 50*100, 20, 1)
    OF.max_dvh(ss, plan, ROIS.heart.name, 40*100, 30, 1)
    OF.max_dvh(ss, plan, ROIS.heart.name, 25*100, 50, 1)
    if total_dose >59:
      OF.max_dose(ss, plan, ROIS.a_aorta.name, 60*100, 1)
      OF.max_dose(ss, plan, ROIS.esophagus.name, 60*100, 1)
      OF.max_dose(ss, plan, ROIS.trachea.name, 60*100, 1)
      OF.max_dose(ss, plan, ROIS.bronchus.name, 60*100, 1)
    if total_dose == 45:
      OF.max_dose(ss, plan, ROIS.a_aorta.name, 45*100, 1)
      OF.max_dose(ss, plan, ROIS.esophagus.name, 45*100, 1)
      OF.max_dose(ss, plan, ROIS.trachea.name, 45*100, 1)
      OF.max_dose(ss, plan, ROIS.bronchus.name, 45*100, 1)
  elif total_dose < 40: # Palliative fractionation
    OF.uniform_dose(ss, plan, target, total_dose*100, 35)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 120)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 80)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 3, 2)
    OF.max_eud(ss, plan, ROIS.heart.name, 0.29*total_dose*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.lungs.name, 0.23*total_dose*100, 1, 15)
    OF.max_eud(ss, plan, ROIS.spinal_canal.name, 0.9*total_dose*100, 1, 5)


# Stereotactic lung
def create_lung_stereotactic_objectives(ss, plan, region_code, total_dose):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  for i in range(0, nr_targets):
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 3, 5)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*130, 15)
    OF.max_dose(ss, plan, ROIS.skin.name, 30*100, 10)
    OF.max_dose(ss, plan, ROIS.spinal_canal.name, 13*100, 5)
    OF.max_dvh(ss, plan, ROIS.chestwall.name, 30*100, 2, 100)
    OF.max_eud(ss, plan, ROIS.lungs.name, 4.5*100, 1, 1)
    if region_code in RC.lung_r_codes:
      OF.max_eud(ss, plan, ROIS.lung_r.name, 6.5*100, 1, 3)
      OF.max_dose(ss, plan, ROIS.ribs_r.name, total_dose*120, 10)
    else:
      OF.max_eud(ss, plan, ROIS.lung_l.name, 6.5*100, 1, 3)
      OF.max_dose(ss, plan, ROIS.ribs_l.name, total_dose*120, 10)
  if nr_targets == 1:
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 250)
    OF.fall_off(ss, plan, ROIS.wall_ptv.name, total_dose*100, 0.7*total_dose*100, 0.8, 5)
  else:
    for i in range(0, nr_targets):
      OF.min_dose(ss, plan, ROIS.ptv.name+str(i+1), total_dose*100, 250)
      OF.fall_off(ss, plan, "zPTV"+str(i+1)+"_Wall", total_dose*100, 0.7*total_dose*100, 0.8, 5)
'''
def create_breast_objectives(ss, plan, region_code, total_dose, target):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 100)
  OF.min_dose(ss, plan, ROIS.ptv_c.name, 38.5*100, 3000)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, 20, 1, 1)
  OF.max_dose(ss, plan, ROIS.external.name,41.5*100, 3000)
  if target == ROIS.ctv_sb.name:
    OF.max_eud(ss, plan, ROIS.heart.name, 0.5*100, 1, 1)
  else:
    OF.max_eud(ss, plan, ROIS.heart.name, 1.6*100, 1, 1)
  if region_code in RC.breast_tang_l_codes:
    OF.max_eud(ss, plan, ROIS.breast_r.name, 0.5*100, 1, 1)
  elif region_code in RC.breast_tang_r_codes:
    OF.max_eud(ss, plan, ROIS.breast_l.name, 0.5*100, 1, 1)
'''
#Only breast and breast with regional lymph nodes
def create_breast_objectives(ss, plan, region_code, total_dose, technique_name):
  if technique_name == '3D-CRT':
    if region_code in RC.breast_reg_codes:
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30, beam_set_index = 1)
      OF.uniform_dose(ss, plan, ROIS.ctv_n.name, total_dose*100, 30, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_nc.name, 38.4*100, 1000, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.4*100, 1000, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.ptv_nc.name, total_dose*100, 38.05*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, 30*100, 2, 1, beam_set_index = 1)
      OF.max_dose(ss, plan, ROIS.external.name, 42*100, 50000, beam_set_index = 1)
      OF.max_eud(ss, plan, ROIS.heart.name, 1.8*100, 1, 5, beam_set_index = 1)
      if region_code in RC.breast_reg_l_codes:
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 20*100, 20, 5, beam_set_index = 1)
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 5*100, 45, 5, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 10*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 5*100, 1, 5, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.breast_r.name, 0.8*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.humeral_l.name, 15*100, 1, 10, beam_set_index = 1)
      elif region_code in RC.breast_reg_r_codes:
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 20*100, 20, 5, beam_set_index = 1)
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 5*100, 45, 5, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 10*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 5*100, 1, 5, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.breast_l.name, 0.8*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.humeral_r.name, 15*100, 1, 10, beam_set_index = 1)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_n_ring.name):
        OF.fall_off(ss, plan, ROIS.x_ctv_n_ring.name, total_dose*100, 30*100, 2, 20, beam_set_index = 1)
      elif SSF.has_roi_with_shape(ss, "xCTVn_L2-L4_Ring"):
        OF.fall_off(ss, plan, "xCTVn_L2-L4_Ring", total_dose*100, 30*100, 2, 20, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.esophagus.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.thyroid.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.trachea.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 100, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.5*100, 3000, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 20*100, 1, 1, beam_set_index = 1)
      OF.max_dose(ss, plan, ROIS.body.name,41.5*100, 30000, beam_set_index = 1)
      
      if region_code in RC.breast_tang_l_codes:
        OF.max_eud(ss, plan, ROIS.breast_r.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 4*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.heart.name, 1.6*100, 1, 1, beam_set_index = 1)
      elif region_code in RC.breast_tang_r_codes:
        OF.max_eud(ss, plan, ROIS.breast_l.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 4*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 0.5*100, 1, 1, beam_set_index = 1)
        OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 1, beam_set_index = 1)
  elif technique_name == 'VMAT':
    if region_code in RC.breast_reg_codes:
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 10)
      OF.uniform_dose(ss, plan, ROIS.ctv_n.name, total_dose*100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.imn.name):
        OF.uniform_dose(ss, plan, ROIS.imn.name, total_dose*100, 10)
        OF.min_dose(ss, plan, ROIS.ptv_n_imn.name, 38.2*100, 1000)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.2*100, 1000)
      OF.min_dose(ss, plan, ROIS.ptv_nc.name, 38.2*100, 1000)
      OF.max_dose(ss, plan, ROIS.body.name,42*100, 30000)
      OF.fall_off(ss, plan, ROIS.body.name, 40*100, 20*100, 1, 1)
      if region_code in RC.breast_reg_l_codes:
        OF.max_eud(ss, plan, ROIS.lung_l.name, 8*100, 1, 100)
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 2*100, 45, 10)
        OF.max_eud(ss, plan, ROIS.humeral_l.name, 12*100, 1, 10)
        OF.max_dose(ss, plan, ROIS.humeral_l.name, 30*100, 10)
        if SSF.has_roi_with_shape(ss, ROIS.imn.name):
          OF.max_eud(ss, plan, ROIS.lung_r.name, 1*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.breast_r.name, 1*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.heart.name, 1.8*100, 1, 100)
        else:
          OF.max_eud(ss, plan, ROIS.lung_r.name, 0.3*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.breast_r.name, 0.3*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 100)
      elif region_code in RC.breast_reg_r_codes:
        OF.max_eud(ss, plan, ROIS.lung_r.name, 8*100, 1, 100)
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 2*100, 45, 10)
        OF.max_eud(ss, plan, ROIS.humeral_r.name, 12*100, 1, 10)
        OF.max_dose(ss, plan, ROIS.humeral_r.name, 30*100, 10)
        if SSF.has_roi_with_shape(ss, ROIS.imn.name):
          OF.max_eud(ss, plan, ROIS.lung_l.name, 1*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.breast_l.name, 1*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 100)
        else:
          OF.max_eud(ss, plan, ROIS.lung_l.name, 0.3*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.breast_l.name, 0.3*100, 1, 5)
          OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 100)
      
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_n_ring.name):
        OF.fall_off(ss, plan, ROIS.x_ctv_n_ring.name, 42*100, 20*100, 1.5, 10)
      elif SSF.has_roi_with_shape(ss, "xCTVn_L2-L4_Ring"):
        OF.fall_off(ss, plan, "xCTVn_L2-L4_Ring", 42*100, 20*100, 1.5, 10)
      OF.fall_off(ss, plan, ROIS.esophagus.name, 40*100, 10*100, 1, 10)
      OF.fall_off(ss, plan, ROIS.thyroid.name, 40*100, 10*100, 1, 10)
      OF.fall_off(ss, plan, ROIS.trachea.name, 40*100, 10*100, 1, 10)
      OF.min_dose_robust(ss, plan, ROIS.ptv_pc.name, 38*100, 1000)
      OF.max_dose_robust(ss, plan, ROIS.ptv_pc.name, 42*100, 5000)
      OF.min_dose_robust(ss, plan, ROIS.ptv_nc.name, 38*100, 1000)
      OF.max_dose_robust(ss, plan, ROIS.ptv_nc.name, 42*100, 5000)
    elif region_code in RC.breast_tang_codes:
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.5*100, 1000)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 20*100, 1, 1)
      OF.max_dose(ss, plan, ROIS.body.name,41.5*100, 30000)
      if region_code in RC.breast_tang_l_codes:
        OF.max_eud(ss, plan, ROIS.breast_r.name, 0.5*100, 1, 1)
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 18*100, 10, 1)
        OF.max_dvh(ss, plan, ROIS.lung_l.name, 2*100, 35, 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 4*100, 1, 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 0.3*100, 1, 1)
        OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 1)
      elif region_code in RC.breast_tang_r_codes:
        OF.max_eud(ss, plan, ROIS.breast_l.name, 0.5*100, 1, 1)
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 18*100, 10, 1)
        OF.max_dvh(ss, plan, ROIS.lung_r.name, 2*100, 35, 1)
        OF.max_eud(ss, plan, ROIS.lung_r.name, 4*100, 1, 1)
        OF.max_eud(ss, plan, ROIS.lung_l.name, 0.3*100, 1, 1)
        OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 1)
      OF.max_dose(ss, plan, ROIS.a_lad.name, 20*100, 1)
      OF.min_dose_robust(ss, plan, ROIS.ptv_pc.name, 38*100, 1000)
      OF.max_dose_robust(ss, plan, ROIS.ptv_pc.name, 42*100, 3000)
def create_prostate_objectives(ss, plan, total_dose):
  if total_dose == 60: 
    OF.uniform_dose(ss, plan, ROIS.ctv_p1_60.name, total_dose*100, 3)
    OF.uniform_dose(ss, plan, ROIS.ctv_p2_60.name, total_dose*100, 3)
    OF.min_dose(ss, plan, ROIS.ptv_p1_60.name, 57*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv_p1_60.name, 63*100, 100)
    OF.min_dose(ss, plan, ROIS.ptv_p2_60.name, 57*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv_p2_60.name, 63*100, 100)
    OF.max_dose(ss, plan, ROIS.external.name, 63*100, 100)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, 25*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 20*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.rectum.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 20*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.anal_canal.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 20*100, 2, 1)
    OF.max_eud(ss, plan, ROIS.bladder.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 44*100, 1)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 44*100, 1)
  elif total_dose == 77: # Normo-fractionation 
    OF.uniform_dose(ss, plan, ROIS.ctv_p1_77.name, 77*100, 3)
    OF.uniform_dose(ss, plan, ROIS.ptv_p2_70.name, 70*100, 3)
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    for c in ctv_n_70: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, ROIS.ctv_n_70.name, 70*100, 3)
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_56.name):  
      OF.uniform_dose(ss, plan, ROIS.x_ctv_56.name, 56*100, 3)    
    OF.min_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*0.95, 100)
    OF.max_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*1.05, 100)
    OF.min_dose(ss, plan, ROIS.ptv_p2_70.name, 66.5*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
      OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.5*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73.5*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.x_ptv_56.name):  
      OF.min_dose(ss, plan, ROIS.x_ptv_56.name, 53.2*100, 100)
      OF.max_dose(ss, plan, ROIS.x_ptv_56.name, 58.8*100, 100)
    OF.fall_off(ss, plan, ROIS.ptv_p2_70.name, 77*100, 70*100, 0.4, 10)
    if SSF.has_roi_with_shape(ss, ROIS.x_ptv_56.name): 
      OF.fall_off(ss, plan, ROIS.x_ptv_56.name, 77*100, 56*100, 0.5, 3)
    OF.fall_off(ss, plan, ROIS.external.name, 77*100, 30*100, 3.5, 3)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 100)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.rectum.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 3, 3)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.anal_canal.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
    OF.max_eud(ss, plan, ROIS.bladder.name, 30*100, 1, 1) #ses på
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 1)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 1)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 3)
    OF.min_dose(ss, plan, ROIS.ptv.name, 0.95*total_dose*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv.name, 1.05*total_dose*100, 100)
    OF.max_dose(ss, plan, ROIS.external.name, 1.05*total_dose*100, 100)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose/2*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 20*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 20*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 20*100, 2, 1)
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 44*100, 1)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 44*100, 1)




# Prostate bed
def create_prostate_bed_objectives(ss, plan, total_dose):
  if total_dose > 69:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb_70.name, total_dose*100, 3)
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    for c in ctv_n_70: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, total_dose*100, 3)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      OF.uniform_dose(ss, plan, ROIS.x_ctv_56.name, 56*100, 10)
    OF.min_dose(ss, plan, ROIS.ptv_sb_70.name, 66.5*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv_sb_70.name, 73.5*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name): # With boost to lymph node
      OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.5*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73.5*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      OF.min_dose(ss, plan, ROIS.x_ptv_56.name, 53.2*100, 100)
      OF.max_dose(ss, plan, ROIS.x_ptv_56.name, 58.8*100, 100)
      OF.fall_off(ss, plan, ROIS.ptv_e_56.name, 70*100, 56*100, 0.5, 3)
    OF.max_dose(ss, plan, ROIS.external.name, 73.5*100, 100)
    OF.fall_off(ss, plan, ROIS.external.name, 70*100, 30*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 2.5, 3)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 0)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 0)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb.name, total_dose*100, 3)
    OF.min_dose(ss, plan, ROIS.ptv_sb.name, total_dose*0.95*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv_sb.name, total_dose*1.05*100, 100)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*1.05*100, 100)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose/2*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 2.5, 3)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 0)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 0)


# Gyn
'''
def create_gyn_objectives(plan, ss, total_dose):
  if total_dose == 45:
    OF.min_eud(ss, plan, ROIS.ctv_45.name, 44.9*100, 1, 100)
    OF.max_eud(ss, plan, ROIS.ctv_45.name, 45.2*100, 1, 100)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)
    OF.max_dose(ss, plan, ROIS.ptv_45.name, 47.5*100, 400)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46*100, 10)
    OF.max_dose(ss, plan, ROIS.body.name, 47.5*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, 46*100, 5*100, 5, 1)
    OF.fall_off(ss, plan, ROIS.body.name, 46*100, 36*100, 1.5, 3)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 3*100, 1, 50)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 3*100, 1, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 30*100, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 38*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 46*100, 15*100, 10, 3) 
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 46.5*100, 20)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 46*100, 6*100, 5, 3)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 35*100, 1, 0.5)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 46.5*100, 10)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 46.5*100, 10)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 40*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.bladder.name, 46.5*100, 20)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
    OF.max_eud(ss, plan, ROIS.femoral_l.name, 38*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.femoral_r.name, 38*100, 1, 1)
  if total_dose == 55:
    OF.min_dose(ss, plan, ROIS.ctv_n_55.name, 55*100, 600)
    OF.min_dvh(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)
    OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 52.3*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58.8*100, 600)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 20)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_45.name, 45*100, 20)
    OF.fall_off(ss, plan, ROIS.body.name, 56*100, 45*100, 1.5, 3)
    OF.fall_off(ss, plan, ROIS.body.name, 56*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.body.name, 58.8*100, 100)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 50)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 30*100, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 38*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 56*100, 15*100, 5, 5)
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 46.5*100, 20)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 56*100, 5)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 35*100, 1, 0.5)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 56*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 46.5*100, 10)
    OF.max_dose(ss, plan, ROIS.bladder.name, 46.5*100, 20)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 42*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 20)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 20)
    OF.max_eud(ss, plan, ROIS.femoral_l.name, 38*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.femoral_r.name, 38*100, 1, 1)
  elif total_dose == 57.5:
    OF.min_dose(ss, plan, ROIS.ctv_n_57.name, 57.5*100, 600)
    OF.min_dvh(ss, plan, ROIS.ctv_n_57.name, 58.7*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_n_55.name, 55*100, 600)
    OF.min_dvh(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.8*100, 800)
    OF.min_dose(ss, plan, ROIS.ptv_n_57.name, 54.7*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_57.name, 61.5*100, 600)
    OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 52.3*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58.8*100, 600)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 30)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_45.name, 45*100, 2)
    OF.fall_off(ss, plan, ROIS.body.name, 58*100, 45*100, 1.5, 3)
    OF.fall_off(ss, plan, ROIS.body.name, 58*100, 15*100, 5, 1)
    OF.max_dose(ss, plan, ROIS.body.name, 61*100, 400)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 30)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 30)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 48*100, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 58*100, 15*100, 5, 5)
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 47*100, 20)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 57.5*100, 10)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 40*100, 1, 0.5)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 58*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 47*100, 5)
    OF.max_dose(ss, plan, ROIS.bladder.name, 46.5*100, 20)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 42*100, 1, 0.5)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
'''
def create_gyn_objectives(plan, ss, total_dose):
  if total_dose == 45:
    OF.min_eud(ss, plan, ROIS.ctv_45.name, 44.9*100, 1, 100)
    OF.max_eud(ss, plan, ROIS.ctv_45.name, 45.2*100, 1, 100)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)
    OF.max_dose(ss, plan, ROIS.ptv_45.name, 47.5*100, 400)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46*100, 10)
    OF.max_dose(ss, plan, ROIS.body.name, 47.5*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, 46*100, 5*100, 5, 1)
    OF.fall_off(ss, plan, ROIS.body.name, 46*100, 36*100, 1.5, 3)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 3*100, 1, 50)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 3*100, 1, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 30*100, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 38*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 46*100, 15*100, 10, 3) 
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 46.5*100, 20)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 46*100, 6*100, 5, 3)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 35*100, 1, 0.5)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 46.5*100, 10)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 46.5*100, 10)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 40*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.bladder.name, 46.5*100, 20)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
    OF.max_eud(ss, plan, ROIS.femoral_l.name, 38*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.femoral_r.name, 38*100, 1, 1)
  if total_dose == 55:
    ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name]
    if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
      for c in ctv_n_55: # With boost to lymph node
        if SSF.has_roi_with_shape(ss, c):
          OF.min_dose(ss, plan, c, total_dose*100, 600)
          OF.min_dvh(ss, plan, c, 56.2*100, 50, 600)
    else:
      OF.min_dose(ss, plan, ROIS.ctv_n_55.name, total_dose*100, 600)
      OF.min_dvh(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 20)
    OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 52.3*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58.8*100, 600)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 20)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_45.name, 45*100, 20)
    OF.fall_off(ss, plan, ROIS.body.name, 56*100, 45*100, 1.5, 3)
    OF.fall_off(ss, plan, ROIS.body.name, 56*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.body.name, 58.8*100, 100)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 50)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 30*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 56*100, 15*100, 5, 5)
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 35*100, 1, 0.5)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 56*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 46.5*100, 10)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 42*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 20)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 20)
  elif total_dose == 57.5:
    OF.min_dose(ss, plan, ROIS.ctv_n_57.name, 57.5*100, 600)
    OF.min_dvh(ss, plan, ROIS.ctv_n_57.name, 58.7*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_n_55.name, 55*100, 600)
    OF.min_dvh(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 50, 600)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 44*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.8*100, 800)
    OF.min_dose(ss, plan, ROIS.ptv_n_57.name, 54.7*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_57.name, 61.5*100, 600)
    OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 52.3*100, 600)
    OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58.8*100, 600)
    OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 30)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_45.name, 45*100, 2)
    OF.fall_off(ss, plan, ROIS.body.name, 58*100, 45*100, 1.5, 3)
    OF.fall_off(ss, plan, ROIS.body.name, 58*100, 15*100, 5, 1)
    OF.max_dose(ss, plan, ROIS.body.name, 61*100, 400)
    OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 30)
    OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 30)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 48*100, 50)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 50*100, 50)
    OF.fall_off(ss, plan, ROIS.rectum.name, 58*100, 15*100, 5, 5)
    OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 47*100, 20)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 57.5*100, 10)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 40*100, 1, 0.5)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, 58*100, 15*100, 5, 3)
    OF.max_dose(ss, plan, ROIS.sigmoid.name, 47*100, 5)
    OF.max_dose(ss, plan, ROIS.bladder.name, 46.5*100, 20)
    OF.fall_off(ss, plan, ROIS.bladder.name, 46*100, 26*100, 5, 3) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 42*100, 1, 0.5)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
# Bladder
def create_bladder_objectives(plan, ss, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)
  OF.max_dvh(ss, plan, ROIS.femoral_l.name, 45*100, 2, 2)
  OF.max_dvh(ss, plan, ROIS.femoral_r.name, 45*100, 2, 2)


# Rectum
def create_rectum_objectives(ss, plan, total_dose):
  if total_dose == 50:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_50.name, total_dose*100, 20)
    OF.uniform_dose(ss, plan, ROIS.ctv_e_46_5.name, 46.5*100, 35)
    OF.min_dose(ss, plan, ROIS.ptv_e_46_5.name, 44.8*100, 200)
    OF.min_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*0.95*100, 150)
    OF.max_dvh(ss, plan, ROIS.ptv_e_46_5.name, total_dose*0.95*100, 3, 20)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 2, 10)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 20)
    OF.max_dvh(ss, plan, ROIS.femoral_l.name, 35*100, 2, 10)
    OF.max_dvh(ss, plan, ROIS.femoral_r.name, 35*100, 2, 10)
    OF.max_eud(ss, plan, ROIS.bladder.name, 28*100, 1, 2)
    OF.max_eud(ss, plan, ROIS.bowel_space.name, 20*100, 1, 5)
  #elif total_dose == 25:
  else: # (Had to to change this for a rare 1.5*30 case.)
    OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 35)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 50)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.8, 15)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 20)
    OF.max_eud(ss, plan, ROIS.bladder.name, 16.2*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.spc_bowel.name, 14*100, 1, 2)

# Rectum
def create_anus_objectives(ss, plan, total_dose):
  if total_dose == 50:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_50.name, total_dose*100, 20)
    OF.uniform_dose(ss, plan, ROIS.ctv_e_46.name, 46.5*100, 35)
    OF.min_dose(ss, plan, ROIS.ptv_e_46.name, 44.8*100, 200)
    OF.min_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*0.95*100, 150)
    OF.max_dvh(ss, plan, ROIS.ptv_e_46.name, total_dose*0.95*100, 3, 20)
    OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 2, 10)
    OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 20)
    OF.max_dvh(ss, plan, ROIS.femoral_l.name, 35*100, 2, 10)
    OF.max_dvh(ss, plan, ROIS.femoral_r.name, 35*100, 2, 10)
    OF.max_eud(ss, plan, ROIS.bladder.name, 28*100, 1, 2)
    OF.max_eud(ss, plan, ROIS.bowel_space.name, 20*100, 1, 5)



# Bone/Spine SBRT
def create_bone_stereotactic_objectives(ss, plan, total_dose):
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 200)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*106, 3*100, 3, 3)
  OF.fall_off(ss, plan, ROIS.z_ptv_wall.name, total_dose*100, 0.65*total_dose*100, 0.5, 10)
