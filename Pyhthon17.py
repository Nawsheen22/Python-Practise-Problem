my_list = ["apple", "banana", "car", "dog", "orange", "cat"]

# Sorting the list by the length of each element
sorted_list = sorted(my_list, key=len)

print(sorted_list)

my_list = ['car', 'dog', 'cat', 'apple', 'banana', 'orange']

# Group words by their length
length_dict = {}
for word in my_list:
    length = len(word)  # Get the length of the word
    length_dict.setdefault(length, []).append(word)  # Group words by their length

print(length_dict)

user_dict = {}

num_entries = int(input("Enter the number of entries you want to add:"))

for i in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("Dictionary after adding user input:", user_dict)
