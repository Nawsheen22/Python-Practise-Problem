# Take a string from the user
s = input("Enter a string: ")

# Variable to count vowels
count = 0

# Loop through every character in the string
for letter in s:

    # Check if the character is a vowel
    if letter in "aeiouAEIOU":
        count += 1

# Display the result
print("Number of vowels:", count)