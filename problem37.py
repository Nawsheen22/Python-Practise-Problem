# List Comprehention
x = [1,2,3,4,5,6,7,8,9,10]

odd = [x[i] for i in range(len(x)) if i%2==0]

print(odd)

even = [x[i] for i in range(len(x)) if i%2 !=0]
print(even)