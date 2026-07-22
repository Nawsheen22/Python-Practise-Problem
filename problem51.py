'''Introduction to file
Why Do We Need Files?
Imagine:

Your app closes ❌
Variables disappear ❌
Data is lost ❌
👉 Files solve this problem.'''

## Introduction to file

#### Why Do We Need Files?
Imagine:

- Your app closes ❌
- Variables disappear ❌
- Data is lost ❌
  
👉 Files solve this problem.


# Variables are temporary
user = "Alice"
print(user)

# After program ends → data gone
#File Handling Basic Syntax

file = open(filepath, mode)

'''

Mode	Meaning
"r"	Read (default)
"w"	Write (overwrite)
"a"	Append (add at end)


'''''

#Create and write to a file
file = open(filepath, "w")  # open file in write mode
file.write("Hello World")
file.close()     # file must be closed


'''Write mode ("w") overwrites existing content.
If the file does not exist, it will be created'''


file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Ostad\n")
file.write("Mastering Python : From Zero to Hero\n")
file.close()