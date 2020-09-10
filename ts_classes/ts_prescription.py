# encoding: utf8

# Contains treatment plan tests for individual beams.
#
# Verified for RayStation 6.0.

# System configuration:
from connect import *
import sys
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\lib".decode('utf8'))

# GUI framework (debugging only):
#clr.AddReference("PresentationFramework")
#from System.Windows import *

# Local script imports:
import test_p as TEST
import raystation_utilities as RSU
import structure_set_functions as SSF
import rois as ROIS
import region_codes as RC
from tkinter import *
from tkinter import messagebox

# This class contains tests for the RayStation Prescription object:
class TSPrescription(object):
  def __init__(self, prescription, ts_beam_set=None):
    # RayStation object:
    self.prescription = prescription
    # Related test suite objects:
    self.ts_beam_set = ts_beam_set
    if ts_beam_set:
      ts_beam_set.ts_prescription = self
      self.parent_param = ts_beam_set.param
    else:
      self.parent_param = None
    # Parameters:
    self.param = TEST.Parameter('Prescription', str(prescription.PrimaryDosePrescription.DoseValue/100.0), self.parent_param)
    self.roi = TEST.Parameter('ROI', self.prescription.PrimaryDosePrescription.OnStructure.Name, self.param)
    self.type = TEST.Parameter('Type', self.prescription.PrimaryDosePrescription.PrescriptionType, self.param)
    self.dose = TEST.Parameter('Dose', '', self.param)
    self.mu = TEST.Parameter('MU', '', self.param)
    self.maks = TEST.Parameter('Klinisk maksdose', '', self.param)

  def has_prescription(self):
    if self.prescription.PrimaryDosePrescription==None:
      return False
    else:
      return True

  def clinical_max_test(self):
    t = TEST.Test("Skal i utgangspunktet være mindre enn 105% av normeringsdosen", True, self.maks)
    ts = TEST.Test("Skal i utgangspunktet være mindre enn 150% av normeringsdosen", True, self.maks)
    diff_pr_dose = RSU.differential_prescription_dose(self.ts_beam_set.ts_plan.plan, self.ts_beam_set.beam_set)
    ss = self.ts_beam_set.ts_structure_set().structure_set
    if SSF.has_named_roi_with_contours(ss, ROIS.external.name):
      #external = RSU.ss_roi_geometry(self.ts_beam_set.beam_set, self.ts_beam_set.ts_plan.ts_case.case.PatientModel.RegionsOfInterest[ROIS.external.name])
      external = ss.OutlineRoiGeometry
      volume = external.GetRoiVolume()
      # Determine the fraction corresponding to a 2cc volume:
      fraction = 2 / volume
      #clinical_max_dose = RSU.gy(self.ts_beam_set.beam_set.FractionDose.GetDoseAtRelativeVolumes(RoiName = external.OfRoi.Name, RelativeVolumes = [fraction])[0]) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
      if self.ts_beam_set.ts_label.is_hybrid_mamma() or self.ts_beam_set.ts_label.is_hybrid_mamma_reg() or self.ts_beam_set.ts_label.is_hybrid_mamma_boost():
        expected_fraction_dose = 267
        for ts_bs in self.ts_beam_set.ts_plan.ts_beam_sets:
          if ts_bs.ts_label.label.technique == 'V':
            diff_pr_dose = 267
            t.expected = diff_pr_dose
      if self.ts_beam_set.ts_label.label.technique:
        if not self.ts_beam_set.ts_label.label.technique.upper() == 'S':
          clinical_max_dose = RSU.gy(self.ts_beam_set.beam_set.FractionDose.GetDoseAtRelativeVolumes(RoiName = external.OfRoi.Name, RelativeVolumes = [fraction])[0]) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
          if clinical_max_dose > diff_pr_dose * 1.05:
            t.expected = "<" + str(round(diff_pr_dose * 1.05, 2))
            return t.fail(round(clinical_max_dose, 2))
          else:
            return t.succeed()
        elif self.ts_beam_set.ts_label.label.technique.upper() == 'S':
          clinical_max_dose = RSU.gy(self.ts_beam_set.beam_set.FractionDose.GetDoseAtRelativeVolumes(RoiName = external.OfRoi.Name, RelativeVolumes = [0])[0]) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
          if clinical_max_dose > diff_pr_dose * 1.50:
            ts.expected = "<" + str(round(diff_pr_dose * 1.50, 2))
            ts.fail(round(clinical_max_dose, 2))
          else:
            ts.succeed()

  def ctv_prescription_test(self):
    t = TEST.Test("Skal i utgangspunktet benytte CTV til normalisering.", True, self.roi)
    ts = TEST.Test("Skal i utgangspunktet benytte PTV til normalisering.", True, self.roi)
    if self.ts_beam_set.ts_label.label.technique:
      if self.ts_beam_set.ts_label.label.technique.upper() == 'S':
        if self.prescription.PrimaryDosePrescription.OnStructure.Type == 'Ptv':
          ts.succeed()
        else:
          ts.fail(self.prescription.PrimaryDosePrescription.OnStructure.Type)
      else:
        if self.prescription.PrimaryDosePrescription.OnStructure.Type == 'Ctv':
          return t.succeed()
        else:
          return t.fail(self.prescription.PrimaryDosePrescription.OnStructure.Type)

  # FIXME: Egen prescription test for stereotaksi og om planen har målvolum eller ikke. NEAR MAX DOSE for bryst konv
  def prescription_type_test(self):
    t = TEST.Test("Skal være en av disse", ['MedianDose', 'DoseAtPoint', 'DoseAtVolume', 'NearMinimumDose','NearMaximumDose'], self.type)
    if self.prescription.PrimaryDosePrescription.PrescriptionType in ('MedianDose', 'DoseAtPoint', 'DoseAtVolume','NearMinimumDose','NearMaximumDose'):
      return t.succeed()
    else:
      return t.fail()

  def prescription_poi_technique_test(self):
    t = TEST.Test("Punktnormering skal bare benyttes i kombinasjon med plan-type 'U'", False, self.type)
    if self.prescription.PrimaryDosePrescription.PrescriptionType == 'DoseAtPoint':
      if self.ts_beam_set.ts_label.label.technique:
        if self.ts_beam_set.ts_label.label.technique.upper() == 'U':
          return t.succeed()
        else:
          return t.fail(True)

  # FIXME: Bruk struktursett tilhørende aktuell plan istedenfor case.
  def prescription_poi_target_volume_test(self):
    t = TEST.Test("Punktnormering skal kun benyttes for planer som ikke har målvolum definert", False, self.type)
    if self.prescription.PrimaryDosePrescription.PrescriptionType == 'DoseAtPoint':
      if self.ts_beam_set.ts_plan.ts_case.has_target_volume:
        return t.fail(True)
      else:
        return t.succeed()

  def prescription_dose_test(self):
    t = TEST.Test("Skal stemme overens med totaldose indikert av beam set label.", True, self.dose)
    if self.ts_beam_set.ts_label.is_hybrid_mamma() or self.ts_beam_set.ts_label.is_hybrid_mamma_boost() or self.ts_beam_set.ts_label.is_hybrid_mamma_reg():
      if self.has_prescription():
        for ts_beam_set in self.ts_beam_set.ts_plan.ts_beam_sets:
          if ts_beam_set.ts_label.label.technique == 'V':
            if RSU.prescription_dose(ts_beam_set.beam_set) > 0:
              pr_dose = round(float(RSU.prescription_dose(ts_beam_set.beam_set)),2)
              label_dose = round(float(ts_beam_set.ts_label.label.end_dose_str)-float(ts_beam_set.ts_label.label.start_dose_str),2)
              t.expected = label_dose
              if label_dose != pr_dose:
                return t.fail(pr_dose)
              else:
                return t.succeed()
    else:
      if self.has_prescription():
        cum_pr_dose = RSU.prescription_dose(self.ts_beam_set.beam_set)
        diff_pr_dose = RSU.differential_prescription_dose(self.ts_beam_set.ts_plan.plan, self.ts_beam_set.beam_set)
        if self.ts_beam_set.ts_label.label.valid:
          label_dose_acc = RSU.accumulated_label_dose(self.ts_beam_set.ts_plan.plan, self.ts_beam_set.beam_set, self.ts_beam_set.ts_label.label)
          t.expected = label_dose_acc
          if label_dose_acc != cum_pr_dose:
            return t.fail(cum_pr_dose)
          else:
            return t.succeed()


  def prescription_real_dose_test(self):
    t = TEST.Test("Skal stemme overens (innenfor 0.5%) med aktuell dose for nomeringsvolum (eller punkt)", True, self.dose)
    
    if self.ts_beam_set.beam_set.Modality == 'Photons':
      cum_pr_dose = RSU.prescription_dose(self.ts_beam_set.beam_set)
      if self.ts_beam_set.ts_label.is_hybrid_mamma() or self.ts_beam_set.ts_label.is_hybrid_mamma_reg():
        diff_pr_dose = 40.05
        #messagebox.showinfo("Error.","hei")
      elif self.ts_beam_set.ts_label.is_hybrid_mamma_boost():
        diff_pr_dose = 16
      else:
        diff_pr_dose = RSU.differential_prescription_dose(self.ts_beam_set.ts_plan.plan, self.ts_beam_set.beam_set)
      low_dose = round(diff_pr_dose * 0.995, 2)
      high_dose = round(diff_pr_dose * 1.005, 2)
      t.expected = "<" + str(low_dose) + " - " + str(high_dose) + ">"
      if self.prescription.PrimaryDosePrescription.PrescriptionType == 'DoseAtPoint':
        norm_poi = ss_poi_geometry(self.ts_beam_set.beam_set, self.prescription.PrimaryDosePrescription.OnStructure)
        p = {'x': norm_poi.Point.x, 'y': norm_poi.Point.y, 'z': norm_poi.Point.z}
        real_poi_dose = RSU.gy(self.ts_beam_set.beam_set.FractionDose.InterpolateDoseInPoint(Point = p)) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
        if real_poi_dose < low_dose or real_poi_dose > high_dose:
          return t.fail(round(real_poi_dose, 2))
        else:
          return t.succeed()
      if self.prescription.PrimaryDosePrescription.PrescriptionType == 'MedianDose':
        if self.ts_beam_set.ts_label.is_hybrid_mamma() or self.ts_beam_set.ts_label.is_hybrid_mamma_boost() or self.ts_beam_set.ts_label.is_hybrid_mamma_reg():
          real_dose_d50 = (self.ts_beam_set.ts_plan.plan.TreatmentCourse.TotalDose.GetDoseAtRelativeVolumes(RoiName = self.prescription.PrimaryDosePrescription.OnStructure.Name, RelativeVolumes = [0.50])[0])/100
          #messagebox.showinfo("Error.",real_dose_d50)
        else:  
          real_dose_d50 = RSU.gy(self.ts_beam_set.beam_set.FractionDose.GetDoseAtRelativeVolumes(RoiName = self.prescription.PrimaryDosePrescription.OnStructure.Name, RelativeVolumes = [0.50])[0]) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
        if real_dose_d50 < low_dose or real_dose_d50 > high_dose:
          return t.fail(round(real_dose_d50, 2))
        else:
          return t.succeed()
      if self.prescription.PrimaryDosePrescription.PrescriptionType == 'DoseAtVolume':
        real_dose_d99 = RSU.gy(self.ts_beam_set.beam_set.FractionDose.GetDoseAtRelativeVolumes(RoiName = self.prescription.PrimaryDosePrescription.OnStructure.Name, RelativeVolumes = [0.99])[0]) * self.ts_beam_set.beam_set.FractionationPattern.NumberOfFractions
        if real_dose_d99 < low_dose or real_dose_d99 > high_dose:
          return t.fail(round(real_dose_d99, 2))
        else:
          return t.succeed()

  # MÅ testes
  def stereotactic_prescription_technique_test(self):
    t = TEST.Test("Ved stereotaksi skal prescription være: DoseAtVolume >=98 %. Planteknikk skal være S.", True, self.type)
    if self.prescription.PrimaryDosePrescription.PrescriptionType == 'DoseAtVolume' and self.prescription.PrimaryDosePrescription.DoseVolume >= 98 and self.ts_beam_set.beam_set.DeliveryTechnique == 'Arc':
      if self.ts_beam_set.ts_label.label.technique:
        if self.ts_beam_set.ts_label.label.technique.upper() == 'S':
          return t.succeed()
        else:
          return t.fail()
      else:
        return t.fail(self.prescription.PrimaryDosePrescription.PrescriptionType)





