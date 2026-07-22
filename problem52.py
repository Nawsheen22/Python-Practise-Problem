file = open(filepath, "r")  # open file in read mode
content = file.read()
print(content)
file.close()                # file must be closed



file = open(filepath, "r")
content = file.read(30)     # reads first 30 characters from the file
print(content)
file.close()                # file must be closed


file = open(filepath, "r")
lines = file.readlines()   # returns a list of lines
print(lines)               # Example Output: ["line1\n", "line2\n"]
file.close()               # file must be closed


file = open(filepath, "r")
for line in file:
    print(line)                 # you may use print(line.strip()) to remove extra new line character
file.close()                    # file must be closed