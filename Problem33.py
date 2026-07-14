#Question 5: List Comprehension

#Given the list:

#numbers = [10, 25, 30, 45, 50, 65, 70]

#Using list comprehension:

#1. Create a new list containing only numbers greater than 40

#2. Print the new list


# Given list
numbers = [10, 25, 30, 45, 50, 65, 70]

# Creating a new list with numbers greater than 40
new_list = [num for num in numbers if num > 40]

# Printing the new list
print("Numbers greater than 40:", new_list)