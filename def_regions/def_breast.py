# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for breast treatments (local/locoregional, with/without IMN, with/without boost).
class DefBreast(object):


  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Local/Regional/Regional with IMN
    region = choices[1]
    # Choice 2: Side - Left or right?
    side = choices[2]
    if region == 'tang':
      # Breast with tangential fields
      site.add_oars(DEF.breast_tang_oars)
      if side == 'right':
        site.add_oars([ROIS.breast_r_draft,ROIS.breast_l_contralat_draft,ROIS.breast_l])
        ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv_p.color, sourcesA = [ROIS.breast_r_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
        ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_tang_ptv_p_expansion, marginsB = MARGINS.uniform_5mm_contraction)
        z_match = ROI.ROIAlgebra(ROIS.z_match.name, ROIS.z_match.type, ROIS.z_match.color, sourcesA = [ptv_pc], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.breast_tang_r_match_expansion, marginsB = MARGINS.zero)
      else:
        site.add_oars([ROIS.breast_l_draft,ROIS.breast_r_contralat_draft,ROIS.breast_r])
        ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv_p.color, sourcesA = [ROIS.breast_l_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
        ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_tang_ptv_p_expansion, marginsB = MARGINS.uniform_5mm_contraction)
        z_match = ROI.ROIAlgebra(ROIS.z_match.name, ROIS.z_match.type, ROIS.z_match.color, sourcesA = [ptv_pc], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.breast_tang_l_match_expansion, marginsB = MARGINS.zero)

      site.add_targets([ctv_p, ptv_pc,z_match])
      # Choice 2: With our without boost?
      boost = choices[3]
      # Add volumes for boost (2Gy x 8) if selected:
      if boost == 'with':
        ptv_boost = ROI.ROIAlgebra(ROIS.ptv_boost.name, ROIS.ptv_boost.type, ROIS.ptv_boost.color, sourcesA = [ROIS.ctv_boost], sourcesB = [ptv_pc], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
        site.add_targets([ROIS.ctv_boost, ptv_boost])
    elif region in ['reg-1','reg','imn']:
      if region == 'reg-1':
        # Breast where regional lymph nodes minus level 1 with or without IMN included
        # Choice 3: With our without boost?
        imn = choices[2]
        side = choices[3]
        boost = choices[4]
        site.add_oars(DEF.breast_reg_oars)
        # Hypofractionated
        if side == 'right':
          ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv.color, sourcesA = [ROIS.breast_r_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
          ctv_n = ROI.ROIAlgebra(ROIS.ctv_n.name, ROIS.ctv_n.type, ROIS.ctv_n.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ctv_p], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_ptv_p = ROI.ROIExpanded(ROIS.x_ptv_p.name, ROIS.x_ptv_p.type, ROIS.x_ptv_p.color, source = ctv_p, margins = MARGINS.breast_ptv_p_r_expansion)
          ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_ptv_pc_r_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          site.add_oars([ROIS.breast_r_draft, ROIS.breast_l_contralat_draft, ROIS.humeral_r, ROIS.breast_l, ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r])
        else: # (left)
          ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv.color, sourcesA = [ROIS.breast_l_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
          ctv_n = ROI.ROIAlgebra(ROIS.ctv_n.name, ROIS.ctv_n.type, ROIS.ctv_n.color, sourcesA = [ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ctv_p], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_ptv_p = ROI.ROIExpanded(ROIS.x_ptv_p.name, ROIS.x_ptv_p.type, ROIS.x_ptv_p.color, source = ctv_p, margins = MARGINS.breast_ptv_p_l_expansion)
          ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_ptv_pc_l_expansion, marginsB = MARGINS.uniform_5mm_contraction)        
          site.add_oars([ROIS.breast_l_draft, ROIS.breast_r_contralat_draft, ROIS.humeral_l, ROIS.breast_r, ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l])
        
        if imn == 'not_imn':
          if side == 'right':
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_r], sourcesB = [ROIS.level2_r, ROIS.level3_r, ROIS.level4_r],  marginsA = MARGINS.breast_ptv_n_r_expansion, marginsB = MARGINS.breast_ptv_n_r_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          else:
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_l],sourcesB = [ ROIS.level2_l, ROIS.level3_l, ROIS.level4_l],  marginsA = MARGINS.breast_ptv_n_l_expansion, marginsB = MARGINS.breast_ptv_n_l_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
        elif imn == 'imn':
          if side == 'right':
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.imn],  marginsA = MARGINS.breast_ptv_n_r_expansion, marginsB = MARGINS.uniform_5mm_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          else:
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.imn],  marginsA = MARGINS.breast_ptv_n_l_expansion, marginsB = MARGINS.uniform_5mm_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          ctv_n.sourcesA.extend([ROIS.imn])
          ptv_n_imn = ROI.ROIExpanded(ROIS.ptv_n_imn.name, ROIS.ptv_n_imn.type, ROIS.ptv_n_imn.color, source = ROIS.imn, margins = MARGINS.uniform_5mm_expansion)
          site.add_targets([ptv_n_imn])
          site.add_oars([ROIS.imn])
      elif region in ['reg','imn']:
        # Breast where regional lymph nodes or IMN is included
        # Choice 3: With our without boost?
        imn = choices[2]
        side = choices[3]
        boost = choices[4]
        site.add_oars(DEF.breast_reg_oars)
        
        # Hypofractionated
        if side == 'right':
          ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv.color, sourcesA = [ROIS.breast_r_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
          ctv_n = ROI.ROIAlgebra(ROIS.ctv_n.name, ROIS.ctv_n.type, ROIS.ctv_n.color, sourcesA = [ROIS.level_r, ROIS.level1_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ctv_p], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_ptv_p = ROI.ROIExpanded(ROIS.x_ptv_p.name, ROIS.x_ptv_p.type, ROIS.x_ptv_p.color, source = ctv_p, margins = MARGINS.breast_ptv_p_r_expansion)
          ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_ptv_pc_r_expansion, marginsB = MARGINS.uniform_5mm_contraction)
          site.add_oars([ROIS.breast_r_draft, ROIS.breast_l_contralat_draft, ROIS.humeral_r, ROIS.breast_l, ROIS.level_r, ROIS.level1_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r])
        else: # (left)
          ctv_p = ROI.ROIAlgebra(ROIS.ctv_p.name, ROIS.ctv_p.type, ROIS.ctv.color, sourcesA = [ROIS.breast_l_draft], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
          ctv_n = ROI.ROIAlgebra(ROIS.ctv_n.name, ROIS.ctv_n.type, ROIS.ctv_n.color, sourcesA = [ROIS.level_l, ROIS.level1_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ctv_p], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          x_ptv_p = ROI.ROIExpanded(ROIS.x_ptv_p.name, ROIS.x_ptv_p.type, ROIS.x_ptv_p.color, source = ctv_p, margins = MARGINS.breast_ptv_p_l_expansion)
          ptv_pc = ROI.ROIAlgebra(ROIS.ptv_pc.name, ROIS.ptv_pc.type, ROIS.ptv_pc.color, sourcesA = [ctv_p], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.breast_ptv_pc_l_expansion, marginsB = MARGINS.uniform_5mm_contraction)          
          site.add_oars([ROIS.breast_l_draft, ROIS.breast_r_contralat_draft, ROIS.humeral_l, ROIS.breast_r, ROIS.level_l, ROIS.level1_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l])
        if imn == 'not_imn':
          if side == 'right':
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_r], sourcesB = [ROIS.level1_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r],  marginsA = MARGINS.breast_ptv_n_r_expansion, marginsB = MARGINS.breast_ptv_n_r_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          else:
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_l], sourcesB = [ROIS.level1_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l],  marginsA = MARGINS.breast_ptv_n_l_expansion, marginsB = MARGINS.breast_ptv_n_l_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
        elif imn == 'imn':
          if side == 'right':
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_r, ROIS.level1_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.imn],  marginsA = MARGINS.breast_ptv_n_r_expansion, marginsB = MARGINS.uniform_5mm_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_r, ROIS.level2_r, ROIS.level3_r, ROIS.level4_r], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          else:
            x_ptv_n = ROI.ROIAlgebra(ROIS.x_ptv_n.name, ROIS.x_ptv_n.type, ROIS.x_ptv_n.color, sourcesA = [ROIS.level_l, ROIS.level1_l, ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.imn],  marginsA = MARGINS.breast_ptv_n_l_expansion, marginsB = MARGINS.uniform_5mm_expansion)
            #x_ptv_n_ring = ROI.ROIAlgebra(ROIS.x_ptv_n_ring.name, ROIS.x_ptv_n_ring.type, ROIS.x_ptv_n_ring.color, sourcesA = [ROIS.level_l,  ROIS.level2_l, ROIS.level3_l, ROIS.level4_l], sourcesB = [ROIS.body,x_ptv_n], operator = 'Intersection', marginsA = MARGINS.x_ptv_n_ring_expansion, marginsB = MARGINS.zero_contract)
          ctv_n.sourcesA.extend([ROIS.imn])
          ptv_n_imn = ROI.ROIExpanded(ROIS.ptv_n_imn.name, ROIS.ptv_n_imn.type, ROIS.ptv_n_imn.color, source = ROIS.imn, margins = MARGINS.uniform_5mm_expansion)
          site.add_targets([ptv_n_imn])
          site.add_oars([ROIS.imn])
      # Common for left and right:
      ctv = ROI.ROIAlgebra(ROIS.ctv.name, ROIS.ctv.type, ROIS.ctv.color, sourcesA = [ctv_n], sourcesB = [ctv_p], operator = 'Union', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
      ptv_nc = ROI.ROIAlgebra(ROIS.ptv_nc.name, ROIS.ptv_nc.type, ROIS.ptv_nc.color, sourcesA = [x_ptv_n], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_contraction)
      x_ptv = ROI.ROIAlgebra(ROIS.x_ptv.name, ROIS.x_ptv.type, ROIS.x_ptv.color, sourcesA = [x_ptv_n], sourcesB = [x_ptv_p], operator = 'Union', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
      z_match = ROI.ROIAlgebra(ROIS.z_match.name, ROIS.z_match.type, ROIS.z_match.color, sourcesA = [x_ptv_p, x_ptv_n], sourcesB = [ROIS.body], operator = 'Subtraction', marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
      
      # Common for all regional:
      site.add_targets([ctv_p, ctv_n, ctv, x_ptv_p,ptv_pc, x_ptv_n,x_ptv,ptv_nc,z_match])

      # Add volumes for boost (2Gy x 8) if selected:
      if boost == 'with':
        ptv_boost = ROI.ROIAlgebra(ROIS.ptv_boost.name, ROIS.ptv_boost.type, ROIS.ptv_boost.color, sourcesA = [ROIS.ctv_boost], sourcesB = [ptv_pc], operator = 'Intersection', marginsA = MARGINS.uniform_10mm_expansion, marginsB = MARGINS.zero)
        site.add_targets([ROIS.ctv_boost, ptv_boost])
           
    # Create all targets and OARs in RayStation:
    site.create_rois()
