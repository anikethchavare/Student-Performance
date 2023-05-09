# Student Performance

''' This project visualizes and queries data of a university's CSV database. '''

# Imports
import Counseling
import Departments
import Employees
import Students

# User Choice - Operations
print("\nHello, welcome to Student Performance! What do you want to do?\n")
print("\n1) Employee Information")
print("2) Number of Employees in a Department")
print("3) Department Information")
print("4) Student Counseling Information")
print("5) Student Performance")
print("6) Student Performance (Bar Chart)")
print("7) Compare Students in a Semester (Bar Chart)")
print("8) Compare Semesters of a Students (Bar Chart)")

userChoice = int(input("\nEnter your Choice: (1/2/3/4/5/6/7/8) "))

# User Choices
if (userChoice == 1): # Choice - 1
    employeeId = input("\nWhat's the employee's ID? ")

    Employees.employeeInformation(employeeId)
elif (userChoice == 2): # Choice - 2
    departmentId = input("\nWhat's the department ID? ")

    Employees.employeesInDepartment(departmentId)
elif (userChoice == 3): # Choice - 3
    departmentId = input("\nWhat's the student ID? ")

    Departments.departmentInformation(departmentId)
elif (userChoice == 4): # Choice - 4
    studentId = input("\nWhat's the student ID? ")

    Counseling.studentCounseling(studentId)
elif (userChoice == 5): # Choice - 5
    studentId = input("\nWhat's the student ID? ")
    semester = eval(input("What's the semester? (Enter 'None' if No Value) "))
    paper = eval(input("What's the paper ID? (Enter 'None' if No Value) "))

    Students.getStudentPerformance(studentId, semester, paper)
elif (userChoice == 6): # Choice - 6
    studentId = input("\nWhat's the student ID? ")
    semester = input("What's the semester? ")

    Students.getStudentPerformanceBarChart(studentId, semester)
elif (userChoice == 7): # Choice - 7
    studentId1 = input("\nWhat's the first student's ID? ")
    studentId2 = input("\nWhat's the second student's ID? ")
    semester = input("What's the semester? ")

    Students.compareStudentsBarChart(studentId1, studentId2, semester)
elif (userChoice == 8): # Choice - 8
    studentId = input("\nWhat's the student ID? ")
    semester1 = input("What's the first semester? ")
    semester2 = input("What's the second semester? ")

    Students.compareSemestersBarChart(studentId, semester1, semester2)
else:
    print("\nEnter a valid choice.\n")