
from __future__ import division
import math
# encoding: utf8
#!/usr/bin/python

# Import system libraries:
from connect import *
import clr, sys
import datetime, string
from tkinter import *
from tkinter import messagebox

# Add necessary folders to the system path:
patient_db = get_current('PatientDB')
patient_nr = -1
patient_info = patient_db.QueryPatientInfo(Filter = {})



nr_cases = 0
tot_nr_cases = 0
start_date = "01.06.2019 00:00:00"
stop_date = "01.01.2020 00:00:00"
new_plan = False
start_date = datetime.datetime(int(start_date[6:10]),int(start_date[3:5]),int(start_date[0:2]))
stop_date = datetime.datetime(int(stop_date[6:10]),int(stop_date[3:5]),int(stop_date[0:2]))
for i in range(len(patient_info)):
  p = str(patient_info[i]['LastModified'])
  current_patient_date = datetime.datetime(int(p[6:10]),int(p[3:5]),int(p[0:2])) 
  if current_patient_date > start_date and current_patient_date < stop_date:
    try:
      patient = patient_db.LoadPatient(PatientInfo=patient_info[i])
    except:
      print ("hei")
    try:
      patient_nr += 1
      #messagebox.showinfo("Antall caser", "Totalt antall pasienter: " + str(patient_nr) + "\n\n" "Totalt antall caser: " + str(tot_nr_cases) + "\n\n" + "Antall caser: " + str(nr_cases) + "\n\n")
      for case in patient.Cases:
        tot_nr_cases +=1
        plan = case.TreatmentPlans
        plan_info = case.QueryPlanInfo(Filter = {})
        if len(plan)>0:
          for i in range(len(plan)):   
            #if plan[i].Review:
            #if plan[i].Review.ApprovalStatus == 'Approved':
            c = str(plan_info[i]['LastModified'])
            current_date = datetime.datetime(int(c[6:10]),int(c[3:5]),int(c[0:2])) 
            if current_date > start_date and current_date < stop_date and current_patient_date > start_date and current_patient_date < stop_date:
              new_plan = True
          if new_plan:
            nr_cases+=1
            new_plan = False
            #messagebox.showinfo("1Antall caser", "Totalt antall caser: " + str(tot_nr_cases) + "\n\n" + "Antall caser: " + str(nr_cases) + "\n\n")
        else:
          nr_cases +=1
          #messagebox.showinfo("2Antall caser", "Totalt antall caser: " + str(tot_nr_cases) + "\n\n" + "Antall caser: " + str(nr_cases) + "\n\n")
    except:
      print ("hei")

messagebox.showinfo("Antall caser", "Totalt antall pasienter: " + str(patient_nr) + "\n\n" "Totalt antall caser: " + str(tot_nr_cases) + "\n\n" + "Antall caser: " + str(nr_cases) + "\n\n")









