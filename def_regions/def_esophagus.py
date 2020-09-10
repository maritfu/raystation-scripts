# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for rectum treatments (conventional 50 Gy SIB and hypofractionated 25 Gy).
class DefEsophagus(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Fractionation - normo or hypofractionated?
    intent = choices[2]
    
    site.add_oars(DEF.esophagus_oars)
    if intent == 'neo':
      ctv_p_41_4 = ROI.ROIExpanded(ROIS.ctv_p_41_4.name, ROIS.ctv_p_41_4.type, ROIS.ctv_p_41_4.color, source = ROIS.gtv_p_41_4, margins = MARGINS.esophagus_ctv_p_expansion)
      ctv_n_41_4 = ROI.ROIExpanded(ROIS.ctv_n_41_4.name, ROIS.ctv_n_41_4.type, ROIS.ctv_n_41_4.color, source = ROIS.gtv_n_41_4, margins = MARGINS.uniform_7mm_expansion)
      ptv_p_41_4 = ROI.ROIExpanded(ROIS.ptv_p_41_4.name, ROIS.ptv_p_41_4.type, ROIS.ptv_p_41_4.color, source = ctv_p_41_4, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
      ptv_n_41_4 = ROI.ROIExpanded(ROIS.ptv_n_41_4.name, ROIS.ptv_n_41_4.type, ROIS.ptv_n_41_4.color, source = ctv_n_41_4, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
      ptv_e_41_4 = ROI.ROIExpanded(ROIS.ptv_e_41_4.name, ROIS.ptv_e_41_4.type, ROIS.ptv_e_41_4.color, source = ROIS.ctv_e_41_4, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
      ptv_41_4 = ROI.ROIAlgebra(ROIS.ptv_41_4.name, ROIS.ptv_41_4.type, COLORS.ptv_high, sourcesA = [ptv_p_41_4], sourcesB = [ptv_n_41_4,ptv_e_41_4], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
      x_ctv_e = ROI.ROIExpanded(ROIS.x_ctv_e.name, ROIS.x_ctv_e.type, ROIS.x_ctv_e.color, source = ROIS.gtv_p_41_4, margins = MARGINS.esophagus_ctv_p_expansion)
      x_gtv_p = ROI.ROIExpanded(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, source = ROIS.gtv_p_41_4, margins = MARGINS.uniform_20mm_expansion)
      site.add_targets([ROIS.gtv_p_41_4,ROIS.gtv_n_41_4, ROIS.ctv_e_41_4,ctv_p_41_4,ctv_n_41_4,ptv_p_41_4, ptv_n_41_4,  ptv_e_41_4,ptv_41_4,x_ctv_e, x_gtv_p])
    elif intent == 'radical':
      frak = choices[3]
      if frak == '50':
        ctv_p_50 = ROI.ROIExpanded(ROIS.ctv_p_50.name, ROIS.ctv_p_50.type, ROIS.ctv_p_50.color, source = ROIS.gtv_p_50, margins = MARGINS.esophagus_ctv_p_expansion)
        ctv_n_50 = ROI.ROIExpanded(ROIS.ctv_n_50.name, ROIS.ctv_n_50.type, ROIS.ctv_n_50.color, source = ROIS.gtv_n_50, margins = MARGINS.uniform_7mm_expansion)
        ptv_p_50 = ROI.ROIExpanded(ROIS.ptv_p_50.name, ROIS.ptv_p_50.type, ROIS.ptv_p_50.color, source = ctv_p_50, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_n_50 = ROI.ROIExpanded(ROIS.ptv_n_50.name, ROIS.ptv_n_50.type, ROIS.ptv_n_50.color, source = ctv_n_50, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_e_46 = ROI.ROIExpanded(ROIS.ptv_e_46.name, ROIS.ptv_e_46.type, ROIS.ptv_e_46.color, source = ROIS.ctv_e_46, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_50 = ROI.ROIAlgebra(ROIS.ptv_50.name, ROIS.ptv_50.type, COLORS.ptv_high, sourcesA = [ptv_p_50], sourcesB = [ptv_n_50], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ctv_e = ROI.ROIExpanded(ROIS.x_ctv_e.name, ROIS.x_ctv_e.type, ROIS.x_ctv_e.color, source = ROIS.gtv_p_50, margins = MARGINS.esophagus_ctv_p_expansion)
        x_gtv_p = ROI.ROIExpanded(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, source = ROIS.gtv_p_50, margins = MARGINS.uniform_20mm_expansion)
        x_ctv_46 = ROI.ROIAlgebra(ROIS.x_ctv_46.name, ROIS.x_ctv_46.type, ROIS.x_ctv_46.color, sourcesA = [ROIS.ctv_e_46], sourcesB = [ptv_50],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        x_ptv_46 = ROI.ROIAlgebra(ROIS.x_ptv_46.name, ROIS.x_ptv_46.type, ROIS.x_ptv_46.color, sourcesA = [ptv_e_46], sourcesB = [ptv_50],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)

        site.add_targets([ROIS.gtv_p_50,ROIS.gtv_n_50, ROIS.ctv_e_46,ctv_p_50,ctv_n_50,ptv_p_50, ptv_n_50,ptv_e_46,ptv_50,x_ctv_e, x_gtv_p,x_ctv_46,x_ptv_46])
      elif frak == '60':
        ctv_p_60 = ROI.ROIExpanded(ROIS.ctv_p_60.name, ROIS.ctv_p_60.type, ROIS.ctv_p_60.color, source = ROIS.gtv_p_60, margins = MARGINS.esophagus_ctv_p_expansion)
        ctv_n_60 = ROI.ROIExpanded(ROIS.ctv_n_60.name, ROIS.ctv_n_60.type, ROIS.ctv_n_60.color, source = ROIS.gtv_n_60, margins = MARGINS.uniform_7mm_expansion)
        ptv_p_60 = ROI.ROIExpanded(ROIS.ptv_p_60.name, ROIS.ptv_p_60.type, ROIS.ptv_p_60.color, source = ctv_p_60, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_n_60 = ROI.ROIExpanded(ROIS.ptv_n_60.name, ROIS.ptv_n_60.type, ROIS.ptv_n_60.color, source = ctv_n_60, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_e_46 = ROI.ROIExpanded(ROIS.ptv_e_46.name, ROIS.ptv_e_46.type, ROIS.ptv_e_46.color, source = ROIS.ctv_e_46, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_60 = ROI.ROIAlgebra(ROIS.ptv_60.name, ROIS.ptv_60.type, COLORS.ptv_high, sourcesA = [ptv_p_60], sourcesB = [ptv_n_60], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ctv_e = ROI.ROIExpanded(ROIS.x_ctv_e.name, ROIS.x_ctv_e.type, ROIS.x_ctv_e.color, source = ROIS.gtv_p_60, margins = MARGINS.esophagus_ctv_p_expansion)
        x_gtv_p = ROI.ROIExpanded(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, source = ROIS.gtv_p_60, margins = MARGINS.uniform_20mm_expansion)
        x_ctv_46 = ROI.ROIAlgebra(ROIS.x_ctv_46.name, ROIS.x_ctv_46.type, ROIS.x_ctv_46.color, sourcesA = [ROIS.ctv_e_46], sourcesB = [ptv_60],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        x_ptv_46 = ROI.ROIAlgebra(ROIS.x_ptv_46.name, ROIS.x_ptv_46.type, ROIS.x_ptv_46.color, sourcesA = [ptv_e_46], sourcesB = [ptv_60],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        site.add_targets([ROIS.gtv_p_60,ROIS.gtv_n_60, ROIS.ctv_e_46,ctv_p_60,ctv_n_60,ptv_p_60, ptv_n_60,  ptv_e_46,ptv_60,x_ctv_e, x_gtv_p,x_ctv_46,x_ptv_46])
      elif frak == '66':
        ctv_p_66 = ROI.ROIExpanded(ROIS.ctv_p_66.name, ROIS.ctv_p_66.type, ROIS.ctv_p_66.color, source = ROIS.gtv_p_66, margins = MARGINS.esophagus_ctv_p_expansion)
        ctv_n_66 = ROI.ROIExpanded(ROIS.ctv_n_66.name, ROIS.ctv_n_66.type, ROIS.ctv_n_66.color, source = ROIS.gtv_n_66, margins = MARGINS.uniform_7mm_expansion)
        ptv_p_66 = ROI.ROIExpanded(ROIS.ptv_p_66.name, ROIS.ptv_p_66.type, ROIS.ptv_p_66.color, source = ctv_p_66, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_n_66 = ROI.ROIExpanded(ROIS.ptv_n_66.name, ROIS.ptv_n_66.type, ROIS.ptv_n_66.color, source = ctv_n_66, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_e_46 = ROI.ROIExpanded(ROIS.ptv_e_46.name, ROIS.ptv_e_46.type, ROIS.ptv_e_46.color, source = ROIS.ctv_e_46, margins = MARGINS.esophagus_ptv_6d_expansion) #MARGINER?
        ptv_66 = ROI.ROIAlgebra(ROIS.ptv_66.name, ROIS.ptv_66.type, COLORS.ptv_high, sourcesA = [ptv_p_66], sourcesB = [ptv_n_66], marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        x_ctv_e = ROI.ROIExpanded(ROIS.x_ctv_e.name, ROIS.x_ctv_e.type, ROIS.x_ctv_e.color, source = ROIS.gtv_p_66, margins = MARGINS.esophagus_ctv_p_expansion)
        x_gtv_p = ROI.ROIExpanded(ROIS.x_gtv_p.name, ROIS.x_gtv_p.type, ROIS.x_gtv_p.color, source = ROIS.gtv_p_66, margins = MARGINS.uniform_20mm_expansion)
        x_ctv_46 = ROI.ROIAlgebra(ROIS.x_ctv_46.name, ROIS.x_ctv_46.type, ROIS.x_ctv_46.color, sourcesA = [ROIS.ctv_e_46], sourcesB = [ptv_66],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        x_ptv_46 = ROI.ROIAlgebra(ROIS.x_ptv_46.name, ROIS.x_ptv_46.type, ROIS.x_ptv_46.color, sourcesA = [ptv_e_46], sourcesB = [ptv_66],operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.uniform_5mm_expansion)
        site.add_targets([ROIS.gtv_p_66,ROIS.gtv_n_66, ROIS.ctv_e_46,ctv_p_66,ctv_n_66,ptv_p_66, ptv_n_66,  ptv_e_46,ptv_66,x_ctv_e, x_gtv_p,x_ctv_46,x_ptv_46])
    # Create all targets and OARs in RayStation:
    site.create_rois()
