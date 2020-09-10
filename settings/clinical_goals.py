# encoding: utf8

# Import local files:
import clinical_goal as CG
import rois as ROIS
import tolerance_doses as TOL
import roi_functions as ROIF
import structure_set_functions as SSF
import region_codes as RC


# Criterias:
at_most = 'AtMost'
at_least = 'AtLeast'

# Types:
volume_at_dose = 'VolumeAtDose'
abs_volume_at_dose = 'AbsoluteVolumeAtDose'
dose_at_abs_volume = 'DoseAtAbsoluteVolume'
dose_at_volume = 'DoseAtVolume'
average_dose = 'AverageDose'
homogeneity_index = 'HomogeneityIndex'
conformity_index = 'ConformityIndex'

# Priorities:
priority1 = 1
priority2 = 2
priority3 = 3
priority4 = 4
priority5 = 5
priority6 = 6
priority7 = 7
priority8 = 8

# Absolute volumes:
cc0 = 0
cc0_1 = 0.1
cc0_2 = 0.2
cc0_03 = 0.03
cc0_05 = 0.05
cc0_35 = 0.35
cc0_5 = 0.5
cc1 = 1
cc1_2 = 1.2
cc2 = 2
cc3 = 3
cc4 = 4
cc5 = 5
cc10 = 10
cc15 = 15
cc20 = 20
cc30 = 30
cc70 = 70
cc100 =100
cc195 = 195
cc200 = 200
cc250 = 250
cc310 = 310
cc350 = 350
cc500 = 500
cc700 = 700
cc1000 = 1000
cc1500 = 1500

# Percent volumes:

pc1 = 0.01
pc2 = 0.02
pc3 = 0.03
pc5 = 0.05
pc10 = 0.1
pc15 = 0.15
pc17 = 0.17
pc20 = 0.2
pc25 = 0.25
pc26 = 0.26
pc30 = 0.3
pc33 = 0.33
pc32 = 0.32
pc35 = 0.35
pc37 = 0.37
pc40 = 0.40
pc49 = 0.49
pc74_34 = 0.7434782608695
pc50 = 0.5
pc55 = 0.55
pc60 = 0.6
pc65 = 0.65
pc66 = 0.66
pc69_1 = 0.6909090909
pc70 = 0.7
pc71_3 = 0.713
pc72_36 = 0.7236363636
pc73_09 = 0.7309090909
pc75 = 0.75
pc76 = 0.76
pc76_36 = 0.763636363636
pc77_72 = 0.7772727272
pc78 = 0.78
pc78_26 = 0.7826086956521
pc78_4 = 0.784
pc79_6 = 0.796
pc80 = 0.8
pc80_4 = 0.804
pc80_71 = 0.80714285714
pc81_81 = 0.818181818181
pc83_82 = 0.838260869565
pc84 = 0.84
pc84_27 = 0.842727272727
pc84_6 = 0.846
pc85 = 0.85
pc86 = 0.86
pc88 = 0.88
pc86_36 = 0.863636
pc87_54= 0.87545454545454
pc88_36 = 0.8836
pc89_1 = 0.891
pc89_3 = 0.893
pc90 = 0.9
pc90_24 = 0.9024
pc90_25 = 0.9025
pc90_45 = 0.9045454545
pc90_86 = 0.9086956521739
pc91_36 = 0.9136363636
pc92 = 0.92
pc92_12 = 0.9212
pc93 = 0.93
pc93_53 = 0.9353
pc94_52 = 0.94525
pc94_47 = 0.9447
pc94 = 0.94
pc95 = 0.95
pc95_47 = 0.95475
pc95_65 = 0.9565217391304
pc95_88 = 0.9588
pc96 = 0.96
pc93_1 = 0.931
pc97 = 0.97
pc97_73 = 0.9773913043478
pc98 = 0.98
pc98_5 = 0.985
pc98_7 = 0.987
pc99 = 0.99
pc99_5 = 0.995
pc99_75 = 0.9975
pc99_8 = 0.998
pc99_9 = 0.999
pc100 = 1
pc100_5 = 1.005
pc105 = 1.05
pc102 = 1.02
pc102_43 = 1.0243478260869
pc102_08=1.0208695652173
pc103 = 1.03
pc107 = 1.07
pc110 = 1.1
pc132 = 1.32
pc139 = 1.386
pc140 = 1.4
pc147 = 1.469475655
pc150 = 1.5
pc170 = 1.7


# Create CG.ClinicalGoal objects:
# Example:
#ClinicalGoal(name, criteria, type, tolerance, value, priority)

# Create Clinical goals for ORGANS AT RISK
# (Sorted cranio-caudally)

# Brain:
def brain_oars(nr_fractions, region_code):
  if region_code in RC.brain_whole_codes:
    brain_oars = [
      CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority3),
      CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority3),
      CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0, priority3),
      CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0, priority3),
      CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean, None, priority3),
      CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_adx, cc0, priority3)
		]
  elif region_code in RC.brain_partial_codes:
    if nr_fractions == 1: # Stereotactic, one fraction
      brain_oars = [
        CG.ClinicalGoal(ROIS.brain_ptv.name, at_most, abs_volume_at_dose, cc10,TOL.brain_srt_1fx_v10,  priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_srt_1fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, abs_volume_at_dose, cc1,TOL.brainstem_srt_1fx_v1,  priority1),
        CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_srt_1fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, abs_volume_at_dose,cc0_2, TOL.optic_chiasm_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_1fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_1fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.eye_r.name, at_most, dose_at_abs_volume, TOL.eye_srt_1fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.eye_l.name, at_most, dose_at_abs_volume, TOL.eye_srt_1fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.skin.name, at_most, abs_volume_at_dose,cc10, TOL.skin_srt_1fx_v10,  priority3),
        CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_srt_1fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_srt_1fx_v0, cc0_03, priority4)
      ]
    elif nr_fractions == 3: # Stereotactic, three fractions litt strenge krav?
      brain_oars = [
        CG.ClinicalGoal(ROIS.brain_ptv.name, at_most, abs_volume_at_dose, cc10,TOL.brain_srt_3fx_v10,  priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, abs_volume_at_dose, cc1,TOL.brainstem_srt_3fx_v1,  priority1),
        CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, abs_volume_at_dose,  cc1,TOL.spinal_cord_srt_3fx_v1, priority1),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_chiasm_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_3fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_3fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.eye_r.name, at_most, dose_at_abs_volume, TOL.eye_srt_3fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.eye_l.name, at_most, dose_at_abs_volume, TOL.eye_srt_3fx_v0, cc0_03, priority3),
        CG.ClinicalGoal(ROIS.skin.name, at_most, abs_volume_at_dose,  cc10,TOL.skin_srt_3fx_v10, priority3),
        CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_srt_3fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_srt_3fx_v0, cc0_03, priority4)
      ]
    else: # Partial brain 
      brain_oars = [
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.brain.name, at_most, dose_at_abs_volume, TOL.brain_v003, cc3, priority5),
        CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority5),
        CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority5),
        CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean, None, priority5),
        CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean, None, priority5),
        CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean, None, priority5),
        CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_2_mean, None, priority5),
        CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_adx, cc0_03, priority5),
	CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_adx, cc0_03, priority5),
	CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_adx, cc0_03, priority6),
	CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean, None, priority4),
	CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean, None, priority4),
	CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_v40, pc40, priority6),
	CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_v40, pc40, priority6)
      ]
  return brain_oars


'''
# Når ny prosedyre for del av hjerne og total hjerne er på plass
partial_brain = [
  CG.ClinicalGoal(ROIS.brain.name, at_most, dose_at_abs_volume, TOL.brain_v0.03, cc0, priority1)
  CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_v0.03_adx, cc0, priority1),
  CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_v0.03_adx, cc0, priority1),
  CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_v0.03_adx, cc0, priority2),
  CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_l_v0.03_adx, cc0, priority2),
  CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_r_v0.03_adx, cc0, priority2),
  CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_l_mean, None, priority2),
  CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_r_mean, None, priority2),
  CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, average_dose, TOL.hippocampus_l_mean, None, priority2),
  CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, average_dose, TOL.hippocampus_r_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_l_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_r_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_l_v0.03_adx, cc0, priority3),
  CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_r_v0.03_adx, cc0, priority3),
  CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean, None, priority1),
  CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_l_v0.03_adx, cc0, priority2),
  CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_r_v0.03_adx, cc0, priority2),
  CG.ClinicalGoal(ROIS.scalp.name, at_most, dose_at_abs_volume, TOL.scalp_v0.03_adx, cc0, priority3)
]
whole_brain = [
  CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_l_mean, None, priority2),
  CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_r_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_l_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_r_mean, None, priority2),
  CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_l_v0.03_adx, cc0, priority3),
  CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_r_v0.03_adx, cc0, priority3),
  CG.ClinicalGoal(ROIS.scalp.name, at_most, dose_at_abs_volume, TOL.scalp_v0.03_adx, cc0, priority3)
]
'''
def head_neck_oars(nr_fractions):
  if nr_fractions == 30:
    head_neck_oars = [
      CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotid_mean_30, None, priority4),
      CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotid_mean_30, None, priority4),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_30_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_30_v003_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_30_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_30_v003_adx, cc0_03, priority2)
    ]
  elif nr_fractions == 33:
    head_neck_oars = [
      CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotid_mean_33, None, priority4),
      CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotid_mean_33, None, priority4),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_33_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_33_v003_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_33_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_33_v003_adx, cc0_03, priority2)
    ]
  elif nr_fractions == 34:
    head_neck_oars = [
      CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotid_mean_34, None, priority4),
      CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotid_mean_34, None, priority4),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_34_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_34_v003_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_34_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_34_v003_adx, cc0_03, priority2)
    ]
  elif nr_fractions == 35:
    head_neck_oars = [
      CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotid_mean_35, None, priority4),
      CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotid_mean_35, None, priority4),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_35_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_35_v003_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_35_v003_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2), #0.03?
      CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_35_v003_adx, cc0_03, priority2)
    ]
  return head_neck_oars

# Breast tangential:
breast_tang_oars = [
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast, None, priority3),
  CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
  CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4)
]


# Breast with regional lymph nodes, clinical goal for 'Humeral_L' is added for left sided and vice versa
def breast_oars(region_code, nr_fractions, target):
  if region_code in RC.breast_reg_l_codes: # Left
    breast = [
      #CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v2_adx, cc2, priority1),
      CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast_15, None, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc33, TOL.lung_v30_adx_15, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc55, TOL.lung_v65_adx_15, priority5),
      CG.ClinicalGoal(ROIS.breast_r.name, at_most, average_dose, TOL.contralat_breast_mean, None, priority5),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contralateral_mean_reg,None, priority5)
    ]
  elif region_code in RC.breast_reg_r_codes: # Right
    breast = [
      #CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v2_adx, cc2, priority1),
      CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast_15, None, priority4),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc33, TOL.lung_v30_adx_15, priority4),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc55, TOL.lung_v65_adx_15, priority5),
      CG.ClinicalGoal(ROIS.breast_l.name, at_most, average_dose, TOL.contralat_breast_mean, None, priority5),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contralateral_mean_reg,None, priority5)
    ]
  elif region_code in RC.breast_tang_l_codes:
    breast = [
      CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast_tang, None, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contralateral_mean,None, priority5),
      CG.ClinicalGoal(ROIS.breast_r.name, at_most, average_dose, TOL.contralat_breast_mean, None, priority5)
    ]
  elif region_code in RC.breast_tang_r_codes:
    breast = [
      CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast_tang, None, priority4),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contralateral_mean,None, priority5),
      CG.ClinicalGoal(ROIS.breast_l.name, at_most, average_dose, TOL.contralat_breast_mean, None, priority5)
    ]

  return breast

# Øsofagus
def esophagus_oars(ss, total_dose):
  if total_dose < 45:
    esophagus = [
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinal_cord_prv_23_v0_03_adx, cc0_03, priority2), #spinal canal
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc30, TOL.lung_23_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc30, TOL.lung_23_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc30, TOL.kidney_23_v30_adx, priority3), 
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc30, TOL.kidney_23_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_23_mean, None, priority3),#kidneys?
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_23_mean, None, priority3),
      CG.ClinicalGoal(ROIS.liver.name, at_most, volume_at_dose, pc60, TOL.liver_23_v60_adx, priority3),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_23_v30_adx, priority3) 
    ]
  elif total_dose == 50:
    esophagus = [
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcanal_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc30, TOL.lung_25_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc30, TOL.lung_25_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc30, TOL.kidney_25_v30_adx, priority3), 
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc30, TOL.kidney_25_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_25_mean, None, priority3),#kidneys?
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_25_mean, None, priority3),
      CG.ClinicalGoal(ROIS.liver.name, at_most, volume_at_dose, pc60, TOL.liver_25_v60_adx, priority3),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_25_v30_adx, priority3) 
    ]
  elif total_dose == 60:
    esophagus = [
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcanal_30_v0_03_adx, cc0_03, priority2), #spinal canal
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc30, TOL.lung_30_v35_adx, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc30, TOL.lung_30_v35_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc30, TOL.kidney_30_v30_adx, priority3), 
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc30, TOL.kidney_30_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_30_mean, None, priority3),#kidneys?
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_30_mean, None, priority3),
      CG.ClinicalGoal(ROIS.liver.name, at_most, volume_at_dose, pc60, TOL.liver_30_v60_adx, priority3),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_30_v30_adx, priority3)
    ]
  else:
    esophagus = [
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcord_33_v0_03_adx, cc0_03, priority2), #spinal canal
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume , TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5), #spinal canal
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc30, TOL.lung_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc30, TOL.lung_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc30, TOL.kidney_33_v30_adx, priority3), 
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc30, TOL.kidney_33_v30_adx, priority3),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_33_mean, None, priority3),#kidneys?
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_33_mean, None, priority3),
      CG.ClinicalGoal(ROIS.liver.name, at_most, volume_at_dose, pc60, TOL.liver_33_v60_adx, priority3),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx, priority3) 
    ]
  return esophagus
# Lung:
# In cases where a GTV/IGTV is present, clinical goals are created for 'Lungs-GTV'/'Lungs-IGTV' instead of 'Lungs'.
'''
  lung.extend([
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_33_v0_03_adx, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_33_v0_03_adx, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_v20_adx, priority3),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx, priority3),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v50_adx, priority3),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority2),
    CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc55, TOL.lung_v55_adx, priority4,
    CG.ClinicalGoal(ROIS.esophagus_prv.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume,  TOL.heart_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume,  TOL.trachea_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.trachea_prv.name, at_most, dose_at_abs_volume,  TOL.trachea_prv_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume,  TOL.bronchus_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.bronchus_prv.name, at_most, dose_at_abs_volume,  TOL.bronchus_prv_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.a_aorta.name, at_most, dose_at_abs_volume,  TOL.aorta_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.connective_tissue.name, at_most, dose_at_abs_volume,  TOL.connective_tissue_v1_33_adx ,cc1, priority2),
    CG.ClinicalGoal(ROIS.chest_wall.name, at_most, dose_at_abs_volume,  TOL.chestwall_v1_33_adx ,cc1, priority2),                 
  ])
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
    l = ROIS.lungs_gtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
    l = ROIS.lungs_igtv.name
  else:
    l = ROIS.lungs.name
  lung.extend([
    CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_v35_adx, priority3),
    CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_v55_adx, priority4),
    CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_mean, None, priority3)
  ])
'''
def lung_oars(ss, nr_fractions):
  lung = []

  if nr_fractions == 33:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_33_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_33_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v50_adx, priority4),
      CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority4),
    ])
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_v55_adx, priority5),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_mean, None, priority4)
    ])
    if SSF.has_roi_with_shape(ss, ROIS.esophagus_prv.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.esophagus_prv.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority4),
        CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume,  TOL.heart_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.trachea.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume,  TOL.trachea_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.spinal_cord.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_33_v0_03_adx, cc0_03, priority2)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.spinal_cord_prv.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_33_v0_03_adx, cc0_03, priority2)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.trachea_prv.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.trachea_prv.name, at_most, dose_at_abs_volume,  TOL.trachea_prv_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.bronchus.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume,  TOL.bronchus_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.bronchus_prv.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.bronchus_prv.name, at_most, dose_at_abs_volume,  TOL.bronchus_prv_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.a_aorta.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.a_aorta.name, at_most, dose_at_abs_volume,  TOL.aorta_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.connective_tissue.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.connective_tissue.name, at_most, dose_at_abs_volume,  TOL.connective_tissue_v1_33_adx ,cc1, priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.chestwall.name):
      lung.extend([
        CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_v1_33_adx ,cc1, priority4)   
      ])
  elif nr_fractions == 30:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_30_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_30_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_30_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_30_v50_adx, priority4),
      CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_30_adx,cc1, priority4)
    ])
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_30_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_30_v55_adx, priority5),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_30_mean, None, priority3)
    ])
  elif nr_fractions == 35:
    lung = [
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_35_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_35_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_35_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v50_adx, priority4),
      CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_v1_35_adx,cc1,  priority4),
    ]
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_35_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_35_v55_adx, priority5),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_35_mean, None, priority4)
    ])
  elif nr_fractions == 15:
    lung = [
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_15_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_15_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_15_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_15_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_15_v50_adx, priority4),
      CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_v1_15_adx,cc1,  priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_15_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_15_v55_adx, priority5),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_15_mean, None, priority4)
    ])
  elif nr_fractions == 17:
    lung = [
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_17_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_17_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_17_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_17_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_17_v50_adx, priority4),
      CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_v1_17_adx,cc1,  priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_17_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_17_v55_adx, priority5),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_17_mean, None, priority4)
    ])
  else:
    lung = [
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.z_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority5)
    ]
  return lung



# Lung SBRT:
# For a treatment with three fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_3fx_oars(region_code):
  lung = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v1_2, cc1_2, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
    CG.ClinicalGoal(ROIS.liver.name, at_most, dose_at_abs_volume, TOL.liver_sbrt_3fx_v700 , cc700, priority3),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v4, cc4, priority1),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_3fx_v30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v0, cc0, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_3fx_v1500, cc1500, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_3fx_v1000, cc1000, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_3fx_v37, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc40, TOL.lung_sbrt_3fx_v40, priority3),
  ]
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v2, cc2, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_3fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v4, cc4, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_3fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v2, cc2, priority4),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v4, cc4, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_3fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v2, cc2, priority4),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v2, cc2, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_3fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v4, cc4, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_3fx_v4, cc4, priority1)
    ])
  return lung


# Lung SBRT:
# For a treatment with five fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_5fx_oars(region_code):
  lung = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v1_2, cc1_2, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
    CG.ClinicalGoal(ROIS.liver.name, at_most, dose_at_abs_volume, TOL.liver_sbrt_5fx_v700 , cc700, priority3),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_5fx_v4, cc4, priority1),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_5fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_5fx_v30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v0, cc0, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_5fx_v1500, cc1500, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_5fx_v1000, cc1000, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_5fx_v37, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc40, TOL.lung_sbrt_3fx_v40, priority3)
  ]
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.rib_x_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.rib_y_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.rib_x_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.rib_y_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  return lung


# Lung SBRT:
# For a treatment with eight fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_8fx_oars(region_code):
  lung= [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v1_2, cc1_2, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_8fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_8fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.greatves.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_8fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
    CG.ClinicalGoal(ROIS.liver.name, at_most, dose_at_abs_volume, TOL.liver_sbrt_5fx_v700 , cc700, priority3),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_5fx_v4, cc4, priority1),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_8fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_5fx_v30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v0, cc0, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_5fx_v1500, cc1500, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_5fx_v1000, cc1000, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_5fx_v37, priority3),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc40, TOL.lung_sbrt_3fx_v40, priority3),
  ]
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_r.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, average_dose, TOL.lung_contra_sbrt_5fx_mean, None, priority3),
      CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc26, TOL.lung_contra_sbrt_5fx_v26, priority3),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v1, cc1, priority4),
      CG.ClinicalGoal(ROIS.ribs_l.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.main_bronchus_r.name, at_most, dose_at_abs_volume, TOL.main_bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.main_bronchus_l.name, at_most, dose_at_abs_volume, TOL.main_bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  return lung
# Gyn:
'''
gyn_45_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority3),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority3),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc2, TOL.bladder_v2_adx, priority4)
]
'''
gyn_45_oars = [
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc85, TOL.bladder_v85_adx,  priority4),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc75, TOL.bladder_v75_adx,  priority4),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, dose_at_abs_volume, TOL.bladder_v003_adx, cc0_03, priority3),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc350, TOL.bowelbag_v350_adx, priority4),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc100, TOL.bowelbag_v100_adx, priority4),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, dose_at_abs_volume, TOL.bowelbag_v003_adx, cc0_03, priority3),
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_v003_adx, cc0_03, priority3),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc95, TOL.rectum_v95_adx,  priority4),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc85, TOL.rectum_v85_adx,  priority4),
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4),
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4),
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_10, None, priority3),
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_10, None, priority3),
  CG.ClinicalGoal(ROIS.ovary_r.name, at_most, average_dose, TOL.ovary_mean_5, None, priority4),
  CG.ClinicalGoal(ROIS.ovary_l.name, at_most, average_dose, TOL.ovary_mean_5, None, priority4),
  CG.ClinicalGoal(ROIS.ovary_r.name, at_most, average_dose, TOL.ovary_mean_8, None, priority3),
  CG.ClinicalGoal(ROIS.ovary_l.name, at_most, average_dose, TOL.ovary_mean_8, None, priority3),
  CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2),
  CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_38_v003_adx, cc0_03, priority5),
  CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_cord_prv_v003_adx, cc0_03, priority3),
  CG.ClinicalGoal(ROIS.sigmoid.name, at_most, dose_at_abs_volume, TOL.sigmoid_v003_adx, cc0_03, priority3)
]
# Gyn
gyn_55_oars = [
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc85, TOL.bladder_v85_adx,  priority5),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc75, TOL.bladder_v75_adx,  priority5),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, dose_at_abs_volume, TOL.bladder_v003_adx, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc500, TOL.bowelbag_v350_adx, priority5),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc250, TOL.bowelbag_v100_adx, priority5),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, dose_at_abs_volume, TOL.bowelbag_v003_adx, cc0_03, priority6),
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority5), #50
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority5), #50
  CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_v003_adx, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc95, TOL.rectum_v95_adx,  priority5),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc85, TOL.rectum_v85_adx,  priority5),
  #CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4), #15
  #CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4), #15
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_10, None, priority4),
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_10, None, priority4),
  #CG.ClinicalGoal(ROIS.ovary_r.name, at_most, average_dose, TOL.ovary_mean_5, None, priority4),
  #CG.ClinicalGoal(ROIS.ovary_l.name, at_most, average_dose, TOL.ovary_mean_5, None, priority4),
  CG.ClinicalGoal(ROIS.ovary_r.name, at_most, average_dose, TOL.ovary_mean_8, None, priority4),
  CG.ClinicalGoal(ROIS.ovary_l.name, at_most, average_dose, TOL.ovary_mean_8, None, priority4),
  CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_48_v003_adx, cc0_03, priority2),
  #CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_38_v003_adx, cc0_03, priority5),
  #CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_cord_prv_v003_adx, cc0_03, priority3),
  CG.ClinicalGoal(ROIS.sigmoid.name, at_most, dose_at_abs_volume, TOL.sigmoid_v003_adx, cc0_03, priority4)
]
# Rectum
rectum_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, volume_at_dose, pc2, TOL.femoral_25_v2_adx, priority3),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, volume_at_dose, pc2, TOL.femoral_25_v2_adx, priority3),
  #CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority3),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc310, TOL.bowelspace_25_v310_adx, priority3),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc70, TOL.bowelspace_25_v70_adx, priority3),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_25_adx,None, priority3)
]

# Anus:
anus_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, volume_at_dose, pc2, TOL.femoral_27_v2_adx, priority3),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, volume_at_dose, pc2, TOL.femoral_27_v2_adx, priority3),
  #CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority3),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc310, TOL.bowelspace_27_v310_adx, priority4),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc70, TOL.bowelspace_27_v70_adx, priority4),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_27_adx, None,priority3)
]
'''
# Rectum: må fikses
rectum_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority3),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc2, TOL.bladder_v2_adx, priority3)
]

# Anus: må fikses
anus_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority3),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc2, TOL.bladder_v2_adx, priority3)
]
'''

# Bladder:
bladder_oars = [
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx,  priority2),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx,  priority2),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx,  priority2),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority2),
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority3)
]

# Prostate:
def prostate_oars(ss, total_dose):
  if total_dose in [55, 60]:
    prostate = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_hypo, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc35, TOL.bladder_v35_adx_hypo, priority5),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, volume_at_dose, pc90, TOL.penile_bulb_v90_adx_hypo,  priority6),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume,  TOL.femoral_v2_adx_hypo,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo,pc2,   priority6)
    ]
  elif total_dose > 60:
    prostate = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc35, TOL.bladder_v35_adx, priority5),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx,  priority4),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, volume_at_dose, pc90, TOL.penile_bulb_v90_adx,  priority6),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_v2_adx,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx,pc2,  priority6),
      CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority5)
    ]
    if total_dose > 70:
      prostate.extend([
        CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority4),
        CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority4),
        CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc25, TOL.bladder_v25_adx, priority5),
        CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc15, TOL.bladder_v15_adx, priority5)
      ])
    else:
      prostate.extend([
        CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx,  priority4)
      ])  
  elif total_dose <40:
    prostate = [
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume,  TOL.femoral_v2_adx_hypo,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo,pc2,   priority6),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_hypo, priority5)
    ]

  return prostate

# Bone/Spine SBRT:
# For a treatment with one fraction, from the region code, one finds whether the
# tumor is in the thoracic or pelvis area, and clinical goals are added accordingly.
# There is also a separation between spine/non-spine treatment.
def bone_stereotactic_1fx_oars(region_code):
  spine= [
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, dose_at_volume, TOL.kidney_hilum_1fx_v66, pc66, priority3),
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, dose_at_volume, TOL.kidney_hilum_1fx_v66, pc66, priority3),
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, dose_at_volume, TOL.kidney_sbrt_1fx_v0, cc0, priority3),
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, dose_at_volume, TOL.kidney_sbrt_1fx_v0, cc0, priority3),
    CG.ClinicalGoal(ROIS.kidneys.name, at_most, dose_at_abs_volume, TOL.kidneys_col_1fx_v200, cc200, priority3),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_1fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_1fx_v0, cc0, priority4)
  ]
  if region_code in RC.stereotactic_spine_thorax_codes or region_code in RC.stereotactic_spine_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_1fx_v0_35, cc0_35, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_1fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_3mm_sbrt_1fx_v0_1, cc0_1, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_3mm_sbrt_1fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_1fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_1fx_v0, cc5, priority1)
    ])
    if region_code in RC.stereotactic_spine_thorax_codes:
      spine.extend([
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_1fx_v5, cc5, priority2),
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_1fx_v0, cc0, priority2),
        CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_1fx_v15, cc15, priority2),
        CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_1fx_v0, cc0, priority2),
        CG.ClinicalGoal(ROIS.lungs.name, at_most, dose_at_abs_volume, TOL.lungs_sbrt_1fx_v1000, cc1000, priority2),
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_1fx_v4, cc4, priority1),
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_1fx_v0, cc0, priority1)
      ])

  if region_code in RC.stereotactic_spine_pelvis_codes or region_code in RC.stereotactic_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.small_bowel.name, at_most, dose_at_abs_volume, TOL.small_bowel_sbrt_1fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.small_bowel.name, at_most, dose_at_abs_volume, TOL.small_bowel_sbrt_1fx_v5, cc5, priority3),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_1fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_1fx_v20, cc20, priority3),
      CG.ClinicalGoal(ROIS.colon.name, at_most, dose_at_abs_volume, TOL.colon_sbrt_1fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.colon.name, at_most, dose_at_abs_volume, TOL.colon_sbrt_1fx_v20, cc20, priority3)
    ])
  return spine


# Bone/Spine SBRT:
# For a treatment with three fractions, from the region code, one finds whether the
# tumor is in the thoracic or pelvis area, and clinical goals are added accordingly.
# There is also a separation between spine/non-spine treatment.
def bone_stereotactic_3fx_oars(region_code):
  spine= [
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, dose_at_volume, TOL.kidney_3fx_v10, pc10, priority3),
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, dose_at_volume, TOL.kidney_3fx_v10, pc10, priority3),
    CG.ClinicalGoal(ROIS.kidneys.name, at_most, dose_at_abs_volume, TOL.kidneys_col_3fx_v200, cc200, priority3),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_col_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_col_sbrt_3fx_v0, cc0, priority4)
  ]
  if region_code in RC.stereotactic_spine_thorax_codes or region_code in RC.stereotactic_spine_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v5, cc5, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0_35, cc0_35, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0, priority1)
    ])
    if region_code in RC.stereotactic_spine_thorax_codes:
      spine.extend([
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0, priority2),
        CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v15, cc15, priority2),
        CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v0, cc0, priority2),
        CG.ClinicalGoal(ROIS.lungs.name, at_most, dose_at_abs_volume, TOL.lung_sbrt_3fx_v1000, cc1000, priority2),
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v4, cc4, priority1),
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v0, cc0, priority1),
      ])
  if region_code in RC.stereotactic_spine_pelvis_codes or region_code in RC.stereotactic_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.small_bowel.name, at_most, dose_at_abs_volume, TOL.small_bowel_sbrt_3fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.small_bowel.name, at_most, dose_at_abs_volume, TOL.small_bowel_sbrt_3fx_v5, cc5, priority3),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v20, cc20, priority3),
      CG.ClinicalGoal(ROIS.colon.name, at_most, dose_at_abs_volume, TOL.colon_sbrt_3fx_v0, cc0, priority3),
      CG.ClinicalGoal(ROIS.colon.name, at_most, dose_at_abs_volume, TOL.colon_sbrt_3fx_v20, cc20, priority3)
    ])
  return spine


# Palliative:
head = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0, priority4),
  CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0, priority4),
  CG.ClinicalGoal(ROIS.brain.name, at_most, dose_at_abs_volume, TOL.brain_v003, cc0, priority3)
]
neck = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.parotids.name, at_most, average_dose, TOL.parotids_mean, None, priority3)
]
thorax = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean, None, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_v30_adx, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc60, TOL.heart_v60_adx, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc80, TOL.heart_v80_adx, priority2),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc30, TOL.lung_v30_adx, priority3),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc35, TOL.lung_v35_adx, priority2),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, average_dose, TOL.lung_mean, None, priority2)
]
thorax_and_abdomen = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean, None, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_v30_adx, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc60, TOL.heart_v60_adx, priority2),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc80, TOL.heart_v80_adx, priority2),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc30, TOL.lung_v30_adx, priority3),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc35, TOL.lung_v35_adx, priority2),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, average_dose, TOL.lung_mean, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx, priority2),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2)
]
abdomen = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx, priority2),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2)
]
abdomen_and_pelvis = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_volume, TOL.spinalcord_v2_adx, pc2, priority1),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx, priority2),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx, priority3),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx,  priority2)
]
pelvis = [
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx, priority3),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx,  priority2)
]
other = []




# Create Clinical goals for TARGETS
# (Sorted cranio-caudally)

# Common targets:
# Used for simple cases and most palliative cases.
targets = [
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95, pc99_5, priority2),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority2),
  #CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
  #CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc95, priority5),
  CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
]

# Palliative thorax targets:
# FIXME: Er det riktig å ha andre krav for thorax relaterte palliative MV?!? Vurdere å ta bort.
thorax_targets = [
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc95, pc98, priority2),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc95, pc95, priority5),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc90, pc95, priority5),
  CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
]

# Palliative:
def palliative_targets(ss, plan, target):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  targets = [CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)]
  if nr_targets > 1 and len(list(plan.BeamSets)) > 1:
    for i in range(0, nr_targets):
      targets.extend([
        CG.ClinicalGoal(ROIS.ctv.name+str(i+1), at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv.name+str(i+1), at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv.name+str(i+1), at_least, volume_at_dose, pc95, pc99_5, priority2),
        CG.ClinicalGoal(ROIS.ptv.name+str(i+1), at_least, volume_at_dose, pc95, pc98, priority2),
        #CG.ClinicalGoal(ROIS.ctv.name+str(i+1), at_least, homogeneity_index, pc95, pc98, priority5),
        #CG.ClinicalGoal(ROIS.ptv.name+str(i+1), at_least, conformity_index, pc90, pc95, priority5)
      ])
  else:
    targets.extend([
      CG.ClinicalGoal(target, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(target, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(target, at_least, volume_at_dose, pc95, pc99_5, priority2),
      CG.ClinicalGoal(target.replace("C", "P"), at_least, volume_at_dose, pc95, pc98, priority2),
      #CG.ClinicalGoal(target, at_least, homogeneity_index, pc95, pc98, priority5),
      #CG.ClinicalGoal(target.replace("C", "P"), at_least, conformity_index, pc90, pc95, priority5)
    ])

  return targets


# Brain:
def brain_targets(ss, nr_fractions):
  if nr_fractions in [1,3]: # Stereotactic, one target
    if nr_fractions == 1:
      gtv_dose = 22
      max_dose = 30
    elif nr_fractions == 3:
      gtv_dose = 29
      max_dose = 38
    brain_targets = [
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc100, pc98_5, priority1),
      CG.ClinicalGoal(ROIS.gtv.name, at_least, dose_at_volume, pc100*gtv_dose, pc99_9, priority5),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc100*max_dose, cc0, priority4)
    ]
    nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
    if nr_targets in [2, 3, 4]: # Stereotactic, 2, 3 or 4 targets
      brain_targets.extend([
        CG.ClinicalGoal(ROIS.ptv1.name, at_least, dose_at_volume, pc100, pc98_5, priority1),
        CG.ClinicalGoal(ROIS.gtv1.name, at_least, dose_at_volume, pc100*gtv_dose, pc99_9, priority5),
        CG.ClinicalGoal(ROIS.ptv1.name, at_least, conformity_index, pc90, pc100, priority5),
        CG.ClinicalGoal(ROIS.ptv2.name, at_least, dose_at_volume, pc100, pc98_5, priority1),
        CG.ClinicalGoal(ROIS.gtv2.name, at_least, dose_at_volume, pc100*gtv_dose, pc99_9, priority5),
        CG.ClinicalGoal(ROIS.ptv2.name, at_least, conformity_index, pc90, pc100, priority5),
      ])
      if nr_targets in [3, 4]: # Stereotactic, 3 or 4 targets
        brain_targets.extend([
          CG.ClinicalGoal(ROIS.ptv3.name, at_least, dose_at_volume, pc100, pc98_5, priority1),
          CG.ClinicalGoal(ROIS.gtv3.name, at_least, dose_at_volume, pc100*gtv_dose, pc99_9, priority5),
          CG.ClinicalGoal(ROIS.ptv3.name, at_least, conformity_index, pc90, pc100, priority5)
        ])
        if nr_targets == 4: # Stereotactic, 4 targets
          brain_targets.extend([
            CG.ClinicalGoal(ROIS.ptv4.name, at_least, dose_at_volume, pc100, pc98_5, priority1),
            CG.ClinicalGoal(ROIS.gtv4.name, at_least, dose_at_volume, pc100*gtv_dose, pc99_9, priority5),
            CG.ClinicalGoal(ROIS.ptv4.name, at_least, conformity_index, pc90, pc100, priority5)
        ])
  else: # Whole brain or partial brain MÅ FIKSES
    brain_targets = [
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95,pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
      #CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
      #CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc95, pc95, priority5),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
  return brain_targets

def head_neck_targets(ss, total_dose):
  head_neck_targets = []
  if total_dose == 60:
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, dose_at_volume, pc99_5*60, pc50, priority1), 
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_most, dose_at_volume, pc100_5*60, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, volume_at_dose, pc95*60, pc99_5, priority3), 
        CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_sb_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_54.name, at_most, dose_at_abs_volume, pc105*54, cc2, priority4),
        CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ])
    elif SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, dose_at_volume, pc99_5*60, pc50, priority1), 
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_most, dose_at_volume, pc100_5*60, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_50.name, at_least, dose_at_volume, pc99_5*50, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_50.name, at_most, dose_at_volume, pc100_5*50, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, volume_at_dose, pc95*60, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_sb_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ctv_50.name, at_least, volume_at_dose, pc95*50, pc99_5, priority3), 
        CG.ClinicalGoal(ROIS.x_ptv_50.name, at_least, volume_at_dose, pc95*50, pc98, priority3), 
        CG.ClinicalGoal(ROIS.x_ptv_50.name, at_most, dose_at_abs_volume, pc105*50, cc2, priority4),
        CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ])
  if total_dose == 66:
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_sb_66.name, at_least, dose_at_volume, pc99_5*66, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_sb_66.name, at_most, dose_at_volume, pc100_5*66, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_sb_66.name, at_least, volume_at_dose, pc95*66, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, volume_at_dose, pc95*60, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_sb_66.name, at_least, volume_at_dose, pc95*66, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_sb_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_most, dose_at_abs_volume, pc105*54, cc2, priority4),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ])

  if total_dose == 68: 
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_p_68.name, at_least, dose_at_volume, pc99_5*68, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_68.name, at_most, dose_at_volume, pc100_5*68, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_68.name, at_least, volume_at_dose, pc95*68, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ctv_p_60.name, at_least, volume_at_dose, pc95*60, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p_68.name, at_least, volume_at_dose, pc95*68, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_n_68.name, at_least, volume_at_dose, pc95*68, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_p_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_n_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_most, dose_at_abs_volume, pc105*54, cc2, priority4),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ])
    ctv_n_68 = [ROIS.ctv_n_68.name, ROIS.ctv_n1_68.name,ROIS.ctv_n2_68.name,ROIS.ctv_n3_68.name]
    ctv_n_60 = [ROIS.ctv_n_60.name, ROIS.ctv_n1_60.name,ROIS.ctv_n2_60.name,ROIS.ctv_n3_60.name]
    for c in ctv_n_68:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([                             
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*68, pc99_5, priority3),
         CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*68, pc50, priority1),
         CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*68, pc50, priority1)
      ])
    for c in ctv_n_60:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([  
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*60, pc99_5, priority3)
       ])

  if total_dose == 70:
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_p_70.name, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_70.name, at_most, dose_at_volume, pc100_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_70.name, at_least, volume_at_dose, pc95*70, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ctv_p_60.name, at_least, volume_at_dose, pc95*60, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.x_ctv_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_p_70.name, at_least, volume_at_dose, pc95*70, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_p_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_54.name, at_most, dose_at_abs_volume, pc105*54, cc2, priority4),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ])
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    ctv_n_60 = [ROIS.ctv_n_60.name, ROIS.ctv_n1_60.name,ROIS.ctv_n2_60.name,ROIS.ctv_n3_60.name]
    for c in ctv_n_70:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([                             
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*70, pc99_5, priority3), 
         CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
         CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*70, pc50, priority1)
       ])
    for c in ctv_n_60:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([  
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*60, pc99_5, priority3)
       ])        

  return head_neck_targets

# Breast:
def breast_targets(ss, region_code, target):
  if region_code in RC.breast_reg_codes: # Regional lymph nodes
    breast_targets = [
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_n.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_pc.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_nc.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.imn.name):
      breast_targets.extend([
        CG.ClinicalGoal(ROIS.imn.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.imn.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.imn.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_n_imn.name, at_least, volume_at_dose, pc95, pc98, priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ctv_boost.name): # If there is a 2 Gy x 8 boost
      breast_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_least, dose_at_volume, pc99_5*16*100, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_most, dose_at_volume, pc100_5*16*100, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_least, volume_at_dose, 16*0.95*100, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_boost.name, at_least, volume_at_dose, 16*0.95*100, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc139, cc2, priority4)
      ])
  else: # Tangential
    breast_targets = [
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_pc.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.ctv_sb.name): # If there is a 2 Gy x 8 boost
      breast_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_least, dose_at_volume, pc99_5*16*100, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_most, dose_at_volume, pc100_5*16*100, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_boost.name, at_least, volume_at_dose, 16*0.95*100, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_boost.name, at_least, volume_at_dose, 16*0.95*100, pc98, priority3),
        CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc147, cc2, priority4)
      ])
  return breast_targets

def esophagus_targets(ss, total_dose):
  if total_dose == 66:
    dose = str(66)
  elif total_dose == 60:
    dose = str(60)
  elif total_dose == 41.4:
    dose = str(41.4)
  elif total_dose == 50:
    dose = str(50)
  esophagus_targets = [
    CG.ClinicalGoal(ROIS.ctv_p.name+"_"+dose, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_p.name+"_"+dose, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_n.name+"_"+dose, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_n.name+"_"+dose, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_p.name+"_"+dose, at_least, dose_at_volume, pc95, pc98, priority2),
    CG.ClinicalGoal(ROIS.ctv_n.name+"_"+dose, at_least, dose_at_volume, pc95, pc98, priority2),
    CG.ClinicalGoal(ROIS.ptv_p.name+"_"+dose, at_least, dose_at_volume, pc95, pc98, priority2),
    CG.ClinicalGoal(ROIS.ptv_n.name+"_"+dose, at_least, dose_at_volume, pc95, pc98, priority2)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_46.name):
    esophagus_targets.extend([
      CG.ClinicalGoal(ROIS.x_ctv_46.name, at_least, dose_at_volume, pc99_5*46, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_46.name, at_most, dose_at_volume, pc100_5*46, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_46.name, at_least, dose_at_volume, pc95*46, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_e_46.name, at_least, dose_at_volume, pc95*46, pc98, priority2)
    ])
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_e_41_4.name):
    esophagus_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_e_41_4.name, at_least, dose_at_volume, pc99_5*41_4, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_41_4.name, at_most, dose_at_volume, pc100_5*41_4, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_41_4.name, at_least, dose_at_volume, pc95*41_4, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_e_41_4.name, at_least, dose_at_volume, pc95*41_4, pc98, priority2)
    ])
  return esophagus_targets
  

# Lung SBRT:
def lung_stereotactic_targets(ss):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)

  targets = [
    CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc140, cc2, priority4),
    CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc150, cc0, priority4)
  ]
  if nr_targets == 1:
    targets.extend([
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc100, pc99, priority1),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc88, pc100, priority5),
      CG.ClinicalGoal(ROIS.igtv.name, at_most, dose_at_abs_volume, pc150, cc0, priority5)
    ])
  else:
    for i in range(0, nr_targets):
      targets.extend([
        CG.ClinicalGoal(ROIS.ptv.name+str(i+1), at_least, dose_at_volume, pc100, pc99, priority1),
        CG.ClinicalGoal(ROIS.ptv.name+str(i+1), at_least, conformity_index, pc88, pc100, priority5),
        CG.ClinicalGoal(ROIS.igtv.name+str(i+1), at_most, dose_at_abs_volume, pc150, cc0, priority5)
      ])
  return targets


# Lung:
def lung_targets(ss):
  lung = [
    CG.ClinicalGoal(ROIS.ictv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ictv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.x_ptv_vev.name, at_least, volume_at_dose, pc95, pc98, priority3),
    CG.ClinicalGoal(ROIS.x_ptv_lunge.name, at_least, volume_at_dose, pc90, pc99_5, priority3),
    CG.ClinicalGoal(ROIS.ictv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
    CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ]
  ictv_n = [ROIS.ictv_n.name,ROIS.ictv_n1.name, ROIS.ictv_n2.name,ROIS.ictv_n3.name,ROIS.ictv_n4.name,ROIS.ictv_n5.name,ROIS.ictv_n6.name]
  for c in ictv_n:
   if SSF.has_roi_with_shape(ss, c):
     lung.extend([                             
       CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
       CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
       CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3)
     ])
  if SSF.has_roi_with_shape(ss, ROIS.bronchus_prv.name): 
    lung.extend([
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc110*66, cc0_03, priority5),
      CG.ClinicalGoal(ROIS.body.name, at_most, abs_volume_at_dose, pc107*66,cc5, priority5) #denne er litt rart definert i funksjon
    ])
  return lung


# Bone/Spine SBRT:
bone_stereotactic_targets = [
  CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc100, pc99, priority1),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5),
  CG.ClinicalGoal(ROIS.gtv.name, at_most, dose_at_abs_volume, pc150, cc0, priority5)
]


# Prostate:
def prostate_targets(ss, total_dose):
  prostate = [CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)]
  if total_dose == 77: # Normo-fractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ptv_p2_70.name, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.ptv_p2_70.name, at_most, dose_at_volume, pc100_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_p2_70.name, at_least, volume_at_dose, pc95*70, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p1_77.name, at_least, volume_at_dose, pc95, pc98,  priority3),
      CG.ClinicalGoal(ROIS.ptv_p2_70.name, at_least, volume_at_dose, pc95*70, pc98, priority3),
    ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      prostate.extend([
        CG.ClinicalGoal(ROIS.x_ctv_56.name, at_least, dose_at_volume, pc99_5*56, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_56.name, at_most, dose_at_volume, pc100_5*56, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_56.name, at_least, volume_at_dose, pc95*56, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_e_56.name, at_least, volume_at_dose, pc95*56, pc98, priority3)
      ])
  elif total_dose == 60: # Hypofractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p2_60.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p2_60.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_p2_60.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p1_60.name, at_least, volume_at_dose, pc95, pc98,  priority3),
      CG.ClinicalGoal(ROIS.ptv_p2_60.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])
  else: # Hypofractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98,  priority3)
    ])

  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
    prostate.extend([
      CG.ClinicalGoal(ROIS.ptv_n_70.name, at_least, volume_at_dose, pc95*70, pc98, priority3)
    ])
  ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
  for c in ctv_n_70:
    if SSF.has_roi_with_shape(ss, c):
      prostate.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*70, pc50, priority1),
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*70, pc99_5, priority3),
        ])
  return prostate

def prostate_bed_targets(ss):
  prostate_bed= [
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_least, volume_at_dose,pc98,pc99_5, priority3),
    CG.ClinicalGoal(ROIS.ptv_sb_70.name, at_least, volume_at_dose, pc95, pc98, priority3)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
    prostate_bed.extend([
      CG.ClinicalGoal(ROIS.ctv_e_56.name, at_least, dose_at_volume, pc99_5*56, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_56.name, at_most, dose_at_volume, pc100_5*56, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_56.name, at_least, volume_at_dose, pc95*56, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e_56.name, at_least, volume_at_dose, pc95*56, pc98, priority3),
    ])
  # With boost to positive lymph node 
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
    prostate_bed.extend([
      CG.ClinicalGoal(ROIS.ptv_n_70.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])
  ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
  for c in ctv_n_70:
    if SSF.has_roi_with_shape(ss, c):
      prostate_bed.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3),
        ])
  return prostate_bed
'''
# Prostate bed:
def prostate_bed_targets(ss):
  prostate_bed= [
    CG.ClinicalGoal(ROIS.ctv_70.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_70.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_70.name, at_least, dose_at_volume, pc98, pc98, priority2),
    CG.ClinicalGoal(ROIS.ptv_70.name, at_least, dose_at_volume, pc95, pc98, priority2),
    CG.ClinicalGoal(ROIS.ctv_70.name, at_least, homogeneity_index, pc95, pc95, priority5),
    CG.ClinicalGoal(ROIS.ptv_70.name, at_least, conformity_index, pc90, pc95, priority5),
    CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_56.name): # With lymph node volume
    prostate_bed.extend([
      CG.ClinicalGoal(ROIS.ctv_56.name, at_least, dose_at_volume, pc79_6, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_56.name, at_most, dose_at_volume, pc80_4, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_56.name, at_least, dose_at_volume, pc78_4, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_56.name, at_least, dose_at_volume, pc76, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_56.name, at_most, dose_at_volume,  pc84, pc5, priority5),
      CG.ClinicalGoal(ROIS.ptv_56_70.name, at_least, conformity_index, pc70, pc76, priority5)
    ])
  return prostate_bed
'''
# 57.5 Gy

#CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc95, pc74_34, priority1), egentlig dette
#CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, dose_at_volume, pc90_86, pc98, priority2), dette? egentlig 86.08
#CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, dose_at_volume, pc90, pc98, priority2), dette?
'''
def gyn_57_targets(ss):
  gyn = [
    CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc95*45, pc98, priority2),
    CG.ClinicalGoal(ROIS.ptv_45.name, at_most, dose_at_abs_volume, pc107*45, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.ctv_45.name, at_least, dose_at_volume, pc100*45, pc100, priority1), #average? D100> 95%
    #CG.ClinicalGoal(ROIS.ptv_45.name, at_least, dose_at_volume, pc95*45, pc98, priority2), 
    CG.ClinicalGoal(ROIS.x_gtv_p.name, at_most, dose_at_abs_volume, pc103*45, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.x_ptv_45.name, at_least, dose_at_volume, pc100*45, pc50, priority4)
  ]
  ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
    for c in ctv_n_57:
      if SSF.has_roi_with_shape(ss, c):
        gyn.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc100, pc98, priority1),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc102, pc50, priority4)
        ])
  else:
    gyn.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc100, pc98, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc102, pc50, priority4)
    ])
  ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
    for c in ctv_n_55:
      if SSF.has_roi_with_shape(ss, c):
        gyn.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc100*55, pc98, priority1),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc102*55, pc50, priority4)
        ])
  else:
    gyn.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc100*55, pc98, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc102*55, pc50, priority4)
    ])
  ptv_n_57 = [ROIS.ptv_n1_57.name,ROIS.ptv_n2_57.name,ROIS.ptv_n3_57.name,ROIS.ptv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n1_57.name):
    for p in ptv_n_57:
      if SSF.has_roi_with_shape(ss, p):
        gyn.extend([
          CG.ClinicalGoal(p, at_least, volume_at_dose, pc95, pc98, priority2), #flere ptv_n? #D98% > 90%
          CG.ClinicalGoal(p, at_most, dose_at_abs_volume, pc107, cc0_03, priority2)
        ])
  else:
    gyn.extend([
      CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, volume_at_dose, pc95, pc98, priority2), #flere ptv_n?
      CG.ClinicalGoal(ROIS.ptv_n_57.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority2)
    ])

  ptv_n_55 = [ROIS.ptv_n1_55.name,ROIS.ptv_n2_55.name,ROIS.ptv_n3_55.name,ROIS.ptv_n4_55.name]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n1_55.name):
    for p in ptv_n_55:
      if SSF.has_roi_with_shape(ss, p):
        gyn.extend([
          CG.ClinicalGoal(p, at_least, volume_at_dose, pc95*55, pc98, priority2), #flere ptv_n?
          CG.ClinicalGoal(p, at_most, dose_at_abs_volume, pc107*55, cc0_03, priority2)
        ])
  else:
    gyn.extend([
      CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, volume_at_dose, pc95*55, pc98, priority2), #flere ptv_n?
      CG.ClinicalGoal(ROIS.ptv_n_55.name, at_most, dose_at_abs_volume, pc107*55, cc0_03, priority2)
    ])  
  return gyn
'''
def gyn_57_targets(ss):
  gyn = [
    CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc95*45, pc98, priority2),
    #CG.ClinicalGoal(ROIS.ptv_45.name, at_most, dose_at_abs_volume, pc107*45, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.ctv_45.name, at_least, dose_at_volume, pc100*45, pc100, priority1), #average? D100> 95%
    #CG.ClinicalGoal(ROIS.ptv_45.name, at_least, dose_at_volume, pc95*45, pc98, priority2), 
    CG.ClinicalGoal(ROIS.x_gtv_p.name, at_most, dose_at_abs_volume, pc103*45, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.x_ptv_45.name, at_least, dose_at_volume, pc100*45, pc50, priority4),
    CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, volume_at_dose, pc95, pc98, priority3), #flere ptv_n?
    CG.ClinicalGoal(ROIS.ptv_n_57.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority3),
    CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, volume_at_dose, pc95*55, pc98, priority3), #flere ptv_n?
    CG.ClinicalGoal(ROIS.ptv_n_55.name, at_most, dose_at_abs_volume, pc107*55, cc0_03, priority3)
  ]
  ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
    for c in ctv_n_57:
      if SSF.has_roi_with_shape(ss, c):
        gyn.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc100, pc98, priority1),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc102, pc50, priority4)
        ])
  else:
    gyn.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc100, pc98, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc102, pc50, priority4)
    ])
  ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
    for c in ctv_n_55:
      if SSF.has_roi_with_shape(ss, c):
        gyn.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc100*55, pc98, priority1),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc102*55, pc50, priority4)
        ])
  else:
    gyn.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc100*55, pc98, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc102*55, pc50, priority4)
    ])
 
  return gyn
def gyn_55_targets(ss):#først dose så volum
  gyn = [
    CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc95*45, pc95, priority2), #V95 > 95%
    #CG.ClinicalGoal(ROIS.ptv_45.name, at_most, dose_at_abs_volume, pc107*45, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.ctv_45.name, at_least, dose_at_volume, pc100*45*0.95, pc100, priority2), #average?
    #CG.ClinicalGoal(ROIS.ptv_45.name, at_least, dose_at_volume, pc95*45, pc98, priority1), 
    CG.ClinicalGoal(ROIS.x_gtv_p.name, at_most, dose_at_abs_volume, pc103*45, cc0_03, priority5),
    #CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, volume_at_dose, pc95, pc98, priority1), #flere ptv_n?
    #CG.ClinicalGoal(ROIS.ptv_n_55.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.x_ptv_45.name, at_least, dose_at_volume, pc100*45, pc50, priority5)
  ]
  ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
    for c in ctv_n_55:
      if SSF.has_roi_with_shape(ss, c):
        gyn.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc100*55, pc98, priority1),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc102*55, pc50, priority4)
        ])
  else:
    gyn.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc100*55, pc98, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, dose_at_volume, pc102*55, pc50, priority4)
    ])
  ptv_n_55 = [ROIS.ptv_n1_55.name,ROIS.ptv_n2_55.name,ROIS.ptv_n3_55.name,ROIS.ptv_n4_55.name]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n1_55.name):
    for p in ptv_n_55:
      if SSF.has_roi_with_shape(ss, p):
        gyn.extend([
          CG.ClinicalGoal(p, at_least, volume_at_dose, pc95*55, pc98, priority3), #flere ptv_n?
          CG.ClinicalGoal(p, at_most, dose_at_abs_volume, pc107*55, cc0_03, priority3)
        ])
  else:
    gyn.extend([
      CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, volume_at_dose, pc95*55, pc98, priority2), #flere ptv_n?
      CG.ClinicalGoal(ROIS.ptv_n_55.name, at_most, dose_at_abs_volume, pc107*55, cc0_03, priority2)
    ])  
  return gyn

gyn_45_targets = [
  CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc98, pc95, priority1),
  CG.ClinicalGoal(ROIS.ptv_45.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.ctv_45.name, at_least, dose_at_volume, pc95, pc100, priority1), 
  CG.ClinicalGoal(ROIS.ptv_45.name, at_least, dose_at_volume, pc95,pc98, priority1),
  CG.ClinicalGoal(ROIS.x_gtv_p.name, at_most, dose_at_abs_volume, pc103, cc0_03, priority3)
]



# Rectum:
def rectum_targets(ss,total_dose):
  if total_dose == 50:
    rectum_targets = [
      CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, dose_at_volume, pc99_5, pc50, priority5),
      CG.ClinicalGoal(ROIS.ctv_p_50.name, at_most, dose_at_volume, pc100_5, pc50, priority5),
      CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority5),
      CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority5),
      #CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, dose_at_volume, pc98, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, volume_at_dose, pc95, pc99, priority2),
      CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_least, volume_at_dose, pc95*46.5, pc99, priority2),
      #CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_least, dose_at_volume, pc98*46.5, pc98, priority2),
      #CG.ClinicalGoal(ROIS.ptv_p_50.name, at_least, dose_at_volume, pc95, pc98,  priority2),
      #CG.ClinicalGoal(ROIS.ptv_e_46_5.name, at_least, dose_at_volume, pc95*46.5, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_p_50.name, at_least, volume_at_dose, pc95, pc98,  priority2),
      CG.ClinicalGoal(ROIS.ptv_e_46_5.name, at_least, volume_at_dose, pc95*46.5, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, homogeneity_index, pc95, pc95, priority6),
      CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_least, homogeneity_index, pc95, pc95, priority6),
      CG.ClinicalGoal(ROIS.ptv_p_50.name, at_least, conformity_index, pc86, pc95, priority6),
      CG.ClinicalGoal(ROIS.ptv_e_46_5.name, at_most, dose_at_volume, pc105*46.5, pc2, priority6),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_50.name):
      rectum_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_n_50.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_n_50.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ptv_n_50.name, at_least, dose_at_volume, pc95, pc98,  priority4)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ln_l_46.name):
      rectum_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_e_ln_l_46.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ln_l_46.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ln_r_46.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ln_r_46.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ln_l_46.name, at_least, dose_at_volume, pc98*46.5, pc98, priority2),
        CG.ClinicalGoal(ROIS.ctv_e_ln_r_46.name, at_least, dose_at_volume, pc98*46.5, pc98, priority2),
        CG.ClinicalGoal(ROIS.ptv_e_ln_l_46.name, at_least, dose_at_volume, pc95*46.5, pc98, priority4),
        CG.ClinicalGoal(ROIS.ptv_e_ln_r_46.name, at_least, dose_at_volume, pc95*46.5, pc98, priority4)
      ])
  else:
    rectum_targets = [
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc98, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_p.name, at_least, dose_at_volume, pc95, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_p.name, at_least, homogeneity_index, pc95, pc98, priority5),
      CG.ClinicalGoal(ROIS.ptv_p.name, at_least, conformity_index, pc90, pc95, priority5),
      CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
  return rectum_targets

# Anus:
def anus_targets(ss,total_dose, target):
  anus_targets = [
    CG.ClinicalGoal(target, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(target, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(target, at_least, dose_at_volume, pc95, pc98, priority2), #ta bort
    CG.ClinicalGoal(target.replace("C", "P"), at_least, dose_at_volume, pc95, pc98,  priority4),
    CG.ClinicalGoal(target, at_least, homogeneity_index, pc95, pc95, priority5),
    CG.ClinicalGoal(target.replace("C", "P"), at_least, conformity_index, pc86, pc95, priority5),
    CG.ClinicalGoal(ROIS.x_ctv_41.name, at_least, dose_at_volume, pc99_5*41.6, pc50, priority1),
    CG.ClinicalGoal(ROIS.x_ctv_41.name, at_most, dose_at_volume, pc100_5*41.6, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_e_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority2),
    CG.ClinicalGoal(ROIS.ptv_e_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority4),
    CG.ClinicalGoal(ROIS.ctv_e_41.name, at_least, homogeneity_index, pc95, pc95, priority5),
    CG.ClinicalGoal(ROIS.ptv_e_41.name, at_most, dose_at_volume, pc105*41.6, pc2, priority5),
    CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ]
  ctv_n_54 = [ROIS.ctv_n1_54.name,ROIS.ctv_n2_54.name,ROIS.ctv_n3_54.name,ROIS.ctv_n4_54.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_54.name):
    for c in ctv_n_54:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc95*54, pc98, priority2),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*54, pc50, priority1)
        ])
  else:
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_least, dose_at_volume, pc95*54, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1)
    ])       
  ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
    for c in ctv_n_57:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc95, pc98, priority2),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1)
        ])
  else:
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc95, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_most, dose_at_volume, pc100_5, pc50, priority1)
    ])
  ptv_n_54 = [ROIS.ptv_n1_54.name,ROIS.ptv_n2_54.name,ROIS.ptv_n3_54.name,ROIS.ptv_n4_54.name]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n1_54.name):
    for c in ptv_n_54:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc95*54, pc98, priority4),
        ])
  else:
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ptv_n_54.name, at_least, dose_at_volume, pc95*54, pc98, priority4),
    ])       
  ptv_n_57 = [ROIS.ptv_n1_57.name,ROIS.ptv_n2_57.name,ROIS.ptv_n3_57.name,ROIS.ptv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n1_57.name):
    for c in ptv_n_57:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc95, pc98, priority4),
        ])
  else:
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, dose_at_volume, pc95, pc98, priority4),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ln_l_41.name):
    anus_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_e_ln_l_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority2),
      CG.ClinicalGoal(ROIS.ctv_e_ln_r_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority2),
      CG.ClinicalGoal(ROIS.ptv_e_ln_l_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority4),
      CG.ClinicalGoal(ROIS.ptv_e_ln_r_41.name, at_least, dose_at_volume, pc95*41.6, pc98, priority4)
    ])


  return anus_targets

