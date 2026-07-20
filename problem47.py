"""
Introduction to Functions
A function is a reusable block of code that performs a specific task.

🧠 Think of it like a machine:

You give it some input

It does something

It gives back output

💡 so, Function is kind of like a machine (let’s say a coffee machine) 
which can take input (e.g., coffee beans, milk, sugar, etc.),
then process it (grind the beans, heat the water, mix everything together),
 and finally give some output (a cup of coffee).
 
 """


 # Scenario: An e-commerce system needs to calculate final price of products

# -------------------------------
# ❌ BAD PRACTICE: Repeating code
# -------------------------------

# Case 1
price = 1000       # oven
tax_rate = 0.25    # 25%
total_price = price + (price * tax_rate)   # logic / calcultion -> final price
print("Final Price:", total_price)


# Case 2 (same logic repeated)
price = 2000     # tv
tax_rate = 0.25
total_price = price + (price * tax_rate) # logic / calcultion -> final price
print("Final Price:", total_price)


# Case 3 (same logic repeated again)
price = 500     # t-shirt
tax_rate = 0.25
total_price = price + (price * tax_rate)  # logic / calcultion -> final price
print("Final Price:", total_price)



# ❗ Problem:
# - Code duplication
# - Hard to maintain
# - If tax rate changes, you must update everywhere



# ============================================================
# ✅ GOOD PRACTICE: Turn repeated logic into a FUNCTION
# ============================================================

def calculte_final_price(price):
    tax_rate = 0.25
    total_price = price + (price * tax_rate)  # logic / calcultion -> final price
    print("Final Price:", total_price)