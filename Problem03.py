cost=int (input("Enter the cost price for the bike:"))

if cost>100000:
    print("Tax:15%")
elif cost >50000 and cost <=1000000 :
    print("Tax:10%")   

elif cost <=50000:
    print("Tax:5%")    