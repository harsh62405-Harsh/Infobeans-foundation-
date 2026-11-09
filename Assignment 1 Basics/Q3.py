# 3. How many tiles whose length and breadth are 13 cm and 7 cm respectively are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm? 

# Area of rectangle region 
length = 520
breadth = 140

# Area of tiles 
tile_length = 13
tile_breadth = 7 

# Area of Rectangle _region 
Area_tile_required = length * breadth
Area_of_tile = tile_length * tile_breadth

print("Area of tile required", Area_tile_required , "cm2")
print("Area of tile", Area_of_tile ,"cm2")

# To Find the total number of tile we have to divide the area of tile required and area of tile
total_number = Area_tile_required / Area_of_tile
print("Total no. of Tile Required in the given area = ",total_number)

      