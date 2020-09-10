# encoding: utf8

# Contains treatment plan tests for individual treatment plans.
#
# Verified for RayStation 6.0.

# System configuration:
from connect import *
import sys
import math
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\lib".decode('utf8'))

# GUI framework (debugging only):
#clr.AddReference("PresentationFramework")
#from System.Windows import *
from tkinter import messagebox
# Local script imports:
import test_p as TEST
import raystation_utilities as RSU
import structure_set_functions as SSF
import rois as ROIS
import region_codes as RC

# This class contains tests for the RayStation TreatmentPlan object:
class TSPlan(object):
  def __init__(self, plan, ts_case=None):
    # RayStation objects:
    self.plan = plan
    # Related test suite objects:
    self.ts_case = ts_case
    self.ts_beam_sets = []
    if ts_case:
      ts_case.ts_plan = self
      self.parent_param = ts_case.param
    else:
      self.parent_param = None
    # Parameters:
    self.param = TEST.Parameter('Plan', self.plan.Name, self.parent_param)
    self.planned_by = TEST.Parameter('Planlagt av', self.plan.PlannedBy, self.param)
    self.isocenter = TEST.Parameter('Isocenter', '', self.param)
    self.numbers = TEST.Parameter('Beam numbers', '', self.param)
    self.defined_roi = TEST.Parameter('Geometri','', self.param)
    self.mu = TEST.Parameter('MU','', self.param)
    self.number = TEST.Parameter('Feltnummer','', self.param)
    self.isosenter = TEST.Parameter('Isosenter','', self.param)


  #Tests if all ROI's are defined, except 'LAD' for right sided breast, and contralateral breast for conventional treatment (ie. not VMAT)
  def breast_oar_defined_test(self):
    failed_geometries = []
    t = TEST.Test("Regionen må ha definert volum:", True, self.defined_roi)
    t.expected = None
    ss = self.ts_beam_sets[0].ts_structure_set().structure_set
    roi_not_contours_dict = SSF.create_roi_dict_not_contours(ss)
    roi_and_region_dict = {ROIS.lad.name: RC.breast_r_codes, ROIS.breast_r_draft.name:RC.breast_l_codes, ROIS.breast_r.name:RC.breast_l_codes, ROIS.breast_l.name :RC.breast_r_codes}
    if self.ts_case.ts_plan.ts_beam_sets[0].ts_label.label.region:
      for key, value in roi_and_region_dict.items():
        if roi_not_contours_dict.get(key) and self.ts_beam_sets[0].ts_label.label.region in value:
          del roi_not_contours_dict[key]

    structure_sets = self.ts_case.case.PatientModel.StructureSets
    for i in range(len(structure_sets)):
      if structure_sets[i].OnExamination.Name != self.ts_beam_sets[0].ts_structure_set().structure_set.OnExamination.Name:
        roi = structure_sets[i].RoiGeometries
        for j in range(len(roi)):
          if roi[j].HasContours() and roi_not_contours_dict.get(roi[j].OfRoi.Name):
            del roi_not_contours_dict[roi[j].OfRoi.Name]

    if len(roi_not_contours_dict.keys()) >= 1:
      return t.fail(list(roi_not_contours_dict.keys()))
    else:
      return t.succeed()


  # Tests the presence of a planned by label.
  def planned_by_test(self):
    t = TEST.Test('Doseplanleggerens initialer bør være fylt inn her (Planned by)', True, self.planned_by)
    if self.plan.PlannedBy:
      return t.succeed()
    else:
      return t.fail()


  # Tests that beam numbers are not repeated among beam sets in the treatment plan.
  def unique_beam_numbers_test(self):
    t = TEST.Test("Skal være unik for alle felt i planen", True, self.numbers)
    beam_numbers = set([])
    has_duplicate_beam_nr = False
    for beam_set in self.plan.BeamSets:
      for beam in beam_set.Beams:
        if beam.Number in beam_numbers:
          has_duplicate_beam_nr = beam
        else:
          beam_numbers.add(beam.Number)
    if has_duplicate_beam_nr:
      return t.fail(has_duplicate_beam_nr.Number)
    else:
      return t.succeed()

  def beam_number_for_breast_test(self):
    numbers = []
    order = True
    t = TEST.Test("Feltnummereringen ser ikke ut til å være riktig.", True, self.number)
    if self.ts_case.ts_plan.ts_beam_sets[0].ts_label.label.region in RC.breast_codes:
      for beam_set in self.plan.BeamSets:
        for beam in beam_set.Beams:
          numbers.append(beam.Number)
      numbers.sort()
      if len(numbers) > 1:
        for i in range(0, len(numbers)-1):
          if numbers[i+1] != numbers[i]+1:
            order = False
      if order:
        return t.succeed()
      else:
        return t.fail()

  def equal_isocenter_for_beams_test(self):
    t = TEST.Test("Alle feltene ser ikke ut til å ha samme isosenter", True, self.isosenter)
    match = True
    if len(list(self.plan.BeamSets[0].Beams)) > 0:
      first_iso = self.plan.BeamSets[0].Beams[0].Isocenter.Position
    for beam_set in self.plan.BeamSets:
      for beam in beam_set.Beams:
        if beam.Isocenter.Position.x == first_iso.x and beam.Isocenter.Position.y == first_iso.y and beam.Isocenter.Position.z == first_iso.z:  
          match = True
        else:
          match = False
    if match:
      return t.succeed()
    else:
      return t.fail()


  # Tests that number of monitor units corresponds to fraction dose (within 15 %) for conventional plans (non-VMAT) that is not locoregional breast.
  def prescription_mu_breast_test(self):
    t = TEST.Test("Skal stå i forhold til fraksjonsdosen for beam-settet, bør som hovedregel være innenfor +/- 15% av fraksjonsdosen (cGy)", True, self.mu)
    mu_total = 0
    if self.ts_case.ts_plan.ts_beam_sets[0].ts_label.is_hybrid_mamma():
      expected_fraction_dose = 267
      for ts_bs in self.ts_case.ts_plan.ts_beam_sets:
        if ts_bs.ts_label.label.technique == 'V':
          expected_fraction_dose = RSU.fraction_dose(ts_bs.beam_set) * 100
          t.expected = expected_fraction_dose

      for beam_set in self.plan.BeamSets:
        for beam in beam_set.Beams:
          mu_total += beam.BeamMU

      percent_dev = (mu_total - expected_fraction_dose) / (expected_fraction_dose) * 100
      #t.expected = RSU.fraction_dose(self.beam_set) * 100
      if abs(percent_dev) > 15:
        return t.fail(round(mu_total, 1))
      else:
        return t.succeed()

  # Tests that number of monitor units corresponds to fraction dose (within 20%) for the caudal part of conventional, locoregional breast plans.
  def prescription_mu_breast_regional_caudal_test(self):
    t = TEST.Test("Skal stå i forhold til fraksjonsdosen for beam-settet, det ser ut som MU kaudalt for isosenter avviker med mer enn 20% av fraksjonsdosen (cGy).", True, self.mu)
    for ts_beam_set in self.ts_case.ts_plan.ts_beam_sets:
      if ts_beam_set.ts_label.is_hybrid_mamma_reg():
        if ts_beam_set.beam_set.Prescription.PrimaryDosePrescription != None:
          mu_total_over = 0
          expected_fraction_dose = 0
          text = ""
          for ts_beam_set in self.ts_case.ts_plan.ts_beam_sets:
            if ts_beam_set.ts_label.label.region in RC.breast_reg_codes:
              beam_set = ts_beam_set.beam_set
              if ts_beam_set.ts_label.label.technique == 'V':
                expected_fraction_dose = RSU.fraction_dose(beam_set) * 100
                if expected_fraction_dose == 0:
                  expected_fraction_dose = 267
                t.expected = expected_fraction_dose
                #messagebox.showinfo("1", str(RSU.fraction_dose(beam_set) * 100))
              for beam in beam_set.Beams:
                segment_partial_area = []
                for index, segment in enumerate(beam.Segments):
                  jaw = segment.JawPositions
                  y1 = jaw[2]
                  y2 = jaw[3]
                  if y2 > 0:
                    y2 = 0
                  if y2 <= 0 and y1 < 0 or y1 < 0:
                    leaf_positions = segment.LeafPositions
                    mlc_y1 = int(math.floor((y1 + 20) * 2))
                    mlc_y2 = int(math.ceil ((y2 + 20) * 2))-1
                    segment_partial_area.extend([0])
                    segment_partial_area[index] += (leaf_positions[1][mlc_y1] - leaf_positions[0][mlc_y1])*(((mlc_y1+1)-(y1+20)*2)/2)
                    for mlc in range(mlc_y1+1, mlc_y2):
                      segment_partial_area[index] += (leaf_positions[1][mlc] - leaf_positions[0][mlc])*0.5
                    segment_partial_area[index] += (leaf_positions[1][mlc_y2] - leaf_positions[0][mlc_y2])*(((y2+20)*2-(mlc_y2))/2)
                  else:
                    segment_partial_area.extend([0])
                max_area = max(segment_partial_area)
                for index, segment in enumerate(beam.Segments):
                  jaw = segment.JawPositions
                  if segment_partial_area[index] > 1.5 and segment_partial_area[index]/max_area > 0.2 or round(jaw[3],1) <=0:
                    mu_total_over += beam.BeamMU*segment.RelativeWeight
          if abs((mu_total_over - expected_fraction_dose) / (expected_fraction_dose) * 100) > 20:
            return t.fail(round(mu_total_over,1))
          else:
            return t.succeed()


  # Tests that number of monitor units corresponds to fraction dose (within 20%) for the cranial part of conventional, locoregional breast plans.
  def prescription_mu_breast_regional_cranial_test(self):
    t = TEST.Test("Skal stå i forhold til fraksjonsdosen for beam-settet, det ser ut som MU kranielt for isosenter avviker med mer enn 20% av fraksjonsdosen (cGy).", True, self.mu)
    for ts_beam_set in self.ts_case.ts_plan.ts_beam_sets:
      if ts_beam_set.ts_label.is_hybrid_mamma_reg():
        if ts_beam_set.beam_set.Prescription.PrimaryDosePrescription!=None:
          mu_total_over = 0
          expected_fraction_dose = 0
          text = ""
          for ts_beam_set in self.ts_case.ts_plan.ts_beam_sets:
            if ts_beam_set.ts_label.label.region in RC.breast_reg_codes:
              beam_set = ts_beam_set.beam_set
              if ts_beam_set.ts_label.label.technique == 'V':
                expected_fraction_dose = RSU.fraction_dose(beam_set) * 100
                if expected_fraction_dose == 0:
                  expected_fraction_dose = 267
                t.expected = expected_fraction_dose

              for beam in beam_set.Beams:
                segment_partial_area = []
                for index, segment in enumerate(beam.Segments):
                  jaw = segment.JawPositions
                  y1 = jaw[2]
                  if y1 < 0:
                    y1 = 0
                  y2 = jaw[3]
                  if y1 >= 0 and y2 > 0 or y2 > 0:
                    leaf_positions = segment.LeafPositions
                    mlc_y1 = int(math.floor((y1 + 20) * 2))
                    mlc_y2 = int(math.ceil ((y2 + 20) * 2))-1
                    segment_partial_area.extend([0])
                    segment_partial_area[index] += (leaf_positions[1][mlc_y1] - leaf_positions[0][mlc_y1])*(((mlc_y1+1)-(y1+20)*2)/2)
                    for mlc in range(mlc_y1+1, mlc_y2):
                      segment_partial_area[index] += (leaf_positions[1][mlc] - leaf_positions[0][mlc])*0.5
                    segment_partial_area[index] += (leaf_positions[1][mlc_y2] - leaf_positions[0][mlc_y2])*(((y2+20)*2-(mlc_y2))/2)
                  else:
                    segment_partial_area.extend([0])
                max_area = max(segment_partial_area)
                for index, segment in enumerate(beam.Segments):
                  jaw = segment.JawPositions
                  if segment_partial_area[index] > 1.5 and segment_partial_area[index]/max_area > 0.4 or round(jaw[2],1) >=0:
                    mu_total_over += beam.BeamMU*segment.RelativeWeight

          if abs((mu_total_over - expected_fraction_dose) / (expected_fraction_dose) * 100) > 20:
            return t.fail(round(mu_total_over,1))
          else:
            return t.succeed()        
'''


      if self.ts_beam_sets[0].beam_set.DeliveryTechnique != 'Arc':
        if roi_not_contours_dict.get(ROIS.breast_r_draft.name) and self.ts_beam_sets[0].ts_label.label.region in RC.breast_l_codes:
          del roi_not_contours_dict[ROIS.breast_r_draft.name]

        if roi_not_contours_dict.get(ROIS.breast_r.name) and self.ts_beam_sets[0].ts_label.label.region in RC.breast_l_codes:
          del roi_not_contours_dict[ROIS.breast_r.name]

        if roi_not_contours_dict.get(ROIS.breast_l_draft.name) and self.ts_beam_sets[0].ts_label.label.region in RC.breast_r_codes:
          del roi_not_contours_dict[ROIS.breast_l_draft.name]

        if roi_not_contours_dict.get(ROIS.breast_l.name) and self.ts_beam_sets[0].ts_label.label.region in RC.breast_r_codes:
          del roi_not_contours_dict[ROIS.breast_l.name]
  #Tests if all ROI's are defined, except 'LAD' for right sided breast, and contralateral breast for conventional treatment (ie. not VMAT)
  def breast_oar_defined_test(self):
    failed_geometries = []
    t = TEST.Test("Regionen må ha definert volum:", True, self.defined_roi)
    t.expected = None
    ss = self.ts_beam_sets[0].ts_structure_set().structure_set
    roi_dict = SSF.create_roi_dict(ss)
    for rg in self.ts_beam_sets[0].ts_structure_set().structure_set.RoiGeometries:
      
      if rg.HasContours() == False:
        if self.ts_beam_sets[0].beam_set.DeliveryTechnique != 'Arc':
          if self.ts_case.ts_plan.ts_beam_sets[0].ts_label.label.region:
            if rg.OfRoi.Name == ROIS.lad.name and self.ts_beam_sets[0].ts_label.label.region in RC.breast_l_codes:
              failed_geometries.append(str(rg.OfRoi.Name))
            elif not rg.OfRoi.Name in (ROIS.breast_r.name, ROIS.breast_r_draft.name) and self.ts_beam_sets[0].ts_label.label.region in RC.breast_l_codes:
              failed_geometries.append(str(rg.OfRoi.Name))
            elif not rg.OfRoi.Name in (ROIS.lad.name, ROIS.breast_r.name, ROIS.breast_r_draft.name):
              failed_geometries.append(str(rg.OfRoi.Name))
        elif self.ts_beam_sets[0].beam_set.DeliveryTechnique == 'Arc':
          if self.ts_case.ts_plan.ts_beam_sets[0].ts_label.label.region:
            if rg.OfRoi.Name == ROIS.lad.name and self.ts_beam_sets[0].ts_label.label.region in RC.breast_l_codes:
              failed_geometries.append(str(rg.OfRoi.Name))
            elif rg.OfRoi.Name != ROIS.lad.name:
              failed_geometries.append(str(rg.OfRoi.Name))
    
    new_failed_geometries = []
    if len(failed_geometries) >= 1:
      for structure_set in self.ts_case.case.PatientModel.StructureSets:
        structure_sets = []
        if structure_set != self.ts_beam_sets[0].ts_structure_set().structure_set:
          structure_sets.append(structure_set)
      for struct_set in structure_sets:
        for rg in struct_set.RoiGeometries:
          for roi in list(set(failed_geometries)):
            if rg.OfRoi.Name == roi:
              if rg.HasContours() == True:
                failed_geometries.remove(roi)

    
    if len(failed_geometries) >= 1:
      return t.fail(list(set(failed_geometries)))
    else:
      return t.succeed()
'''
