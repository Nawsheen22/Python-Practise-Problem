#taking list user input and we will need loop here


n=5
l=[]


for i in range(n):
 k =int(input("Enter the list:"))
 l.append(k)



print(l)

sum_numbers = 0
for i in range(n):
  sum_numbers += l[i]

print(sum_numbers)

sum_numbers1 = 1
for i in range(n):
  sum_numbers1 *= l[i]

print(sum_numbers1)