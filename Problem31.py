#Question 3: String Manipulation

#Take a string input from the user and:

#1. Print the string in uppercase

#2. Print the length of the string

#3. Print the string reversed



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