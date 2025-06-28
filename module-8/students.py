# Daniel Graham
# Date: 6/28/25
# Module 8.2 Assignment: JSON Practice

import json

# Function to print student information
def print_students(student_list):
    for student in student_list:
        print(student["L_Name"] + ", " + student["F_Name"] +
              " : ID = " + str(student["Student_ID"]) +
              " , Email = " + student["Email"])

# Step 1: Load the student list from the JSON file
with open("student.json", "r") as file:
    students = json.load(file)

# Step 2: Print the original list
print("Original Student List:")
print_students(students)

# Step 3: Create a new student and add to the JSON list
new_student = {
    "F_Name": "Daniel",
    "L_Name": "Graham",
    "Student_ID": 123456,
    "Email": "learning@python.com"
}
students.append(new_student)

# Step 4: Print the updated list with new entry
print("\nUpdated Student List:")
print_students(students)

# Step 5: Write the updated list back to the JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

# Step 6: Tell the user the file was updated
print("\nstudent.json file has been updated!")