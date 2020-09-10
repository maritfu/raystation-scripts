# encoding: utf8

# Creates an Anal Canal ROI from a Rectum ROI by copying the caudal 4 cm of Rectum ROI.
#
# Authors:
# Marit Funderud
# Helse Møre og Romsdal HF
#
# Made for RayStation version: 9.A
# Python 3.6

# Import system libraries:
from connect import *
import clr, sys, os
import math

# Add necessary folders to the system path:
sys.path.append("C:\\temp\\raystation-scripts\\def_regions")
sys.path.append("C:\\temp\\raystation-scripts\\functions")
sys.path.append("C:\\temp\\raystation-scripts\\gui_classes")
sys.path.append("C:\\temp\\raystation-scripts\\quality_control")
sys.path.append("C:\\temp\\raystation-scripts\\rt_classes")
sys.path.append("C:\\temp\\raystation-scripts\\settings")

# Import local files:
import patient_model_functions as PMF
import structure_set_functions as SSF
import roi as ROI
import rois as ROIS

# Load case data:
try:
    case = get_current("Case")
except SystemError:
    raise IOError("No case loaded.")

# Load patient model, examination and structure set:
pm = case.PatientModel
examination = get_current("Examination")
ss = PMF.get_structure_set(pm, examination)

# Create the posterior half ROI:
if SSF.has_roi_with_shape(ss, 'GTV-T'):
  pm.RegionsOfInterest['GTV-T'].Name = ROIS.gtv_p.name
if SSF.has_roi_with_shape(ss, 'GTV-N1_55'):
  pm.RegionsOfInterest['GTV-N1_55'].Name = ROIS.gtv_n1_55.name
if SSF.has_roi_with_shape(ss, 'GTV-N2_55'):
  pm.RegionsOfInterest['GTV-N2_55'].Name = ROIS.gtv_n2_55.name
if SSF.has_roi_with_shape(ss, 'CTV-T_45'):
  pm.RegionsOfInterest['CTV-T_45'].Name = ROIS.ctv_p_45.name
if SSF.has_roi_with_shape(ss, 'CTV-N1_55'):
  pm.RegionsOfInterest['CTV-N1_55'].Name = ROIS.ctv_n1_55.name
if SSF.has_roi_with_shape(ss, 'CTV-N2_55'):
  pm.RegionsOfInterest['CTV-N2_55'].Name = ROIS.ctv_n2_55.name
if SSF.has_roi_with_shape(ss, 'CTV-E_45'):
  pm.RegionsOfInterest['CTV-E_45'].Name = ROIS.ctv_e_45.name
if SSF.has_roi_with_shape(ss, 'PTV-E_45'):
  pm.RegionsOfInterest['PTV-E_45'].Name = ROIS.ptv_e_45.name
if SSF.has_roi_with_shape(ss, 'PTV-T_45'):
  pm.RegionsOfInterest['PTV-T_45'].Name = ROIS.ptv_p_45.name
if SSF.has_roi_with_shape(ss, 'PTV-N1_55'):
  pm.RegionsOfInterest['PTV-N1_55'].Name = ROIS.ptv_n1_55.name
if SSF.has_roi_with_shape(ss, 'PTV-N2_55'):
  pm.RegionsOfInterest['PTV-N2_55'].Name = ROIS.ptv_n2_55.name
if SSF.has_roi_with_shape(ss, 'CTV-N_55union'):
  pm.RegionsOfInterest['CTV-N_55union'].Name = ROIS.ctv_n_55.name
if SSF.has_roi_with_shape(ss, 'GTV-T+10mm'):
  pm.RegionsOfInterest['GTV-T+10mm'].Name = ROIS.x_gtv_p.name
if SSF.has_roi_with_shape(ss, 'PTV_45union'):
  pm.RegionsOfInterest['PTV_45union'].Name = ROIS.ptv_45.name
if SSF.has_roi_with_shape(ss, 'PTV-N_55union'):
  pm.RegionsOfInterest['PTV-N_55union'].Name = ROIS.ptv_n_55.name
if SSF.has_roi_with_shape(ss, 'PTV_45Help'):
  pm.RegionsOfInterest['PTV_45Help'].Name = ROIS.x_ptv_45.name
if SSF.has_roi_with_shape(ss, 'CTV_45union'):
  pm.RegionsOfInterest['CTV_45union'].Name = ROIS.ctv_45.name
if SSF.has_roi_with_shape(ss, 'Bowel bag'):
  pm.RegionsOfInterest['Bowel bag'].Name = ROIS.bowel_bag.name
if SSF.has_roi_with_shape(ss, 'Kidney (Left)'):
  pm.RegionsOfInterest['Kidney (Left)'].Name = ROIS.kidney_l.name
if SSF.has_roi_with_shape(ss, 'Kidney (Right)'):
  pm.RegionsOfInterest['Kidney (Right)'].Name = ROIS.kidney_r.name
if SSF.has_roi_with_shape(ss, 'FemoralHead (Left)'):
  pm.RegionsOfInterest['FemoralHead (Left)'].Name = ROIS.femoral_l.name
if SSF.has_roi_with_shape(ss, 'FemoralHead (Right)'):
  pm.RegionsOfInterest['FemoralHead (Right)'].Name = ROIS.femoral_r.name
if SSF.has_roi_with_shape(ss, 'Spinal Canal'):
  pm.RegionsOfInterest['Spinal Canal'].Name = ROIS.spinal_cord.name
if SSF.has_roi_with_shape(ss, 'Spinal Canal PRV 3mm'):
  pm.RegionsOfInterest['Spinal Canal PRV 3mm'].Name = ROIS.spinal_cord_prv.name
if SSF.has_roi_with_shape(ss, 'EXTERNAL'):
  pm.RegionsOfInterest['EXTERNAL'].Name = ROIS.external.name
