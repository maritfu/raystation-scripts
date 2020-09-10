from __future__ import division
import math
# Compute perturbed doses based on user input
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
from tkinter import *
from tkinter import messagebox


# Add necessary folders to the system path:
sys.path.append("C:\\temp\\raystation-scripts\\gui_classes")

# Import local files:
import eqd2_frame as FRAME

# Load beam set and examination 
beam_set = get_current("BeamSet")
examination = get_current("Examination")
name = examination.Name

# Setup and run GUI:
my_window = Tk()
frame = FRAME.TextBoxFrame(my_window)
frame.grid(row=0,column=0)
my_window.mainloop()

# Extract information from the users's selections in the GUI:
if frame.ok:
    (total_dose,nr_fractions,alphabeta,alternative_nr_fractions) = frame.get_results()
elif not frame.ok:
    print ("Script execution cancelled by user...")
    sys.exit(0)
else:
    messagebox.showinfo("Error.","Unexpected error.")
    sys.exit(0)


dose = total_dose 


# Calculates the EQD2 equivalent dose
# Returned value is rounded to 1 decimal.
def equivalent(dose, nr_fractions, alphabeta, alternative_nr_fractions):
  if alternative_nr_fractions == nr_fractions:
    return dose
  else:
    d = dose/nr_fractions
    par = 4*((nr_fractions*(d**2)+(nr_fractions*d*alphabeta))/alternative_nr_fractions)
    return round(alternative_nr_fractions*(((-alphabeta) + math.sqrt(alphabeta**2+ par ))/2), 1)

def eqd2(dose, nr_fractions, alphabeta):
  d = dose/nr_fractions
  return (dose*(d+alphabeta))/(2+alphabeta)

new_dose = equivalent(dose, nr_fractions, alphabeta, alternative_nr_fractions)
eqd_dose = eqd2(dose, nr_fractions, alphabeta)
text = "EQD2-dose: " + str(round(eqd_dose,1))+"\n"
text += "Ekvivalent doseverdi ved alternativt antall fraksjoner: "+str(new_dose)+"\n"

messagebox.showinfo("", text)
