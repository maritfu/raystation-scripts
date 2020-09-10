# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for lung treatments (palliative, curative and stereotactiv).
class DefLung(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    
    # Choice 1: Intent (curative or palliative)
    intent = choices[1]
    # Curative:
    if intent == 'curative':
      # Choice 2: Diagnosis
      diagnosis = choices[2]
      # Non small cell lung cancer (with 4DCT) or small cell lung cancer (with 4DCT):
      if diagnosis == 'narlal':
        site.add_oars(DEF.lung_narlal_oars)
        nr_nodes = choices[3]
        igtv_p = ROI.ROIExpanded(ROIS.igtv_p.name, ROIS.igtv_p.type, ROIS.igtv_p.color, source = ROIS.gtv_p, margins = MARGINS.zero)
        ictv_p = ROI.ROIExpanded(ROIS.ictv_p.name, ROIS.ictv_p.type, COLORS.ctv_high, source = igtv_p, margins = MARGINS.uniform_5mm_expansion)
        if nr_nodes == 'one':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n = ROI.ROIExpanded(ROIS.igtv_n.name, ROIS.igtv_n.type, ROIS.igtv_n.color, source = ROIS.gtv_n, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n = ROI.ROIExpanded(ROIS.ictv_n.name, ROIS.ictv_n.type, COLORS.ctv_high, source = igtv_n, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIExpanded(ROIS.ptv_n.name, ROIS.ptv_n.type, ROIS.ptv_n.color, source = ictv_n, margins = MARGINS.uniform_5mm_expansion)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n,ROIS.gtv_p_pt, ROIS.gtv_n_pt, igtv_p,igtv_n,ictv_p,ictv_n])
        elif nr_nodes == 'two':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n1, ROIS.gtv_n2], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n1_pt,ROIS.gtv_n2_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n1 = ROI.ROIExpanded(ROIS.igtv_n1.name, ROIS.igtv_n1.type, ROIS.igtv_n1.color, source = ROIS.gtv_n1, margins = MARGINS.zero)
          igtv_n2 = ROI.ROIExpanded(ROIS.igtv_n2.name, ROIS.igtv_n2.type, ROIS.igtv_n2.color, source = ROIS.gtv_n2, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n1, igtv_n2], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1 = ROI.ROIExpanded(ROIS.ptv_n1.name, ROIS.ptv_n1.type, ROIS.ptv_n1.color, source = ictv_n1, margins = MARGINS.uniform_6mm_expansion)
          ptv_n2 = ROI.ROIExpanded(ROIS.ptv_n2.name, ROIS.ptv_n2.type, ROIS.ptv_n2.color, source = ictv_n2, margins = MARGINS.uniform_6mm_expansion)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ptv_n1], sourcesB = [ptv_n2], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_p_pt, ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,igtv_p,igtv_n1,igtv_n2,ictv_p,ictv_n1,ictv_n2,ptv_n1,ptv_n2])
        elif nr_nodes == 'three':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n1 = ROI.ROIExpanded(ROIS.igtv_n1.name, ROIS.igtv_n1.type, ROIS.igtv_n1.color, source = ROIS.gtv_n1, margins = MARGINS.zero)
          igtv_n2 = ROI.ROIExpanded(ROIS.igtv_n2.name, ROIS.igtv_n2.type, ROIS.igtv_n2.color, source = ROIS.gtv_n2, margins = MARGINS.zero)
          igtv_n3 = ROI.ROIExpanded(ROIS.igtv_n3.name, ROIS.igtv_n3.type, ROIS.igtv_n3.color, source = ROIS.gtv_n3, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n1, igtv_n2,igtv_n3], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1 = ROI.ROIExpanded(ROIS.ptv_n1.name, ROIS.ptv_n1.type, ROIS.ptv_n1.color, source = ictv_n1, margins = MARGINS.uniform_6mm_expansion)
          ptv_n2 = ROI.ROIExpanded(ROIS.ptv_n2.name, ROIS.ptv_n2.type, ROIS.ptv_n2.color, source = ictv_n2, margins = MARGINS.uniform_6mm_expansion)
          ptv_n3 = ROI.ROIExpanded(ROIS.ptv_n3.name, ROIS.ptv_n3.type, ROIS.ptv_n3.color, source = ictv_n3, margins = MARGINS.uniform_6mm_expansion)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ptv_n1], sourcesB = [ptv_n2,ptv_n3], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_p_pt, ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt,igtv_p,igtv_n1,igtv_n2,igtv_n3,ictv_p,ictv_n1,ictv_n2,ictv_n3,
                            ptv_n1,ptv_n2,ptv_n3,ptv_n])
        elif nr_nodes == 'four':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt,ROIS.gtv_n4_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n1 = ROI.ROIExpanded(ROIS.igtv_n1.name, ROIS.igtv_n1.type, ROIS.igtv_n1.color, source = ROIS.gtv_n1, margins = MARGINS.zero)
          igtv_n2 = ROI.ROIExpanded(ROIS.igtv_n2.name, ROIS.igtv_n2.type, ROIS.igtv_n2.color, source = ROIS.gtv_n2, margins = MARGINS.zero)
          igtv_n3 = ROI.ROIExpanded(ROIS.igtv_n3.name, ROIS.igtv_n3.type, ROIS.igtv_n3.color, source = ROIS.gtv_n3, margins = MARGINS.zero)
          igtv_n4 = ROI.ROIExpanded(ROIS.igtv_n4.name, ROIS.igtv_n4.type, ROIS.igtv_n4.color, source = ROIS.gtv_n4, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n1, igtv_n2,igtv_n3,igtv_n4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1 = ROI.ROIExpanded(ROIS.ptv_n1.name, ROIS.ptv_n1.type, ROIS.ptv_n1.color, source = ictv_n1, margins = MARGINS.uniform_6mm_expansion)
          ptv_n2 = ROI.ROIExpanded(ROIS.ptv_n2.name, ROIS.ptv_n2.type, ROIS.ptv_n2.color, source = ictv_n2, margins = MARGINS.uniform_6mm_expansion)
          ptv_n3 = ROI.ROIExpanded(ROIS.ptv_n3.name, ROIS.ptv_n3.type, ROIS.ptv_n3.color, source = ictv_n3, margins = MARGINS.uniform_6mm_expansion)
          ptv_n4 = ROI.ROIExpanded(ROIS.ptv_n4.name, ROIS.ptv_n4.type, ROIS.ptv_n.color, source = ictv_n4, margins = MARGINS.uniform_6mm_expansion)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ptv_n1], sourcesB = [ptv_n2,ptv_n3,ptv_n4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4,ROIS.gtv_p_pt, ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt, ROIS.gtv_n4_pt,igtv_p,igtv_n1,igtv_n2,igtv_n3,
                            igtv_n4,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ptv_n1,ptv_n2,ptv_n3,ptv_n4,ptv_n])
        elif nr_nodes == 'five':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4,ROIS.gtv_n5], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt,ROIS.gtv_n4_pt,ROIS.gtv_n5_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n1 = ROI.ROIExpanded(ROIS.igtv_n1.name, ROIS.igtv_n1.type, ROIS.igtv_n1.color, source = ROIS.gtv_n1, margins = MARGINS.zero)
          igtv_n2 = ROI.ROIExpanded(ROIS.igtv_n2.name, ROIS.igtv_n2.type, ROIS.igtv_n2.color, source = ROIS.gtv_n2, margins = MARGINS.zero)
          igtv_n3 = ROI.ROIExpanded(ROIS.igtv_n3.name, ROIS.igtv_n3.type, ROIS.igtv_n3.color, source = ROIS.gtv_n3, margins = MARGINS.zero)
          igtv_n4 = ROI.ROIExpanded(ROIS.igtv_n4.name, ROIS.igtv_n4.type, ROIS.igtv_n4.color, source = ROIS.gtv_n4, margins = MARGINS.zero)
          igtv_n5 = ROI.ROIExpanded(ROIS.igtv_n5.name, ROIS.igtv_n5.type, ROIS.igtv_n5.color, source = ROIS.gtv_n5, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n1, igtv_n2,igtv_n3,igtv_n4,igtv_n5], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv_n5 = ROI.ROIExpanded(ROIS.ictv_n5.name, ROIS.ictv_n5.type, COLORS.ctv_high, source = igtv_n5, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n1 = ROI.ROIExpanded(ROIS.ptv_n1.name, ROIS.ptv_n1.type, ROIS.ptv_n1.color, source = ictv_n1, margins = MARGINS.uniform_6mm_expansion)
          ptv_n2 = ROI.ROIExpanded(ROIS.ptv_n2.name, ROIS.ptv_n2.type, ROIS.ptv_n2.color, source = ictv_n2, margins = MARGINS.uniform_6mm_expansion)
          ptv_n3 = ROI.ROIExpanded(ROIS.ptv_n3.name, ROIS.ptv_n3.type, ROIS.ptv_n3.color, source = ictv_n3, margins = MARGINS.uniform_6mm_expansion)
          ptv_n4 = ROI.ROIExpanded(ROIS.ptv_n4.name, ROIS.ptv_n4.type, ROIS.ptv_n4.color, source = ictv_n4, margins = MARGINS.uniform_6mm_expansion)
          ptv_n5 = ROI.ROIExpanded(ROIS.ptv_n5.name,ROIS.ptv_n5.type, ROIS.ptv_n5.color, source = ictv_n5, margins = MARGINS.uniform_6mm_expansion)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ptv_n1], sourcesB = [ptv_n2,ptv_n3,ptv_n4,ptv_n5], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4,ROIS.gtv_n5,ROIS.gtv_p_pt, ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt, ROIS.gtv_n4_pt,ROIS.gtv_n5_pt,
                            igtv_p,igtv_n1,igtv_n2,igtv_n3,igtv_n4,igtv_n5,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ptv_n1,ptv_n2,ptv_n3,ptv_n4,ptv_n5,ptv_n])
        elif nr_nodes == 'six':
          gtv = ROI.ROIAlgebra(ROIS.gtv.name, ROIS.gtv.type, COLORS.gtv_high, sourcesA=[ROIS.gtv_p], sourcesB = [ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4,ROIS.gtv_n5,ROIS.gtv_n6], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          gtv_pt = ROI.ROIAlgebra(ROIS.gtv_pt.name, ROIS.gtv_pt.type, ROIS.gtv_pt.color, sourcesA=[ROIS.gtv_p_pt], sourcesB = [ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt,ROIS.gtv_n4_pt,ROIS.gtv_n5_pt,ROIS.gtv_n6_pt], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          igtv_n1 = ROI.ROIExpanded(ROIS.igtv_n1.name, ROIS.igtv_n1.type, ROIS.igtv_n1.color, source = ROIS.gtv_n1, margins = MARGINS.zero)
          igtv_n2 = ROI.ROIExpanded(ROIS.igtv_n2.name, ROIS.igtv_n2.type, ROIS.igtv_n2.color, source = ROIS.gtv_n2, margins = MARGINS.zero)
          igtv_n3 = ROI.ROIExpanded(ROIS.igtv_n3.name, ROIS.igtv_n3.type, ROIS.igtv_n3.color, source = ROIS.gtv_n3, margins = MARGINS.zero)
          igtv_n4 = ROI.ROIExpanded(ROIS.igtv_n4.name, ROIS.igtv_n4.type, ROIS.igtv_n4.color, source = ROIS.gtv_n4, margins = MARGINS.zero)
          igtv_n5 = ROI.ROIExpanded(ROIS.igtv_n5.name, ROIS.igtv_n5.type, ROIS.igtv_n5.color, source = ROIS.gtv_n5, margins = MARGINS.zero)
          igtv_n6 = ROI.ROIExpanded(ROIS.igtv_n6.name, ROIS.igtv_n6.type, ROIS.igtv_n6.color, source = ROIS.gtv_n6, margins = MARGINS.zero)
          igtv = ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.igtv.color, sourcesA=[igtv_p], sourcesB = [igtv_n1, igtv_n2,igtv_n3,igtv_n4,igtv_n5,igtv_n6], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv_n5 = ROI.ROIExpanded(ROIS.ictv_n5.name, ROIS.ictv_n5.type, COLORS.ctv_high, source = igtv_n5, margins = MARGINS.uniform_5mm_expansion)
          ictv_n6 = ROI.ROIExpanded(ROIS.ictv_n6.name, ROIS.ictv_n6.type, COLORS.ctv_high, source = igtv_n6, margins = MARGINS.uniform_5mm_expansion)
          ptv_n1 = ROI.ROIExpanded(ROIS.ptv_n1.name, ROIS.ptv_n1.type, ROIS.ptv_n1.color, source = ictv_n1, margins = MARGINS.uniform_6mm_expansion)
          ptv_n2 = ROI.ROIExpanded(ROIS.ptv_n2.name, ROIS.ptv_n2.type, ROIS.ptv_n2.color, source = ictv_n2, margins = MARGINS.uniform_6mm_expansion)
          ptv_n3 = ROI.ROIExpanded(ROIS.ptv_n3.name, ROIS.ptv_n3.type, ROIS.ptv_n3.color, source = ictv_n3, margins = MARGINS.uniform_6mm_expansion)
          ptv_n4 = ROI.ROIExpanded(ROIS.ptv_n4.name, ROIS.ptv_n4.type, ROIS.ptv_n4.color, source = ictv_n4, margins = MARGINS.uniform_6mm_expansion)
          ptv_n5 = ROI.ROIExpanded(ROIS.ptv_n5.name,ROIS.ptv_n5.type, ROIS.ptv_n5.color, source = ictv_n5, margins = MARGINS.uniform_6mm_expansion)
          ptv_n6 = ROI.ROIExpanded(ROIS.ptv_n6.name,ROIS.ptv_n6.type, ROIS.ptv_n6.color, source = ictv_n6, margins = MARGINS.uniform_6mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ptv_n1], sourcesB = [ptv_n2,ptv_n3,ptv_n4,ptv_n5,ptv_n6], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          site.add_targets([ROIS.gtv_p, ROIS.gtv_n1, ROIS.gtv_n2,ROIS.gtv_n3,ROIS.gtv_n4,ROIS.gtv_n5,ROIS.gtv_n6,ROIS.gtv_p_pt, ROIS.gtv_n1_pt,ROIS.gtv_n2_pt,ROIS.gtv_n3_pt, ROIS.gtv_n4_pt,ROIS.gtv_n5_pt,ROIS.gtv_n6_pt,
                            igtv_p,igtv_n1,igtv_n2,igtv_n3,igtv_n4,igtv_n5,igtv_n6,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6,ptv_n1,ptv_n2,ptv_n3,ptv_n4,ptv_n5,ptv_n6,ptv_n])
        lungs_igtv = ROI.ROIAlgebra(ROIS.lungs_igtv.name, ROIS.lungs_igtv.type, COLORS.lungs, sourcesA = [ROIS.lungs], sourcesB = [igtv], operator='Subtraction')
        ptv_p = ROI.ROIExpanded(ROIS.ptv_p.name, ROIS.ptv_p.type, COLORS.ptv, source = ictv_p, margins = MARGINS.uniform_6mm_expansion)
        ptv = ROI.ROIAlgebra(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv, sourcesA = [ptv_p], sourcesB = [ptv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ptv_lunge = ROI.ROIAlgebra(ROIS.x_ptv_lunge.name, ROIS.x_ptv_lunge.type, ROIS.x_ptv_lunge.color, sourcesA = [ptv], sourcesB = [lungs_igtv], operator = 'Intersection',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ptv_vev = ROI.ROIAlgebra(ROIS.x_ptv_vev.name, ROIS.x_ptv_vev.type, ROIS.x_ptv_vev.color, sourcesA = [ptv], sourcesB = [x_ptv_lunge], operator = 'Subtraction',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        site.add_targets([ptv_p,ptv_n,x_ptv_lunge,x_ptv_vev,igtv,gtv, gtv_pt,ictv,ptv])
        site.add_oars([lungs_igtv])

      elif diagnosis == '4dct':
        site.add_oars(DEF.lung_oars)
        nr_nodes = choices[4]
        lungs_igtv = ROI.ROIAlgebra(ROIS.lungs_igtv.name, ROIS.lungs_igtv.type, COLORS.lungs, sourcesA = [ROIS.lungs], sourcesB = [ROIS.igtv_p], operator='Subtraction')
        ictv_margin = choices[3]
        if ictv_margin == '5':
          ictv_p = ROI.ROIExpanded(ROIS.ictv_p.name, ROIS.ictv_p.type, COLORS.ctv_high, source = ROIS.igtv_p, margins = MARGINS.uniform_5mm_expansion)
        elif ictv_margin == '7':
          ictv_p = ROI.ROIExpanded(ROIS.ictv_p.name, ROIS.ictv_p.type, COLORS.ctv_high, source = ROIS.igtv_p, margins = MARGINS.uniform_7mm_expansion)
        if nr_nodes == 'one':
          ictv_n = ROI.ROIExpanded(ROIS.ictv_n.name, ROIS.ictv_n.type, COLORS.ctv_high, source = ROIS.igtv_n, margins = MARGINS.uniform_5mm_expansion)
          ptv_n = ROI.ROIExpanded(ROIS.ptv_n.name, ROIS.ptv_n.type, ROIS.ptv_n.color, source = ictv_n, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ictv.color, sourcesA=[ictv_p], sourcesB = [ictv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv.sourcesA.extend([ictv_n])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n])
          site.add_targets([ROIS.igtv_p, ROIS.igtv_n, ictv_p,ictv_n,ictv]) 
        elif nr_nodes == 'two':
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = ROIS.igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = ROIS.igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ictv_n1], sourcesB = [ictv_n2], marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_6mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ctv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ictv.sourcesA.extend([ictv_n1,ictv_n2])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n1,ROIS.igtv_n2])
          site.add_targets([ROIS.igtv_p,ROIS.igtv_n1,ROIS.igtv_n2,ictv_p, ictv_n1,ictv_n2,ictv])
        elif nr_nodes == 'three':
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = ROIS.igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = ROIS.igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = ROIS.igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ctv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ictv_n1], sourcesB = [ictv_n2,ictv_n3], marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_6mm_expansion)
          ictv.sourcesA.extend([ictv_n1,ictv_n2,ictv_n3])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3])
          site.add_targets([ROIS.igtv_p,ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3,ictv_p, ictv_n1,ictv_n2,ictv_n3,ictv])
        elif nr_nodes == 'four':
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = ROIS.igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = ROIS.igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = ROIS.igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = ROIS.igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ctv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ictv_n1], sourcesB = [ictv_n2,ictv_n3,ictv_n4], marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_6mm_expansion)
          ictv.sourcesA.extend([ictv_n1,ictv_n2,ictv_n3,ictv_n4])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3,ROIS.igtv_n4])
          site.add_targets([ROIS.igtv_p,ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3, ROIS.igtv_n4,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv])
        elif nr_nodes == 'five':
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = ROIS.igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = ROIS.igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = ROIS.igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = ROIS.igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv_n5 = ROI.ROIExpanded(ROIS.ictv_n5.name, ROIS.ictv_n5.type, COLORS.ctv_high, source = ROIS.igtv_n5, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ctv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ictv_n1], sourcesB = [ictv_n2,ictv_n3,ictv_n4,ictv_n5], marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_6mm_expansion)
          ictv.sourcesA.extend([ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3,ROIS.igtv_n4,ROIS.igtv_n5])
          site.add_targets([ROIS.igtv_p,ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3, ROIS.igtv_n4,ROIS.igtv_n5,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv])
        elif nr_nodes == 'six':
          ictv_n1 = ROI.ROIExpanded(ROIS.ictv_n1.name, ROIS.ictv_n1.type, COLORS.ctv_high, source = ROIS.igtv_n1, margins = MARGINS.uniform_5mm_expansion)
          ictv_n2 = ROI.ROIExpanded(ROIS.ictv_n2.name, ROIS.ictv_n2.type, COLORS.ctv_high, source = ROIS.igtv_n2, margins = MARGINS.uniform_5mm_expansion)
          ictv_n3 = ROI.ROIExpanded(ROIS.ictv_n3.name, ROIS.ictv_n3.type, COLORS.ctv_high, source = ROIS.igtv_n3, margins = MARGINS.uniform_5mm_expansion)
          ictv_n4 = ROI.ROIExpanded(ROIS.ictv_n4.name, ROIS.ictv_n4.type, COLORS.ctv_high, source = ROIS.igtv_n4, margins = MARGINS.uniform_5mm_expansion)
          ictv_n5 = ROI.ROIExpanded(ROIS.ictv_n5.name, ROIS.ictv_n5.type, COLORS.ctv_high, source = ROIS.igtv_n5, margins = MARGINS.uniform_5mm_expansion)
          ictv_n6 = ROI.ROIExpanded(ROIS.ictv_n6.name, ROIS.ictv_n6.type, COLORS.ctv_high, source = ROIS.igtv_n6, margins = MARGINS.uniform_5mm_expansion)
          ictv =  ROI.ROIAlgebra(ROIS.ictv.name, ROIS.ictv.type, ROIS.ctv.color, sourcesA=[ictv_p], sourcesB = [ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          ptv_n = ROI.ROIAlgebra(ROIS.ptv_n.name, ROIS.ptv_n.type, COLORS.ptv, sourcesA = [ictv_n1], sourcesB = [ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6], marginsA = MARGINS.uniform_6mm_expansion, marginsB = MARGINS.uniform_6mm_expansion)
          ictv.sourcesA.extend([ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6])
          lungs_igtv.sourcesB.extend([ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3,ROIS.igtv_n4,ROIS.igtv_n5,ROIS.igtv_n6])
          site.add_targets([ROIS.igtv_p,ROIS.igtv_n1,ROIS.igtv_n2,ROIS.igtv_n3, ROIS.igtv_n4,ROIS.igtv_n5,ROIS.igtv_n6,ictv_p,ictv_n1,ictv_n2,ictv_n3,ictv_n4,ictv_n5,ictv_n6,ictv])
        ptv_p = ROI.ROIExpanded(ROIS.ptv_p.name, ROIS.ptv_p.type, COLORS.ptv, source = ictv_p, margins = MARGINS.uniform_6mm_expansion)
        ptv = ROI.ROIAlgebra(ROIS.ptv.name, ROIS.ptv.type, COLORS.ptv, sourcesA = [ptv_p], sourcesB = [ptv_n], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ptv_lunge = ROI.ROIAlgebra(ROIS.x_ptv_lunge.name, ROIS.x_ptv_lunge.type, ROIS.x_ptv_lunge.color, sourcesA = [ptv], sourcesB = [lungs_igtv], operator = 'Intersection',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ptv_vev = ROI.ROIAlgebra(ROIS.x_ptv_vev.name, ROIS.x_ptv_vev.type, ROIS.x_ptv_vev.color, sourcesA = [ptv], sourcesB = [x_ptv_lunge], operator = 'Subtraction',marginsA = MARGINS.zero, marginsB = MARGINS.zero)

        site.add_targets([ptv_p,ptv_n,ptv,x_ptv_lunge,x_ptv_vev])
        site.add_oars([lungs_igtv])


    # Stereotactic treatment:
    elif intent == 'stereotactic':
      # Choice 2: Side - left or right?
      side = choices[2]
      if side == 'right':
        site.add_oars([ROIS.rib_x_r, ROIS.rib_y_r, ROIS.ribs_r])
      elif side == 'left':
        site.add_oars([ROIS.rib_x_l, ROIS.rib_y_l, ROIS.ribs_l])
      nr_targets = choices[3]
      # Choice 3: Number of target volumes?
      if nr_targets == 'one':
        site.add_targets([ROIS.igtv, ROIS.ictv, ROIS.iptv, ROIS.wall_ptv])
        site.add_oars([ROIS.lungs_igtv])
      elif nr_targets in ['two', 'three']:
        igtv =  ROI.ROIAlgebra(ROIS.igtv.name, ROIS.igtv.type, ROIS.gtv.color, sourcesA=[ROIS.igtv1], sourcesB=[ROIS.igtv2])
        site.add_targets([ROIS.igtv1, ROIS.igtv2, igtv, ROIS.ictv1, ROIS.ictv2, ROIS.iptv1, ROIS.iptv2, ROIS.wall_ptv1, ROIS.wall_ptv2])
        if nr_targets == 'three':
          igtv.sourcesB.extend([ROIS.igtv3])
          site.add_targets([ROIS.igtv3, ROIS.ictv3, ROIS.iptv3, ROIS.wall_ptv3])
        lungs_igtv = ROI.ROIAlgebra(ROIS.lungs_igtv.name, 'Organ', COLORS.lungs, sourcesA=[ROIS.lungs], sourcesB=[igtv], operator = 'Subtraction')
        site.add_oars([lungs_igtv])
      site.add_oars(DEF.lung_stereotactic_oars)

    # Create all targets and OARs in RayStation:
    site.create_rois()
