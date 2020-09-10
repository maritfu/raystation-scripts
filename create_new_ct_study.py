
# encoding: utf8

# Exports and imports the current CT study. Creates and deletes a temporary folder where the CT study is placed.
# Sets imagingsystem
# Computes rigid registation
#
# Authors:
# Marit Funderud
# St Olavs Hospital
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
import roi as ROI
import rois as ROIS
import case_functions as CF
try:
  patient_db = get_current('PatientDB')
except SystemError:
  raise IOError("No case loaded.")
try:
  patient = get_current("Patient")
except SystemError:
  raise IOError("No patient loaded.")
# Load case data:
try:
    case = get_current("Case")
except SystemError:
    raise IOError("No case loaded.")

# Load patient model, examination and structure set:
pm = case.PatientModel
examination = get_current("Examination")
ss = PMF.get_structure_set(pm, examination)

new_examination_name = "CT-Robust"
CF.export_and_import_ct_study(patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
CF.compute_rigid_image_registration(case, examination, new_examination_name)
