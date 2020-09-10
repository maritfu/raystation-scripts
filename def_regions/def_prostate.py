# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for prostate treatments (prostate/prostate bed, with or without lymph nodes, normo/hypofractionated).
class DefProstate(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Region - prostate or bed?
    region = choices[1]
    # Prostate:
    if region == 'prostate':
      # Choice 2: Fractionation - normo or hypo?
      frac = choices[2]
      if frac == 'palliative':
        site.add_oars(DEF.prostate_palliative_oars)
      else:
        site.add_oars(DEF.prostate_oars)
      # Conventionally fractionated prostate with vesicles (2.2Gy x 35):
      if frac == 'normo':
        # Choice 3: Nodes - included or not?
        nodes = choices[3]
        ptv_p1_77 = ROI.ROIExpanded(ROIS.ptv_p1_77.name, ROIS.ptv_p1_77.type, ROIS.ptv_p1_77.color, source = ROIS.ctv_p1_77, margins = MARGINS.prostate_seed_expansion)
        ptv_p2_70 = ROI.ROIExpanded(ROIS.ptv_p2_70.name, ROIS.ptv_p2_70.type, ROIS.ptv_p2_70.color, source = ROIS.ctv_p2_70, margins = MARGINS.uniform_10mm_expansion)
        x_ptv_70 =  ROI.ROIAlgebra(ROIS.x_ptv_70.name, ROIS.x_ptv_70.type, ROIS.x_ptv_70.color, sourcesA = [ptv_p2_70], sourcesB = [ptv_p1_77], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        x_bowelbag = ROI.ROIAlgebra(ROIS.x_bowelbag.name, ROIS.x_bowelbag.type, ROIS.x_bowelbag.color, sourcesA = [ROIS.bowel_bag], sourcesB = [ptv_p1_77, ptv_p2_70], operator='Subtraction', marginsB = MARGINS.uniform_10mm_expansion)
        site.add_targets([ROIS.ctv_p1_77, ROIS.ctv_p2_70, ptv_p1_77,  ptv_p2_70])
        if nodes == 'without':
          site.add_targets([x_ptv_70])
        elif nodes in ['with_node','with']:
          ptv_e_56 = ROI.ROIExpanded(ROIS.ptv_e_56.name, ROIS.ptv_e_56.type, ROIS.ptv_e_56.color, source = ROIS.ctv_e_56, margins = MARGINS.prostate_lymph_nodes_seed_expansion)
          x_ctv_56 = ROI.ROIAlgebra(ROIS.x_ctv_56.name, ROIS.x_ctv_56.type, ROIS.x_ctv_56.color, sourcesA = [ROIS.ctv_e_56], sourcesB = [ptv_p1_77, ptv_p2_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_56 = ROI.ROIAlgebra(ROIS.x_ptv_56.name, ROIS.x_ptv_56.type, ROIS.x_ptv_56.color, sourcesA = [ptv_e_56], sourcesB = [ptv_p1_77, ptv_p2_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          x_bowelbag.sourcesB.extend([ptv_e_56])
          site.add_targets([x_ctv_56, x_ptv_56]) 
          if nodes == 'with_node':
            nr_nodes = choices[4]
            if nr_nodes == 'with_node_1':
              ptv_n_70 = ROI.ROIExpanded(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, source = ROIS.ctv_n_70, margins = MARGINS.prostate_lymph_nodes_seed_expansion) #Ha en samlet ptv70?
              site.add_targets([ROIS.ctv_n_70, ptv_n_70])
            elif nr_nodes in ['with_node_2','with_node_3']:
              ptv_n_70 = ROI.ROIAlgebra(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, sourcesA = [ROIS.ctv_n1_70], sourcesB = [ROIS.ctv_n1_70], marginsA = MARGINS.prostate_lymph_nodes_seed_expansion, marginsB = MARGINS.prostate_lymph_nodes_seed_expansion)
              x_bowelbag.sourcesB.extend([ptv_n_70])
              site.add_targets([ROIS.ctv_n1_70, ROIS.ctv_n2_70, ptv_n_70])
              if nr_nodes == 'with_node_3':
                ptv_n_70.sourcesB.extend([ROIS.ctv_n3_70])
                site.add_targets([ROIS.ctv_n3_70])
          
        site.add_oars([x_bowelbag])
        site.add_targets([ROIS.ctv_e_56, ptv_e_56,x_ptv_70])                     
        
      # Hypofractionated prostate with vesicles (3 Gy x 20):
      elif frac == 'hypo_60':
        vesicles = choices[3]
        if vesicles == 'vesicles':
          ctv_60 = ROI.ROIAlgebra(ROIS.ctv_60.name, ROIS.ctv_60.type, ROIS.ctv_60.color, sourcesA = [ROIS.ctv_p1_60], sourcesB = [ROIS.ctv_p2_60], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_p1_60 = ROI.ROIExpanded(ROIS.ptv_p1_60.name, ROIS.ptv_p1_60.type, ROIS.ptv_p1_60.color, source = ROIS.ctv_p1_60, margins = MARGINS.prostate_seed_expansion)
          ptv_p2_60 = ROI.ROIExpanded(ROIS.ptv_p2_60.name, ROIS.ptv_p2_60.type, ROIS.ptv_p2_60.color, source = ROIS.ctv_p2_60, margins = MARGINS.uniform_10mm_expansion)
          ptv_60 = ROI.ROIAlgebra(ROIS.ptv_60.name, ROIS.ptv_60.type, ROIS.ptv_60.color, sourcesA = [ptv_p1_60], sourcesB = [ptv_p2_60], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ctv_60, ROIS.ctv_p1_60, ptv_p1_60, ROIS.ctv_p2_60, ptv_p2_60, ptv_60])
        else:
          ptv_p1_60 = ROI.ROIExpanded(ROIS.ptv_p1_60.name, ROIS.ptv_p1_60.type, ROIS.ptv_p1_60.color, source = ROIS.ctv_p1_60, margins = MARGINS.prostate_seed_expansion)
          site.add_targets([ROIS.ctv_p1_60, ptv_p1_60])
      elif frac == 'palliative':
        ptv = ROI.ROIExpanded(ROIS.ptv.name, ROIS.ptv.type, ROIS.ptv.color, source = ROIS.ctv_underived , margins = MARGINS.prostate_bone_match_expansion)
        site.add_targets([ptv, ROIS.ctv_underived])
    # Prostate bed:
    else:
      # Choice 2: Nodes - included or not?
      frac = choices[2]
      site.add_oars(DEF.prostate_bed_oars)
      # With nodes:
      if frac == 'normo':
        nodes = choices[3]
        ptv_sb_70 = ROI.ROIExpanded(ROIS.ptv_sb_70.name, ROIS.ptv_sb_70.type, ROIS.ptv_sb_70.color, source = ROIS.ctv_sb_70, margins = MARGINS.prostate_bone_match_expansion)
        x_bowelbag = ROI.ROIAlgebra(ROIS.x_bowelbag.name, ROIS.x_bowelbag.type, ROIS.x_bowelbag.color, sourcesA = [ROIS.bowel_bag], sourcesB = [ptv_sb_70], operator='Subtraction', marginsB = MARGINS.uniform_10mm_expansion)
        site.add_targets([ROIS.ctv_sb_70, ptv_sb_70])
        if nodes in ['with_node','with']:
          ptv_e_56 = ROI.ROIExpanded(ROIS.ptv_e_56.name, ROIS.ptv_e_56.type, ROIS.ptv_e_56.color, source = ROIS.ctv_e_56, margins = MARGINS.uniform_7mm_expansion)
          x_ctv_56 = ROI.ROIAlgebra(ROIS.x_ctv_56.name, ROIS.x_ctv_56.type, ROIS.x_ctv_56.color, sourcesA = [ROIS.ctv_e_56], sourcesB = [ptv_sb_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          x_ptv_56 = ROI.ROIAlgebra(ROIS.x_ptv_56.name, ROIS.x_ptv_56.type, ROIS.x_ptv_56.color, sourcesA = [ptv_e_56], sourcesB = [ptv_sb_70], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_7mm_expansion)
          x_bowelbag.sourcesB.extend([ptv_e_56])
          site.add_targets([x_ctv_56, x_ptv_56])                           
          if nodes == 'with_node':
            nr_nodes = choices[4]
            if nr_nodes == 'with_node_1':
              ptv_n_70 = ROI.ROIExpanded(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, source = ROIS.ctv_n_70, margins = MARGINS.prostate_lymph_nodes_seed_expansion) #Ha en samlet ptv70?
              x_bowelbag.sourcesB.extend([ptv_n_70])
              site.add_targets([ROIS.ctv_n_70, ptv_n_70])
            elif nr_nodes in ['with_node_2','with_node_3']:
              ptv_n_70 = ROI.ROIAlgebra(ROIS.ptv_n_70.name, ROIS.ptv_n_70.type, ROIS.ptv_n_70.color, sourcesA = [ROIS.ctv_n1_70], sourcesB = [ROIS.ctv_n2_70], marginsA = MARGINS.prostate_lymph_nodes_seed_expansion, marginsB = MARGINS.prostate_lymph_nodes_seed_expansion)
              x_bowelbag.sourcesB.extend([ptv_n_70])
              site.add_targets([ROIS.ctv_n1_70, ROIS.ctv_n2_70, ptv_n_70])
              if nr_nodes == 'with_node_3':
                ptv_n_70.sourcesB.extend([ROIS.ctv_n3_70])
                site.add_targets([ROIS.ctv_n3_70])
                
        # Common for bed (with or without nodes):
        site.add_oars([x_bowelbag, ROIS.bowel_bag])
        site.add_targets([ROIS.ctv_e_56, ptv_e_56])
      else:
        ptv = ROI.ROIExpanded(ROIS.ptv_sb.name, ROIS.ptv_sb.type, ROIS.ptv_sb.color, source = ROIS.ctv_sb, margins = MARGINS.prostate_bone_match_expansion)
        x_bowelbag = ROI.ROIAlgebra(ROIS.x_bowelbag.name, ROIS.x_bowelbag.type, ROIS.x_bowelbag.color, sourcesA = [ROIS.bowel_bag], sourcesB = [ptv], operator='Subtraction', marginsB = MARGINS.uniform_10mm_expansion)
        
        site.add_oars([x_bowelbag, ROIS.bowel_bag])
        site.add_targets([ptv, ROIS.ctv_sb])

    # Create all targets and OARs in RayStation:
    site.create_rois()
