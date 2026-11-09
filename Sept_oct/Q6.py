# Q5. Student Result Menu — match-case + loops + if-else

# Write a menu-driven Python program for managing the result of N students.

# The program should repeatedly display:

# 1. Enter student marks
# 2. Display average marks
# 3. Display highest marks
# 4. Display lowest marks
# 5. Display result
# 6. Exit

# Use match-case for menu selection.

# For each student, marks are entered for:

# Python
# Database
# Programming

# A student passes only if:

# Marks in each subject >= 40
# Overall percentage >= 50

# For the Display Result option, print:

# Student 1: Pass
# Student 2: Fail
# Student 3: Pass

# The menu should continue until the user selects the 6 .Exit

n = int(input("Enter the Total number of students:-"))  #the result of N students.

student_1 = int(input("Enter the Total marks for Student 1:-"))  #1. Enter student marks
student_1_py = int(input("Enter the marks for Python in Student 1:-"))  #1. Enter Python student marks
student_1_db = int(input("Enter the marks for Database in Student 1:-"))  #1. Enter Database student marks
student_1_prog = int(input("Enter the marks for Programming in Student 1:-"))  #1. Enter Programming student marks

student_2 = int(input("Enter the Total marks for Student 2:-"))  #2. Enter student marks
student_2_py = int(input("Enter the marks for Python in Student 2:-"))  #2. Enter Python student marks
student_2_db = int(input("Enter the marks for Database in Student 2:-"))  #2. Enter Database student marks
student_2_prog = int(input("Enter the marks for Programming in Student 2:-"))  #2. Enter Programming student marks

student_3 = int(input("Enter the Total marks for student 3:-"))  #3. Enter student marks
student_3_py = int(input("Enter the marks for Python in student 3 :-")) #3 Enter Python student marks
student_3_db = int(input("Enter the marks for Database in student 3 :-")) #3 Enter Database student marks
student_3_prog = int(input("Enter the marks for Programming in student 3 :-")) #3 Enter Programming student marks

Average_marks_students = (student_1 + student_2 + student_3) / 3

Average_marks_students_py = (student_1_py + student_2_py + student_3_py) / 3
Average_marks_students_db = (student_1_db + student_2_db + student_3_db) / 3
Average_marks_students_prog = (student_1_prog + student_2_prog + student_3_prog) / 3

Average_marks_individual_students = (student_1_py + student_1_db + student_1_prog) / 3
Average_marks_individual_students = (student_2_py + student_2_db + student_2_prog) / 3
Average_marks_individual_students = (student_3_py + student_3_db + student_3_prog) / 3

highest_marks_students = max(student_1, student_2, student_3)
lowest_marks_students = min(student_1, student_2, student_3)