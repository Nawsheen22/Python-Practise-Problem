"""Input a list like ["apple","banana","car","dog","orange","cat"] and sort them by their length"""


Old_list=["apple","banana","car","dog","orange","cat"]
New_list=sorted(Old_list,key=len)


m1=["3","5","6"]


y=dict(zip(m1,New_list))
print(y)


"""Print this New_list using dictionary where len is key and items are value"""


# Input list
Old_list = ["apple", "banana", "car", "dog", "orange", "cat"]

# Sort the list by length
New_list = sorted(Old_list, key=len)

# Initialize an empty dictionary
length_dict = {}

# Populate the dictionary
for x in New_list:
    length = len(x)  # Get the length of the item
    if length not in length_dict:
        length_dict[length] = []  # Create a new list if the length is not a key
    length_dict[length].append(x)  # Append the item to the list for that length

# Print the resulting dictionary
print(length_dict)