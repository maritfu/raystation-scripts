from connect import *
from shutil import copytree, rmtree, copy2
import os
from tkinter import *
from tkinter import messagebox
destination = "C:/temp/tempexport/"


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

try:
    delete_files_and_folders(destination)  
except: 
    print("hei")
if not os.path.exists(destination):
  os.makedirs(destination)

patient_db = get_current("PatientDB")
clinic_db = get_current("ClinicDB")
patient = get_current("Patient")
case = get_current("Case")
examination = get_current("Examination")
patient.Save()
patient_id = "111111 11111"
patient_name = "Robust"
imaging_system = "TRCTGA004"
new_examination_name = "CT-Robust"
def export_and_import_ct_study(patient_db, patient, case, examination, destination, patient_id, patient_name, new_examination_name, imaging_system):
  if len(case.Registrations)>0 :
    for_registration = case.Registrations[0]
    to_for = for_registration.ToFrameOfReference
    from_for = for_registration.FromFrameOfReference
    to_examinations = [e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == to_for]
    from_examinations = [e for e in case.Examinations if e.EquipmentInfo.FrameOfReference == from_for]
    #messagebox.showinfo("", from_examinations)
    #messagebox.showinfo("", to_examinations)
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


export_and_import_ct_study(patient_db, patient, case, examination, destination, patient_id, patient_name, new_examination_name, imaging_system)
'''


import json

def LogWarning(warning):
  try:
    jsonWarnings = json.loads(str(warning))
    print(" ")
    print("Warning! Export Aborted")
    print("Comment:")
    print(" "),
    print(jsonWarnings["Comment"])
    print("Warnings:")
    for w in jsonWarnings["Warnings"]:
      print( " "),
      print(w)
  except ValueError as error:
    print("Error occured. Could not export")
        
def LogCompleted(completed):
  try:
    jsonWarnings = json.loads(str(completed))
    print(" ")
    print("Completed!")
    print("Comment:")
    print(" "),
    print(jsonWarnings["Comment"])
    print("Warnings:")
    for w in jsonWarnings["Warnings"]:
      print( " "),
      print( w)
    print("Export Notifications")
    for w in jsonWarnings["ExportNotifications"]:
      print( " "),
      print( w)
  except ValueError as error:
    print("Error reading completion messages.")
try:
  result = case.ScriptableDicomExport(
      ExportFolderPath = "C:\\temp\\testexport\\",
      Examinations = [examination.Name],
      RtStructureSetsForExaminations= [examination.Name],
      DicomFilter = "",
      IgnorePreConditionWarnings = False
  )
  LogCompleted(result)
except SystemError as error:
  print(" ")
  print("Trying to export again with IgonorePreConditionWarnings=True")
  print(" ")
  result = case.ScriptableDicomExport(
      ExportFolderPath = "C:\\temp\\testexport\\",
      Examinations = [examination.Name],
      RtStructureSetsForExaminations= [examination.Name],
      DicomFilter = "",
      IgnorePreConditionWarnings = True
  )
  LogCompleted(result)
'''
