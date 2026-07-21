# ==========================================
# Python String and Loop Example
# Author: Your Name
# Description:
# This program demonstrates basic string
# operations and the use of loops.
# ==========================================

# Store a string in a variable
message = "Hello, GitHub!"

# Print the original string
print("Original Message:", message)

# Convert the string to uppercase
print("Uppercase:", message.upper())

# Convert the string to lowercase
print("Lowercase:", message.lower())

# Count the number of characters
print("Length of the message:", len(message))

# ------------------------------------------
# Loop through each character in the string
# ------------------------------------------
print("\nCharacters in the message:")

for character in message:
    print(character)

# ------------------------------------------
# Print the message multiple times using a loop
# ------------------------------------------
print("\nRepeating the message 5 times:")

for i in range(1, 6):
    print(f"{i}. {message}")

# ------------------------------------------
# Count the vowels in the string
# ------------------------------------------
vowels = "aeiouAEIOU"
vowel_count = 0

for character in message:
    if character in vowels:
        vowel_count += 1

print("\nNumber of vowels:", vowel_count)

# ------------------------------------------
# Reverse the string using a loop
# ------------------------------------------
reversed_message = ""

for character in message:
    reversed_message = character + reversed_message

print("Reversed Message:", reversed_message)