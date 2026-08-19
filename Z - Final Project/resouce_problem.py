# You find the resource file, and you are somewhat surprised to see that the problem that needs to be solved deals with
# food.

# Here's some background information.  Martian colonists have simple joys — and pizza is one of them. Due to supply shortages, thin-atmosphere baking challenges, and incoming new colonists every meal must be optimized.

# You have been sent to Mars with three Automatrons that were designed specifically for making pizza.  The problem is
# that no one has taken the time to figure out which Automatron is most efficient (produces the most pizza with the least
# amount of dough).

# The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
# The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
# The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

# As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.  Once we avert total disaster and save all 1000 lives on board of the incoming shuttle,
# we will want to welcome them with some warm, Martian pizza after all.

# Write a Python Script to determine which of these are the best deal.  Use functions to calculate the areas of the pizzas.

# Once you have completed this, navigate to root directory to find Problem 3.

import math


def calculate_circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius**2)


# Pizza 1: 2 circular pizzas (15 inch diameter) that require 20 units of dough
def pizza1_efficiency():
    diameter = 15
    area = calculate_circle_area(diameter)
    total_area = area * 2
    dough_used = 20
    efficiency = total_area / dough_used
    return efficiency


print(f"Pizza 1 Efficiency: {pizza1_efficiency()} square inches per unit of dough")


# Pizza 2: equilateral triangle pizza, side length 20, that requires 20 units of dough
def calculate_triangle_area(side_length):
    return (math.sqrt(3) / 4) * (side_length**2)


def pizza2_efficiency():
    side_length = 20
    area = calculate_triangle_area(side_length)
    total_area = area
    dough_used = 20
    efficiency = total_area / dough_used
    return efficiency


print(f"Pizza 2 Efficiency: {pizza2_efficiency()} square inches per unit of dough")


# Pizza 3: square pizza with side length 18, that requires 18 units of dough
def calculate_square_area(side_length):
    return side_length**2


def pizza3_efficiency():
    side_length = 18
    area = calculate_square_area(side_length)
    total_area = area
    dough_used = 18
    efficiency = total_area / dough_used
    return efficiency


print(f"Pizza 3 Efficiency: {pizza3_efficiency()} square inches per unit of dough")
