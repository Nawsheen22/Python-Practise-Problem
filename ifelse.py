#Write a program to calculate electricity bill first 100 = 0 ,next 100 rs 5 , next 200 10 rs

Calculate=0
Money=int(input("Enter the money:"))
print("The money you have entered:",Money)


if Money<=100:
 Calculate=0

elif Money>100 and Money<=200:
 Calculate=(Money-100)*5
elif Money>200:
  Calculate=500+(Money-200)*10



print("The money is:",Calculate)  
  