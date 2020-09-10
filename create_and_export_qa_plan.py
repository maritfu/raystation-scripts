# encoding: utf8
# Creates a QA plan with standard settings and exports it to specified folder.
#
# Authors:
# Marit Funderud
# Helse Møre og Romsdal HF
#
# Made for RayStation version: 9A
# Python 3.6

# Import system libraries:
from connect import *
import clr, sys, os

import math
from tkinter import *
from tkinter import messagebox

# Load patient and case data:
try:
    patient = get_current("Patient")
except SystemError:
    raise IOError("No plan loaded.")
try:
    plan = get_current("Plan")
except SystemError:
    raise IOError("No plan loaded.")
try:
    beam_set = get_current("BeamSet")
except SystemError:
    raise IOError("No beam set loaded.")

#name = 'QA'
patient_name = patient.Name
patient_name_split = patient_name.split('^')
patient_last_name = patient_name_split[0]
beam_set_label = beam_set.DicomPlanLabel
label_split = beam_set_label.split(':')
dose_label = label_split[1]
name = patient_last_name + dose_label
if len(name)>15:
  name = patient_last_name[0:16-len(dose_label)]+dose_label
#messagebox.showinfo("1", name)
org_name = name
name_conflict = False
if len(list(plan.VerificationPlans)) > 0:
  for p in plan.VerificationPlans:
    if p.BeamSet.DicomPlanLabel == org_name:
      name_conflict = True
  if name_conflict:
    i = 0
    while True:
      i += 1
      name = org_name + " " + str(i) + ""
      if len(name)>15:
        org_name = patient_last_name[0:16-(len(dose_label)+2)]+dose_label
        name = org_name + " " + str(i) + ""
      name_conflict = False
      
      for p in plan.VerificationPlans:
        if p.BeamSet.DicomPlanLabel == name:
          name_conflict = True
      if name_conflict == False:
        break
#messagebox.showinfo("2", name)
#isocenter = plan.VerificationPlans[0].PhantomStudy.PhantomPatientModel.StructureSets[0].RoiGeometries['ytterkontur'].GetCenterOfRoi()
isocenter ={ 'x': -0.107395034360885, 'y': 1.22745308220494, 'z': -3.69975236266017 }
beam_set.CreateQAPlan(
    PhantomName= "Delta4 2016 Q4_medio_sept",
    PhantomId= "100564 465",
    QAPlanName=name,
    IsoCenter=isocenter,
    DoseGrid={ 'x': 0.2, 'y': 0.2, 'z': 0.2 },
    GantryAngle=None,
    CollimatorAngle=None,
    CouchRotationAngle=None,
    ComputeDoseWhenPlanIsCreated=True,
)

# Unscriptable Action 'Save' Completed : SaveAction(...)

# Save
patient.Save()
last_plan = len(list(plan.VerificationPlans))-1
plan.VerificationPlans[last_plan].ScriptableQADicomExport(
	ExportFolderPath = "I:\STOLAV - Kreftklinikken\Avdelinger kreft\Avdeling for stråleterapi\VMAT QA",
	QaPlanIdentity = 'Patient',
	ExportExamination = False,
	ExportExaminationStructureSet = False,
	ExportBeamSet = True,
	ExportBeamSetDose = True,
	ExportBeamSetBeamDose = True,
	IgnorePreConditionWarnings = False
)


