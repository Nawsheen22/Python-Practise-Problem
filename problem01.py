#Write a program to check if it is leap year or not 


year =int(input("Enter the year:"))



if  year%4==0 :
  print("Leap year ")
elif year%100==0:
  print("Leap year")
elif year%400==0:
  print("Leap year")

else:

  print("Not a Leap Year")    

