#Question 5: Dictionary with Enumerate

#Given the dictionary:

#marks = {

    #"Math": 80,

    #"Physics": 75,

    #"Chemistry": 85

#}

#Using a loop and enumerate():

#Print the subject number, subject name, and marks

#Example Output:

#1 Math: 80  

#2 Physics: 75  

#3 Chemistry: 85

marks = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85
}

for number, (subject, mark) in enumerate(marks.items(), start=1):
    print(number, subject + ":", mark)