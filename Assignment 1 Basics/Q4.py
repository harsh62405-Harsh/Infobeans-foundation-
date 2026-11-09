#  Find the cost of tiling a rectangular plot of land 300 m long and 150 m wide at the rate of $6 per hundred square m. 

# Area of Plot
Long  = 300 
wide  = 150

# To find the cost of the tiling we have to find the area of the plot 
Area_of_plot = Long * wide

# now we get the area of the plot so now we Multply the area of plot into the range of tile pr 100 square m.
cost  = Area_of_plot * 6

# this is the cost for tile in 100 square m if we want the cost of per square m we have to divide with 100
Total_cost = cost / 100

print("Area of Plot =", Area_of_plot  , "m2")
print("Total cost of tiling = ", Total_cost ,"$")