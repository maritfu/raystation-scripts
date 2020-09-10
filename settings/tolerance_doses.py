# encoding: utf8

# Import local files:
import tolerance as EQD


# Alpha/beta values:
ab_kidney = 2
ab_kidneys = 2
ab_lung = 3
ab_heart = 3
ab_bowelspace = 3
ab_spinalcord = 2
ab_eye = 3
ab_lens = 1
ab_parotid = 3
ab_brain = 2
ab_esophagus = 3
ab_lung = 3
ab_bladder = 5
ab_rectum = 3
ab_femoral = 3
ab_brainstem = 2
ab_optic_nerve = 2
ab_optic_chiasm = 2
ab_lacrimal = 3
ab_cochlea = 3
ab_hippocampus = 2
ab_pituitary = 2
ab_retina = 3
ab_scalp = 2
ab_humeral = 3
ab_trachea = 3
ab_chestwall = 3
ab_ribs = 3
ab_greatves = 3
ab_bronchus = 3
ab_liver = 2
ab_brachial = 2
ab_stomach = 2
ab_skin = 2
ab_kidney_hilum = 2
ab_cauda = 3
ab_colon = 3
ab_bowel = 3
ab_breast = 3
ab_lad = 2
ab_cornea = 3
ab_ovary = 3
ab_sigmoid = 3
ab_aorta = 3
ab_connective_tissue = 3
ab_penile_bulb = 3

# Reference number of fractions:
fractions_kidney = 25
fractions_lung = 33
fractions_heart = 33
#fractions_bowelspace = 25
fractions_bowelspace = 35
fractions_bowelspace_27 = 27
fractions_spinalcord_eqd2 = 22.5
fractions_spinalcord = 25
fractions_spinalcord_35 = 35
fractions_spinalcord_34 = 34
fractions_spinalcord_33 = 33
fractions_spinalcord_30 = 30
fractions_parotid = 25
fractions_parotid_30 = 30
fractions_parotid_35 = 35
fractions_parotid_33 = 33
fractions_parotid_34 = 34
fractions_esophagus = 33
#fractions_bladder = 41
fractions_bladder = 35
fractions_bladder_hypo = 20
fractions_bladder_gyn = 25
fractions_bladder_27 = 27
#fractions_rectum = 39
fractions_rectum = 35
fractions_rectum_hypo = 20
fractions_rectum_gyn = 25
#fractions_femoral = 21
fractions_femoral = 35
fractions_femoral_gyn = 25
fractions_femoral_27 = 27
fractions_ovary = 25
fractions_bladder_at_rectum = 25
fractions_breast = 25
fractions_breast_15 = 15
fractions_eye = 33
fractions_sbrt_3 = 3
fractions_sbrt_5 = 5
fractions_sbrt_8 = 8
fractions_sbrt_1 = 1
# Til ny prosedyre, del av hjerne og total hjerne
fractions_brainstem_surface = 30
fractions_brainstem_core = 27
fractions_brainstem_30 = 30
fractions_brainstem_35 = 35
fractions_brainstem_33 = 33
fractions_brainstem_34 = 34
fractions_optic_nerve = 27.5
fractions_optic_chiasm = 27.5
fractions_cochlea = 22.5
fractions_cochlea_tinnitus = 16
fractions_hippocampus = 3.65
fractions_lens = 5
fractions_humeral = 25
fractions_pituitary = 22.5
fractions_pituitary_2 = 10
fractions_brain = 30
fractions_cornea = 25
fractions_lacrimal = 12.5
fractions_retina = 22.5
fractions_skin = 12.5
fractions_sigmoid = 25
fractions_penile_bulb = 35
# Example:
# EQD.Tolerance(organ, endpoint, alphabeta, nr_fractions, dose, criteria, comment)

# Conventional RT:

# Head


# Partial brain

lens_v003_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, fractions_lens, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brain_v003 = EQD.Tolerance('Brain','Some failure', ab_brain, fractions_brain, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_surface_v003_adx = EQD.Tolerance('BrainstemSurface', 'Some failure', ab_brainstem, fractions_brainstem_surface, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_core_v003_adx = EQD.Tolerance('BrainstemCore', 'Some failure', ab_brainstem, fractions_brainstem_core, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_nrv_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, fractions_optic_nerve, 55,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_optic_chiasm, 55, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
lacrimal_mean = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, fractions_lacrimal, 25,  'Mean', 'Conventional RT')
cochlea_mean = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_cochlea, 45, 'Mean', 'Conventional RT')
cochlea_mean_tinnitus = EQD.Tolerance('Cochlea_R', 'Some failure', ab_cochlea, fractions_cochlea_tinnitus, 32, 'Mean', 'Conventional RT')
pituitary_mean = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, fractions_pituitary, 45, 'Mean', 'Conventional RT')
pituitary_2_mean = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, fractions_pituitary_2, 20, 'Mean', 'Conventional RT')
retina_v003_adx = EQD.Tolerance('Retina_R', 'Some failure', ab_retina, fractions_retina, 45, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
cornea_v003_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, fractions_cornea, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
skin_v003_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_skin, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, fractions_hippocampus, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')



# Neck
parotids_mean = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid, 25, 'Mean', 'Conventional RT')
#parotid_mean = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid, 20, 'Mean', 'Conventional RT')
parotid_mean_30 = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid_30, 26, 'Mean', 'Conventional RT')
parotid_mean_35 = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid_35, 26, 'Mean', 'Conventional RT')
parotid_mean_33 = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid_33, 26, 'Mean', 'Conventional RT')
parotid_mean_34 = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid_34, 26, 'Mean', 'Conventional RT')
brainstem_30_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_30, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_35_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_35, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_33_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_33, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_34_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_prv_30_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_30, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_prv_35_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_35, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_prv_33_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_33, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_prv_34_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
spinalcord_30_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_30, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_33_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_33, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_34_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_35_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_35, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_prv_30_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_prv_33_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_33, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_prv_34_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_prv_35_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_35, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')

# Thorax
kidney_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 15, 'Mean', 'Conventional RT')
kidney_v20_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 28, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
kidney_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 23, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_v32_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 20, 'Volume receiving tolerance dose being less than 32%', 'Conventional RT')
kidney_v55_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 12, 'Volume receiving tolerance dose being less than 12%', 'Conventional RT')
lung_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Mean', 'Conventional RT')
lung_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_v65_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 5, 'Volume receiving tolerance dose being less than 65%', 'Conventional RT')
heart_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 20, 'Mean', 'Conventional RT')
heart_v25_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 50, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 60, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_v60_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 45, 'Volume receiving tolerance dose being less than 60%', 'Conventional RT')
heart_v80_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 80%', 'Conventional RT')
spinalcord_v2_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v2_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
esophagus_mean = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 34, 'Mean', 'Conventional RT')
esophagus_v15_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 60, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_v17_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 60, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')

spinalcord_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')

spinalcanal_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
heart_narlal_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
esophagus_v1_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
lung_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung,5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')

spinalcanal_30_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_30_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
heart_narlal_30_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_30_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_30_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
esophagus_v1_30_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 30, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
lung_30_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_30_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_30_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 20, 'Mean', 'Conventional RT')
lung_35_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 20, 'Mean', 'Conventional RT')

heart_v1_33_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
trachea_v1_33_adx = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
trachea_prv_v1_33_adx = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, 33, 78, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
bronchus_v1_33_adx = EQD.Tolerance('Bronchus', 'Some failure', ab_bronchus, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
bronchus_prv_v1_33_adx = EQD.Tolerance('Bronchus', 'Some failure', ab_bronchus, 33, 78, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
aorta_v1_33_adx = EQD.Tolerance('A Aorta', 'Some failure', ab_aorta, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
connective_tissue_v1_33_adx = EQD.Tolerance('Connective tissue', 'Some failure', ab_connective_tissue, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
chestwall_v1_33_adx = EQD.Tolerance('Chest wall', 'Some failure', ab_chestwall, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')


spinalcanal_35_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 35, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_35_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 35, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
heart_narlal_35_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_35_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_35_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
esophagus_v1_35_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 35, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
lung_35_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_35_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')

heart_narlal_15_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_15_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_15_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
esophagus_v1_15_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 15, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
lung_15_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_15_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
heart_narlal_17_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_17_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_17_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
esophagus_v1_17_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 17, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
lung_17_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_17_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
spinalcanal_17_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 17, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_17_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 17, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_15_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 15, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_15_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 15, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')


spinalcanal_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
lung_17_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 20, 'Mean', 'Conventional RT')
lung_15_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 20, 'Mean', 'Conventional RT')


# Esophagus
lung_23_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 23, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_23_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 23, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_23_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung, 23, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_23_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 23, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
spinal_cord_prv_23_v0_03_adx = EQD.Tolerance('SpinalCord_PRV', 'Some failure', ab_spinalcord, 23, 45,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
kidney_23_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 23, 18, 'Mean', 'Conventional RT')

lung_25_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 25, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_25_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 25, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_25_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung, 25, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_25_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 25, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_25_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 25, 18, 'Mean', 'Conventional RT')


kidney_30_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 30, 18, 'Mean', 'Conventional RT')
kidney_30_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 30, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_30_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung,30, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_33_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 33, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_33_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 33, 18, 'Mean', 'Conventional RT')
liver_33_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung,33, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')

# Breast
lung_v15_adx = EQD.Tolerance('Lung_L', 'Some failure', ab_lung, fractions_breast_15, 18, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
heart_mean_breast = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast, 2, 'Mean', 'Conventional RT')
heart_mean_breast_15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast_15, 2, 'Mean', 'Conventional RT')
humeral_v33_adx = EQD.Tolerance('Humeral', 'Some failure', ab_humeral, fractions_breast, 25, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
contralat_breast_mean = EQD.Tolerance('Breast', 'Some failure', ab_breast, fractions_breast_15, 2, 'Mean', 'Conventional RT')
lung_v30_adx_25 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v30_adx_15 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 18, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v65_adx_15 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 5, 'Volume receiving tolerance dose being less than 65%', 'Conventional RT')
lad_v100_adx = EQD.Tolerance('LAD', 'Some failure', ab_lad, fractions_breast, 20, 'Volume receiving tolerance dose being less than 100%', 'Conventional RT')
lad_v100_adx_15 = EQD.Tolerance('LAD', 'Some failure', ab_lad, fractions_breast_15, 20, 'Volume receiving tolerance dose being less than 100%', 'Conventional RT')
ipsilateral_breast_v50_adx = EQD.Tolerance('Breast_L/R','Some failure', ab_heart, fractions_breast_15, 40,'Volume receiving tolerance dose being less than 50%', 'Conventional RT' )
heart_mean_breast_tang = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast_15, 1.5, 'Mean', 'Conventional RT')
lung_contralateral_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 0.5, 'Mean', 'Conventional RT')
lung_contralateral_mean_reg = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 1, 'Mean', 'Conventional RT')

# Gyn
bladder_v85_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 30, 'Volume receiving tolerance dose being less than 85%', 'Conventional RT')
bladder_v75_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 40, 'Volume receiving tolerance dose being less than 75%', 'Conventional RT')
bladder_v003_adx = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_bladder_gyn, 47.2, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bowelbag_v350_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelbag_v100_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace,  25, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelbag_v003_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 47.2, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
femoral_v003_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral_gyn, 50, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v003_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 47.2, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v95_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 30, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v85_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 40, 'Mean dose being less than tolerance dose', 'Conventional RT')
kidney_mean_5 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 5, 'Mean', 'Conventional RT')
kidney_mean_10 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 10, 'Mean', 'Conventional RT')
ovary_mean_5= EQD.Tolerance('Ovary', 'Some failure', ab_ovary, fractions_ovary,5, 'Mean', 'Conventional RT')
ovary_mean_8= EQD.Tolerance('Ovary', 'Some failure', ab_ovary, fractions_ovary,8, 'Mean', 'Conventional RT')
spinal_cord_38_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_45_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_48_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 48, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_prv_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
sigmoid_v003_adx = EQD.Tolerance('Sigmoid', 'Some failure', ab_sigmoid, fractions_sigmoid, 47.2, 'Mean dose being less than tolerance dose', 'Conventional RT')
spinal_cord_45_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_eqd2, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')



# Prostate
#bladder_v50_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 65, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
#bladder_v35_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 70, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
#bladder_v25_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 75, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
#bladder_v15_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 80, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
#rectum_v50_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
#rectum_v35_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 60, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
#rectum_v25_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 65, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
#rectum_v20_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 70, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
#rectum_v15_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 75, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')

bladder_v50_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 66, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v35_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 70, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
bladder_v25_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 74, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
bladder_v15_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 78, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
rectum_v50_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v35_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 60, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
rectum_v25_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 66, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
rectum_v20_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 70, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
rectum_v15_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 73, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
femoral_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
bladder_v2_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_at_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bowelspace_v195_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace, 50, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
penile_bulb_v90_adx = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_penile_bulb, 55, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')

femoral_mean_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 42, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_v49_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 50, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_v2_adx_hypo = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 20, 44, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
femoral_v49_adx_hypo = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 20, 42, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
penile_bulb_v90_adx_hypo = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, 20, 46, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')

rectum_v50_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 47, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v35_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 53, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
rectum_v25_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 56, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
rectum_v20_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 59, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
bladder_v50_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 58, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v35_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 62, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
#rectum_v40_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 40.8, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
#rectum_v48_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 48.6, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
#rectum_v52_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 52.8, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
#rectum_v57_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 57, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
#rectum_v60_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 60, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
#bladder_v60_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 60, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
#bladder_v48_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 48.6, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
#bladder_v40_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 40.8, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')

#Anus/rectum
femoral_27_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
bowelspace_27_v310_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace_27, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelspace_27_v70_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace_27, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bladder_mean_27_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_27, 45, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_25_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 25, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
bowelspace_25_v310_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 25, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelspace_25_v70_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 25, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bladder_mean_25_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, 25, 45, 'Mean dose being less than tolerance dose', 'Conventional RT')

# SBRT:

# Lung SBRT 3 fractions
spinal_canal_sbrt_3fx_v1_2 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 12.3, 'Volume receiving tolerance dose being less than 1.2 cm3', 'SBRT')
spinal_canal_sbrt_3fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
esophagus_sbrt_3fx_v5 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_3, 17.7, 'Volume receiving tolerance dose being less than 5 cm3', 'SBRT')
esophagus_sbrt_3fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_3, 25.2, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
greatves_sbrt_3fx_v10 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_3, 39, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
greatves_sbrt_3fx_v0 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_3, 45, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
main_bronchus_sbrt_3fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
main_bronchus_sbrt_3fx_v4 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_3, 15, 'Volume receiving tolerance dose being less than 4 cm3', 'SBRT')
heart_sbrt_3fx_v15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 15 cm3', 'SBRT')
heart_sbrt_3fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
liver_sbrt_3fx_mean = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_3, 15, 'Mean', 'SBRT')
liver_sbrt_3fx_v700 = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_3, 17, 'Volume receiving tolerance dose being less than 700 cm3', 'SBRT')
lung_contra_sbrt_3fx_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 3.6, 'Mean', 'SBRT')
lung_sbrt_3fx_v10 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 20, 'Volume receiving tolerance dose being less than 10%', 'SBRT')
lung_sbrt_3fx_v1500 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 11.6, 'Volume receiving tolerance dose being less than 1500cm3', 'SBRT')
lung_sbrt_3fx_v1000 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 12.4, 'Volume receiving tolerance dose being less than 1000cm3', 'SBRT')
lung_sbrt_3fx_v37 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 4.5, 'Volume receiving tolerance dose being less than 37%', 'SBRT')
lung_sbrt_3fx_v40 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 10, 'Volume receiving tolerance dose being less than 40%', 'SBRT')
trachea_sbrt_3fx_v4 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_3, 15, 'Volume receiving tolerance dose being less than 4cm3', 'SBRT')
trachea_sbrt_3fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
chestwall_sbrt_3fx_v30 = EQD.Tolerance('Chestwall', 'Some failure', ab_chestwall, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 30cm3', 'SBRT')
ribs_sbrt_3fx_v2 = EQD.Tolerance('Ribs', 'Some failure', ab_ribs, fractions_sbrt_3, 27, 'Volume receiving tolerance dose being less than 2cm3', 'SBRT')
ribs_sbrt_3fx_v0 = EQD.Tolerance('Ribs', 'Some failure', ab_ribs, fractions_sbrt_3, 53.76, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
skin_sbrt_3fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 22.5, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
skin_sbrt_3fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
# Not in use by default:
#brachial_sbrt_3fx_v0 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
#brachial_sbrt_3fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_3, 20.4, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
#kidney_hilum_3fx_v66 = EQD.Tolerance('Kidney_Hilum', 'Some failure', ab_kidney_hilum, fractions_sbrt_3, 18.6, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
#kidneys_3fx_v200 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_3, 14.4, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')
#kidneys_3fx_v33 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_3, 15, 'Volume receiving tolerance dose being less than 33%', 'SBRT')
#stomach_3fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 22.2, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
#stomach_3fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 16.5, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')

# Lung SBRT 5 fractions
spinal_canal_sbrt_5fx_v1_2 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_5, 14.5, 'Volume receiving tolerance dose being less than 1.2 cm3', 'SBRT')
spinal_canal_sbrt_5fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
esophagus_sbrt_5fx_v5 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_5, 19.5, 'Volume receiving tolerance dose being less than 5 cm3', 'SBRT')
esophagus_sbrt_5fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_5, 35, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
greatves_sbrt_5fx_v10 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_5, 47, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
greatves_sbrt_5fx_v0 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_5, 53, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
main_bronchus_sbrt_5fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
main_bronchus_sbrt_5fx_v4 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_5, 18, 'Volume receiving tolerance dose being less than 4 cm3', 'SBRT')
heart_sbrt_5fx_v15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 15 cm3', 'SBRT')
heart_sbrt_5fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
liver_sbrt_5fx_v700 = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_5, 21, 'Volume receiving tolerance dose being less than 700 cm3', 'SBRT')
lung_contra_sbrt_5fx_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 3.6, 'Mean', 'SBRT')
lung_contra_sbrt_5fx_v26 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 5, 'Volume receiving tolerance dose being less than 26%', 'SBRT')
lung_sbrt_5fx_v1500 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 12.5, 'Volume receiving tolerance dose being less than 1500cm3', 'SBRT')
lung_sbrt_5fx_v1000 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 13.5, 'Volume receiving tolerance dose being less than 1000cm3', 'SBRT')
lung_sbrt_5fx_v37 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 5, 'Volume receiving tolerance dose being less than 37%', 'SBRT')
trachea_sbrt_5fx_v4 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_5, 18, 'Volume receiving tolerance dose being less than 4cm3', 'SBRT')
trachea_sbrt_5fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
chestwall_sbrt_5fx_v30 = EQD.Tolerance('Chestwall', 'Some failure', ab_chestwall, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 30cm3', 'SBRT')
ribs_sbrt_5fx_v1 = EQD.Tolerance('Ribs', 'Some failure', ab_ribs, fractions_sbrt_5, 35, 'Volume receiving tolerance dose being less than 2cm3', 'SBRT')
skin_sbrt_5fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
skin_sbrt_5fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
# Not in use by default:
#brachial_sbrt_sbrt_5fx_v0 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_5, 30.5, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
#brachial_sbrt_sbrt_5fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_5, 27, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
#kidney_hilum_sbrt_5fx_v66 = EQD.Tolerance('Kidney_Hilum', 'Some failure', ab_kidney_hilum, fractions_sbrt_5, 23, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
#kidneys_sbrt_5fx_v200 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_5, 17.5, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')
#idneys_sbrt_5fx_v33 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_5, 18.5, 'Volume receiving tolerance dose being less than 33%', 'SBRT')
#stomach_sbrt_5fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
#stomach_sbrt_5fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 18, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')

# Lung SBRT 8 fractions
esophagus_sbrt_8fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_8, 41.6, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
heart_sbrt_8fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_8, 41.6, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_canal_sbrt_8fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_8, 33.6, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
trachea_sbrt_8fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_8, 56, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
main_bronchus_sbrt_8fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_8, 56, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
main_bronchus_contra_sbrt_8fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_8, 48.8, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')


# Brain SRT 1 fraction
cochlea_srt_1fx_v0 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_sbrt_1, 9, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_1fx_v0 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_1fx_v0_2 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
optic_chiasm_srt_1fx_v0 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_chiasm_srt_1fx_v0_2 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
eye_srt_1fx_v0 = EQD.Tolerance('Eye_R','Some failure', ab_eye, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
lens_srt_1fx_v0 = EQD.Tolerance('Lens_L','Some failure', ab_lens, fractions_sbrt_1, 5, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_1fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_1fx_v1 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.5 cm3', 'SBRT')
brainstem_prv_srt_1fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 12, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')

brain_srt_1fx_v10 = EQD.Tolerance('Brain', 'Some failure', ab_brain, fractions_sbrt_1, 12, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
skin_srt_1fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_1, 14.4, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
spinal_cord_srt_1fx_v0 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_1, 12.5, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_cord_srt_1fx_v0_25 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0.25 cm3', 'SBRT')

# Brain SRT 3 fractions
cochlea_srt_3fx_v0 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_sbrt_3, 17, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_3fx_v0 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_3fx_v0_2 = EQD.Tolerance('OpticNrv_R','Some failure', ab_optic_nerve, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
optic_chiasm_srt_3fx_v0 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_chiasm_srt_3fx_v0_2 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
eye_srt_3fx_v0 = EQD.Tolerance('Eye_L','Some failure', ab_eye, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
lens_srt_3fx_v0 = EQD.Tolerance('Lens_R','Some failure', ab_lens, fractions_sbrt_3, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_3fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_3fx_v1 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.5 cm3', 'SBRT')
brainstem_prv_srt_3fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 20, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')

brain_srt_3fx_v10 = EQD.Tolerance('Brain', 'Some failure', ab_brain, fractions_sbrt_3, 20, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
skin_srt_3fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 22.5, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
spinal_cord_srt_3fx_v0 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_cord_srt_3fx_v1 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.25 cm3', 'SBRT')


# Bone/Spine SBRT 1 fractions
esophagus_sbrt_1fx_v5 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_1, 11.9, 'Volume receiving tolerance dose being less than 5 cm3', 'SBRT')
esophagus_sbrt_1fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_1, 16, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_canal_sbrt_1fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_1, 14, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_canal_sbrt_1fx_v0_35 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0.35 cm3', 'SBRT')
spinal_canal_3mm_sbrt_1fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_1, 16, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_canal_3mm_sbrt_1fx_v0_1 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_1, 15, 'Volume receiving tolerance dose being less than 0.35 cm3', 'SBRT')
trachea_sbrt_1fx_v4 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_1, 10.5, 'Volume receiving tolerance dose being less than 4cm3', 'SBRT')
trachea_sbrt_1fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_1, 20.2, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
heart_sbrt_1fx_v15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_1, 16, 'Volume receiving tolerance dose being less than 15 cm3', 'SBRT')
heart_sbrt_1fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_1, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
skin_sbrt_1fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_1, 23, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
skin_sbrt_1fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_1, 26, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
lungs_sbrt_1fx_v1000 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_1, 7.4, 'Volume receiving tolerance dose being less than 1000cm3', 'SBRT')
brachial_sbrt_1fx_v0 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_1, 17.5, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
brachial_sbrt_1fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_1, 14, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
cauda_equina_sbrt_1fx_v0 = EQD.Tolerance('CaudaEquina', 'Some failure', ab_cauda, fractions_sbrt_1, 16, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
cauda_equina_sbrt_1fx_v5 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_cauda, fractions_sbrt_1, 14, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
small_bowel_sbrt_1fx_v0 = EQD.Tolerance('SmallBowel', 'Some failure', ab_bowel, fractions_sbrt_1, 15.4, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
small_bowel_sbrt_1fx_v5 = EQD.Tolerance('SmallBowel', 'Some failure', ab_bowel, fractions_sbrt_1, 11.9, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
rectum_sbrt_1fx_v0 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_1, 18.4, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
rectum_sbrt_1fx_v20 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_1, 14.3, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
colon_sbrt_1fx_v0 = EQD.Tolerance('Colon', 'Some failure', ab_colon, fractions_sbrt_1, 18.4, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
colon_sbrt_1fx_v20 = EQD.Tolerance('Rectum', 'Some failure', ab_colon, fractions_sbrt_1, 14.3, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
kidney_hilum_1fx_v66 = EQD.Tolerance('Kidney_Hilum', 'Some failure', ab_kidney_hilum, fractions_sbrt_1, 10.6, 'Volume receiving tolerance dose being less than 2/3 volume', 'SBRT')
kidney_sbrt_1fx_v0 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_sbrt_1, 18.6, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
kidneys_col_1fx_v200 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_1, 8.4, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')

# Bone/Spine SBRT 3 fractions
spinal_canal_sbrt_3fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 21.9, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_canal_sbrt_3fx_v0_35 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0.35 cm3', 'SBRT')
cauda_equina_sbrt_3fx_v0 = EQD.Tolerance('CaudaEquina', 'Some failure', ab_cauda, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
cauda_equina_sbrt_3fx_v5 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_cauda, fractions_sbrt_3, 21.9, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
small_bowel_sbrt_3fx_v0 = EQD.Tolerance('SmallBowel', 'Some failure', ab_bowel, fractions_sbrt_3, 25.2, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
small_bowel_sbrt_3fx_v5 = EQD.Tolerance('SmallBowel', 'Some failure', ab_bowel, fractions_sbrt_3, 17.7, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
skin_col_sbrt_3fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
skin_col_sbrt_3fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 33, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
rectum_sbrt_3fx_v0 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_3, 28.8, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
rectum_sbrt_3fx_v20 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
colon_sbrt_3fx_v0 = EQD.Tolerance('Colon', 'Some failure', ab_colon,  fractions_sbrt_3, 28.8, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
colon_sbrt_3fx_v20 = EQD.Tolerance('Colon', 'Some failure', ab_colon,  fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
kidney_3fx_v10 = EQD.Tolerance('Kidney_Hilum', 'Some failure', ab_kidney_hilum, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 1/10 volume', 'SBRT')
kidneys_col_3fx_v200 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_3, 16, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')


'''
eye_prv_v2_adx_5 = EQD.Tolerance('Eye_PRV','Some failure', ab_eye, fractions_eye_5, 22, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_5 = EQD.Tolerance('Lens_PRV','Some failure', ab_lens, fractions_lens_5, 12, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx_10 = EQD.Tolerance('Eye_PRV','Some failure', ab_eye, fractions_eye_10, 28, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_10 = EQD.Tolerance('Lens_PRV','Some failure', ab_lens, fractions_lens_10, 14, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx = EQD.Tolerance('Eye_PRV','Some failure', ab_eye, fractions_eye, 50, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx = EQD.Tolerance('Lens_PRV','Some failure', ab_lens, fractions_lens, 25, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_13 = EQD.Tolerance('Lens_PRV_R','Some failure', ab_lens, fractions_lens_13, 15, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_15 = EQD.Tolerance('Lens_PRV_R','Some failure', ab_lens, fractions_lens_15, 16, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_30 = EQD.Tolerance('Lens_PRV_R','Some failure', ab_lens, fractions_lens_30, 25, 'Maximum dose at less than 2% volume', 'Conventional RT')
lens_prv_v2_adx_33 = EQD.Tolerance('Lens_PRV_R','Some failure', ab_lens, fractions_lens_33, 25, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx_13 = EQD.Tolerance('Eye_PRV_R','Some failure', ab_eye, fractions_eye_13, 38, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx_15 = EQD.Tolerance('Eye_PRV_R','Some failure', ab_eye, fractions_eye_15, 40, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx_30 = EQD.Tolerance('Eye_PRV_R','Some failure', ab_eye, fractions_eye_30, 49, 'Maximum dose at less than 2% volume', 'Conventional RT')
eye_prv_v2_adx_33 = EQD.Tolerance('Eye_PRV_R','Some failure', ab_eye, fractions_eye_33, 50, 'Maximum dose at less than 2% volume', 'Conventional RT')
hippocampus_mean_33 = EQD.Tolerance('Hippocampus', 'Some failure', ab_hippocampus, fractions_hippocampus_33, 17, 'Mean', 'Conventional RT')
hippocampus_mean_30 = EQD.Tolerance('Hippocampus', 'Some failure', ab_hippocampus, fractions_hippocampus_30, 17, 'Mean', 'Conventional RT')
hippocampus_mean_15 = EQD.Tolerance('Hippocampus', 'Some failure', ab_hippocampus, fractions_hippocampus_15, 15, 'Mean', 'Conventional RT')
hippocampus_mean_13 = EQD.Tolerance('Hippocampus', 'Some failure', ab_hippocampus, fractions_hippocampus_13, 14, 'Mean', 'Conventional RT')
lacrimal_mean_13 = EQD.Tolerance('Glnd_Lacrimal_R', 'Some failure', ab_lacrimal, fractions_lacrimal_13, 21,  'Mean', 'Conventional RT')
lacrimal_mean_15 = EQD.Tolerance('Glnd_Lacrimal_R', 'Some failure', ab_lacrimal, fractions_lacrimal_15, 21,  'Mean', 'Conventional RT')
lacrimal_mean_30 = EQD.Tolerance('Glnd_Lacrimal_R', 'Some failure', ab_lacrimal, fractions_lacrimal_30, 25,  'Mean', 'Conventional RT')
lacrimal_mean_33 = EQD.Tolerance('Glnd_Lacrimal_R', 'Some failure', ab_lacrimal, fractions_lacrimal_33, 25,  'Mean', 'Conventional RT')
brainstem_prv_v2_adx_33 = EQD.Tolerance('Brainstem_PRV', 'Some failure', ab_brainstem, fractions_brainstem_33, 54, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
brainstem_prv_v2_adx_30 = EQD.Tolerance('Brainstem_PRV', 'Some failure', ab_brainstem, fractions_brainstem_30, 53, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
brain_max = EQD.Tolerance('Brain','Some failure', ab_brain, fractions_brain, 60, 'Maximum dose', 'Conventional RT')
brain_gtv_max = EQD.Tolerance('Brain-GTV','Some failure', ab_brain, fractions_brain, 60, 'Maximum dose', 'Conventional RT')
brainstem_prv_v2_adx = EQD.Tolerance('Brainstem_PRV', 'Some failure', ab_brainstem, fractions_brainstem, 54, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
optic_nrv_prv_v2_adx = EQD.Tolerance('OpticNrv_PRV_R','Some failure', ab_optic_nerve, fractions_optic_nerve, 54,  'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
optic_nrv_prv_v2_adx_30 = EQD.Tolerance('OpticNrv_PRV_R','Some failure', ab_optic_nerve, fractions_optic_nerve_30, 53,  'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
optic_chiasm_prv_v2_adx = EQD.Tolerance('OpticChiasm_PRV', 'Some failure', ab_optic_chiasm, fractions_optic_chiasm, 54, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
optic_chiasm_prv_v2_adx_30 = EQD.Tolerance('OpticChiasm_PRV', 'Some failure', ab_optic_chiasm, fractions_optic_chiasm_30, 53, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
lacrimal_prv_v2_adx = EQD.Tolerance('Glnd_Lacrimal_PRV_L', 'Some failure', ab_lacrimal, fractions_lacrimal, 30, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
lacrimal_mean = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, fractions_lacrimal, 25,  'Mean', 'Conventional RT')
cochlea_mean = EQD.Tolerance('Cochlea', 'Some failure', ab_cochlea, fractions_cochlea, 35, 'Mean', 'Conventional RT')
hippocampus_mean = EQD.Tolerance('Hippocampus', 'Some failure', ab_hippocampus, fractions_hippocampus, 17, 'Mean', 'Conventional RT')
'''
'''
fractions_hippocampus_33 = 33
fractions_hippocampus_30 = 30
fractions_hippocampus_15 = 15
fractions_hippocampus_13 = 13
fractions_lens_10 = 10
fractions_lens_5 = 5
fractions_lens_33 = 33
fractions_lens_30 = 30
fractions_lens_15 = 15
fractions_lens_13 = 13
fractions_lacrimal_33 = 33
fractions_lacrimal_30 = 30
fractions_lacrimal_15 = 15
fractions_lacrimal_13 = 13
fractions_eye_5 = 5
fractions_eye_10 = 10
fractions_eye_13 = 13
fractions_eye_15 = 15
fractions_eye_30 = 30
fractions_eye_33 = 33
fractions_optic_nerve_30 = 30
fractions_brainstem_33 = 33
fractions_brainstem_30 = 30
fractions_optic_chiasm = 33
fractions_optic_chiasm_30 = 30
fractions_lacrimal = 33
'''
