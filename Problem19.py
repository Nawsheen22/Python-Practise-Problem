"""Input a number list and find how many numbers are greater than 10 in the list
and print the count"""

n=7
l=[]
for x in range (n):
    user_input=int(input("Enter the numbers in the list:"))
    l.append(user_input)
print(l)

count=0
for x1 in l:
    if x1>10:
        count+=1


print("Count:",count)
