"""
Docstring for Assignment5_Task1_Create_Dictionary_of_student_marks
  
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

""" 

# Step 1: Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found.")