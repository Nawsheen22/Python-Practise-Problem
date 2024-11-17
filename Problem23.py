user_dict = {}

num_entries = int(input("Enter the number of entries you want to add:"))

for i in range(num_entries):
    key = input("Enter key:")
    value = int(input("Enter value:"))  # Convert input value to integer
    user_dict[key] = value

print("Dictionary after adding user input:", user_dict)

# Finding the minimum value in the dictionary
min_value = min(user_dict.values())
print("Minimum value in the dictionary:", min_value)