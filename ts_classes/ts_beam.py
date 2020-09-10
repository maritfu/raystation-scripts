# encoding: utf8

# Contains treatment plan tests for individual beams.
#
# Verified for RayStation 6.0.

# System configuration:
from connect import *
import sys
#sys.path.append("I:\\HSM - Kreftavdelingen - gammelt fellesområde\\Program\\Skript\\RayStation\\lib".decode('utf8'))
from tkinter import messagebox
# GUI framework (debugging only):
#clr.AddReference("PresentationFramework")
#from System.Windows import *

# Local script imports:
import test_p as TEST
import raystation_utilities as RSU
import region_codes as RC

# This class contains tests for the RayStation Beam object:
class TSBeam(object):
  def __init__(self, beam, ts_beam_set=None):
    # RayStation object:
    self.beam = beam
    # Related test suite objects:
    self.ts_beam_set = ts_beam_set
    self.ts_segments = []
    if ts_beam_set:
      ts_beam_set.ts_beams.append(self)
      self.parent_param = ts_beam_set.param
    else:
      self.parent_param = None
    # Parameters:
    self.param = TEST.Parameter('Felt', str(beam.Number), self.parent_param)
    self.name = TEST.Parameter('Navn', '', self.param)
    self.mu = TEST.Parameter('MU', '', self.param)
    self.gantry = TEST.Parameter('Gantryvinkel', str(round(self.beam.GantryAngle, 1)), self.param)
    self.energy = TEST.Parameter('Energi', str( self.beam.MachineReference.Energy), self.param)
    self.collimator = TEST.Parameter('Kollimatorvinkel', str(round(beam.InitialCollimatorAngle, 1)), self.param)
    self.segments = TEST.Parameter('Segmenter', '', self.param)
    self.gantry_spacing = TEST.Parameter('Gantry spacing', '', self.param)
    self.isocenter = TEST.Parameter('Isosenter', '', self.param)
    self.opening = TEST.Parameter('Åpning', '', self.param)
    self.mlc = TEST.Parameter('MLC', '', self.param)
    self.couch_angle = TEST.Parameter('Bordvinkel','',self.param)

  # Gives true/false if the beam has segments or not.
  def has_segment(self):
    if len(list(self.beam.Segments)) > 0:
      return True
    else:
      return False

  # Gives true/false if the beam is an VMAT arc
  def is_vmat(self):
    if self.beam.ArcRotationDirection != 'None':
      return True
    else:
      return False
 
  # Tests that for arcs that a gantry spacing of 4 is used. MÅ TESTES
  def arc_gantry_spacing_test(self):
    t = TEST.Test("Skal normalt være 2 ved bruk av sliding window, og 4 ellers", 4, self.gantry_spacing)
    if self.is_vmat():
      expected_gantry_spacing = 4
      if self.ts_beam_set.ts_optimization.is_sliding_window():
        expected_gantry_spacing = 2
      # VMAT optimization settings:
      beam_s = RSU.beam_settings(self.ts_beam_set.ts_plan.plan, self.ts_beam_set.beam_set, self.beam)
      if beam_s:
        if beam_s.ArcConversionPropertiesPerBeam.FinalArcGantrySpacing != expected_gantry_spacing:
          return t.fail(beam_s.ArcConversionPropertiesPerBeam.FinalArcGantrySpacing)
        else:
          return t.succeed()
  # MASKIN MÅ FIKSES
  # Tests if the field is asymmetric, i.e. ifthe maximum jaw opening is more than 7.5 cm for Y1 and Y2 jaws for an VMAT arc, for filter free energies,
  def asymmetric_jaw_opening_for_filter_free_energies(self):
    t = TEST.Test("Maksimal avstand fra isosenter til feltgrense ved bruk av filter fri energi bør være < 7.5 cm  ", '<7.5 cm', self.collimator)
    # Perform the test only for VMAT beams:
    if self.is_vmat():
      if self.ts_beam_set.beam_set.MachineReference.MachineName == "Agility Trh FFF":
        if self.has_segment():
          maxJawY1 = self.beam.Segments[0].JawPositions[2]
          maxJawY2 = self.beam.Segments[0].JawPositions[3]
          for segment in self.beam.Segments:
            if segment.JawPositions[2] < maxJawY1:
              maxJawY1 = segment.JawPositions[2]
            if segment.JawPositions[3] > maxJawY1:
              maxJawY2 = segment.JawPositions[3]
          if maxJawY1 < -7.5:
            return t.fail(maxJawY1)
          elif maxJawY2 > 7.5:
            return t.fail(maxJawY2)
          else:
            return t.succeed()

  # Tests if the maximum jaw opening is more than 10.5 cm for both Y1 and Y2 jaws for an VMAT arc, to be able to measure it with the ArcCHECK-phantom
  def asymmetric_jaw_opening_for_vmat_qa_detector_test(self):
    t = TEST.Test("Isosenter ser ut til å være asymmetrisk, det bør vurderes å flytte isosenter. Dette for å få målt hele målvolumet med ArcCheck-fantomet", '<10.5 cm', self.isocenter)
    # Perform the test only for VMAT beams:
    if self.is_vmat():
      if self.has_segment():
        maxJawY1 = self.beam.Segments[0].JawPositions[2]
        maxJawY2 = self.beam.Segments[0].JawPositions[3]
        
        for segment in self.beam.Segments:
          if segment.JawPositions[2] < maxJawY1:
            maxJawY1 = segment.JawPositions[2]
          if segment.JawPositions[3] > maxJawY1:
            maxJawY2 = segment.JawPositions[3]
        #messagebox.showinfo("", "2")
        if maxJawY1 < -10.5 and maxJawY2 > 10.5:
          return t.succeed()
        elif maxJawY1 < -10.5:
          return t.fail(abs(maxJawY1))
        elif maxJawY2 > 10.5:
          return t.fail(maxJawY2)
        else:
          return t.succeed()

  # Tests for cardinal collimator angles for VMAT arcs. MÅ TESTES
  def collimator_angle_of_arc_test(self):
    t = TEST.Test("Skal normalt unngå rette vinkler for VMAT buer", 'Ulik [0, 90, 180, 270]', self.collimator)
    forbidden_angles = [90, 180, 270]
    if self.beam.ArcRotationDirection != 'None':
      if not self.ts_beam_set.ts_label.label.region in RC.breast_reg_codes:
        forbidden_angles.append(0)
      if self.beam.InitialCollimatorAngle in forbidden_angles:
        return t.fail(self.beam.InitialCollimatorAngle)
      else:
        return t.succeed()    

  def couch_angle_test(self):
    t = TEST.Test("Bordvinkel skal i utgangspunktet være lik 0.", '0', self.couch_angle)
    t.expected = 0
    match = True
    if self.ts_beam_set.has_prescription():
      if len(list(self.ts_beam_set.beam_set.Beams)) > 0:
        if self.ts_beam_set.ts_label.label.technique:
          if self.ts_beam_set.ts_label.label.technique.upper() != 'S':
            if int(self.beam.CouchRotationAngle) != 0 or int(self.beam.CouchPitchAngle)!=0 or int(self.beam.CouchRollAngle)!=0 :
              match = False
    if match:
      t.succeed()
    else:
      t.fail(self.beam.CouchRotationAngle)
      
  # Tests for energy used for VMAT arcs. MÅ TESTES
  def energy_of_arc_test(self):
    t = TEST.Test("Skal normalt ikke bruke 15 MV ved VMAT", '6 eller 10', self.energy)
    if self.is_vmat():
      if self.beam.MachineReference.Energy == '15':
        return t.fail(self.beam.MachineReference.Energy)
      else:
        return t.succeed()

  # Tests for gantry angle (we want to avoid using the exact 180.0 angle).
  def gantry_angle_test(self):
    t = TEST.Test("Gantryvinkel lik 180 grader bør unngås, da denne vinkelen er tvetydig. Bruk < eller > enn 180.0, og velg den siden som best passer overens med øvrige feltvinkler samt planlagt XVI-protokoll.", '!= 180.0', self.gantry)
    if self.beam.GantryAngle == 180:
      return t.fail(self.beam.GantryAngle)
    else:
      return t.succeed()
    
  def max_mu_for_sliding_window_test(self):
    t = TEST.Test("Skal i utgangspunktet bruke begrensninger på antall MU per bue ved bruk av sliding window <= 2.5*fraksjonsdose (cGy).", True, self.mu)
    if self.ts_beam_set.ts_optimization.is_sliding_window():
      for po in self.ts_beam_set.ts_plan.plan.PlanOptimizations:
        for beam_settings in po.OptimizationParameters.TreatmentSetupSettings[0].BeamSettings:
          if self.beam.Number == beam_settings.ForBeam.Number and beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU:
            t.expected = "<" + str(RSU.fraction_dose(self.ts_beam_set.beam_set) * 250)
            if beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU <= (RSU.fraction_dose(self.ts_beam_set.beam_set) * 250*1.015):
              return t.succeed()
            else:
              return t.fail(round(beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU,1))

  # Tests for low number of monitor units.
  def mu_beam_vmat_test(self):
    t = TEST.Test("Skal være høyere enn nedre praktiserte grense", '>2', self.mu)
    if self.is_vmat():
      if self.beam.BeamMU < 2:
        return t.fail(self.beam.BeamMU)
      else:
        return t.succeed()

  # Tests for low number of monitor units for 3D-CRT beams
  def mu_segment_3dcrt_test(self):
    t = TEST.Test("Skal være høyere enn nedre praktiserte grense", '>2', self.mu)
    if self.beam.ArcRotationDirection == 'None':
      for segment in self.beam.Segments:
        if self.beam.BeamMU*segment.RelativeWeight < 2:
          return t.fail(round(self.beam.BeamMU*segment.RelativeWeight, 2))
        else:
          return t.succeed()

  # Tests name capitalization (test passes also if first character is a non-letter (e.g. number)).
  def name_capitalization_test(self):
    t = TEST.Test("Skal være navngitt med stor forbokstav", None, self.name)
    if self.beam.Name[0].isupper() or not self.beam.Name[0].isalpha():
      return t.succeed()
    else:
      t.expected = self.beam.Name[0].upper()
      return t.fail(self.beam.Name[0])

  # Tests that name format is gantry start angle - gantry stop angle, eks 178 - 182, VMAT arcs.MÅ TESTES
  def name_of_arc_test(self):
    t = TEST.Test("Feltnavn for VMAT buer skal følge formatet gantry startvinkel - gantry stoppvinkel (f.eks. 178-182)", None, self.name)
    if self.is_vmat():
      beam_start = self.beam.GantryAngle
      beam_stop = self.beam.ArcStopGantryAngle
      expected = str(int(beam_start)) + "-" + str(round(beam_stop))
      #expected = 'Arc ' + str(self.beam.Number)
      if expected != self.beam.Name:
        t.expected = expected
        return t.fail(self.beam.Name)
      else:
        return t.succeed()

  # Tests presence of name.
  def name_of_beam_test(self):
    t = TEST.Test("Feltnavn for konvensjonelle felt skal i utgangspunktet være lik/inneholde gantryvinkelen ", str(int(self.beam.GantryAngle)), self.name)
    match = True
    if self.beam.Name:
      if self.beam.ArcRotationDirection == 'None':
        beam_name = str(self.beam.Name)
        gantry_angle = str(int(self.beam.GantryAngle))
        if gantry_angle in beam_name:
          match = True
        else:
          match = False
    if match:
      return t.succeed()
    else:
      return t.fail(beam_name)

  # Tests presence of name.
  def name_test(self):
    t = TEST.Test("Skal ha angitt et feltnavn", True, self.name)
    if self.beam.Name and len(self.beam.Name) > 0:
      return t.succeed()
    else:
      return t.fail()

  # Tests the number of segments used on a static beam.
  def number_of_segments_of_static_beam_test(self):
    t = TEST.Test("Skal i utgangspunktet være tilbakeholden med å bruke mange segmenter (ved IMRT)", '<8', self.segments)
    if self.beam.ArcRotationDirection == 'None':
      nr_segments = RSU.soc_length(self.beam.Segments)
      if nr_segments >= 8:
        return t.fail(nr_segments)
      else:
        return t.succeed()

  # Tests if the beam has segments.
  def segment_test(self):
    t = TEST.Test("Segment skal være definert.", True, self.segments)
    if self.has_segment():
      return t.succeed()
    else:
      return t.fail()
    


  # Tests if the number of MU per beam is evenly distributed among the beams
  def stereotactic_beam_distribution_mu_test(self):
    t = TEST.Test("Antall MU bør være jevnt fordelt per bue (buelengde tatt i betraktning). MU på denne buen er > 1.15 * forventningsverdien.", True, self.mu)
    beam_start = 0
    beam_stop = 0
    beam_length = 0
    total_beam_length = 0
    if self.ts_beam_set.has_prescription():
      if len(list(self.ts_beam_set.beam_set.Beams)) > 1:
        if self.ts_beam_set.ts_label.label.technique:
          if self.ts_beam_set.ts_label.label.technique.upper() == 'S':
            for beam in self.ts_beam_set.beam_set.Beams:
              beam_start = beam.GantryAngle
              beam_stop = beam.ArcStopGantryAngle
              if beam_start > 180:
                total_beam_length += 360 - beam_start
              else:
                total_beam_length += beam_start
              if beam_stop > 180:
                total_beam_length += 360 - beam_stop
              else:
                total_beam_length += beam_stop

            beam_start = self.beam.GantryAngle
            beam_stop = self.beam.ArcStopGantryAngle
            if beam_start > 180:
              beam_length += 360 - beam_start
            else:
              beam_length += beam_start
            if beam_stop > 180:
              beam_length += 360 - beam_stop
            else:
              beam_length += beam_stop
            t.expected = "<" + str(round((beam_length/total_beam_length)*RSU.fraction_dose(self.ts_beam_set.beam_set) * 140))
            if self.beam.BeamMU > (beam_length/total_beam_length)*RSU.fraction_dose(self.ts_beam_set.beam_set) * 140 *1.15:
              return t.fail(round(self.beam.BeamMU, 1))
            else:
              return t.succeed()

  # Tests if a constraint is set for the maximum number of MU per beam, and if it is lower than 1.4 times the fraction dose
  def stereotactic_mu_constraints_for_single_beam(self):
    t = TEST.Test("Skal i utgangspunktet bruke begrensninger på antall MU per bue <= 1.4*fraksjonsdose (cGy).", True, self.mu)
    beam_start = 0
    beam_stop = 0
    beam_length = 0
    total_beam_length = 0
    if self.ts_beam_set.has_prescription():
      if len(list(self.ts_beam_set.beam_set.Beams)) == 1:
        if self.ts_beam_set.ts_label.label.technique:
          if self.ts_beam_set.ts_label.label.technique.upper() == 'S':
            for po in self.ts_beam_set.ts_plan.plan.PlanOptimizations:
              for beam_settings in po.OptimizationParameters.TreatmentSetupSettings[0].BeamSettings:
                if self.beam.Number == beam_settings.ForBeam.Number and beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU:
                  t.expected = "<" + str(RSU.fraction_dose(self.ts_beam_set.beam_set) * 140)
                  if beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU <= (RSU.fraction_dose(self.ts_beam_set.beam_set) * 140*1.15):
                    return t.succeed()
                  else:
                    return t.fail(round(beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU,1))

  # Tests if a constraint is set for the maximum number of MU per beam, and if it is lower than 1.4 times the fraction dose
  def stereotactic_mu_constraints_for_multiple_beams(self):
    t = TEST.Test("Skal i utgangspunktet bruke begrensninger på antall MU per bue <= 1.4*fraksjonsdose (cGy), disse bør også ta hensyn til buelengden. Begrensningen på MU for denne buen er > 1.15 * forventningsverdien.", True, self.mu)
    beam_start = 0
    beam_stop = 0
    beam_length = 0
    total_beam_length = 0
    if self.ts_beam_set.has_prescription():
      if len(list(self.ts_beam_set.beam_set.Beams)) > 1:
        if self.ts_beam_set.ts_label.label.technique:
          if self.ts_beam_set.ts_label.label.technique.upper() == 'S':
            for po in self.ts_beam_set.ts_plan.plan.PlanOptimizations:
              for beam_settings in po.OptimizationParameters.TreatmentSetupSettings[0].BeamSettings:
                if self.beam.Number == beam_settings.ForBeam.Number and beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU:
                  for beam in self.ts_beam_set.beam_set.Beams:
                    beam_start = beam.GantryAngle
                    beam_stop = beam.ArcStopGantryAngle
                    if beam_start > 180:
                      total_beam_length += 360 - beam_start
                    else:
                      total_beam_length += beam_start
                    if beam_stop > 180:
                      total_beam_length += 360 - beam_stop
                    else:
                      total_beam_length += beam_stop

                  beam_start = beam_settings.ForBeam.GantryAngle
                  beam_stop = beam_settings.ForBeam.ArcStopGantryAngle
                  if beam_start > 180:
                    beam_length += 360 - beam_start
                  else:
                    beam_length += beam_start
                  if beam_stop > 180:
                    beam_length += 360 - beam_stop
                  else:
                    beam_length += beam_stop
                  t.expected = "<" + str(round((beam_length/total_beam_length)*RSU.fraction_dose(self.ts_beam_set.beam_set) * 140))
                  if beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU <= ((beam_length/total_beam_length)*RSU.fraction_dose(self.ts_beam_set.beam_set) * 140*1.15):
                    return t.succeed()
                  else:
                    return t.fail(round(beam_settings.ArcConversionPropertiesPerBeam.MaxArcMU,1))

  # Tests if the jaw opening on a vmat plan is big enough to risk exposing the electronics of the QA detector.
  # The "limit" towards the electronics is 15 cm away from the gantry from the isocenter.
  def wide_jaw_opening_which_can_hit_vmat_qa_detector_electronics_test(self):
    t = TEST.Test("Høy kollimator-åpning detektert. Avhengig av kollimatorvinkel og kollimatoråpning, kan man i slik situasjoner risikere å bestråle elektronikken på ArcCheck-detektoren, som bør unngås. Ved asymmetrisk isosenter, bør isosenter vurderes flyttet for å unngå dette.", '<14.3 cm', self.opening)
    # Perform the test only for VMAT beams:
    if self.ts_beam_set.ts_plan.ts_case.case.Examinations[0].PatientPosition == 'HFS':
      if self.is_vmat():
        if self.has_segment():
          jaws = self.beam.Segments[0].JawPositions
          if jaws[2] < -14.3:
            return t.fail(round(abs(jaws[2]),1))
          else:
            return t.succeed()
    elif self.ts_beam_set.ts_plan.ts_case.case.Examinations[0].PatientPosition == 'FFS':
      if self.is_vmat():
        if self.has_segment():
          jaws = self.beam.Segments[0].JawPositions
          if jaws[3] > 14.3:
            return t.fail(round(jaws[3],1))
          else:
            return t.succeed()

  # Tests if the maximal jaw opening is less than 15 cm for filter free energies. MÅ TESTES
  def wide_jaw_opening_for_filter_free_energies(self):
    t = TEST.Test("Høy kollimatoråpning detektert, det bør vurderes om filter-energi bør brukes. Maksimal feltstørrelse ved bruk av filter fri energi er 15 cm  ", '<15 cm', self.opening)
    # Perform the test only for VMAT beams:
    if self.is_vmat():
      if self.ts_beam_set.beam_set.MachineReference.MachineName == 'Agility Trh FFF':
        if self.has_segment():
          maxJawY1 = self.beam.Segments[0].JawPositions[2]
          maxJawY2 = self.beam.Segments[0].JawPositions[3]
          for segment in self.beam.Segments:
            if segment.JawPositions[2] < maxJawY1:
              maxJawY1 = segment.JawPositions[2]
            if segment.JawPositions[3] > maxJawY1:
              maxJawY2 = segment.JawPositions[3]
          if abs(maxJawY1)+abs(maxJawY2) > 15:
            return t.fail(abs(maxJawY1)+abs(maxJawY2))
          else:
            return t.succeed()
            
    # Tests if the maximal jaw opening is less than 15 cm for filter free energies.
  def narrow_jaw_opening_for_filter_energies(self):
    t = TEST.Test("Liten kollimatoråpning detektert. Det bør vurderes om filterfri-energi kan brukes for å spare tid.", '<15 cm', self.opening)
    # Perform the test only for VMAT beams:
    if self.is_vmat():
      if self.ts_beam_set.beam_set.MachineReference.MachineName == 'Agility Trh':
        if self.has_segment():
          maxJawY1 = self.beam.Segments[0].JawPositions[2]
          maxJawY2 = self.beam.Segments[0].JawPositions[3]
          for segment in self.beam.Segments:
            if segment.JawPositions[2] < maxJawY1:
              maxJawY1 = segment.JawPositions[2]
            if segment.JawPositions[3] > maxJawY1:
              maxJawY2 = segment.JawPositions[3]

          if abs(maxJawY1)+abs(maxJawY2) < 14:
            return t.fail(abs(maxJawY1)+abs(maxJawY2))
          else:
            return t.succeed()


