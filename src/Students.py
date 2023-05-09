# Student Performance - Students

''' This program contains functions related to the 'Student Performance' CSV database. '''

# Imports
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Function 1 - Get Student Performance
def getStudentPerformance(studentId, semester=None, paper=None):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    if (semester == None): # StudentId
        try:
            reader2 = reader.loc[studentId]

            print()
            print(reader2)
            print()
        except:
            print("\nPlease enter valid details.\n")
    else:
        if (paper == None): # StudentId and Semester
            try:
                reader2 = reader.loc[studentId]
                reader2.set_index("Semester_Name", inplace=True)
                reader3 = reader2.loc[semester]

                print()
                print(reader3)
                print()
            except:
                print("\nPlease enter valid details.\n")
        else: # StudentId, Semester, and Paper
            try:
                reader2 = reader.loc[studentId]
                reader2.set_index("Semester_Name", inplace=True)
                reader3 = reader2.loc[semester]
                reader3.set_index("Paper_ID", inplace=True)
                reader4 = reader3.loc[paper]

                print()
                print(reader4)
                print()
            except:
                print("\nPlease enter valid details.\n")

# Function 2 - Get Student Performance Bar Chart
def getStudentPerformanceBarChart(studentId, semester):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    try:
        reader2 = reader.loc[studentId]
        reader2.set_index("Semester_Name", inplace=True)
        reader3 = reader2.loc[semester]

        marks1 = reader3.loc[:, "Marks"][0]
        marks2 = reader3.loc[:, "Marks"][1]
        marks3 = reader3.loc[:, "Marks"][2]
        marks4 = reader3.loc[:, "Marks"][3]
        marks5 = reader3.loc[:, "Marks"][4]
        marks6 = reader3.loc[:, "Marks"][5]
        marks7 = reader3.loc[:, "Marks"][6]

        data = {
            "Paper 1": marks1,
            "Paper 2": marks2,
            "Paper 3": marks3,
            "Paper 4": marks4,
            "Paper 5": marks5,
            "Paper 6": marks6,
            "Paper 7": marks7
        }

        paper = list(data.keys())
        marks = list(data.values())

        fig = plt.figure(figsize = (10, 5))

        plt.bar(paper, marks, color = 'blue', width = 0.4)

        plt.xlabel("List of Papers")
        plt.ylabel("Marks")
        plt.title("Student Performance - Bar Chart")
        plt.show()
    except:
        print("\nPlease enter valid details.\n")

# Function 3 - Compare Students Bar Chart
def compareStudentsBarChart(studentId1, studentId2, semester):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Semester_Name", inplace=True)

    try:
        reader2 = reader.loc[semester]
        reader2.set_index("Student_ID", inplace=True)
        reader4 = reader2.loc[studentId1]

        reader5 = reader.loc[semester]
        reader5.set_index("Student_ID", inplace=True)
        reader6 = reader5.loc[studentId2]

        x_axis = ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7"]
        student1 = [reader4.loc[:, "Marks"][0], reader4.loc[:, "Marks"][1], reader4.loc[:, "Marks"][2], reader4.loc[:, "Marks"][3], reader4.loc[:, "Marks"][4], reader4.loc[:, "Marks"][5], reader4.loc[:, "Marks"][6]]
        student2 = [reader6.loc[:, "Marks"][0], reader6.loc[:, "Marks"][1], reader6.loc[:, "Marks"][2], reader6.loc[:, "Marks"][3], reader6.loc[:, "Marks"][4], reader6.loc[:, "Marks"][5], reader6.loc[:, "Marks"][6]]

        x_x_axis = np.arange(len(x_axis))

        fig = plt.figure(figsize = (10, 5))

        plt.bar(x_x_axis - 0.2, student1, 0.4, label = "Student - 1", color = "blue")
        plt.bar(x_x_axis + 0.2, student2, 0.4, label = "Student - 2", color = "maroon")

        plt.xlabel("Both Students")
        plt.ylabel("Marks")
        plt.title("Student Performance - Bar Chart (Comparision of 2 Students)")
        plt.legend()
        plt.show()
    except:
        print("\nPlease enter valid details.\n")

# Function 4 - Compare Semesters Bar Chart
def compareSemestersBarChart(studentId, semester1, semester2):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    reader = pd.read_csv("Data/Student Performance.csv")
    reader.set_index("Student_ID", inplace=True)

    try:
        reader2 = reader.loc[studentId]
        reader2.set_index("Semester_Name", inplace=True)

        reader3 = reader2.loc[semester1]
        reader4 = reader2.loc[semester2]

        x_axis = ["Paper 1", "Paper 2", "Paper 3", "Paper 4", "Paper 5", "Paper 6", "Paper 7"]
        sem1 = [reader3.loc[:, "Marks"][0], reader3.loc[:, "Marks"][1], reader3.loc[:, "Marks"][2], reader3.loc[:, "Marks"][3], reader3.loc[:, "Marks"][4], reader3.loc[:, "Marks"][5], reader3.loc[:, "Marks"][6]]
        sem2 = [reader4.loc[:, "Marks"][0], reader4.loc[:, "Marks"][1], reader4.loc[:, "Marks"][2], reader4.loc[:, "Marks"][3], reader4.loc[:, "Marks"][4], reader4.loc[:, "Marks"][5], reader4.loc[:, "Marks"][6]]

        x_x_axis = np.arange(len(x_axis))

        fig = plt.figure(figsize = (10, 5))

        plt.bar(x_x_axis - 0.2, sem1, 0.4, label = "First Semester You Selected", color = "blue")
        plt.bar(x_x_axis + 0.2, sem2, 0.4, label = "Second Semester You Selected", color = "maroon")

        plt.xlabel("Both Semesters")
        plt.ylabel("Marks")
        plt.title("Student Performance - Bar Chart (Comparision of 2 Semesters)")
        plt.legend()
        plt.show()
    except:
        print("\nPlease enter valid details.\n")