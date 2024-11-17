""" Write a python program that takes a list of numbers and replaces all negative numbers with zero
numbers using loop
"""
n=5
l=[]
for x in range(n):
    user_input=int(input("Enter the list numbers:"))
    l.append(user_input)
print("List:",l)

new_list=[]
for x1 in l:
    if x1<0:
        new_list.append(0)
    else:
        new_list.append(x1)

print("Final List:",new_list)