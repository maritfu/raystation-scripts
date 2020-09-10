# encoding: utf8
import os
# Import local files:
import isodose_color_tables as ISODOSES
import plan_functions as PF
import region_codes as RC
import structure_set_functions as SSF
import rois as ROIS

# Contains a collection of case functions.
from tkinter import *
from tkinter import messagebox

# Set up plan, making sure the plan name does not already exist. If the plan name exists, (1), (2), (3) etc is added behind the name.
def create_plan(case, examination, region_text):
  name = region_text
  name_conflict = False
  for p in case.TreatmentPlans:
    if p.Name == region_text:
      name_conflict = True
  if name_conflict:
    i = 0
    while True:
      i += 1
      name = region_text + " (" + str(i) + ")"
      name_conflict = False
      for p in case.TreatmentPlans:
        if p.Name == name:
          name_conflict = True
      if name_conflict == False:
        break
  plan = case.AddNewPlan(PlanName = name, ExaminationName = examination.Name)
  return plan


'''
def copy_ct_study_and_create_density_volume(case, examination, ss):
  case.CopyExamination(ExaminationName = examination.Name, NewExaminationName = "CT - Robust")
'''
def delete_files_and_folders(destination):
  if os.path.isdir(destination):
    for file in os.listdir(destination):
      p = os.path.join(destination, file)
      if os.path.isdir(p):
        delete_files_and_folders(p)
      else:
        try:
          os.remove(p)
        except: 
          print("hei")
    try:
      os.rmdir(destination)
    except:
      print ("hei")
# Exports and imports the current CT study. Creates and deletes a temporary folder where the CT study is placed.
# Sets imagingsystem 
def export_and_import_ct_study(clinic_db, patient_db, patient, case, examination, destination, patient_id, patient_name, new_examination_name, imaging_system):
  match = True
  for ex in case.Examinations:
    if ex.Name == new_examination_name:
      match = False
  if match:
    try:
        delete_files_and_folders(destination)  
    except: 
        print("hei")
    if not os.path.exists(destination):
      os.makedirs(destination)

    patient.Save()
    if len(case.Registrations) > 0:
      for_registration = case.Registrations[0]
      to_for = for_registration.ToFrameOfReference
      from_for = for_registration.FromFrameOfReference
      to_examinations = [e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == to_for]
      from_examinations = [e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == from_for]
      #patient_id = "111111 11111"
      try:
        default_anonymization_options = clinic_db.GetSiteSettings().DicomSettings.DefaultAnonymizationOptions
        anonymization_settings = {"Anonymize": True, 
                                "AnonymizedName": patient_name, 
                                "AnonymizedID": patient_id, 
                                "RetainDates": default_anonymization_options.RetainLongitudinalTemporalInformationFullDatesOption, 
                                "RetainDeviceIdentity": default_anonymization_options.RetainDeviceIdentityOption, 
                                "RetainInstitutionIdentity": default_anonymization_options.RetainInstitutionIdentityOption, 
                                "RetainUIDs": default_anonymization_options.RetainUIDs, 
                                "RetainSafePrivateAttributes": default_anonymization_options.RetainSafePrivateOption}
        if len(from_examinations) > 0:
          result = case.ScriptableDicomExport(
            AnonymizationSettings=anonymization_settings,
            ExportFolderPath = destination,
            Examinations = [examination.Name],
            RtStructureSetsForExaminations= [examination.Name],
            SpatialRegistrationForExaminations=["%s:%s"%(from_examinations[0].Name,to_examinations[0].Name)],
            DicomFilter = "",
            IgnorePreConditionWarnings = True
          )
        else:
          result = case.ScriptableDicomExport(
            AnonymizationSettings=anonymization_settings,
            ExportFolderPath = destination,
            Examinations = [examination.Name],
            RtStructureSetsForExaminations= [examination.Name],
            DicomFilter = "",
            IgnorePreConditionWarnings = True
          )
      except:
        print("hei")
      matching_patients = patient_db.QueryPatientsFromPath(Path = destination, SearchCriterias = {'PatientID':patient_id})
      if len(matching_patients)>0:
        matching_patient =matching_patients[0]
      else:
        matching_patient=matching_patients 
      studies = patient_db.QueryStudiesFromPath(Path = destination, SearchCriterias = matching_patient)
      series = []
      for study in studies:
        series +=patient_db.QuerySeriesFromPath(Path = destination, SearchCriterias = study)
      warnings = patient.ImportDataFromPath(Path = destination, SeriesOrInstances = series, CaseName = case.CaseName, AllowMismatchingPatientID = True)
      print( warnings)
      #ex_name = ct_name
      for ex in case.Examinations:
        if ex.Name != examination.Name:
          exa_name = ex.Name
          #messagebox.showinfo("", exa_name[0:2])
          if ex.GetExaminationDateTime() == None and exa_name[0:2]=="CT":
            ex.Name = new_examination_name
            ex.EquipmentInfo.SetImagingSystemReference(ImagingSystemName =imaging_system)
            break
          else:
            print("hei")
        else:
          print("hei")
      try:
          delete_files_and_folders(destination)  
      except: 
          print("hei")
    else:
      default_anonymization_options = clinic_db.GetSiteSettings().DicomSettings.DefaultAnonymizationOptions
      anonymization_settings = {"Anonymize": True, 
                                "AnonymizedName": patient_name, 
                                "AnonymizedID": patient_id, 
                                "RetainDates": default_anonymization_options.RetainLongitudinalTemporalInformationFullDatesOption, 
                                "RetainDeviceIdentity": default_anonymization_options.RetainDeviceIdentityOption, 
                                "RetainInstitutionIdentity": default_anonymization_options.RetainInstitutionIdentityOption, 
                                "RetainUIDs": default_anonymization_options.RetainUIDs, 
                                "RetainSafePrivateAttributes": default_anonymization_options.RetainSafePrivateOption}

      
      result = case.ScriptableDicomExport(
        AnonymizationSettings=anonymization_settings,
        ExportFolderPath = destination,
        Examinations = [examination.Name],
        RtStructureSetsForExaminations= [examination.Name],
        DicomFilter = "",
        IgnorePreConditionWarnings = True
      )


      matching_patients = patient_db.QueryPatientsFromPath(Path = destination, SearchCriterias = {'PatientID':patient_id})
      if len(matching_patients)>0:
        matching_patient =matching_patients[0]
      else:
        matching_patient=matching_patients 
      studies = patient_db.QueryStudiesFromPath(Path = destination, SearchCriterias = matching_patient)
      series = []
      for study in studies:
        series +=patient_db.QuerySeriesFromPath(Path = destination, SearchCriterias = study)
      warnings = patient.ImportDataFromPath(Path = destination, SeriesOrInstances = series, CaseName = case.CaseName, AllowMismatchingPatientID = True)
      print( warnings)
      
      for ex in case.Examinations:
        if ex.Name != examination.Name:
          exa_name = ex.Name
          #messagebox.showinfo("", exa_name[0:2])
          if ex.GetExaminationDateTime() == None and exa_name[0:2]=="CT":
            ex.Name = new_examination_name
            ex.EquipmentInfo.SetImagingSystemReference(ImagingSystemName =imaging_system)
            break
          else:
            print("hei")
        else:
          print("hei")
      try:
          delete_files_and_folders(destination)  
      except: 
          print("hei")
        


def compute_rigid_image_registration(case, examination, new_examination_name):
  case.ComputeRigidImageRegistration(
    FloatingExaminationName=new_examination_name,
    ReferenceExaminationName=examination.Name,
    UseOnlyTranslations=False,
    HighWeightOnBones=False,
    InitializeImages=True,
    FocusRoisNames=[],
    RegistrationName=None
  )


# Loads a plan in the RayStation GUI. This is used when a new plan is created by script, in which case
# it is not automatically loaded in the GUI.
def load_plan(case, plan):
  current_plan = case.QueryPlanInfo(Filter = {'Name': plan.Name})
  case.LoadPlan(PlanInfo = current_plan[0])


# Set isodose lines:
def determine_isodoses(case, ss, region_code, nr_fractions, fraction_dose):
  #case.CaseSettings.DoseColorMap.PresentationType = 'Relative'
  case.CaseSettings.DoseColorMap.PresentationType = 'Absolute'
  case.CaseSettings.DoseColorMap.ReferenceValue = nr_fractions*fraction_dose*100
  total_dose = nr_fractions*fraction_dose
  if region_code in RC.breast_codes and fraction_dose == 2 or region_code in RC.rectum_codes and fraction_dose == 2:
    ISODOSES.sib_47_50.apply_to(case)
  elif region_code in RC.head_neck_codes:
    if total_dose == 70:
      ISODOSES.head_neck_54_60_70.apply_to(case)
    elif total_dose == 68:
      ISODOSES.head_neck_54_60_68.apply_to(case)
    elif total_dose == 66:
      ISODOSES.head_neck_54_60_66.apply_to(case)
    elif total_dose == 60:
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
        ISODOSES.head_neck_54_60.apply_to(case)
      else:
        ISODOSES.head_neck_50_60.apply_to(case)
  elif region_code in RC.prostate_codes:
    if fraction_dose in [2.0, 2.2]:
      if region_code in RC.prostate_bed_codes:
        if SSF.has_roi_with_shape(ss, ROIS.ctv_56.name):
          ISODOSES.prostate_bed_56_70.apply_to(case)
        else:
          ISODOSES.standard.apply_to(case)
      else:
        if SSF.has_roi_with_shape(ss, ROIS.ctv_56.name):
          ISODOSES.prostate_56_70_77.apply_to(case)
        else:
          ISODOSES.prostate_70_77.apply_to(case)
    elif fraction_dose == 3 and SSF.has_roi_with_shape(ss, ROIS.ctv_57.name):
      ISODOSES.prostate_57_60.apply_to(case)
    else:
      ISODOSES.standard.apply_to(case)
  elif PF.is_stereotactic(nr_fractions, fraction_dose):
    ISODOSES.stereotactic.apply_to(case)
  else:
    ISODOSES.standard.apply_to(case)

def determine_patient_position(examination):
  patient_position = "HeadFirstSupine"
  if examination.PatientPosition == 'FFS':
    patient_position = "FeetFirstSupine"
  elif examination.PatientPosition == 'HFP':
    patient_position = "HeadFirstProne"
  elif examination.PatientPosition == 'FFP':
    patient_position = "FeetFirstProne"
  return patient_position


def is_head_first_supine(examination):
  if determine_patient_position(examination) == 'HeadFirstSupine':
    return True
  else:
    return False


  
  
