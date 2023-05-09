# Student Performance - Counseling

''' This program contains functions related to the 'Student Counseling' CSV database. '''

# Imports
import csv
import pandas as pd
import os

# Function 1 - Student Counseling
def studentCounseling(studentId):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    reader = pd.read_csv("Data/Student Counseling.csv")
    reader.set_index("Student_ID", inplace=True)

    reader2 = reader.loc[studentId]

    if (reader2.empty):
        print("\nEnter a valid student ID!\n")
    else:
        dateOfAdmission = str(reader2[0])
        dateOfBirth = str(reader2[1])
        departmentChoice = str(reader2[2])
        departmentAdmission = str(reader2[3])

        # Print the Information
        print("\033[1m" + "\nStudent ID: " + "\033[0m" + studentId)
        print("\033[1m" + "Date of Admission: " + "\033[0m" + dateOfAdmission)
        print("\033[1m" + "Date of Birth: " + "\033[0m" + dateOfBirth)
        print("\033[1m" + "Department of Choice: " + "\033[0m" + departmentChoice)
        print("\033[1m" + "Deparment of Admission: " + "\033[0m" + departmentAdmission + "\n")