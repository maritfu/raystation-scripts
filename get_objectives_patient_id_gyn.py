
from __future__ import division
import math
# encoding: utf8
#!/usr/bin/python

# Import system libraries:
from connect import *
import clr, sys
import System.Array
clr.AddReference("Office")
clr.AddReference("Microsoft.Office.Interop.Excel")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("PresentationFramework")
from System.Windows import *
import Microsoft.Office.Interop.Excel as interop_excel


# Add necessary folders to the system path:
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\Test_mfu\\Klinisk\\def_regions".decode('utf8'))
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\Test_mfu\\Klinisk\\functions".decode('utf8'))
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\Test_mfu\\Klinisk\\gui_classes".decode('utf8'))
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\Test_mfu\\Klinisk\\rt_classes".decode('utf8'))
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\Test_mfu\\Klinisk\\settings".decode('utf8'))

#import region_codes as RC

# Utility function to create 2-dimensional array
def create_array(m, n):
    dims = System.Array.CreateInstance(System.Int32, 2)
    dims[0] = m
    dims[1] = n
    return System.Array.CreateInstance(System.Object, dims)


patient_db = get_current('PatientDB')
#all_patients = patient_db.QueryPatientInfo(Filter = {})
#patient_id = patient.PatientID


#patient_list = ['Anonymized 24 Jun 2019, 09:34:04 (hr:min:sec)','Anonymized 27 Jun 2019, 10:50:17 (hr:min:sec)','Anonymized 01 Jul 2019, 14:17:33 (hr:min:sec)','Anonymized 27 Jun 2019, 15:12:20 (hr:min:sec)']
patient_list = ['TR17']
#patient_list = ['Rød'.decode('utf8', 'replace')]
# Create data array to hold ROI data
data_array = create_array(500,500)
#patient_nr = 0
#test_patient_info = patient_db.QueryPatientInfo(Filter = {'LastName': 'LYNGE'})
#patient_test = patient_db.LoadPatient(PatientInfo=test_patient_info[0])
#time_test = patient_test.ModificationInfo.ModificationTime
#patient_info = patient_db.QueryPatientInfo(Filter = {'LastName': 'Knutsen' })
#patient_info = patient_db.QueryPatientInfo(Filter = {'Gender': 'Male'})
#patient_info = patient_db.QueryPatientInfo(Filter = {})



plan = None

k=0
for i, pas in enumerate(patient_list):
  try:
    patient_info = patient_db.QueryPatientInfo(Filter = {'PatientID': pas})
  except:
    print "hei"
  for j in range(0, len(patient_info)):
		try:
			patient = patient_db.LoadPatient(PatientInfo=patient_info[j])
		except:
			print "hei"
		for case in patient.Cases:
			for plan in case.TreatmentPlans:
				if plan.Name == 'V101:0-55:25':
					cf = plan.PlanOptimizations[0].Objective.ConstituentFunctions
					for i, v in enumerate(cf):
						try:
							data_array[i, 1+k] = cf[i].DoseFunctionParameters.FunctionType
						except:
							data_array[i, 1+k] = 'Dose Fall-Off'
						try:
							data_array[i, 3+k] = cf[i].DoseFunctionParameters.DoseLevel/100
						except:
							print "Hei"
						try:
							data_array[i, 4+k] = cf[i].DoseFunctionParameters.PercentVolume
						except:
							print "Hei"
						try: 
							data_array[i, 3+k] = cf[i].DoseFunctionParameters.HighDoseLevel/100
							data_array[i, 4+k] = cf[i].DoseFunctionParameters.LowDoseLevel/100
							data_array[i, 5+k] = cf[i].DoseFunctionParameters.LowDoseDistance
						except:
							print "Hei"
							
						try:
							data_array[i, 2+k] = cf[i].OfDoseGridRoi.OfRoiGeometry.OfRoi.Name
							data_array[i, 6+k] = cf[i].DoseFunctionParameters.Weight
						except:
							print "Hei"

						try:
							data_array[0, 0+k] = patient.Name
						except:
							print "Hei"
		k += 7
# Select path where the Excel file should be saved
# Set file_path = None if the file should not be automatically saved
file_path = None

# Should the Excel file be closed after it is created?
# If no file path is selected, the Excel application will not be closed
close_excel = True
# Create an Excel file

try:
		# Open Excel with new worksheet
		excel = interop_excel.ApplicationClass(Visible=True)
		workbook = excel.Workbooks.Add(interop_excel.XlWBATemplate.xlWBATWorksheet)
		worksheet = workbook.Worksheets[1]
		l=0
		# Set up header row
		# Edit this if other dose statistics are desired
		header_col = create_array(50,200)
		for m in range(0, 22):
			header_col[0,0+l] = plan.Name
			header_col[0,1+l] = 'Objective'
			header_col[0,2+l] = 'ROI'
			header_col[0,3+l] = 'Dose'
			header_col[0,4+l] = 'Prosent volum/ Lavdose fall-off'
			header_col[0,5+l] = 'Avstand fall-off'
			header_col[0,6+l] = 'Vekt'
			l+=7


		# Add header row to work sheet
		startcell = worksheet.Cells(1, 1)
		header_range = worksheet.Range(startcell, startcell.Cells(header_col.GetLength(0), header_col.GetLength(1)))
		header_range.Value2 = header_col

		# Add ROI data array to work sheet
		startcell = worksheet.Cells(2,1)
		data_range = worksheet.Range(startcell, startcell.Cells(data_array.GetLength(0), data_array.GetLength(1)))
		data_range.Value2 = data_array

		# Auto-fit the width of all columns
		worksheet.Columns.AutoFit()

		if file_path != None:
				# File name is PatientNamePlanNameDoseStatistics
				# Edit this if another file name is desired
				filename = r"{0}\{1}{2}DoseStatistics.xlsx".format(file_path, patient.PatientName, plan.Name)
				excel.DisplayAlerts = False
				workbook.SaveAs(filename)
finally:
    # The following is needed for the excel process to die when user closes worksheet
    if file_path != None and close_excel:
        excel.Quit()
    System.Runtime.InteropServices.Marshal.FinalReleaseComObject(worksheet)
    System.Runtime.InteropServices.Marshal.FinalReleaseComObject(workbook)
    System.Runtime.InteropServices.Marshal.FinalReleaseComObject(excel)
    seriesCollection = None
    chart = None
    worksheet = None
    workbook = None
    excel = None
    System.GC.WaitForPendingFinalizers()
    System.GC.Collect()




