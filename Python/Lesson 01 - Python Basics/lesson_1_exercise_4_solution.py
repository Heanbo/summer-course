pizza_diameter = input("What is the diameter of the pizza? ")
pizza_diameter = float(pizza_diameter)

area = 3.14 * (pizza_diameter / 2) ** 2
print(area)

pizza_cost = input("What is the cost of the pizza? ")
pizza_cost = float(pizza_cost)
print(pizza_cost)

print(f"The cost per area is {pizza_cost / area:.02f}")