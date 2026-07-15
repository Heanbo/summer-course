# Another Comment
# Lesson One Area Cost Solution File
# prompt user for value
diameter_str = input("Please enter the diameter: ")

# convert to float
diameter_float = float(diameter_str)

# area = pi * r ** 2
area_float = 3.14 * (diameter_float / 2) ** 2

print("The area is " + str(area_float))

price_str = input("Please enter the cost: $")
price_float = float(price_str)

# cost per area = cost / area
cost_per_area = price_float / area_float

print("The cost per area is " + str(cost_per_area))
