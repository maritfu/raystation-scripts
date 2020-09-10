# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for gyneocological treatments (with pelvic lymph nodes, with pelvic lymph nodes and boost to positive lymph nodes in small pelvis or with pelvic lymph nodes
# and boost to positive lymph nodes in large pelvis, and number of positive lymph nodes)
class DefGyn(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: With pelvic lymph nodes, with pelvic lymph nodes and boost to positive lymph nodes in small pelvis or with pelvic lymph nodes and boost to positive lymph nodes in large pelvis
    nodes = choices[1]
    # Gyn:
    site.add_oars(DEF.gyn_oars) #Andre risikoorganer for andre gyn? 
    if nodes == 'not':
      frac = choices[2]
      if frac == '30': #Flere volumer her?
        ctv_30 = ROI.ROIAlgebra(ROIS.ctv_30.name, ROIS.ctv_30.type, ROIS.ctv_30.color, sourcesA = [ROIS.ctv_p_30], sourcesB = [ROIS.ctv_e_30], marginsA = MARGINS.zero, marginsB = MARGINS.zero) 
        ptv_30 = ROI.ROIAlgebra(ROIS.ptv_30.name, ROIS.ptv_30.type, ROIS.ptv_30.color, sourcesA = [ROIS.ctv_p_30], sourcesB = [ROIS.ctv_e_30], marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_8mm_expansion)   
        site.add_targets([ROIS.gtv_p, ROIS.ctv_e_30, ROIS.ctv_p_30, ctv_30, ptv_30])
      if frac == '50':
        ctv_50 = ROI.ROIAlgebra(ROIS.ctv_50.name, ROIS.ctv_50.type, ROIS.ctv_50.color, sourcesA = [ROIS.ctv_p_50], sourcesB = [ROIS.ctv_e_50, ROIS.ctv_ln_l, ROIS.ctv_ln_r], marginsA = MARGINS.zero, marginsB = MARGINS.zero) 
        ptv_50 = ROI.ROIAlgebra(ROIS.ptv_50.name, ROIS.ptv_50.type, ROIS.ptv_50.color, sourcesA = [ROIS.ctv_p_50], sourcesB = [ROIS.ctv_e_50, ROIS.ctv_ln_l, ROIS.ctv_ln_r], marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_8mm_expansion)   
        site.add_targets([ROIS.gtv_p, ctv_50]) #flere elektive volumer?
        nr_nodes = choices[3]
        if nr_nodes == 'with_node_1':
          ctv_n_50 = ROI.ROIExpanded(ROIS.ctv_n_50.name, ROIS.ctv_n_50.type, ROIS.ctv_n_50.color, source = ROIS.gtv_n_50, margins = MARGINS.uniform_5mm_expansion)
          #ptv_n_50 = ROI.ROIExpanded(ROIS.ptv_n_50.name, ROIS.ptv_n_50.type, ROIS.ptv_n_50.color, source = ctv_n_50, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          ptv_50.sourcesB.extend([ctv_n_50])
          site.add_targets([ROIS.gtv_n_50, ctv_n_50])
        elif nr_nodes in ['with_node_2','with_node_3','with_node_4']:
          ctv_n1_50 = ROI.ROIExpanded(ROIS.ctv_n1_50.name, ROIS.ctv_n1_50.type, ROIS.ctv_n1_50.color, source = ROIS.gtv_n1_50, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_50 = ROI.ROIExpanded(ROIS.ctv_n2_50.name, ROIS.ctv_n2_50.type, ROIS.ctv_n2_50.color, source = ROIS.gtv_n2_50, margins = MARGINS.uniform_5mm_expansion)
          #ptv_n_50 = ROI.ROIAlgebra(ROIS.ptv_n_50.name, ROIS.ptv_n_50.type, ROIS.ptv_n_50.color, sourcesA = [ctv_n1_50], sourcesB = [ctv_n2_50], marginsA = MARGINS.uniform_8mm_expansion, marginsB = MARGINS.uniform_8mm_expansion)
          ptv_50.sourcesB.extend([ctv_n1_50, ctv_n2_50])
          site.add_targets([ROIS.gtv_n1_50, ROIS.gtv_n2_50, ctv_n1_50, ctv_n2_50])
          if nr_nodes in ['with_node_3','with_node_4']:
            ctv_n3_50 = ROI.ROIExpanded(ROIS.ctv_n3_50.name, ROIS.ctv_n3_50.type, ROIS.ctv_n3_50.color, source = ROIS.gtv_n3_50, margins = MARGINS.uniform_5mm_expansion)
            ptv_50.sourcesB.extend([ctv_n3_50])
            site.add_targets([ROIS.gtv_n3_50, ctv_n3_50])
            if nr_nodes == 'with_node_4':
              ctv_n4_50 = ROI.ROIExpanded(ROIS.ctv_n4_50.name, ROIS.ctv_n4_50.type, ROIS.ctv_n4_50.color, source = ROIS.gtv_n4_50, margins = MARGINS.uniform_5mm_expansion)
              ptv_50.sourcesB.extend([ctv_n4_50])
              site.add_targets([ROIS.gtv_n4_50, ctv_n4_50])
        site.add_targets([ROIS.ctv_p_50, ROIS.ctv_e_50, ROIS.ctv_ln_r,ROIS.ctv_ln_l,ptv_50 ])   
      
    else:
      ctv_45 = ROI.ROIAlgebra(ROIS.ctv_45.name, ROIS.ctv_45.type, ROIS.ctv_45.color, sourcesA = [ROIS.ctv_p_45], sourcesB = [ROIS.ctv_e_45], marginsA = MARGINS.zero, marginsB = MARGINS.zero) 
      ptv_45 = ROI.ROIAlgebra(ROIS.ptv_45.name, ROIS.ptv_45.type, ROIS.ptv_45.color, sourcesA = [ROIS.ctv_p_45], sourcesB = [ROIS.ctv_e_45], marginsA = MARGINS.gyn_ptv_p_45_expansion, marginsB = MARGINS.uniform_8mm_expansion)   
      #ptv_p_45 = ROI.ROIExpanded(ROIS.ptv_p_45.name, ROIS.ptv_p_45.type, ROIS.ptv_p_45.color, source = ROIS.ctv_p_45, margins = MARGINS.gyn_ptv_p_45_expansion)
      #ptv_e_45 = ROI.ROIExpanded(ROIS.ptv_e_45.name, ROIS.ptv_e_45.type, ROIS.ptv_e_45.color, source = ROIS.ctv_e_45, margins = MARGINS.uniform_8mm_expansion)
      

      site.add_targets([ROIS.gtv_p])
      
      if nodes == 'with':
        x_gtv_p = ROI.ROIExpanded(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, source = ROIS.gtv_p, margins = MARGINS.uniform_10mm_expansion)
        site.add_targets([ROIS.ctv_p_45, ROIS.ctv_e_45, ctv_45, ptv_45, x_gtv_p])   
      elif nodes == 'with_node':
        # Choice 2: Number of nodes included?
        nr_nodes = choices[2]
        
        if nr_nodes == 'with_node_1':
          ctv_n_55 = ROI.ROIExpanded(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, source = ROIS.gtv_n_55, margins = MARGINS.uniform_5mm_expansion)
          ptv_n_55 = ROI.ROIExpanded(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, source = ctv_n_55, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
          site.add_targets([ROIS.gtv_n_55, ctv_n_55, ctv_45, x_gtv_p,x_ptv_45])
        elif nr_nodes in ['with_node_2','with_node_3','with_node_4']:
          ctv_n1_55 = ROI.ROIExpanded(ROIS.ctv_n1_55.name, ROIS.ctv_n1_55.type, ROIS.ctv_n1_55.color, source = ROIS.gtv_n1_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_55 = ROI.ROIExpanded(ROIS.ctv_n2_55.name, ROIS.ctv_n2_55.type, ROIS.ctv_n2_55.color, source = ROIS.gtv_n2_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_55 = ROI.ROIAlgebra(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, sourcesA = [ctv_n1_55], sourcesB = [ctv_n2_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_55 = ROI.ROIExpanded(ROIS.ptv_n1_55.name, ROIS.ptv_n1_55.type, ROIS.ptv_n1_55.color, source = ctv_n1_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n2_55 = ROI.ROIExpanded(ROIS.ptv_n2_55.name, ROIS.ptv_n2_55.type, ROIS.ptv_n2_55.color, source = ctv_n2_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n_55 = ROI.ROIAlgebra(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, sourcesA = [ ptv_n1_55], sourcesB = [ptv_n2_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)   
          site.add_targets([ROIS.gtv_n1_55, ROIS.gtv_n2_55, ctv_n1_55, ctv_n2_55, ctv_n_55,ctv_45,x_gtv_p,x_ptv_45,ptv_n1_55, ptv_n2_55])
          if nr_nodes in ['with_node_3','with_node_4']:
            ctv_n3_55 = ROI.ROIExpanded(ROIS.ctv_n3_55.name, ROIS.ctv_n3_55.type, ROIS.ctv_n3_55.color, source = ROIS.gtv_n3_55, margins = MARGINS.uniform_5mm_expansion)
            ptv_n3_55 = ROI.ROIExpanded(ROIS.ptv_n3_55.name, ROIS.ptv_n3_55.type, ROIS.ptv_n3_55.color, source = ctv_n3_55, margins = MARGINS.uniform_8mm_expansion)
            ptv_n_55.sourcesB.extend([ctv_n3_55])
            site.add_targets([ROIS.gtv_n3_55, ctv_n3_55, ptv_n3_55])
            if nr_nodes == 'with_node_4':
              ctv_n4_55 = ROI.ROIExpanded(ROIS.ctv_n4_55.name, ROIS.ctv_n4_55.type, ROIS.ctv_n4_55.color, source = ROIS.gtv_n4_55, margins = MARGINS.uniform_5mm_expansion)
              ptv_n4_55 = ROI.ROIExpanded(ROIS.ptv_n4_55.name, ROIS.ptv_n4_55.type, ROIS.ptv_n4_55.color, source = ctv_n4_55, margins = MARGINS.uniform_8mm_expansion)
              ptv_n_55.sourcesB.extend([ctv_n4_55])
              site.add_targets([ROIS.gtv_n4_55, ctv_n4_55, ptv_n4_55])
        site.add_targets([ROIS.ctv_p_45, ROIS.ctv_e_45,ptv_n_55, ptv_45 ])
      elif nodes == 'with_node_57':
        nr_nodes_55 = choices[2]
        nr_nodes_57 = choices[3]
        ctv_45 = ROI.ROIAlgebra(ROIS.ctv_45.name, ROIS.ctv_45.type, ROIS.ctv_45.color, sourcesA = [ROIS.ctv_p_45], sourcesB = [ROIS.ctv_e_45], marginsA = MARGINS.zero, marginsB = MARGINS.zero) 
        if nr_nodes_57 == 'with_node_57_1':
          ctv_n_57 = ROI.ROIExpanded(ROIS.ctv_n_57.name, ROIS.ctv_n_57.type, ROIS.ctv_n_57.color, source = ROIS.gtv_n_57, margins = MARGINS.uniform_5mm_expansion)
          ptv_n_57 = ROI.ROIExpanded(ROIS.ptv_n_57.name, ROIS.ptv_n_57.type, ROIS.ptv_n_57.color, source = ctv_n_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n_57,x_gtv_p,x_ptv_45])
        elif nr_nodes_57 =='with_node_57_2': 
          ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_57 = ROI.ROIAlgebra(ROIS.ctv_n_57.name, ROIS.ctv_n_57.type, ROIS.ctv_n_57.color, sourcesA = [ctv_n1_57], sourcesB = [ctv_n2_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n_57 = ROI.ROIAlgebra(ROIS.ptv_n_57.name, ROIS.ptv_n_57.type, ROIS.ptv_n_57.color, sourcesA = [ptv_n1_57], sourcesB = [ptv_n2_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57,ctv_n1_57, ctv_n2_57, x_gtv_p,x_ptv_45])
        elif nr_nodes_57 =='with_node_57_3':
          ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n3_57 = ROI.ROIExpanded(ROIS.ctv_n3_57.name, ROIS.ctv_n3_57.type, ROIS.ctv_n3_57.color, source = ROIS.gtv_n3_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_57 = ROI.ROIAlgebra(ROIS.ctv_n_57.name, ROIS.ctv_n_57.type, ROIS.ctv_n_57.color, sourcesA = [ctv_n1_57], sourcesB = [ctv_n2_57, ctv_n3_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n3_57 = ROI.ROIExpanded(ROIS.ptv_n3_57.name, ROIS.ptv_n3_57.type, ROIS.ptv_n3_57.color, source = ctv_n3_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n_57 = ROI.ROIAlgebra(ROIS.ptv_n_57.name, ROIS.ptv_n_57.type, ROIS.ptv_n_57.color, sourcesA = [ptv_n1_57], sourcesB = [ptv_n2_57, ptv_n3_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57,ROIS.gtv_n3_57,ctv_n1_57, ctv_n2_57,ctv_n3_57, x_gtv_p,x_ptv_45])
        elif nr_nodes_57 == 'with_node_57_4':
          ctv_n1_57 = ROI.ROIExpanded(ROIS.ctv_n1_57.name, ROIS.ctv_n1_57.type, ROIS.ctv_n1_57.color, source = ROIS.gtv_n1_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_57 = ROI.ROIExpanded(ROIS.ctv_n2_57.name, ROIS.ctv_n2_57.type, ROIS.ctv_n2_57.color, source = ROIS.gtv_n2_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n3_57 = ROI.ROIExpanded(ROIS.ctv_n3_57.name, ROIS.ctv_n3_57.type, ROIS.ctv_n3_57.color, source = ROIS.gtv_n3_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n4_57 = ROI.ROIExpanded(ROIS.ctv_n4_57.name, ROIS.ctv_n4_57.type, ROIS.ctv_n4_57.color, source = ROIS.gtv_n4_57, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_57 = ROI.ROIAlgebra(ROIS.ctv_n_57.name, ROIS.ctv_n_57.type, ROIS.ctv_n_57.color, sourcesA = [ctv_n1_57], sourcesB = [ctv_n2_57, ctv_n3_57,ctv_n4_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_57 = ROI.ROIExpanded(ROIS.ptv_n1_57.name, ROIS.ptv_n1_57.type, ROIS.ptv_n1_57.color, source = ctv_n1_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          ptv_n2_57 = ROI.ROIExpanded(ROIS.ptv_n2_57.name, ROIS.ptv_n2_57.type, ROIS.ptv_n2_57.color, source = ctv_n2_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n3_57 = ROI.ROIExpanded(ROIS.ptv_n3_57.name, ROIS.ptv_n3_57.type, ROIS.ptv_n3_57.color, source = ctv_n3_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n4_57 = ROI.ROIExpanded(ROIS.ptv_n4_57.name, ROIS.ptv_n4_57.type, ROIS.ptv_n4_57.color, source = ctv_n4_57, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?         
          ptv_n_57 = ROI.ROIAlgebra(ROIS.ptv_n_57.name, ROIS.ptv_n_57.type, ROIS.ptv_n_57.color, sourcesA = [ptv_n1_57], sourcesB = [ptv_n2_57, ptv_n3_57,ptv_n4_57], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_45 = ROI.ROIAlgebra(ROIS.x_ptv_45.name, ROIS.x_ptv_45.type, ROIS.x_ptv_45.color, sourcesA = [ptv_45], sourcesB = [ptv_n_57], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_57, ROIS.gtv_n2_57,ROIS.gtv_n3_57,ROIS.gtv_n4_57,ctv_n1_57, ctv_n2_57,ctv_n3_57,ctv_n4_57, x_gtv_p,x_ptv_45])
        
        if nr_nodes_55 == 'with_node_55_1':
          ctv_n_55 = ROI.ROIExpanded(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, source = ROIS.gtv_n_55, margins = MARGINS.uniform_5mm_expansion)
          ptv_n_55 = ROI.ROIExpanded(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, source = ctv_n_55, margins = MARGINS.uniform_8mm_expansion) #Ha en samlet ptv55?
          x_gtv_p.sourcesB.extend([ptv_n_55])
          site.add_targets([ROIS.gtv_n_55])
        elif nr_nodes_55 == 'with_node_55_2':
          ctv_n1_55 = ROI.ROIExpanded(ROIS.ctv_n1_55.name, ROIS.ctv_n1_55.type, ROIS.ctv_n1_55.color, source = ROIS.gtv_n1_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_55 = ROI.ROIExpanded(ROIS.ctv_n2_55.name, ROIS.ctv_n2_55.type, ROIS.ctv_n2_55.color, source = ROIS.gtv_n2_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_55 = ROI.ROIAlgebra(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, sourcesA = [ctv_n1_55], sourcesB = [ctv_n2_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_55 = ROI.ROIExpanded(ROIS.ptv_n1_55.name, ROIS.ptv_n1_55.type, ROIS.ptv_n1_55.color, source = ctv_n1_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n2_55 = ROI.ROIExpanded(ROIS.ptv_n2_55.name, ROIS.ptv_n2_55.type, ROIS.ptv_n2_55.color, source = ctv_n2_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n_55 = ROI.ROIAlgebra(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, sourcesA = [ ptv_n1_55], sourcesB = [ptv_n2_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57, ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_55, ROIS.gtv_n2_55, ctv_n1_55, ctv_n2_55])
        elif nr_nodes_55 =='with_node_55_3':
          ctv_n1_55 = ROI.ROIExpanded(ROIS.ctv_n1_55.name, ROIS.ctv_n1_55.type, ROIS.ctv_n1_55.color, source = ROIS.gtv_n1_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_55 = ROI.ROIExpanded(ROIS.ctv_n2_55.name, ROIS.ctv_n2_55.type, ROIS.ctv_n2_55.color, source = ROIS.gtv_n2_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n3_55 = ROI.ROIExpanded(ROIS.ctv_n3_55.name, ROIS.ctv_n3_55.type, ROIS.ctv_n3_55.color, source = ROIS.gtv_n3_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_55 = ROI.ROIAlgebra(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, sourcesA = [ctv_n1_55], sourcesB = [ctv_n2_55, ctv_n3_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_55 = ROI.ROIExpanded(ROIS.ptv_n1_55.name, ROIS.ptv_n1_55.type, ROIS.ptv_n1_55.color, source = ctv_n1_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n2_55 = ROI.ROIExpanded(ROIS.ptv_n2_55.name, ROIS.ptv_n2_55.type, ROIS.ptv_n2_55.color, source = ctv_n2_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n3_55 = ROI.ROIExpanded(ROIS.ptv_n3_55.name, ROIS.ptv_n3_55.type, ROIS.ptv_n3_55.color, source = ctv_n3_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n_55 = ROI.ROIAlgebra(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, sourcesA = [ ptv_n1_55], sourcesB = [ptv_n2_55, ptv_n3_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57, ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_55, ROIS.gtv_n2_55, ROIS.gtv_n3_55, ctv_n1_55, ctv_n2_55, ctv_n3_55])
        elif nr_nodes_55 =='with_node_55_4':
          ctv_n1_55 = ROI.ROIExpanded(ROIS.ctv_n1_55.name, ROIS.ctv_n1_55.type, ROIS.ctv_n1_55.color, source = ROIS.gtv_n1_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n2_55 = ROI.ROIExpanded(ROIS.ctv_n2_55.name, ROIS.ctv_n2_55.type, ROIS.ctv_n2_55.color, source = ROIS.gtv_n2_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n3_55 = ROI.ROIExpanded(ROIS.ctv_n3_55.name, ROIS.ctv_n3_55.type, ROIS.ctv_n3_55.color, source = ROIS.gtv_n3_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n4_55 = ROI.ROIExpanded(ROIS.ctv_n4_55.name, ROIS.ctv_n4_55.type, ROIS.ctv_n4_55.color, source = ROIS.gtv_n4_55, margins = MARGINS.uniform_5mm_expansion)
          ctv_n_55 = ROI.ROIAlgebra(ROIS.ctv_n_55.name, ROIS.ctv_n_55.type, ROIS.ctv_n_55.color, sourcesA = [ctv_n1_55], sourcesB = [ctv_n2_55, ctv_n3_55, ctv_n4_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1_55 = ROI.ROIExpanded(ROIS.ptv_n1_55.name, ROIS.ptv_n1_55.type, ROIS.ptv_n1_55.color, source = ctv_n1_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n2_55 = ROI.ROIExpanded(ROIS.ptv_n2_55.name, ROIS.ptv_n2_55.type, ROIS.ptv_n2_55.color, source = ctv_n2_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n3_55 = ROI.ROIExpanded(ROIS.ptv_n3_55.name, ROIS.ptv_n3_55.type, ROIS.ptv_n3_55.color, source = ctv_n3_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n4_55 = ROI.ROIExpanded(ROIS.ptv_n4_55.name, ROIS.ptv_n4_55.type, ROIS.ptv_n4_55.color, source = ctv_n4_55, margins = MARGINS.uniform_8mm_expansion)
          ptv_n_55 = ROI.ROIAlgebra(ROIS.ptv_n_55.name, ROIS.ptv_n_55.type, ROIS.ptv_n_55.color, sourcesA = [ ptv_n1_55], sourcesB = [ptv_n2_55, ptv_n3_55, ptv_n4_55], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_gtv_p = ROI.ROIAlgebra(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, sourcesA = [ROIS.gtv_p], sourcesB = [ptv_n_57, ptv_n_55], operator = 'Subtraction', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.uniform_7mm_expansion)
          site.add_targets([ROIS.gtv_n1_55, ROIS.gtv_n2_55,ROIS.gtv_n3_55,ROIS.gtv_n4_55, ctv_n1_55, ctv_n2_55,ctv_n3_55,ctv_n4_55])
        if nr_nodes_57 == 'with_node_57_1':
          site.add_targets([ptv_n_57])
        elif nr_nodes_57 == 'with_node_57_2':
          site.add_targets([ptv_n1_57, ptv_n2_57, ptv_n_57])
        elif nr_nodes_57 == 'with_node_57_3':
          site.add_targets([ptv_n1_57, ptv_n2_57,ptv_n3_57, ptv_n_57])
        elif nr_nodes_57 =='with_node_57_4':
          site.add_targets([ptv_n1_57, ptv_n2_57,ptv_n3_57,ptv_n4_57, ptv_n_57])
          
        if nr_nodes_55 == 'with_node_55_2':
          site.add_targets([ptv_n1_55, ptv_n2_55])
        elif nr_nodes_55 == 'with_node_55_3':
          site.add_targets([ptv_n1_55, ptv_n2_55,ptv_n3_55])
        elif nr_nodes_55 =='with_node_55_4':
          site.add_targets([ptv_n1_55, ptv_n2_55, ptv_n3_55, ptv_n4_55])

        if nodes == 'with_node_57':
          site.add_targets([ptv_n_55,ptv_45,ctv_n_57,ctv_n_55,ROIS.ctv_p_45, ROIS.ctv_e_45,ctv_45])
        #if nodes == 'with_node_57':
        #  site.add_targets([ctv_n_57,ctv_n_55,ctv_45]) 

    # Create all targets and OARs in RayStation:
    site.create_rois()
