#dictionary user input


user_dict = {}

total = int(input("Enter the number of entries you want to add:"))

for x in range(total):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("Dictionary after adding user input:", user_dict)
