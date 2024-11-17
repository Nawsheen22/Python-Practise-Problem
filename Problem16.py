from itertools import count

n=9
l=[]

for i in range (n):
    k=int(input("Enter the numbers in the list:"))
    l.append(k)


print(l)

count=sum(1 for x in l if x>10)
print (count)