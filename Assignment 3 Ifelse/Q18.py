# 18. Write a Python program to input electricity unit charges and calculate total electricity bill according to the given condition: For first 50 units Rs. 0.50/unit For next 100 units Rs. 0.75/unit For next 100 units Rs. 1.20/unit For unit above 250 Rs. 1.50/unit An additional surcharge of 20% is added to the bill. 

electricity_unit = int(input("Enter electricity unit :"))
if electricity_unit <= 50 :
  bill = electricity_unit*0.50
elif electricity_unit <= 150 :
  bill = 50*0.50 + ((electricity_unit-50)*0.75)
elif electricity_unit <= 250 :
  bill = 50*0.50 + 100*0.75 + ((electricity_unit-150)*1.20)
else :
  bill = 50*0.50 + 100*0.75 + 100*1.20 +((electricity_unit-250)*1.50)

bill = bill + 0.20*bill
print(f"electricity bill is :{bill:.2f}")