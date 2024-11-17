"""Finding minimum and maximum value from a dictionary"""


Trash={}

total=int(input("Enter Amount of Key and Value in the Dictionary:"))

for x in range(total):
    key=input("Enter Key:")
    Value=input("Enter Value:")
    Trash[key]=Value

print("The Required Dictionary:",Trash)


minvalue=min(Trash.values())
print("The minimum value:",minvalue)

maximumvalue=max(Trash.values())
print("Required Max:",maximumvalue)