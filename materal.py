# Script recorded 04 May 2020, 12:50:31

#   RayStation version: 8.1.2.5
#   Selected patient: ...

from connect import *

case = get_current("Case")


with CompositeAction('Apply ROI changes (Rectum)'):

  case.PatientModel.RegionsOfInterest['Rectum'].SetRoiMaterial(Material=case.PatientModel.Materials[2])

  # CompositeAction ends 

