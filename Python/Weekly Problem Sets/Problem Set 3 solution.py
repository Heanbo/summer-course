# Problem Set 3 Solutions — Importing Modules
# Similar to previous problem sets, solutions are commented out.
# Uncomment the problem you're working on and run the script
# using `python path/to/script.py`

# You can comment/uncomment blocks of code by highlighting
# the lines and using 'Ctrl + /'

import random
import math
import turtle

########################
## Solution Problem 1 - Dice Roll Simulator
########################

def roll(sides):
    """Simulate rolling a single die with the given number of sides."""
    return random.randint(1, sides)

def roll_many(num_dice, sides):
    """Roll multiple dice and return a list of results."""
    results = []
    for _ in range(num_dice):
        results.append(roll(sides))
    return results

# Movement check (2d6)
print("=== MOVEMENT CHECK (2d6) ===")
movement_rolls = roll_many(2, 6)
print(f"Roll 1: {movement_rolls[0]}   Roll 2: {movement_rolls[1]}   Total: {sum(movement_rolls)}")
print()

# Attack check (1d20)
print("=== ATTACK CHECK (1d20) ===")
attack_roll = roll(20)
if attack_roll == 20:
    print(f"Roll: {attack_roll} — CRITICAL HIT!")
elif attack_roll == 1:
    print(f"Roll: {attack_roll} — CRITICAL MISS!")
else:
    print(f"Roll: {attack_roll}")
print()

# Damage roll (3d8)
print("=== DAMAGE ROLL (3d8) ===")
damage_rolls = roll_many(3, 8)
total = sum(damage_rolls)
average = total / len(damage_rolls)
print(f"Rolls: {damage_rolls}   Total: {total}   Average: {average:.1f}")
print()

# Simulation (1000 damage rolls)
print("=== SIMULATION (1000 damage rolls) ===")
total_damage_sum = 0
for _ in range(1000):
    damage = sum(roll_many(3, 8))
    total_damage_sum += damage

simulated_avg = total_damage_sum / 1000
theoretical_avg = 3 * 4.5  # Three d8s, each averaging 4.5
print(f"Simulated average total: {simulated_avg:.2f}")
print(f"Theoretical average:     {theoretical_avg}")

########################
## Solution Problem 1 - Challenge
########################

# # random.seed(42) ensures the same sequence of "random" numbers every time.
# # This is useful for testing, debugging, and reproducible simulations.
# # If you run the program twice with the same seed, you get identical results.
# random.seed(42)

# def roll(sides):
#     """Simulate rolling a single die with the given number of sides."""
#     return random.randint(1, sides)

# def roll_many(num_dice, sides):
#     """Roll multiple dice and return a list of results."""
#     results = []
#     for _ in range(num_dice):
#         results.append(roll(sides))
#     return results

# # Movement check (2d6)
# print("=== MOVEMENT CHECK (2d6) ===")
# movement_rolls = roll_many(2, 6)
# print(f"Roll 1: {movement_rolls[0]}   Roll 2: {movement_rolls[1]}   Total: {sum(movement_rolls)}")
# print()

# # Attack check (1d20)
# print("=== ATTACK CHECK (1d20) ===")
# attack_roll = roll(20)
# if attack_roll == 20:
#     print(f"Roll: {attack_roll} — CRITICAL HIT!")
# elif attack_roll == 1:
#     print(f"Roll: {attack_roll} — CRITICAL MISS!")
# else:
#     print(f"Roll: {attack_roll}")
# print()

# # Damage roll (3d8)
# print("=== DAMAGE ROLL (3d8) ===")
# damage_rolls = roll_many(3, 8)
# total = sum(damage_rolls)
# average = total / len(damage_rolls)
# print(f"Rolls: {damage_rolls}   Total: {total}   Average: {average:.1f}")
# print()

# # Battle quotes
# battle_quotes = [
#     "Victory favors the prepared!",
#     "Stand strong, soldiers!",
#     "For honor and glory!",
#     "Never give up, never surrender!",
#     "The battle is won before it's fought.",
#     "Courage conquers all things."
# ]

# print(f"\n{random.choice(battle_quotes)}")

########################
## Solution Problem 2 - Space Mission Calculator
########################

# def distance(x1, y1, x2, y2):
#     """Calculate the straight-line distance between two points."""
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# def orbit_circumference(radius):
#     """Calculate the circumference of a circular orbit."""
#     return 2 * math.pi * radius

# def fuel_needed(mass, velocity):
#     """Calculate kinetic energy rounded down to 2 decimal places."""
#     energy = 0.5 * mass * velocity ** 2
#     # Note: math.floor doesn't do what we want here for rounding to decimals
#     # But following the instruction literally:
#     return math.floor(energy * 100) / 100  # This would floor to 2 decimals
#     # Better approach would be: return round(energy, 2)

# # Mission data
# ship_pos = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371        # km (Earth's radius)
# ship_mass = 50000          # kg
# ship_velocity = 7800       # m/s

# # Calculate and print report
# print("=== NAVIGATION REPORT ===")
# dist = distance(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# print(f"Distance to station:    {dist:.2f} units")

# orbit_circ = orbit_circumference(orbit_radius)
# print(f"Orbit circumference:    {orbit_circ:.2f} km")

# energy = 0.5 * ship_mass * ship_velocity ** 2
# print(f"Kinetic energy (fuel):  {energy:.1f} J")

# log_velocity = math.log(ship_velocity, 10)
# print(f"Log10 of velocity:      {log_velocity:.2f}")

# # This represents the power of 10 needed to get the velocity
# # i.e., 10^3.89 ≈ 7800. It's a logarithmic scale of the velocity magnitude.

########################
## Solution Problem 2 - Challenge
########################

# def distance(x1, y1, x2, y2):
#     """Calculate the straight-line distance between two points."""
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# def orbit_circumference(radius):
#     """Calculate the circumference of a circular orbit."""
#     return 2 * math.pi * radius

# def bearing(x1, y1, x2, y2):
#     """Return the angle in degrees from one point to another."""
#     # atan2 returns radians, convert to degrees
#     angle_rad = math.atan2(y2 - y1, x2 - x1)
#     angle_deg = math.degrees(angle_rad)
#     return angle_deg

# # Mission data
# ship_pos = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371
# ship_mass = 50000
# ship_velocity = 7800

# print("=== NAVIGATION REPORT ===")
# dist = distance(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# print(f"Distance to station:    {dist:.2f} units")

# orbit_circ = orbit_circumference(orbit_radius)
# print(f"Orbit circumference:    {orbit_circ:.2f} km")

# energy = 0.5 * ship_mass * ship_velocity ** 2
# print(f"Kinetic energy (fuel):  {energy:.1f} J")

# log_velocity = math.log(ship_velocity, 10)
# print(f"Log10 of velocity:      {log_velocity:.2f}")

# # Bearing calculation
# bearing_angle = bearing(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# print(f"Bearing to station:     {bearing_angle:.2f} degrees")

# # Ceil vs Floor demonstration
# print(f"\nDistance ceiling:       {math.ceil(dist)}")  # Rounds up to next integer
# print(f"Distance floor:         {math.floor(dist)}")  # Rounds down to previous integer
# # ceil(902.35) = 903, floor(902.35) = 902

########################
## Solution Problem 3 - Animal Habitat Drawing
########################

# def draw_sun(t, x, y):
#     """Draw a yellow sun at the given position."""
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("yellow")
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()

# def draw_tree(t, x, y, height=80):
#     """Draw a tree with a brown trunk and green leaves."""
#     # Draw trunk
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("brown")
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(20)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
#     t.end_fill()

#     # Draw leaves
#     t.penup()
#     t.goto(x + 10, y + height)
#     t.pendown()
#     t.color("green")
#     t.begin_fill()
#     t.circle(30)
#     t.end_fill()

# def draw_pond(t, x, y):
#     """Draw a blue pond."""
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("blue")
#     t.begin_fill()
#     t.circle(60)
#     t.end_fill()

# def draw_grass(t):
#     """Draw a green grass strip along the bottom."""
#     t.penup()
#     t.goto(-400, -200)
#     t.pendown()
#     t.color("green")
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(800)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#     t.end_fill()

# # Setup
# screen = turtle.Screen()
# screen.bgcolor("sky blue")
# t = turtle.Turtle()
# t.speed(0)

# # Draw the scene
# draw_sun(t, -300, 200)
# draw_grass(t)
# draw_pond(t, 150, -150)

# # Draw 3 trees
# tree_positions = [-200, 0, 200]
# for x_pos in tree_positions:
#     draw_tree(t, x_pos, -100)

# t.hideturtle()
# turtle.done()

########################
## Solution Problem 3 - Challenge
########################

# def draw_sun(t, x, y):
#     """Draw a yellow sun at the given position."""
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("yellow")
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()

# def draw_tree(t, x, y, height=80):
#     """Draw a tree with a brown trunk and green leaves."""
#     # Draw trunk
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("brown")
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(20)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
#     t.end_fill()

#     # Draw leaves
#     t.penup()
#     t.goto(x + 10, y + height)
#     t.pendown()
#     t.color("green")
#     t.begin_fill()
#     t.circle(30)
#     t.end_fill()

# def draw_pond(t, x, y):
#     """Draw a blue pond."""
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.color("blue")
#     t.begin_fill()
#     t.circle(60)
#     t.end_fill()

# def draw_grass(t):
#     """Draw a green grass strip along the bottom."""
#     t.penup()
#     t.goto(-400, -200)
#     t.pendown()
#     t.color("green")
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(800)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#     t.end_fill()

# # Setup
# screen = turtle.Screen()
# screen.bgcolor("sky blue")
# t = turtle.Turtle()
# t.speed(0)

# # Draw the scene
# draw_sun(t, -300, 200)
# draw_grass(t)
# draw_pond(t, 150, -150)

# # Draw 10 trees at random positions with random heights
# for _ in range(10):
#     # Clamp x position to keep trees on screen (-350 to 350)
#     x_pos = random.randint(-350, 350)
#     height = random.randint(40, 100)
#     draw_tree(t, x_pos, -100, height)

# t.hideturtle()
# turtle.done()

########################
## Solution Problem 4 - Animal Guessing Game
########################

# print("=== ANIMAL GUESSING GAME ===")
# print("A secret animal is waiting...")
# print()

# secret = random.randint(1, 100)
# num_guesses = 0

# while True:
#     guess = int(input("Guess a number (1-100): "))
#     num_guesses += 1

#     if guess == secret:
#         print(f"CORRECT! The secret animal was: narwhal")
#         print(f"You guessed it in {num_guesses} tries.")

#         # Calculate theoretical minimum guesses
#         min_guesses = math.ceil(math.log2(100))
#         print(f"Minimum possible guesses (optimal): {min_guesses}")
#         # This is the minimum guesses needed with optimal binary search strategy
#         # log2(100) ≈ 6.64, so ceil(6.64) = 7 guesses minimum
#         break

#     # Give hint based on distance
#     distance = math.fabs(guess - secret)

#     if distance > 40:
#         print("Hint: ICE COLD")
#     elif distance > 20:
#         print("Hint: COLD")
#     elif distance > 10:
#         print("Hint: WARM")
#     else:
#         print("Hint: HOT!")
#     print()

########################
## Solution Problem 4 - Challenge
########################

# print("=== ANIMAL GUESSING GAME ===")
# print("A secret animal is waiting...")
# print()

# secret = random.randint(1, 100)
# num_guesses = 0
# all_guesses = []  # Track all guesses

# while True:
#     guess = int(input("Guess a number (1-100): "))
#     num_guesses += 1
#     all_guesses.append(guess)

#     if guess == secret:
#         print(f"CORRECT! The secret animal was: narwhal")
#         print(f"You guessed it in {num_guesses} tries.")

#         # Calculate theoretical minimum guesses
#         min_guesses = math.ceil(math.log2(100))
#         print(f"Minimum possible guesses (optimal): {min_guesses}")

#         # Calculate mean guess
#         sum_guesses = math.fsum(all_guesses)  # High-precision sum
#         mean_guess = sum_guesses / len(all_guesses)
#         print(f"Mean of your guesses: {mean_guess:.2f}")
#         break

#     # Give hint based on distance
#     distance = math.fabs(guess - secret)

#     if distance > 40:
#         print("Hint: ICE COLD")
#     elif distance > 20:
#         print("Hint: COLD")
#     elif distance > 10:
#         print("Hint: WARM")
#     else:
#         print("Hint: HOT!")
#     print()

########################
## Solution Problem 5 - Square Spiral
########################

# laps = int(input("How many times around the square? "))

# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)

# side_length = 10
# total_sides = laps * 4

# for _ in range(total_sides):
#     t.forward(side_length)
#     t.right(90)
#     side_length += 5

# t.hideturtle()
# turtle.done()

########################
## Solution Problem 5 - Challenge
########################

# laps = int(input("How many times around the square? "))
# color_mode = input("Color mode (rainbow/blue/red/green): ")

# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)

# side_length = 10
# total_sides = laps * 4

# # Color options for rainbow mode
# rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# for i in range(total_sides):
#     # Set color based on mode
#     if color_mode == "rainbow":
#         # Cycle through rainbow colors using modulo
#         t.color(rainbow_colors[i % len(rainbow_colors)])
#     else:
#         # Use the specified color
#         t.color(color_mode)

#     t.forward(side_length)
#     t.right(90)
#     side_length += 5

# t.hideturtle()
# turtle.done()
