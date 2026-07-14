#Question 4: String Processing with Loop

#Take a string from the user and count how many vowels (a, e, i, o, u) are in the string.

# Taking a string from the user
text = input("Enter a string: ")

# Initializing vowel counter
count = 0

# Loop through each character
for char in text.lower():
    if char in "aeiou":
        count += 1

# Printing the result
print("Number of vowels:", count)

