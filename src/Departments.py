# Student Performance - Departments

''' This program contains functions related to the 'Departments' CSV database. '''

# Imports
import pandas as pd
import os

# Function 1 - Department Information
def departmentInformation(departmentId):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    reader = pd.read_csv("Data/Departments.csv")
    reader.set_index("Department_ID", inplace=True)

    try:
        reader2 = reader.loc[departmentId]

        departmentName = str(reader2[0])
        dateOfEntry = str(reader2[1])

        # Print the Information
        print("\033[1m" + "\nDepartment ID: " + "\033[0m" + departmentId)
        print("\033[1m" + "Department Name: " + "\033[0m" + departmentName)
        print("\033[1m" + "Date of Entry: " + "\033[0m" + dateOfEntry + "\n")
    except:
        print("\nPlease enter a valid department ID.\n")