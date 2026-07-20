# 🛠️ Space Explorer Game: Class Setup Guide

This guide explains how to create the three essential classes for your terminal-based space exploration game: `Spacecraft`, `Player`, and `Planet`.

---

## Gameplay Overview
Your player has a goal to explore all the planets in the system with their given spacecraft.  The player scores more points the more planets that they visit.  At the beginning, not all of the planets are discovered.  As the player visits more planets, they discover more planets to visit.

### The Planets
There are a variety of planets in this system.  Some of the planets are discovered, but many are not.  The planets have a number of resources and can be of varying danger levels.  Add some descriptive text to the planet to make them feel more alive.

### The Player
The player should keep track of which planets have been visited, how many credits they have, and have the ability to complete missions on the planet they're currently at.  The player can also purchase fuel for their spacecraft when they are on a planet.

### The Spacecraft
The spacecraft has a fuel level and a fuel efficiency.  When a player visits a planet, fuel efficiency has an impact on how much fuel is consumed to travel the distance between the two planets.

Bonus:  allow the player to choose a difficulty level that changes the spacecraft that they have.

---

## 🚀 Spacecraft Class

### Purpose:
Manages travel between planets, including tracking fuel and launching to destinations.

### Instructions:
1. Define a class named `Spacecraft` with an initializer that accepts:
   - `name`: the name of the spacecraft
   - `fuel_level`: current amount of fuel
   - `fuel_efficiency`: how far the ship can go per unit of fuel

2. Create methods to:
   - Add fuel
   - Calculate the fuel required for a given distance
   - Check if enough fuel is available to travel that distance
   - Launch the spacecraft and deduct fuel if successful

---

## 🪐 Planet Class

### Purpose:
Represents each planet in the game, including mission difficulty and reward potential.

### Instructions:
1. Define a class `Planet` with an initializer that sets:
   - `name`: planet’s name
   - `coordinates`: the x, y, z coordinates of the planet
   - `danger`: difficulty of completing missions  
   - `resources`: reward value
   - `atmosphere`: descriptive text

2. Override the `__str__` method to print a summary of the planet.
   
3. Override a built-in method to calculate the distance between two planets. (maybe `__sub__`?)

---

## 👨‍🚀 Player Class

### Purpose:
Keeps track of the player’s progress, including visited planets, credits, fuel purchases, and mission completion.

### Instructions:
1. Define a class `Player` with an initializer that accepts:
   - `name`: the player's name
   - Optional: `difficulty`: affects starting credits and spacecraft

2. Track the following attributes:
   - `current_planet`
   - `distance_traveled`
   - `visited_planets`
   - `score`
   - `credits`
   - `mission_rewards`

3. Add methods to:
   - Record visited planets and update distance and current planet
   - Buy fuel for the spacecraft using available credits
   - Calculate the player's score based off distance, credits, and mission rewards
   - Display a status summary

4. Create a method to simulate a mission on the current planet with varying outcomes:
   - Use danger level to calculate success chance
   - Return success, partial, or fail outcomes with appropriate reward values
   - Optional: limit the number of missions a player can do at a planet

---

## ✅ Next Steps

Once the classes are implemented:
- Use them in a main game loop to let the player explore planets
- Implement mechanics like unlocking new planets, choosing when to do missions, and managing fuel
- Some sample data is below:

```
Planets:
   Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
   Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
   Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
   Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
   Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
   Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
   Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
   Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
   Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
   Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")


Spacecraft:
   Spacecraft("Vostok 1", 250, 1.5)
   Spacecraft("Voyager 1", 400, 2.0)
   Spacecraft("Apollo 11", 600, 2.5)
```

### Other Thoughts
- How many times can a player do a mission at a single planet?
- What's the best way to tune / tweak these values?
- Implement a config file or data file to dynamically store / load data.