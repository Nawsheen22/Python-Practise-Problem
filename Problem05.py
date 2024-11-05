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




#list Slicing:
#finding greater number in the list
print(max(l))
#sorting numbers in the list
l.sort()
print(l)

#finding the minimum number in the list
print(min(l))
#counting in the list
print(l.count(2))
#nested list
list_mixed=[["Hello World"],[0,1,2,3,4,5,6,7,8],[True,False]]
print(list_mixed[0])
print(list_mixed[1])


#reverse and concate two list

Nawsheen=["She owns a cat name"]
Salsabeel=["Khitthi"]
print(Nawsheen+Salsabeel)

#reverse this
rev=(Nawsheen+Salsabeel)
print(rev[::-1] )



#remove duplicate items from the list
dup=[1,22,3,3,56,77,8]
print(set(dup))
