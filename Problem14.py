#Taking list as user input

n=5

l=[]


for i in range(n):

 user_input=int(input("Enter the Number in the list:"))
 l.append(user_input)
print(l)

sum1=sum(l)
print(sum1)

max1=max(l)
print("The Greater Number in the list:",max1)

sort1=sorted(l)
print("The list is sorted:",sort1)
print(sort1)

minimum=min(l)
print("The minimum value:",minimum)

print("The counting in the list:",l.count(45)) #count how much 4 is there in the list
