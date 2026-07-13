# Q5. Student Information Card
# Solution:


#1)Collect student details
student_name = input("Enter student name: ")
class_section = input("Enter class and section (e.g., 8B): ")
school_name = input("Enter school name: ")

#2)Print a neatly formatted ID card using an f-string and newlines
print("\n----- STUDENT ID CARD -----")
print(f"Name: {student_name}")
print(f"Class: {class_section}")
print(f"School: {school_name}")
print("----------------------------")