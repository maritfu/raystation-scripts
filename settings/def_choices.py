# encoding: utf8

# Import local files:
import property as P

# Regions:
brain = P.Property('Hjerne', 'brain', next_category='omfang')
head_neck = P.Property('Øre-nese-hals', 'head_neck', next_category='indikasjon', default = True)
lung = P.Property('Lunge', 'lung', next_category = 'intensjon')
breast = P.Property('Bryst', 'breast', next_category = 'omfang')
bladder = P.Property('Blære', 'bladder')
gyn = P.Property('Gyn','gyn',next_category = 'omfang')
prostate = P.Property('Prostata', 'prostate', next_category = 'omfang')
gi = P.Property('GI', 'gi', next_category = 'diagnose')
other = P.Property('Palliativ (skjelett og øvrig bløtvev)', 'other', next_category = '')
 

# Brain: Scope:
brain_whole = P.Property('Hele hjernen', 'whole', parent=brain, default = True)
brain_partial = P.Property('Del av hjerne', 'part', parent=brain)
brain_stereotactic = P.Property('Stereotaksi','stereotactic', parent = brain, next_category ='antall målvolum')

# Brain: Partial: Diagnosis:
#brain_partial_diag1 = P.Property('Glioblastom WHO grad IV', 'glio', parent=brain_partial, default = True)
#brain_partial_diag2 = P.Property('Anaplastisk astrocytom WHO grad III', 'astro', parent=brain_partial)
#brain_partial_diag3 = P.Property('Atypisk og anaplastisk meningeom', 'meningeom', parent=brain_partial)

# Brain: Stereotactic
brain_stereo_nr1 = P.Property('1','one', parent = brain_stereotactic, default = True)
brain_stereo_nr2 = P.Property('2','two', parent = brain_stereotactic)
brain_stereo_nr3 = P.Property('3','three', parent = brain_stereotactic)
brain_stereo_nr4 = P.Property('4','four', parent = brain_stereotactic)

# Head & Neck
head_neck_primary = P.Property('Primær strålebehandling','primary',parent = head_neck, next_category ='indikasjon',default = True)
head_neck_postop = P.Property('Postoperativ strålebehandling','postop',parent = head_neck, next_category ='')


# Head & Neck: indication
head_neck_glottis_t1 = P.Property('Glottis T1N0','glottis_T1',parent = head_neck_primary, next_category ='stadium')
head_neck_glottis = P.Property('Spyttkjertelkreft høyere stadium enn T1 (54-60-70)','glottis',parent = head_neck_primary, next_category ='antall affiserte lymfeknuter')
head_neck_other = P.Property('Alle andre indikasjoner i ØNH-regionen (54-60-68)','other',parent = head_neck_primary, next_category ='antall affiserte lymfeknuter', default = True)


head_neck_glottis_a = P.Property('Glottis T1A (66 Gy)','glottis_a',parent = head_neck_glottis_t1, next_category ='',default = True)
head_neck_glottis_b = P.Property('Glottis T1B (68 Gy)','glottis_b',parent = head_neck_glottis_t1, next_category ='')


# Head & Neck: Radical surgery? 
head_neck_low_risk = P.Property('Radikalt operert (R0), lavrisiko (50-60)','low risk',parent = head_neck_postop,next_category ='side')
head_neck_radical = P.Property('Radikalt operert (R0) (54-60)','radical',parent = head_neck_postop, next_category ='side',default = True)
head_neck_not_radical = P.Property('Ikke radikalt operert (R+) (54-60-66)', 'not_radical',parent = head_neck_postop,next_category ='side')

for side in [head_neck_low_risk,head_neck_radical,head_neck_not_radical]:
  head_neck_both = P.Property('Både høyre og venstre','both',parent = side,default = True)
  head_neck_right = P.Property('Høyre','right',parent = side)
  head_neck_left = P.Property('Venstre','left',parent = side)

# Head & Neck: Number of affected lymph nodes:
for nr in [head_neck_glottis, head_neck_other]:
  head_neck_nr1 = P.Property('1','one', parent = nr, next_category ='side', default = True)
  head_neck_nr2 = P.Property('2','two', parent = nr, next_category ='side')
  head_neck_nr3 = P.Property('3','three', parent = nr, next_category ='side')
  # Head & Neck: Side:
  for side in [head_neck_nr1,head_neck_nr2,head_neck_nr3]:
    head_neck_both = P.Property('Både høyre og venstre','both',parent = side,default = True)
    head_neck_right = P.Property('Høyre','right',parent = side)
    head_neck_left = P.Property('Venstre','left',parent = side)

# Lung
lung_curative = P.Property('Kurativ', 'curative', parent = lung, next_category = 'diagnose', default = True)
#lung_palliative = P.Property('Palliativ','palliative', parent = lung, next_category = '')
lung_stereotactic = P.Property('Stereotaksi', 'stereotactic', parent = lung, next_category ='side')

# Lung curative:
lung_nsclc = P.Property('Ikke-småcellet lungekreft/ Småcellet lungekreft (med 4DCT)','4dct', parent = lung_curative, next_category ='ICTV margin', default = True)
lung_narlal = P.Property('NARLAL2','narlal', parent = lung_curative, next_category ='antall lymfeknuter')
#lung_sclc = P.Property('Småcellet lungekreft (uten 4DCT)','sclc', parent = lung_curative)
#lung_pancoast =P.Property('Pancoast', 'pancoast', parent = lung_curative)
#lung_postop =P.Property('Postoperativ', 'postop', parent = lung_curative)

# Lung ICTV margin
lung_5mm = P.Property('5 mm','5', parent = lung_nsclc, next_category ='antall lymfeknuter', default = True)
lung_7mm = P.Property('7 mm','7', parent = lung_nsclc, next_category ='antall lymfeknuter')

# Lung number of lymph nodes:
for p in [lung_5mm, lung_7mm,lung_narlal]:
  lung_ln_1 = P.Property('1','one', parent = p, default = True)
  lung_ln_2 = P.Property('2','two', parent = p)
  lung_ln_3 = P.Property('3','three', parent = p)
  lung_ln_4 = P.Property('4','four', parent = p)
  lung_ln_5 = P.Property('5','five', parent = p)
  lung_ln_6 = P.Property('6','six', parent = p)

# Lung stereotactic:
stereo_lung_right = P.Property('Høyre','right', parent = lung_stereotactic, next_category ='antall målvolum', default = True)
stereo_lung_left = P.Property('Venstre','left', parent = lung_stereotactic, next_category ='antall målvolum')

for side in [stereo_lung_right, stereo_lung_left]:
  lung_stereo_nr1 = P.Property('1','one', parent = side, default = True)
  lung_stereo_nr2 = P.Property('2','two', parent = side)
  lung_stereo_nr3 = P.Property('3','three', parent = side)


# Lung palliative:
#lung_with_4dct = P.Property('Med 4DCT', 'with', parent = lung_palliative, default = True)
#lung_without_4dct = P.Property('Uten 4DCT', 'without', parent = lung_palliative)


#Breast:
breast_tangential = P.Property('Bryst/brystvegg', 'tang', parent = breast, next_category = 'side', default = True)
breast_locoregional = P.Property('Bryst/brystvegg og regionale lymfeknuter', 'reg', parent = breast, next_category ='')
breast_locoregional_not_one = P.Property('Bryst/brystvegg og regionale lymfeknuter unntatt nivå 1', 'reg-1', parent = breast, next_category ='')

for b in [breast_locoregional, breast_locoregional_not_one]:
  breast_imn = P.Property('Med parasternale glandler', 'imn', parent = b, next_category = 'side',default = True)
  breast_not_imn = P.Property('Uten parasternale glandler', 'not_imn', parent = b, next_category = 'side')
  # Breast regional: 
  for b in [breast_imn, breast_not_imn]:
    breast_right = P.Property('Høyre','right', parent = b, next_category = '', default = True)
    breast_left = P.Property('Venstre','left', parent = b, next_category = '')
    for side in [breast_right, breast_left]:
      # Breast youth boost:
      for p in [breast_right, breast_left]:
        breast_without_boost = P.Property('Uten boost 2 Gy x 8', 'without', parent = p, default = True)
        breast_with_boost = P.Property('Med boost 2 Gy x 8','with', parent =p)
  
# Breast tangential: 
breast_right = P.Property('Høyre','right', parent = breast_tangential, next_category = '', default = True)
breast_left = P.Property('Venstre','left', parent = breast_tangential, next_category = '')
for side in [breast_right, breast_left]:
  # Breast youth boost:
  for p in [breast_right, breast_left]:
    breast_without_boost = P.Property('Uten boost 2 Gy x 8', 'without', parent = p, default = True)
    breast_with_boost = P.Property('Med boost 2 Gy x 8','with', parent =p)    

# Gyn:

gyn_ln = P.Property('Cervix med bekkenlymfeknuter', 'with', parent = gyn, next_category ='',default = True)
gyn_ln_n = P.Property('Cervix med bekkenlymfeknuter og N+ i det lille bekkenet', 'with_node', parent = gyn, next_category ='antall lymfeknuter')
gyn_ln_n_57 = P.Property('Cervix med bekkenlymfeknuter og N+ i det store bekkenet/paraaortalt', 'with_node_57', parent = gyn, next_category ='antall lymfeknuter i det lille bekkenet')
gyn_not = P.Property('Gyn annet', 'not', parent = gyn, next_category ='fraksjonering')

# Gyn: Fractionation:
gyn_30 = P.Property('Totaldose 30 Gy', '30', parent = gyn_not, next_category ='antall lymfeknuter')
gyn_50 = P.Property('Totaldose 50 Gy', '50', parent = gyn_not, next_category ='antall lymfeknuter', default = True)

# Gyn: Number of lymph nodes
for p in [gyn_50, gyn_ln_n]:
  gyn_with_ln_n_1 = P.Property('1', 'with_node_1', parent = p, default = True)
  gyn_with_ln_n_2 = P.Property('2', 'with_node_2', parent = p)  
  gyn_with_ln_n_3 = P.Property('3', 'with_node_3', parent = p)
  gyn_with_ln_n_4 = P.Property('4', 'with_node_4', parent = p)

gyn_with_ln_n_55_1 = P.Property('1', 'with_node_55_1', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt',default = True)
gyn_with_ln_n_55_2 = P.Property('2', 'with_node_55_2', parent = gyn_ln_n_57,next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_3 = P.Property('3', 'with_node_55_3', parent = gyn_ln_n_57,next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_4 = P.Property('4', 'with_node_55_4', parent = gyn_ln_n_57,next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')

for p in [gyn_with_ln_n_55_1,gyn_with_ln_n_55_2,gyn_with_ln_n_55_3,gyn_with_ln_n_55_4]:
  gyn_with_ln_n_57_1 = P.Property('1', 'with_node_57_1', parent = p, default = True)
  gyn_with_ln_n_57_2 = P.Property('2', 'with_node_57_2', parent = p)
  gyn_with_ln_n_57_3 = P.Property('3', 'with_node_57_3', parent = p)
  gyn_with_ln_n_57_4 = P.Property('4', 'with_node_57_4', parent = p)

# Prostate:
prostate_normal = P.Property('Prostata', 'prostate', parent = prostate, next_category ='', default = True)
prostate_bed = P.Property('Prostataseng', 'bed', parent = prostate, next_category ='')

# Prostate: Fractionation:
prostate_hypo = P.Property('Hypofraksjonering (60 Gy)', 'hypo_60', parent = prostate_normal,  next_category = 'omfang', default = True)#prostata og vesikler
prostate_normo = P.Property('Konvensjonell fraksjonering', 'normo', parent = prostate_normal, next_category ='')
prostate_palliative = P.Property('Palliativ fraksjonering, uten gull', 'palliative', parent = prostate_normal, next_category ='')

prostate_bed_normo = P.Property('Konvensjonell fraksjonering', 'normo', parent = prostate_bed, next_category ='', default = True)
prostate_bed_palliative = P.Property('Palliativ fraksjonering', 'palliative', parent = prostate_bed, next_category ='')

# Prostata hypo: Vesicles or not 
prostate_hypo_prostate = P.Property('Prostata', 'prostata_only', parent = prostate_hypo)
prostate_hypo_vesicles = P.Property('Prostata og vesikler', 'vesicles', parent = prostate_hypo, default = True)

# Prosate/bed: Lymph nodes:
for p in [prostate_normo, prostate_bed_normo]:
  prostate_without_ln =  P.Property('Uten bekkenlymfeknuter', 'without',  parent = p, next_category ='')
  prostate_with_ln =  P.Property('Med bekkenlymfeknuter', 'with', parent = p, next_category ='',default = True)
  prostate_with_ln_boost =  P.Property('Med bekkenlymfeknuter og boost til positiv lymfeknute(r)', 'with_node', parent = p, next_category ='antall lymfeknuter')

  prostate_with_ln_boost_1 =  P.Property('1', 'with_node_1', parent = prostate_with_ln_boost,default = True)
  prostate_with_ln_boost_2 =  P.Property('2', 'with_node_2', parent = prostate_with_ln_boost)
  prostate_with_ln_boost_3 =  P.Property('3', 'with_node_3', parent = prostate_with_ln_boost)

# GI 
anus = P.Property('Anus', 'anus', parent = gi, next_category = 'stadium',default = True)
rectum = P.Property('Rektum', 'rectum', parent = gi, next_category = 'indikasjon')
esophagus = P.Property('Øsofagus', 'esophagus', parent = gi,next_category = 'fraksjonering')

eso_pre = P.Property('Neoadjuvant preoperativ radiokjemoterapi (CROSS-regimet)', 'neo', parent = esophagus,default = True)
eso_radical = P.Property('Radikal (definitiv) radiokjemoterapi', 'radical', parent = esophagus,next_category = 'fraksjonering')


eso_50 = P.Property('Totaldose 50 Gy', '50', parent = eso_radical,default = True)
eso_60 = P.Property('Totaldose 60 Gy', '60', parent = eso_radical)
eso_64 = P.Property('Totaldose 66 Gy', '66', parent = eso_radical)

# Anus:
anus_t1 = P.Property('T1-2 N0', 't1', parent = anus, next_category ='',default = True)
anus_t3 = P.Property('T3-4 N0 eller N+', 't3', parent = anus, next_category ='antall lymfeknuter < 2 cm')

nr_ln_small_0 = P.Property('0', 'with_node_0', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_1 = P.Property('1', 'with_node_1', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm', default = True)
nr_ln_small_2 = P.Property('2', 'with_node_2', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_3 = P.Property('3', 'with_node_3', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_4 = P.Property('4', 'with_node_4', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')

for p in [nr_ln_small_0, nr_ln_small_1, nr_ln_small_2, nr_ln_small_3, nr_ln_small_4]:
  nr_ln_large_0 = P.Property('0', 'with_node_l_0', parent = p, next_category ='omfang')
  nr_ln_large_1 = P.Property('1', 'with_node_l_1', parent = p,next_category ='omfang', default = True)
  nr_ln_large_2 = P.Property('2', 'with_node_l_2', parent = p,next_category ='omfang')
  nr_ln_large_3 = P.Property('3', 'with_node_l_3', parent = p,next_category ='omfang')
  nr_ln_large_4 = P.Property('4', 'with_node_l_4', parent = p,next_category ='omfang')

  for p1 in [nr_ln_large_0, nr_ln_large_1,nr_ln_large_2,nr_ln_large_3,nr_ln_large_4]:
    anus_t3_without_nodes = P.Property('Uten patologisk forstørrede lymfeglandler i lyskene', 'without', parent = p1, default = True)
    anus_t3_with_nodes = P.Property('Med patologisk forstørrede lymfeglandler i lyskene', 'with', parent = p1)

anus_without_nodes = P.Property('Uten patologisk forstørrede lymfeglandler i lyskene', 'without', parent = anus_t1, default = True)
anus_with_nodes = P.Property('Med patologisk forstørrede lymfeglandler i lyskene', 'with', parent = anus_t1)

# Rectum:
rectum_postop = P.Property('Postoperativ strålebehandling', 'postop', parent = rectum, next_category ='')
rectum_preop = P.Property('Preoperativ strålebehandling', 'preop', parent = rectum, next_category ='fraksjonering',default = True)

rectum_hypo = P.Property('Hypofraksjonering', 'hypo', parent = rectum_preop, next_category ='')
rectum_normo = P.Property('Konvensjonell fraksjonering med SIB', 'normo', parent = rectum_preop, next_category ='omfang', default = True)

for p in [rectum_normo, rectum_postop]:
  rectum_with_ln =  P.Property('Med bekkenlymfeknuter', 'with', parent = p, next_category ='omfang',default = True)
  rectum_with_ln_boost =  P.Property('Med bekkenlymfeknuter og boost til positiv lymfeknute(r)', 'with_node', parent = p,next_category ='omfang')

  for p1 in [rectum_with_ln, rectum_with_ln_boost]:
    rectum_without_nodes = P.Property('Uten patologisk forstørrede lymfeglandler i lyskene', 'without', parent = p1, default = True)
    rectum_with_nodes = P.Property('Med patologisk forstørrede lymfeglandler i lyskene', 'with', parent = p1)


# Rectum normo: Nodes:
#rectum_with_nodes = P.Property('Med patologisk forstørrede lymfeglandler i lyskene', 'with', parent = rectum_normo)
#rectum_without_nodes = P.Property('Uten patologisk forstørrede lymfeglandler i lyskene', 'without', parent = rectum_normo, default = True)


# Other (palliative): SBRT:
other_stereotactic = P.Property('Stereotaksi', 'yes', parent =other, next_category = 'region')
other_non_stereotactic = P.Property('Ikke stereotaksi', 'no', parent = other, next_category = 'region', default = True)

# Other non-SBRT: Region:
other_head = P.Property('Hode', 'head', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_neck = P.Property('Hals', 'neck', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_thorax = P.Property('Thorax', 'thorax', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_thorax_and_abdomen = P.Property('Thorax/Abdomen', 'thorax_abdomen', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_abdomen = P.Property('Abdomen', 'abdomen', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_abdomen_and_pelvis = P.Property('Abdomen/Bekken', 'abdomen_pelvis', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_pelvis = P.Property('Bekken', 'pelvis', parent=other_non_stereotactic, next_category = 'antall målvolum', default = True)
other_other = P.Property('Ekstremiteter/Annet', 'other', parent=other_non_stereotactic, next_category = 'antall målvolum')

# Other SBRT: Region:
other_stereotactic_col_thorax =  P.Property('Columna - thorax', 'col thorax', parent=other_stereotactic)
other_stereotactic_col_pelvis =  P.Property('Columna - bekken', 'col pelvis', parent=other_stereotactic)
other_stereotactic_pelvis  = P.Property('Bekken', 'pelvis', parent=other_stereotactic, default = True)

# Other non-SBRT: Number of target volumes:
for region in [other_head, other_neck, other_thorax, other_thorax_and_abdomen, other_abdomen, other_abdomen_and_pelvis, other_pelvis, other_other]:
  other_target_volume_one = P.Property('1','1', parent = region, next_category = '', default = True)
  other_target_volume_two = P.Property('2','2', parent = region, next_category = '')
  # With or without soft tissue component:
  for tv in [other_target_volume_one, other_target_volume_two]:
    other_with_gtv = P.Property('Bløtvevskomponent (med GTV)', 'with', parent = tv)
    other_without_gtv = P.Property('Skjelett (uten GTV)', 'without', parent = tv, default = True)


# Lists to be used with radiobutton objects:
regions = [head_neck, breast]
#regions = [brain, head_neck, lung,breast,bladder,gyn,prostate,gi,other]

# Radiobutton choices for deleting/keeping pre-existing ROIs:
p_delete = P.Property('Slett eksisterende ROIs', 'yes')
p_delete_derived = P.Property('Slett alle bortsett fra inntegnede ROIs','some')
p_not_delete = P.Property('Ikke slett eksisterende ROIs','no', default = True)
delete = [p_delete, p_delete_derived, p_not_delete]
