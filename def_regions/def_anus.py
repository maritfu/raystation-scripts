# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for rectum treatments (conventional 50 Gy SIB and hypofractionated 25 Gy).
class DefAnus(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Fractionation - normo or hypofractionated?
    stad = choices[2]
    site.add_oars(DEF.anus_oars)
    if stad == 't1': 
      ctv_p_54 = ROI.ROIExpanded(ROIS.ctv_p_54.name, ROIS.ctv_p_54.type, ROIS.ctv_p_54.color, source = ROIS.gtv_p_54, margins = MARGINS.uniform_10mm_expansion)
      ptv_p_54 = ROI.ROIExpanded(ROIS.ptv_p_54.name, ROIS.ptv_p_54.type, ROIS.ptv_p_54.color, source = ctv_p_54, margins = MARGINS.uniform_10mm_expansion) #tilpassede marginer?
      ptv_e_41 = ROI.ROIExpanded(ROIS.ptv_e_41.name, ROIS.ptv_e_41.type, ROIS.ptv_e_41.color, source = ROIS.ctv_e_41, margins = MARGINS.rectum_ptv_50_expansion)
      x_ptv_41 = ROI.ROIAlgebra(ROIS.x_ptv_41.name, ROIS.x_ptv_41.type, ROIS.x_ptv_41.color, sourcesA = [ptv_e_41], sourcesB = [ptv_p_54], operator = 'Subtraction', marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
      x_ctv_41 = ROI.ROIAlgebra(ROIS.x_ctv_41.name, ROIS.x_ctv_41.type, ROIS.x_ctv_41.color, sourcesA = [ROIS.ctv_e_41], sourcesB = [ptv_p_54], operator = 'Subtraction', marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
      
      site.add_targets([ROIS.gtv_p_54,ctv_p_54, ptv_p_54, x_ctv_41, x_ptv_41])
      groin = choices[3]
      if groin == 'with': #gtv_groin?
        ptv_e_ln_r_41 = ROI.ROIExpanded(ROIS.ptv_e_ln_r_41.name, ROIS.ptv_e_ln_r_41.type, ROIS.ptv_e_ln_r_41.color, source = ROIS.ctv_e_ln_r_41, margins = MARGINS.uniform_7mm_expansion)
        ptv_e_ln_l_41 = ROI.ROIExpanded(ROIS.ptv_e_ln_l_41.name, ROIS.ptv_e_ln_l_41.type, ROIS.ptv_e_ln_l_41.color, source = ROIS.ctv_e_ln_l_41, margins = MARGINS.uniform_7mm_expansion)
        x_ptv_41.sourcesA.extend([ptv_e_ln_l_41,ptv_e_ln_r_41])
        x_ctv_41.sourcesA.extend([ptv_e_ln_l_41,ptv_e_ln_r_41])
        site.add_targets([ROIS.ctv_e_ln_r_41, ROIS.ctv_e_ln_l_41,ptv_e_ln_r_41,ptv_e_ln_l_41])
      site.add_targets([ROIS.ctv_e_41, ptv_e_41])
    elif stad == 't3':
      ctv_p_57 = ROI.ROIExpanded(ROIS.ctv_p_57.name, ROIS.ctv_p_57.type, ROIS.ctv_p_57.color, source = ROIS.gtv_p_57, margins = MARGINS.uniform_10mm_expansion)
      ptv_p_57 = ROI.ROIExpanded(ROIS.ptv_p_57.name, ROIS.ptv_p_57.type, ROIS.ptv_p_57.color, source = ctv_p_57, margins = MARGINS.uniform_10mm_expansion) #tilpassede marginer?
      ptv_e_41 = ROI.ROIExpanded(ROIS.ptv_e_41.name, ROIS.ptv_e_46.type, ROIS.ptv_e_46.color, source = ROIS.ctv_e_41, margins = MARGINS.rectum_ptv_50_expansion)
      x_ctv_41 = ROI.ROIAlgebra(ROIS.x_ctv_41.name, ROIS.x_ctv_41.type, ROIS.x_ctv_41.color, sourcesA = [ROIS.ctv_e_41], sourcesB = [ptv_p_57], operator = 'Subtraction', marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
      x_ptv_41 = ROI.ROIAlgebra(ROIS.x_ptv_41.name, ROIS.x_ptv_41.type, ROIS.x_ptv_41.color, sourcesA = [ptv_e_41], sourcesB = [ptv_p_57], operator = 'Subtraction', marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
      site.add_targets([ROIS.gtv_p_57, ctv_p_57, ptv_p_57, x_ctv_41, x_ptv_41])  
      # Choice 3: Number of positive lymph nodes > 2 cm ?
      large_nodes = choices[4]
      if large_nodes == 'with_node_l_1':
        ctv_n_57 = ROI.ROIExpanded(ROIS.ctv_n_57.name, ROIS.ctv_n_57.type, ROIS.ctv_n_57.color, source = ROIS.gtv_n_57, margins = MARGINS.uniform_5mm_expansion)
        ptv_n_57 = ROI.ROIExpanded(ROIS.ptv_n_57.name, ROIS.ptv_n_57.type, ROIS.ptv_n_57.color, source = ctv_n_57, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n_57])
        x_ctv_41.sourcesB.extend([ptv_n_57])
        site.add_targets([ROIS.gtv_n_57, ctv_n_57, ptv_n_57])
      elif large_nodes == 'with_node_l_2':
        ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57])
        x_ctv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57])
        site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57, ctv_n1_57,ctv_n2_57, ptv_n1_57, ptv_n2_57])
      elif large_nodes == 'with_node_l_3':
        ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n3_57 = ROI.ROIExpanded(ROIS.ctv_n3_57.name, ROIS.ctv_n3_57.type, ROIS.ctv_n3_57.color, source = ROIS.gtv_n3_57, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n3_57 = ROI.ROIExpanded(ROIS.ptv_n3_57.name, ROIS.ptv_n3_57.type, ROIS.ptv_n3_57.color, source = ctv_n3_57, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57,ptv_n3_57])
        x_ctv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57,ptv_n3_57])
        site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57,ROIS.gtv_n3_57, ctv_n1_57,ctv_n2_57, ctv_n3_57, ptv_n1_57, ptv_n2_57, ptv_n3_57])
      elif large_nodes == 'with_node_l_4':
        ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n3_57 = ROI.ROIExpanded(ROIS.ctv_n3_57.name, ROIS.ctv_n3_57.type, ROIS.ctv_n3_57.color, source = ROIS.gtv_n3_57, margins = MARGINS.uniform_5mm_expansion)
        ctv_n4_57 = ROI.ROIExpanded(ROIS.ctv_n4_57.name, ROIS.ctv_n4_57.type, ROIS.ctv_n4_57.color, source = ROIS.gtv_n4_57, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n3_57 = ROI.ROIExpanded(ROIS.ptv_n3_57.name, ROIS.ptv_n3_57.type, ROIS.ptv_n3_57.color, source = ctv_n3_57, margins = MARGINS.uniform_8mm_expansion)
        ptv_n4_57 = ROI.ROIExpanded(ROIS.ptv_n4_57.name, ROIS.ptv_n4_57.type, ROIS.ptv_n4_57.color, source = ctv_n4_57, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57,ptv_n3_57,ptv_n4_57])
        x_ctv_41.sourcesB.extend([ptv_n1_57,ptv_n2_57,ptv_n3_57,ptv_n4_57])
        site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57,ROIS.gtv_n3_57,ROIS.gtv_n4_57, ctv_n1_57,ctv_n2_57, ctv_n3_57,ctv_n4_57, ptv_n1_57, ptv_n2_57, ptv_n3_57,ptv_n4_57])
      # Choice 2: Number of positive lymph nodes < 2 cm?
      small_nodes = choices[3]
      if small_nodes == 'with_node_1':
        ctv_n_54 = ROI.ROIExpanded(ROIS.ctv_n_54.name, ROIS.ctv_n_54.type, ROIS.ctv_n_54.color, source = ROIS.gtv_n_54, margins = MARGINS.uniform_5mm_expansion)
        ptv_n_54 = ROI.ROIExpanded(ROIS.ptv_n_54.name, ROIS.ptv_n_54.type, ROIS.ptv_n_54.color, source = ctv_n_54, margins = MARGINS.uniform_8mm_expansion) #stor margin? sjekk i templat
        x_ptv_41.sourcesB.extend([ptv_n_54])
        x_ctv_41.sourcesB.extend([ptv_n_54])
        site.add_targets([ROIS.gtv_n_54, ctv_n_54, ptv_n_54])
      elif small_nodes == 'with_node_2':
        ctv_n1_54 = ROI.ROIExpanded(ROIS.ctv_n1_54.name, ROIS.ctv_n1_54.type, ROIS.ctv_n1_54.color, source = ROIS.gtv_n1_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_54 = ROI.ROIExpanded(ROIS.ctv_n2_54.name, ROIS.ctv_n2_54.type, ROIS.ctv_n2_54.color, source = ROIS.gtv_n2_54, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_54 = ROI.ROIExpanded(ROIS.ptv_n1_54.name, ROIS.ptv_n1_54.type, ROIS.ptv_n1_54.color, source = ctv_n1_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_54 = ROI.ROIExpanded(ROIS.ptv_n2_54.name, ROIS.ptv_n2_54.type, ROIS.ptv_n2_54.color, source = ctv_n2_54, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54])
        x_ctv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54])
        site.add_targets([ROIS.gtv_n1_54, ROIS.gtv_n2_54, ctv_n1_54,ctv_n2_54, ptv_n1_54, ptv_n2_54])
      elif small_nodes == 'with_node_3':
        ctv_n1_54 = ROI.ROIExpanded(ROIS.ctv_n1_54.name, ROIS.ctv_n1_54.type, ROIS.ctv_n1_54.color, source = ROIS.gtv_n1_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_54 = ROI.ROIExpanded(ROIS.ctv_n2_54.name, ROIS.ctv_n2_54.type, ROIS.ctv_n2_54.color, source = ROIS.gtv_n2_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n3_54 = ROI.ROIExpanded(ROIS.ctv_n3_54.name, ROIS.ctv_n3_54.type, ROIS.ctv_n3_54.color, source = ROIS.gtv_n3_54, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_54 = ROI.ROIExpanded(ROIS.ptv_n1_54.name, ROIS.ptv_n1_54.type, ROIS.ptv_n1_54.color, source = ctv_n1_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_54 = ROI.ROIExpanded(ROIS.ptv_n2_54.name, ROIS.ptv_n2_54.type, ROIS.ptv_n2_54.color, source = ctv_n2_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n3_54 = ROI.ROIExpanded(ROIS.ptv_n3_54.name, ROIS.ptv_n3_54.type, ROIS.ptv_n3_54.color, source = ctv_n3_54, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54,ptv_n3_54])
        x_ctv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54,ptv_n3_54])
        site.add_targets([ROIS.gtv_n1_54, ROIS.gtv_n2_54,ROIS.gtv_n3_54, ctv_n1_54,ctv_n2_54, ctv_n3_54, ptv_n1_54, ptv_n2_54, ptv_n3_54])
      elif small_nodes == 'with_node_4':
        ctv_n1_54 = ROI.ROIExpanded(ROIS.ctv_n1_54.name, ROIS.ctv_n1_54.type, ROIS.ctv_n1_54.color, source = ROIS.gtv_n1_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n2_54 = ROI.ROIExpanded(ROIS.ctv_n2_54.name, ROIS.ctv_n2_54.type, ROIS.ctv_n2_54.color, source = ROIS.gtv_n2_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n3_54 = ROI.ROIExpanded(ROIS.ctv_n3_54.name, ROIS.ctv_n3_54.type, ROIS.ctv_n3_54.color, source = ROIS.gtv_n3_54, margins = MARGINS.uniform_5mm_expansion)
        ctv_n4_54 = ROI.ROIExpanded(ROIS.ctv_n4_54.name, ROIS.ctv_n4_54.type, ROIS.ctv_n4_54.color, source = ROIS.gtv_n4_54, margins = MARGINS.uniform_5mm_expansion)
        ptv_n1_54 = ROI.ROIExpanded(ROIS.ptv_n1_54.name, ROIS.ptv_n1_54.type, ROIS.ptv_n1_54.color, source = ctv_n1_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n2_54 = ROI.ROIExpanded(ROIS.ptv_n2_54.name, ROIS.ptv_n2_54.type, ROIS.ptv_n2_54.color, source = ctv_n2_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n3_54 = ROI.ROIExpanded(ROIS.ptv_n3_54.name, ROIS.ptv_n3_54.type, ROIS.ptv_n3_54.color, source = ctv_n3_54, margins = MARGINS.uniform_8mm_expansion)
        ptv_n4_54 = ROI.ROIExpanded(ROIS.ptv_n4_54.name, ROIS.ptv_n4_54.type, ROIS.ptv_n4_54.color, source = ctv_n4_54, margins = MARGINS.uniform_8mm_expansion)
        x_ptv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54,ptv_n3_54,ptv_n4_54])
        x_ctv_41.sourcesB.extend([ptv_n1_54,ptv_n2_54,ptv_n3_54,ptv_n4_54])
        site.add_targets([ROIS.gtv_n1_54, ROIS.gtv_n2_54,ROIS.gtv_n3_54,ROIS.gtv_n4_54, ctv_n1_54,ctv_n2_54, ctv_n3_54,ctv_n4_54, ptv_n1_54, ptv_n2_54, ptv_n3_54,ptv_n4_54])

      # Choice 4: Groin target volume - included or not?
      groin = choices[5]
      # Groin targets included:
      if groin == 'with': #gtv_groin?
        ptv_e_ln_r_41 = ROI.ROIExpanded(ROIS.ptv_e_ln_r_41.name, ROIS.ptv_e_ln_r_41.type, ROIS.ptv_e_ln_r_41.color, source = ROIS.ctv_e_ln_r_41, margins = MARGINS.uniform_7mm_expansion)
        ptv_e_ln_l_41 = ROI.ROIExpanded(ROIS.ptv_e_ln_l_41.name, ROIS.ptv_e_ln_l_41.type, ROIS.ptv_e_ln_l_41.color, source = ROIS.ctv_e_ln_l_41, margins = MARGINS.uniform_7mm_expansion)
        x_ptv_41.sourcesA.extend([ptv_e_ln_l_41,ptv_e_ln_r_41])
        x_ctv_41.sourcesA.extend([ROIS.ctv_e_ln_l_41,ROIS.ctv_e_ln_r_41])
        site.add_targets([ROIS.ctv_e_ln_r_41, ROIS.ctv_e_ln_l_41,ptv_e_ln_r_41,ptv_e_ln_l_41])
      site.add_targets([ROIS.ctv_e_41, ptv_e_41])

    # Create all targets and OARs in RayStation:
    site.create_rois()
