# Q1. Electricity Bill Calculator — if-elif-else
# Write a Python program to calculate the electricity bill based on the number of units consumed.
# Use the following slab rates:
# Units	Rate
# First 100 units	₹5/unit
# Next 100 units	₹7/unit
# Next 200 units	₹10/unit
# Above 400 units	₹12/unit
# The program should accept the number of units from the user and calculate the total bill.
# Example:
# Enter units: 350
# Electricity Bill: ₹2700


unit = int(input("Enter the number of units consumed:-"))
bill = 0

if unit <= 100 :
    bill = unit * 5
    print(f"Electricity Bill is:- Rs{bill}")

elif unit <= 200 :
    bill = unit * 7
    print(f"Electricity Bill is:- Rs{bill}")

elif unit <= 400 :
    bill = unit * 10
    print(f"Electricity Bill is -: Rs{bill}")

else :
    bill = unit * 12
    print(f"Electricity Bill is -: Rs{bill}")