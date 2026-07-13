#Q4. Billing Program

#1)Collect item details from the user
item_name = input("Enter item name: ")
price = float(input("Enter price per unit: "))
quantity = int(input("Enter quantity: "))

#2)Calculate the total bill
total = price * quantity

#3)Print the bill clearly
print(f"\nTotal Bill for {item_name} = {total}")