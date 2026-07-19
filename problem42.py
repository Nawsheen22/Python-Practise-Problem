#Question 1: Enumerate with List

#Given the list:

#fruits = ["apple", "banana", "cherry", "mango"]

#Use enumerate() to print each fruit with its index number.

#Output format example:

#0 apple  

#1 banana  

#2 cherry  

#3 mango



fruits = ["apple", "banana", "cherry", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)