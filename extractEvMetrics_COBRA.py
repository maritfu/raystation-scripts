import clr, sys
from connect import*

clr.AddReference('Office')
clr.AddReference('Microsoft.Office.Interop.Excel')

import Microsoft.Office.Interop.Excel as interop_excel
import System.Array

excel = interop_excel.ApplicationClass(Visible=True)
workbook = excel.Workbooks.Add()
worksheet = workbook.Worksheets.Add()

def create_array(m,n):
	dims = System.Array.CreateInstance(System.Int32,2)
	dims[0] = m
	dims[1] = n
	return System.Array.CreateInstance(System.Object, dims)

header_row = create_array(1,7)
header_row[0,1] = 'DSC'
header_row[0,2] = 'Hausdorff'
header_row[0,3] = 'Precision'
header_row[0,4] = 'Sensitivity'
header_row[0,5] = 'Specificity'
header_row[0,6] = 'Mean distance to agreement'


startcell = worksheet.Cells(1, 1)
header_range = worksheet.Range(startcell, startcell.Cells(header_row.GetLength(0), header_row.GetLength(1)))
header_range.Value = header_row

try:
	patient = get_current('Patient')
	#plan = get_current('Plan')
except:
	print 'Patient and plan are not loaded. Exits script.'
	sys.exit()

rois = ["Breast_L", "LN_Ax_L1_L", "LN_Ax_L2_L", "LN_Ax_L3_L", "LN_Ax_L4_L", "LN_Ax_Interpect_L", "LN_IMN1-4_L", "Heart", "ThyroidGland", "Trachea", "A_LAD", "Esophagus", "Ventricle_L", "ScaleneMusc_Ant", "A_Subclavian_L", "A_Carotid_L", "V_Brachioceph_L", "V_Subclavian_L", "V_Jugular_L"]
rois_AL = ["Breast_L_AL", "LN_Ax_L1_L_AL", "LN_Ax_L2_L_AL", "LN_Ax_L3_L_AL", "LN_Ax_L4_L_AL", "LN_Ax_Interpect_L_AL", "LN_Ax_IMN1-4_L_AL", "Heart_AL", "ThyroidGland_AL", "Trachea_AL", "A_LAD_AL", "Esophagus_AL", "Ventricle_L_AL", "ScaleneMusc_Ant_AL", "A_Subclavian_L_AL", "A_Carotid_L_AL", "V_Brachioceph_L_AL", "V_Subclavian_L_AL", "V_Jugular_L_AL"]

data_array = create_array(25,8)
data_array[0,0] = patient.Name
data_array[1,0] = 'Breast_L'
data_array[2,0] = 'LN_Ax_L1_L'
data_array[3,0] = 'LN_Ax_L2_L'
data_array[4,0] = 'LN_Ax_L3_L'
data_array[5,0] = 'LN_Ax_L4_L'
data_array[6,0] = 'LN_Ax_Interpect_L'
data_array[7,0] = 'LN_IMN1-4_L'
data_array[8,0] = 'Heart'
data_array[9,0] = 'ThyroidGland'
data_array[10,0] = 'Trachea'
data_array[11,0] = 'A_LAD'
data_array[12,0] = 'Esophagus'
data_array[13,0] = 'Ventricle_L'
data_array[14,0] = 'ScaleneMusc_Ant'
data_array[15,0] = 'A_Subclavian_L'
data_array[16,0] = 'A_Carotid_L'
data_array[17,0] = 'V_Brachioceph_L'
data_array[18,0] = 'V_Subclavian_L'
data_array[19,0] = 'V_Jugular_L'

#structure_set = plan.GetStructureSet()
structure_set = patient.Cases[1].PatientModel.StructureSets[0]


for i in range(0, 19):
          
   data_array[i+1,1] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=False)['DiceSimilarityCoefficient']
   data_array[i+1,2] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=True)['MaxDistanceToAgreement']
   data_array[i+1,3] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=False)['Precision']
   data_array[i+1,4] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=False)['Sensitivity']
   data_array[i+1,5] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=False)['Specificity']
   data_array[i+1,6] = structure_set.ComparisonOfRoiGeometries(RoiA=rois[i], RoiB=rois_AL[i], ComputeDistanceToAgreementMeasures=True)['MeanDistanceToAgreement']


startcell = worksheet.Cells(2,1)
data_range = worksheet.Range(startcell, startcell.Cells(data_array.GetLength(0), data_array.GetLength(1)))
data_range.Value = data_array
worksheet.Columns.AutoFit()
