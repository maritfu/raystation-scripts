# encoding: utf8

# Import local files:
import rois as ROIS


#Brain

# Whole brain
#brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brain, ROIS.nasal_cavity]
brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain, ROIS.lacrimal_r, ROIS.lacrimal_l, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.skin_brain, ROIS.nasal_cavity]
#brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain]
# Partial brain
#brain_partial_oars = [ROIS.nasal_cavity, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r,
#  ROIS.optic_nrv_l, ROIS.optic_nrv_r,  ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.optic_chiasm, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brainstem,
#  ROIS.brainstem_prv, ROIS.optic_nrv_l_prv, ROIS.optic_nrv_r_prv,  ROIS.lacrimal_l_prv, ROIS.lacrimal_r_prv, ROIS.optic_chiasm_prv, ROIS.brain, ROIS.skin, ROIS.spinal_canal_head
#]
brain_partial_oars = [ROIS.brain, ROIS.brainstem, ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.cochlea_l, ROIS.cochlea_r, 
	ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.lens_l, ROIS.lens_r, ROIS.pituitary, ROIS.skin_brain_5,ROIS.eye_l, ROIS.eye_r,ROIS.retina_l,ROIS.retina_r,ROIS.cornea_l,ROIS.cornea_r,ROIS.spinal_cord]
# Stereotactic
brain_stereotactic_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.optic_chiasm,
                           ROIS.brainstem, ROIS.skin_brain_5,ROIS.spinal_cord,ROIS.spinal_cord_prv_2,ROIS.brainstem_prv_2]

head_neck_oars = [ROIS.brainstem, ROIS.spinal_cord, ROIS.mandible, ROIS.parotid_l, ROIS.parotid_r,  ROIS.spinal_cord_prv, ROIS.brainstem_prv, ROIS.x_skulder_h, ROIS.x_skulder_v, ROIS.x_sparevolum]
head_neck_glottis_oars = [ROIS.spinal_cord, ROIS.a_carotid_l, ROIS.a_carotid_r, ROIS.spinal_cord_prv]

# Lung
lung_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_canal, ROIS.esophagus, ROIS.heart, ROIS.trachea, ROIS.bronchus, ROIS.a_aorta, ROIS.liver, ROIS.brachial_plexus, ROIS.z_spinal_canal, ROIS.z_mask]

# Husk å endre SKIN under BODY
lung_stereotactic_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_canal, ROIS.esophagus_, ROIS.heart, ROIS.trachea_, ROIS.bronchus, ROIS.greatves, ROIS.liver, ROIS.brachial_plexus,
                          ROIS.z_spinal_canal, ROIS.z_mask, ROIS.x_chestwall,ROIS.skin_brain_5,ROIS.stomach,ROIS.spinal_cord, ROIS.spinal_cord_prv ]

# spinal cord? spinal cord prv? lung-igtv?
lung_narlal_oars =  [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_canal, ROIS.spinal_cord,ROIS.esophagus, ROIS.heart, ROIS.trachea, ROIS.bronchus, ROIS.a_aorta, ROIS.liver, ROIS.brachial_plexus_r,ROIS.brachial_plexus_l,
                     ROIS.z_spinal_canal, ROIS.z_mask, ROIS.esophagus_prv, ROIS.bronchus_prv, ROIS.connective_tissue, ROIS.chestwall, ROIS.trachea_prv,ROIS.spinal_cord_narlal_prv]


# Stereotactic
#lung_stereotactic_oars = [ROIS.chestwall,  ROIS.greatves,  ROIS.trachea, ROIS.liver,  ROIS.stomach, ROIS.skin, ROIS.main_bronchus_r, ROIS.main_bronchus_l]

# Esophagus SPINAL CANAL??? GTVcor/GTVsag????
esophagus_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_cord, ROIS.heart,ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.liver,ROIS.spinal_cord_prv, ROIS.bowel_bag]

# Breast:
# Regional lymph nodes  MÅ FIKSES SPINALCANAL??
breast_reg_oars = [ROIS.heart, ROIS.lad, ROIS.heart_prv, ROIS.sternum, ROIS.thyroid, ROIS.trachea, ROIS.esophagus, ROIS.z_crp]
#breast_reg_oars = [ROIS.lung_r, ROIS.lung_l,  ROIS.heart, ROIS.spinal_canal, ROIS.lad, ROIS.heart_prv, ROIS.sternum, ROIS.thyroid, ROIS.trachea, ROIS.esophagus, ROIS.z_crp]

# Tangential
#breast_tang_oars = [ROIS.lung_r, ROIS.lung_l,  ROIS.heart, ROIS.lad,ROIS.heart_prv]
breast_tang_oars = [ROIS.heart, ROIS.lad,ROIS.heart_prv]
breast_part_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.heart, ROIS.spinal_canal, ROIS.lad, ROIS.surgical_bed]

# Gyn
gyn_oars = [ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.rectum, ROIS.bowel_bag,ROIS.spinal_cord, ROIS.spinal_cord_prv, ROIS.sigmoid, ROIS.ovary_l, ROIS.ovary_r]

# Prostate
prostate_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder,ROIS.penile_bulb,ROIS.rectum, ROIS.anal_canal, ROIS.bowel_bag, ROIS.marker1, ROIS.marker2]

# Prostate bed
prostate_bed_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.penile_bulb, ROIS.rectum]

prostate_palliative_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.penile_bulb, ROIS.rectum, ROIS.bowel_bag]

# Rectum
rectum_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.bowel_bag]

# Anus
anus_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.bowel_bag, ROIS.genitals]

# Bladder
bladder_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bladder, ROIS.bowel_bag, ROIS.rectum]


# Palliative
# Head:
palliative_head_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brain, ROIS.brainstem, ROIS.spinal_canal_head]

# Neck
palliative_neck_oars = [ROIS.submand_l, ROIS.submand_r, ROIS.spinal_canal_head, ROIS.parotid_l, ROIS.parotid_r, ROIS.parotids, ROIS.submands]

#Thorax
palliative_thorax_oars = [ROIS.heart, ROIS.spinal_canal, ROIS.lung_r, ROIS.lung_l, ROIS.lungs]

palliative_thorax_abdomen_oars = [ROIS.heart, ROIS.spinal_canal, ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.bowel_space]
#Abdomen
palliative_abdomen_oars = [ROIS.bowel_space, ROIS.kidneys, ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys]

#Abdomen and pelvis
palliative_abdomen_pelvis_oars = [ROIS.bowel_space, ROIS.kidneys, ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.rectum, ROIS.bladder]
#Pelvis
palliative_pelvis_oars = [ROIS.bowel_space, ROIS.rectum, ROIS.spinal_canal, ROIS.bladder]

# Stereotactic, spine thorax
palliative_stereotactic_thorax_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.lungs, ROIS.spinal_cord, ROIS.esophagus, ROIS.heart,  ROIS.trachea, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.skin, ROIS.cauda_equina]

# Stereotactic, spine pelivs
palliative_stereotactic_spine_pelvis_oars = [ROIS.rectum, ROIS.colon, ROIS.small_bowel, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.skin, ROIS.cauda_equina, ROIS.spinal_cord]

# Stereotactic, pelvis
palliative_stereotactic_pelvis_oars = [ROIS.rectum, ROIS.colon, ROIS.small_bowel, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.skin]
