# encoding: utf8

# Import local files:
from tkinter import *
from tkinter import messagebox
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for head & neck treatments (Primary radiation, post operative radiation or primary radiation to glottis only, number of affected lymph nodes, low risk, radiacal surgery or not radical surgery ,left sided, right sided, or both sides ).
class DefHeadNeck(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Primary radiation, post operative radiation or primary radiation to glottis only?
    primary = choices[1]
    if primary == 'primary':
      indication = choices[2]
      if indication in ['other','glottis']:
        site.add_oars(DEF.head_neck_oars)
        if indication == 'other':
          ctv_p_68 =  ROI.ROIAlgebra(ROIS.ctv_p_68.name, ROIS.ctv_p_68.type, ROIS.ctv_p_68.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ctv_p_60 =  ROI.ROIAlgebra(ROIS.ctv_p_60.name, ROIS.ctv_p_60.type, ROIS.ctv_p_60.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
          #ptv_p_68 = ROI.ROIExpanded(ROIS.ptv_p_68.name, ROIS.ptv_p_68.type, ROIS.ptv_p_68.color, source = ctv_p_68, margins = MARGINS.uniform_4mm_expansion)
          #ptv_p_60 = ROI.ROIExpanded(ROIS.ptv_p_60.name, ROIS.ptv_p_60.type, ROIS.ptv_p_60.color, source = ctv_p_60, margins = MARGINS.uniform_4mm_expansion)
          ptv_p_68 =  ROI.ROIAlgebra(ROIS.ptv_p_68.name, ROIS.ptv_p_68.type, ROIS.ptv_p_68.color, sourcesA=[ctv_p_68], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          ptv_p_60 =  ROI.ROIAlgebra(ROIS.ptv_p_60.name, ROIS.ptv_p_60.type, ROIS.ptv_p_60.color, sourcesA=[ctv_p_60], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          site.add_targets([ROIS.gtv_p,ctv_p_68])
          # Choice 2: Number of affected lymph nodes?
          number_ln = choices[3]
          if number_ln == 'one':
            ctv_n_68 =  ROI.ROIAlgebra(ROIS.ctv_n_68.name, ROIS.ctv_n_68.type, ROIS.ctv_n_68.color, sourcesA=[ROIS.gtv_n], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n_60 =  ROI.ROIAlgebra(ROIS.ctv_n_60.name, ROIS.ctv_n_60.type, ROIS.ctv_n_60.color, sourcesA=[ROIS.gtv_n], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            #ptv_n_68 = ROI.ROIExpanded(ROIS.ptv_n_68.name, ROIS.ptv_n_68.type, ROIS.ptv_n_68.color, source = ctv_n_68, margins = MARGINS.uniform_4mm_expansion)
            #ptv_n_60 = ROI.ROIExpanded(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, source = ctv_n_60, margins = MARGINS.uniform_4mm_expansion)
            ptv_n_68 =  ROI.ROIAlgebra(ROIS.ptv_n_68.name, ROIS.ptv_n_68.type, ROIS.ptv_n_68.color, sourcesA=[ctv_n_68], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
            ptv_n_60 =  ROI.ROIAlgebra(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, sourcesA=[ctv_n_60], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

            site.add_targets([ROIS.gtv_n, ctv_n_68, ctv_p_60, ctv_n_60])
          elif number_ln in ['two','three']:
            ctv_n1_68 =  ROI.ROIAlgebra(ROIS.ctv_n1_68.name, ROIS.ctv_n1_68.type, ROIS.ctv_n1_68.color, sourcesA=[ROIS.gtv_n1], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n1_60 =  ROI.ROIAlgebra(ROIS.ctv_n1_60.name, ROIS.ctv_n1_60.type, ROIS.ctv_n1_60.color, sourcesA=[ROIS.gtv_n1], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            ctv_n2_68 =  ROI.ROIAlgebra(ROIS.ctv_n2_68.name, ROIS.ctv_n2_68.type, ROIS.ctv_n2_68.color, sourcesA=[ROIS.gtv_n2], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n2_60 =  ROI.ROIAlgebra(ROIS.ctv_n2_60.name, ROIS.ctv_n2_60.type, ROIS.ctv_n2_60.color, sourcesA=[ROIS.gtv_n2], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            ptv_n_60 = ROI.ROIAlgebra(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, sourcesA = [ctv_n1_60,ctv_n2_60], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
            ptv_n_68 = ROI.ROIAlgebra(ROIS.ptv_n_68.name, ROIS.ptv_n_68.type, ROIS.ptv_n_68.color, sourcesA = [ctv_n1_68,ctv_n2_68], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
            site.add_targets([ROIS.gtv_n1, ROIS.gtv_n2, ctv_n1_68, ctv_n2_68])
            if number_ln == 'three':
              ctv_n3_68 =  ROI.ROIAlgebra(ROIS.ctv_n3_68.name, ROIS.ctv_n3_68.type, ROIS.ctv_n3_68.color, sourcesA=[ROIS.gtv_n3], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
              ctv_n3_60 =  ROI.ROIAlgebra(ROIS.ctv_n3_60.name, ROIS.ctv_n3_60.type, ROIS.ctv_n3_60.color, sourcesA=[ROIS.gtv_n3], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
              ptv_n_60.sourcesA.extend([ctv_n3_60])
              ptv_n_68.sourcesA.extend([ctv_n3_68])
              site.add_targets([ROIS.gtv_n3,ctv_n3_68])
            site.add_targets([ctv_p_60, ctv_n1_60, ctv_n2_60])
            if number_ln == 'three':
              site.add_targets([ctv_n3_60])

        elif indication == 'glottis':
          ctv_p_70 =  ROI.ROIAlgebra(ROIS.ctv_p_70.name, ROIS.ctv_p_70.type, ROIS.ctv_p_70.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ctv_p_60 =  ROI.ROIAlgebra(ROIS.ctv_p_60.name, ROIS.ctv_p_60.type, ROIS.ctv_p_60.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
          #ptv_p_70 = ROI.ROIExpanded(ROIS.ptv_p_70.name, ROIS.ptv_p_70.type, ROIS.ptv_p_70.color, source = ctv_p_70, margins = MARGINS.uniform_4mm_expansion)
          #ptv_p_60 = ROI.ROIExpanded(ROIS.ptv_p_60.name, ROIS.ptv_p_60.type, ROIS.ptv_p_60.color, source = ctv_p_60, margins = MARGINS.uniform_4mm_expansion)
          ptv_p_70 =  ROI.ROIAlgebra(ROIS.ptv_p_70.name, ROIS.ptv_p_70.type, ROIS.ptv_p_70.color, sourcesA=[ctv_p_70], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          ptv_p_60 =  ROI.ROIAlgebra(ROIS.ptv_p_60.name, ROIS.ptv_p_60.type, ROIS.ptv_p_60.color, sourcesA=[ctv_p_60], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          site.add_targets([ROIS.gtv_p,ctv_p_70])
          # Choice 2: Number of affected lymph nodes?
          number_ln = choices[3]
          if number_ln == 'one':
            ctv_n_70 =  ROI.ROIAlgebra(ROIS.ctv_n_70.name, ROIS.ctv_n_70.type, ROIS.ctv_n_70.color, sourcesA=[ROIS.gtv_n], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n_60 =  ROI.ROIAlgebra(ROIS.ctv_n_60.name, ROIS.ctv_n_60.type, ROIS.ctv_n_60.color, sourcesA=[ROIS.gtv_n], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            #ptv_n_70 = ROI.ROIExpanded(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, source = ctv_n_70, margins = MARGINS.uniform_4mm_expansion)
            #ptv_n_60 = ROI.ROIExpanded(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, source = ctv_n_60, margins = MARGINS.uniform_4mm_expansion)
            ptv_n_70 =  ROI.ROIAlgebra(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, sourcesA=[ctv_n_70], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
            ptv_n_60 =  ROI.ROIAlgebra(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, sourcesA=[ctv_n_60], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

            site.add_targets([ROIS.gtv_n, ctv_n_70, ctv_p_60, ctv_n_60])
          elif number_ln in ['two','three']:
            ctv_n1_70 =  ROI.ROIAlgebra(ROIS.ctv_n1_70.name, ROIS.ctv_n1_70.type, ROIS.ctv_n1_70.color, sourcesA=[ROIS.gtv_n1], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n1_60 =  ROI.ROIAlgebra(ROIS.ctv_n1_60.name, ROIS.ctv_n1_60.type, ROIS.ctv_n1_60.color, sourcesA=[ROIS.gtv_n1], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            ctv_n2_70 =  ROI.ROIAlgebra(ROIS.ctv_n2_70.name, ROIS.ctv_n2_70.type, ROIS.ctv_n2_70.color, sourcesA=[ROIS.gtv_n2], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
            ctv_n2_60 =  ROI.ROIAlgebra(ROIS.ctv_n2_60.name, ROIS.ctv_n2_60.type, ROIS.ctv_n2_60.color, sourcesA=[ROIS.gtv_n2], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
            #ptv_n_60 = ROI.ROIAlgebra(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, sourcesA = [ctv_n1_60], sourcesB = [ctv_n2_60], marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_4mm_expansion)
            #ptv_n_70 = ROI.ROIAlgebra(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, sourcesA = [ctv_n1_70], sourcesB = [ctv_n2_70], marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_4mm_expansion)
            ptv_n_60 = ROI.ROIAlgebra(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, sourcesA = [ctv_n1_60,ctv_n2_60], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
            ptv_n_70 = ROI.ROIAlgebra(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, sourcesA = [ctv_n1_70,ctv_n2_70], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
    
            site.add_targets([ROIS.gtv_n1, ROIS.gtv_n2, ctv_n1_70, ctv_n2_70])
            if number_ln == 'three':
              ctv_n3_70 =  ROI.ROIAlgebra(ROIS.ctv_n3_70.name, ROIS.ctv_n3_70.type, ROIS.ctv_n3_70.color, sourcesA=[ROIS.gtv_n3], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
              ctv_n3_60 =  ROI.ROIAlgebra(ROIS.ctv_n3_60.name, ROIS.ctv_n3_60.type, ROIS.ctv_n3_60.color, sourcesA=[ROIS.gtv_n3], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
              ptv_n_60.sourcesA.extend([ctv_n3_60])
              ptv_n_70.sourcesA.extend([ctv_n3_70])
              site.add_targets([ROIS.gtv_n3,ctv_n3_70])
            site.add_targets([ctv_p_60, ctv_n1_60, ctv_n2_60])
            if number_ln == 'three':
              site.add_targets([ctv_n3_60])
        # Choice 3: Left sided, right sided, or both sides?    
        side = choices[4]
        if side == 'right':
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_r_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          #ptv_e_54 = ROI.ROIExpanded(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, source = ROIS.ctv_e_r_54, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ROIS.ctv_e_r_54], sourcesB = [ptv_p_60, ptv_n_60], operator='Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_r_54])
        elif side == 'left':
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          #ptv_e_54 = ROI.ROIExpanded(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, source = ROIS.ctv_e_l_54, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ptv_p_60, ptv_n_60], operator='Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_l_54])
        elif side == 'both':
          ctv_e_54 = ROI.ROIAlgebra(ROIS.ctv_e_54.name, ROIS.ctv_e_54.type, ROIS.ctv_e_54.color, sourcesA = [ROIS.ctv_e_l_54,ROIS.ctv_e_r_54], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          #ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ROIS.ctv_e_r_54], marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_expansion)
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_r_54,ROIS.ctv_e_l_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ctv_e_54], sourcesB = [ptv_p_60, ptv_n_60], operator='Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_r_54, ROIS.ctv_e_l_54, ctv_e_54])
        if indication == 'other':
          x_ptv_54 = ROI.ROIAlgebra(ROIS.x_ptv_54.name, ROIS.x_ptv_54.type, ROIS.x_ptv_54.color, sourcesA = [ptv_e_54], sourcesB = [ptv_p_68, ptv_n_68,ptv_p_60, ptv_n_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          x_tetthetsvolum = ROI.ROIAlgebra(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, sourcesA = [ptv_p_68, ptv_n_68,ptv_p_60, ptv_n_60, ptv_e_54], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          site.add_targets([ptv_p_68, ptv_n_68, ptv_p_60, ptv_n_60, ptv_e_54, x_ctv_54, x_ptv_54,x_tetthetsvolum])
        elif indication == 'glottis':
          x_ptv_54 = ROI.ROIAlgebra(ROIS.x_ptv_54.name, ROIS.x_ptv_54.type, ROIS.x_ptv_54.color, sourcesA = [ptv_e_54], sourcesB = [ptv_p_70, ptv_n_70,ptv_p_60, ptv_n_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          x_tetthetsvolum = ROI.ROIAlgebra(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, sourcesA = [ptv_p_70, ptv_n_70,ptv_p_60, ptv_n_60, ptv_e_54], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          site.add_targets([ptv_p_70, ptv_n_70, ptv_p_60, ptv_n_60, ptv_e_54, x_ctv_54, x_ptv_54,x_tetthetsvolum])
      elif indication == 'glottis_T1':
        site.add_oars(DEF.head_neck_glottis_oars)
        stadium = choices[3]
        if stadium == 'glottis_a':
          ctv_p_66 =  ROI.ROIAlgebra(ROIS.ctv_p_66.name, ROIS.ctv_p_66.type, ROIS.ctv_p_66.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ptv_p_66 = ROI.ROIAlgebra(ROIS.ptv_p_66.name, ROIS.ptv_p_66.type, ROIS.ptv_p_66.color, sourcesA = [ctv_p_66], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          #ptv_p_66 = ROI.ROIExpanded(ROIS.ptv_p_66.name, ROIS.ptv_p_66.type, ROIS.ptv_p_66.color, source = ctv_p_66, margins = MARGINS.uniform_4mm_expansion)
          site.add_targets([ROIS.gtv_p,ctv_p_66, ptv_p_66])
        else:
          ctv_p_68 =  ROI.ROIAlgebra(ROIS.ctv_p_68.name, ROIS.ctv_p_68.type, ROIS.ctv_p_68.color, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          #ptv_p_68 = ROI.ROIExpanded(ROIS.ptv_p_68.name, ROIS.ptv_p_68.type, ROIS.ptv_p_68.color, source = ctv_p_68, margins = MARGINS.uniform_4mm_expansion)
          ptv_p_68 = ROI.ROIAlgebra(ROIS.ptv_p_68.name, ROIS.ptv_p_68.type, ROIS.ptv_p_68.color, sourcesA = [ctv_p_68], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          site.add_targets([ROIS.gtv_p,ctv_p_68, ptv_p_68])
    elif primary == 'postop':
      site.add_oars(DEF.head_neck_oars)
      # Choice 2: low risk, radiacal surgery or not radical surgery
      radical = choices[2]
      site.add_targets([ROIS.gtv_sb])
      if radical == 'low risk':
        ptv_sb_60 = ROI.ROIAlgebra(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, sourcesA = [ROIS.ctv_sb_60], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
 
        #ptv_sb_60 = ROI.ROIExpanded(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, source = ROIS.ctv_sb_60, margins = MARGINS.uniform_4mm_expansion)
        # Choice 4: Left sided, right sided, or both sides?
        side = choices[3]
        if side == 'right':
          ptv_e_50 = ROI.ROIAlgebra(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, sourcesA = [ROIS.ctv_e_r_50], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          #ptv_e_50 = ROI.ROIExpanded(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, source = ROIS.ctv_e_r_50, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_50 = ROI.ROIAlgebra(ROIS.x_ctv_50.name, ROIS.x_ctv_50.type, ROIS.x_ctv_50.color, sourcesA = [ROIS.ctv_e_r_50], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_r_50])
        elif side == 'left':
          ptv_e_50 = ROI.ROIAlgebra(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, sourcesA = [ROIS.ctv_e_l_50], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          #ptv_e_50 = ROI.ROIExpanded(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, source = ROIS.ctv_e_l_50, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_50 = ROI.ROIAlgebra(ROIS.x_ctv_50.name, ROIS.x_ctv_50.type, ROIS.x_ctv_50.color, sourcesA = [ROIS.ctv_e_l_50], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_l_50])
        elif side == 'both':
          ctv_e_50 = ROI.ROIAlgebra(ROIS.ctv_e_50.name, ROIS.ctv_e_50.type, ROIS.ctv_e_50.color, sourcesA = [ROIS.ctv_e_l_50,ROIS.ctv_e_r_50], sourcesB = [ROIS.body],operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          #ptv_e_50 = ROI.ROIAlgebra(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, sourcesA = [ROIS.ctv_e_l_50], sourcesB = [ROIS.ctv_e_r_50], marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_expansion)
          ptv_e_50 = ROI.ROIAlgebra(ROIS.ptv_e_50.name, ROIS.ptv_e_50.type, ROIS.ptv_e_50.color, sourcesA = [ROIS.ctv_e_r_50,ROIS.ctv_e_l_50], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          x_ctv_50 = ROI.ROIAlgebra(ROIS.x_ctv_50.name, ROIS.x_ctv_50.type, ROIS.x_ctv_50.color, sourcesA = [ctv_e_50], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_l_50,ROIS.ctv_e_r_50, ctv_e_50])
        
        x_ptv_50 = ROI.ROIAlgebra(ROIS.x_ptv_50.name, ROIS.x_ptv_50.type, ROIS.x_ptv_50.color, sourcesA = [ptv_e_50], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
        x_tetthetsvolum = ROI.ROIAlgebra(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, sourcesA = [ptv_sb_60, ptv_e_50], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)

        site.add_targets([ROIS.ctv_sb_60, ptv_sb_60, ptv_e_50, x_ctv_50, x_ptv_50,x_tetthetsvolum])
      elif radical in ['radical','not_radical']:
        if radical == 'radical':
          ctv_sb_60 =  ROI.ROIAlgebra(ROIS.ctv_sb_60.name, ROIS.ctv_sb_60.type, ROIS.ctv_sb_60.color, sourcesA=[ROIS.gtv_sb], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
          #ptv_sb_60 = ROI.ROIExpanded(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, source = ctv_sb_60, margins = MARGINS.uniform_4mm_expansion)
          ptv_sb_60 = ROI.ROIAlgebra(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, sourcesA = [ctv_sb_60], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          site.add_targets([ctv_sb_60])
        elif radical == 'not_radical':
          ctv_sb_66 =  ROI.ROIAlgebra(ROIS.ctv_sb_66.name, ROIS.ctv_sb_66.type, ROIS.ctv_sb_66.color, sourcesA=[ROIS.gtv_sb], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ctv_sb_60 =  ROI.ROIAlgebra(ROIS.ctv_sb_60.name, ROIS.ctv_sb_60.type, ROIS.ctv_sb_60.color, sourcesA=[ctv_sb_66], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          ptv_sb_66 = ROI.ROIAlgebra(ROIS.ptv_sb_66.name, ROIS.ptv_sb_66.type, ROIS.ptv_sb_66.color, sourcesA = [ctv_sb_66], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          ptv_sb_60 = ROI.ROIAlgebra(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, sourcesA = [ctv_sb_60], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_4mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          #ptv_sb_66 = ROI.ROIExpanded(ROIS.ptv_sb_66.name, ROIS.ptv_sb_66.type, ROIS.ptv_sb_66.color, source = ctv_sb_66, margins = MARGINS.uniform_4mm_expansion)
          #ptv_sb_60 = ROI.ROIExpanded(ROIS.ptv_sb_60.name, ROIS.ptv_sb_60.type, ROIS.ptv_sb_60.color, source = ctv_sb_60, margins = MARGINS.uniform_4mm_expansion)
          site.add_targets([ctv_sb_66, ctv_sb_60])
        # Choice 4: Left sided, right sided, or both sides?
        side = choices[3]
        if side == 'right':
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_r_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          #ptv_e_54 = ROI.ROIExpanded(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, source = ROIS.ctv_e_r_54, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ROIS.ctv_e_r_54], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_r_54])
        elif side == 'left':
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          #ptv_e_54 = ROI.ROIExpanded(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, source = ROIS.ctv_e_l_54, margins = MARGINS.uniform_5mm_expansion)
          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_l_54])
        elif side == 'both':
          ctv_e_54 = ROI.ROIAlgebra(ROIS.ctv_e_54.name, ROIS.ctv_e_54.type, ROIS.ctv_e_54.color, sourcesA = [ROIS.ctv_e_l_54,ROIS.ctv_e_r_54], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          #ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_l_54], sourcesB = [ROIS.ctv_e_r_54], marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_expansion)
          ptv_e_54 = ROI.ROIAlgebra(ROIS.ptv_e_54.name, ROIS.ptv_e_54.type, ROIS.ptv_e_54.color, sourcesA = [ROIS.ctv_e_r_54,ROIS.ctv_e_l_54], sourcesB = [ROIS.body], operator = 'Intersection',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.uniform_5mm_contraction)

          x_ctv_54 = ROI.ROIAlgebra(ROIS.x_ctv_54.name, ROIS.x_ctv_54.type, ROIS.x_ctv_54.color, sourcesA = [ctv_e_54], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.ctv_e_r_54,ROIS.ctv_e_l_54, ctv_e_54])
        # Common for both radical and not radical
        if radical == 'radical':
          x_tetthetsvolum = ROI.ROIAlgebra(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, sourcesA = [ptv_sb_60, ptv_e_54], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          site.add_targets([ptv_sb_60,x_tetthetsvolum])
        elif radical == 'not_radical':
          x_tetthetsvolum = ROI.ROIAlgebra(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, sourcesA = [ptv_sb_66, ptv_sb_60, ptv_e_54], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
          site.add_targets([ptv_sb_66, ptv_sb_60,x_tetthetsvolum])
        x_ptv_54 = ROI.ROIAlgebra(ROIS.x_ptv_54.name, ROIS.x_ptv_54.type, ROIS.x_ptv_54.color, sourcesA = [ptv_e_54], sourcesB = [ptv_sb_60], operator='Subtraction', marginsB = MARGINS.uniform_7mm_expansion)
        site.add_targets([ptv_e_54, x_ctv_54, x_ptv_54])
    # Create all targets and OARs in RayStation:
    site.create_rois()

#ctv = ROI.ROIAlgebra(ROIS.ctv.name, ROIS.ctv.type, COLORS.ctv_low, sourcesA = [ctv_p_60, ctv_n_60, ctv_p_68, ctv_n_68], sourcesB = [ROIS.ctv_e_l_54, ROIS.ctv_e_r_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
#ptv = ROI.ROIAlgebra(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv_low, sourcesA = [ptv_sb_60, ptv_sb_66], sourcesB = [ROIS.ptv_e_54, ROIS.ptv_e_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
#ctv = ROI.ROIAlgebra(ROIS.ctv.name, ROIS.ctv.type, COLORS.ctv_low, sourcesA = [ctv_sb_60], sourcesB = [ROIS.ctv_e_l_54, ROIS.ctv_e_r_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
#ptv = ROI.ROIAlgebra(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv_low, sourcesA = [ptv_sb_60], sourcesB = [ROIS.ptv_e_54, ROIS.ptv_e_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)      
#ctv = ROI.ROIAlgebra(ROIS.ctv.name, ROIS.ctv.type, COLORS.ctv_low, sourcesA = [ctv_sb_60, ctv_sb_66], sourcesB = [ROIS.ctv_e_l_54, ROIS.ctv_e_r_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
#ptv = ROI.ROIAlgebra(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv_low, sourcesA = [ptv_sb_60, ptv_sb_66], sourcesB = [ROIS.ptv_e_54, ROIS.ptv_e_54], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
# Create all targets and OARs in RayStation:

          #messagebox.showinfo("", str(ptv_sb_66))
