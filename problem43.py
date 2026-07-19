#Question 2: Zip with Two Lists

#Given two lists:

#students = ["Rahim", "Karim", "Ayesha"]

#scores = [85, 90, 78]

#Use zip() to print each student name along with their score.

#Example Output:

#Rahim scored 85  

#Karim scored 90  

#Ayesha scored 78



students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

for student, score in zip(students, scores):
    print(student, "scored", score)