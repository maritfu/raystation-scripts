# encoding: utf8

# Gives a list of OARs in a GUI, and creates those that are selected.
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
from tkinter import *
from tkinter import messagebox
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
import roi as ROI
import rois as ROIS
import property as P
import radio_button as RB
import check_button_frame as FRAME
import structure_set_functions as SSF
import margins as MARGINS

# Load case data:
try:
    case = get_current("Case")
except SystemError:
    raise IOError("No case loaded.")
try:
  patient_db = get_current('PatientDB')
except SystemError:
  raise IOError("No case loaded.")

# Load patient model, examination and structure set:
pm = case.PatientModel
examination = get_current("Examination")
ss = PMF.get_structure_set(pm, case.Examinations["CT-Robust"])

#pm.CopyRoiGeometry(SourceExamination = examination.Name, TargetExamination = "CT-Robust", "zMatch")
for pm_roi in pm.RegionsOfInterest:
  if pm_roi.Name == ROIS.x_tetthetsvolum.name:
    pm_roi.DeleteRoi()
    break
x_tetthetsvolum = ROI.ROIExpanded(ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum.type, ROIS.x_tetthetsvolum.color, source = ROIS.z_match, margins = MARGINS.zero)
PMF.create_expanded_roi(pm, case.Examinations["CT-Robust"], ss, x_tetthetsvolum)
PMF.set_material(patient_db, pm, ss,case.Examinations["CT-Robust"], ROIS.x_tetthetsvolum.name, 'Water')
