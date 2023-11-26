# --- > HEAD < ---

print("")
print("")
print("-----   Welcome to G I O LAB   -----")
print("")

print("------ Enter room data ------")
# Input ------> Room area
rwidth = float(input("Enter room width (m) : "))
rlong = float(input("Enter room long (m) :  "))
rheight = float(input("Enter room hight (m) : "))
print(".....")

# calculate room area
area_width = rwidth * rheight
area_heigh = rlong * rheight
width = area_width * 2
heigh = area_heigh * 2

tt_area = width + heigh  # tt ---> Total
print("| Room Area : ", tt_area, " square meter")
print("")

# Input -----> wall area
print("------ Enter wall area ------")
wall_width = float(input("Enter wall width (m) : "))
wall_heiggh = float(input("Enter wall hight (m) : "))
wall_price = int(input("Enter wall price : "))
print(".....")
print("")

# total wall area
wall_area = wall_width * wall_heiggh

#  calculate area and Wall
pieces = tt_area / wall_area

# calculate Price of wall
price = int(wall_price * pieces)

# Output
print("-- Total room area --")
print("| Total room area : ", tt_area)
print("-- Total wall for use --")
print("| Total pieces : ", pieces)
print("-- wall price --")
print("| Total price : ", price, " Baht")
