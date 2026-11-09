# 5. If it costs 1600 rs. to fence a rectangular park of length 20 m at the rate of 25 rs. per m², find the breadth of the park and its perimeter. Also, find the area of the field. 

# Given Data 
Cost_of_fencing = 1600
length = 20
rate_per_m2 = 25

# To find the breadth of the park we have to find the area of the park
Area = Cost_of_fencing / rate_per_m2 
print("Area of the Park = ", Area , "m2")

# Now we have to find the breadth of the park
breadth  = Area / length
print("Breadth of the Park =", breadth , "m")

# Now at the last We have to Calculate the perimeter of the park
peri = 2 * (length * breadth)
print("Perimeter of the Park =", peri , "m")




