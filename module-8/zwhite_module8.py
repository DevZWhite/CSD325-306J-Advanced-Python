"""
    Author: Zachary White
    Instructor: Darrell Payne
    Date: 05/01/2026
    Assignment: Module 8 - Student JSON
    Description: Python program that reads a student JSON file,
                 displays the list, appends a new student, and
                 saves the updated list back to the file.
"""

import json

# -------------------------------------------
# -- Load the JSON file into a list
# -------------------------------------------
with open("Student.json", "r") as file:
    students = json.load(file)

# -------------------------------------------
# -- Function to print all students
# -------------------------------------------
def print_students(student_list):
    for student in student_list:
        print("{}, {} : ID = {} , Email = {}".format(
            student["L_Name"],
            student["F_Name"],
            student["Student_ID"],
            student["Email"]
        ))

# -------------------------------------------
# -- Display original list
# -------------------------------------------
print("\n-- Original Student List --\n")
print_students(students)

# -------------------------------------------
# -- Append new student record
# -------------------------------------------
new_student = {
    "F_Name": "Zachary",
    "L_Name": "White",
    "Student_ID": 99999,
    "Email": "zwhite@gmail.com"
}

students.append(new_student)

# -------------------------------------------
# -- Display updated list
# -------------------------------------------
print("\n-- Updated Student List --\n")
print_students(students)

# -------------------------------------------
# -- Write updated list back to JSON file
# -------------------------------------------
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\n-- Student.json file has been updated --\n")
