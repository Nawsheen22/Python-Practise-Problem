#Problem Statement

#Write a Python program that takes a list of integers and prints the second largest unique number.

#If there is no second largest unique number, print "Not Possible".

#Example 1

#Input numbers = [10, 5, 20, 20, 8, 10]


numbers = [10, 5, 20, 20, 8, 10]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("Not Possible")
else:
    print(unique_numbers[-2])