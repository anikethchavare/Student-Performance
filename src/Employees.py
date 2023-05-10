# Student Performance - Employees

''' This program contains functions related to the 'Employees' CSV database. '''

# Imports
import pandas as pd
import os

# Function 1 - Employee Information
def employeeInformation(employeeId):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    reader = pd.read_csv("Data/Employees.csv")
    reader.set_index("Employee ID", inplace=True)

    try:
        reader2 = reader.loc[str(employeeId)]

        dateOfBirth = str(reader2[0])
        dateOfJoining = str(reader2[1])
        departmentId = str(reader2[2])

        # Print the Information
        print("\033[1m" + "\nEmployee ID: " + "\033[0m" + employeeId)
        print("\033[1m" + "Date of Birth: " + "\033[0m" + dateOfBirth)
        print("\033[1m" + "Date of Joining: " + "\033[0m" + dateOfJoining)
        print("\033[1m" + "Department ID: " + "\033[0m" + departmentId + "\n")
    except:
        print("\nPlease enter a valid employee ID.\n")

# Function 2 - Employees in Department
def employeesInDepartment(departmentId):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    reader = pd.read_csv("Data/Employees.csv")
    reader.set_index("Department_ID", inplace=True)

    try:
        reader2 = reader.loc[departmentId]

        print("\n\033[1m" + "Total Employees in " + departmentId + " Department: " + "\033[0m" + str(len(reader2.index)) + "\n")
    except:
        print("\nPlease enter a valid department ID.\n")