# 1.	Tuples Packing & Unpacking
dummy_tuple = (1,2,3,4,5)

print(type(dummy_tuple))

list_tuple = list(dummy_tuple)# Converts this to a list # Unpacking

print(type(list_tuple))

list_tuple.append(6) #[1,2,3,4,5,6]


dummy_tuple = tuple(list_tuple) # Packing

print(type(dummy_tuple))

print(dummy_tuple)