# encoding: utf8

# Import local files:
import colors as COLORS
import def_oars as DEF
import margins as MARGINS
import roi as ROI
import rois as ROIS

# Definitions script for rectum treatments (conventional 50 Gy SIB and hypofractionated 25 Gy).
class DefRectum(object):

  # Adds target and OAR ROIs to the given site and creates them in RayStation.
  def __init__(self, pm, examination, ss, choices, site):
    # Choice 1: Fractionation - normo or hypofractionated?
    ind = choices[2]
    site.add_oars(DEF.rectum_oars)
    # Conventionally fractionated (2 Gy x 25): MÅ FIKSES: rektum adipose
    if ind == 'postop':
      ctv_sb_50 = ROI.ROIExpanded(ROIS.ctv_sb_50.name, ROIS.ctv_sb_50.type, ROIS.ctv_sb_50.color, source = ROIS.gtv_sb, margins = MARGINS.uniform_10mm_expansion)
      ptv_sb_50 = ROI.ROIExpanded(ROIS.ptv_sb_50.name, ROIS.ptv_sb_50.type, ROIS.ptv_sb_50.color, source = ctv_sb_50, margins = MARGINS.rectum_ptv_50_expansion)
      ptv_e_46_5 = ROI.ROIExpanded(ROIS.ptv_e_46_5.name, ROIS.ptv_e_46_5.type, ROIS.ptv_e_46_5.color, source = ROIS.ctv_e_46_5, margins = MARGINS.rectum_ptv_50_expansion)
      site.add_targets([ROIS.gtv_sb, ROIS.ctv_e_46_5, ctv_sb_50, ptv_sb_50, ptv_e_46_5])
      nodes = choices[3]
      if nodes == 'with_node':
        ctv_n_50 = ROI.ROIExpanded(ROIS.ctv_n_50.name, ROIS.ctv_n_50.type, ROIS.ctv_n_50.color, source = ROIS.gtv_n, margins = MARGINS.uniform_5mm_expansion)
        ptv_n_50 = ROI.ROIExpanded(ROIS.ptv_n_50.name, ROIS.ptv_n_50.type, ROIS.ptv_n_50.color, source = ctv_n_50, margins = MARGINS.uniform_8mm_expansion)
        site.add_targets([ROIS.gtv_n, ctv_n_50, ptv_n_50])
      groin = choices[4]
      if groin == 'with':
        ptv_e_ln_r_46 = ROI.ROIAlgebra(ROIS.ptv_e_ln_r_46.name, ROIS.ptv_e_ln_r_46.type, ROIS.ptv_e_ln_r_46.color, source = ROIS.ctv_e_ln_r_46, margins = MARGINS.uniform_8mm_expansion)
        ptv_e_ln_l_46 = ROI.ROIAlgebra(ROIS.ptv_e_ln_l_46.name, ROIS.ptv_e_ln_l_46.type, ROIS.ptv_e_ln_l_46.color, source = ROIS.ctv_e_ln_l_46, margins = MARGINS.uniform_8mm_expansion)
        site.add_targets([ROIS.ctv_e_ln_r_46, ROIS.ctv_e_ln_l_46])
    elif ind == 'preop':
      ctv_p_50 = ROI.ROIExpanded(ROIS.ctv_p_50.name, ROIS.ctv_p_50.type, ROIS.ctv_p_50.color, source = ROIS.gtv_p, margins = MARGINS.uniform_10mm_expansion)
      ptv_p_50 = ROI.ROIExpanded(ROIS.ptv_p_50.name, ROIS.ptv_p_50.type, ROIS.ptv_p_50.color, source = ctv_p_50, margins = MARGINS.rectum_ptv_50_expansion)
      ptv_e_46_5 = ROI.ROIExpanded(ROIS.ptv_e_46_5.name, ROIS.ptv_e_46_5.type, ROIS.ptv_e_46_5.color, source = ROIS.ctv_e_46_5, margins = MARGINS.rectum_ptv_50_expansion)
      site.add_targets([ROIS.gtv_p,ctv_p_50, ptv_p_50])
      frac = choices[3]
      if frac == 'normo':
        # Choice 3: Positive lymph nodes - included or not?
        nodes = choices[4]
        if nodes == 'with_node':
          ctv_n_50 = ROI.ROIExpanded(ROIS.ctv_n_50.name, ROIS.ctv_n_50.type, ROIS.ctv_n_50.color, source = ROIS.gtv_n, margins = MARGINS.uniform_5mm_expansion)
          ptv_n_50 = ROI.ROIExpanded(ROIS.ptv_n_50.name, ROIS.ptv_n_50.type, ROIS.ptv_n_50.color, source = ctv_n_50, margins = MARGINS.uniform_8mm_expansion)
          site.add_targets([ROIS.gtv_n, ctv_n_50, ptv_n_50])
        # Choice 4: Groin target volume - included or not?
        groin = choices[5]
        # Groin targets included:
        if groin == 'with': #gtv_groin?
          ptv_e_ln_r_46 = ROI.ROIExpanded(ROIS.ptv_e_ln_r_46.name, ROIS.ptv_e_ln_r_46.type, ROIS.ptv_e_ln_r_46.color, source = ROIS.ctv_e_ln_r_46, margins = MARGINS.uniform_8mm_expansion)
          ptv_e_ln_l_46 = ROI.ROIExpanded(ROIS.ptv_e_ln_l_46.name, ROIS.ptv_e_ln_l_46.type, ROIS.ptv_e_ln_l_46.color, source = ROIS.ctv_e_ln_l_46, margins = MARGINS.uniform_8mm_expansion)
          site.add_targets([ROIS.ctv_e_ln_r_46, ROIS.ctv_e_ln_l_46])
        site.add_targets([ROIS.ctv_e_46_5, ptv_e_46_5])
      # Hypofractionated treatment (5 Gy x 5): med dose i navnet???
      else:
        ctv_p = ROI.ROIExpanded(ROIS.ctv_p.name, ROIS.ctv_p.type, COLORS.ctv_high, source = ROIS.gtv_p, margins = MARGINS.uniform_10mm_expansion )
        ptv_p = ROI.ROIExpanded(ROIS.ptv_p.name, ROIS.ptv_p.type, ROIS.ptv_p.color, source = ctv_p, margins = MARGINS.rectum_ptv_50_expansion)
        site.add_targets([ROIS.gtv_p, ctv_p, ptv_p])
    # Create all targets and OARs in RayStation:
    site.create_rois()
