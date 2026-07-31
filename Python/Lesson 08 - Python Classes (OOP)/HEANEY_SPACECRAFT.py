#### BEGIN #####

### IMPORT ###
import math
import os

#### BLANK VARIBALE ####



### CLASSES ###
class spacecraft():
    def __init__(self, ship_name:str, fuel_efficiency:float=0.1, fuel_level=25, max_fuel=1005, ship_x=0, ship_y=0, ship_z=0):
        self.name = ship_name
        self.fuel_efficiency = fuel_efficiency
        self.fuel_level = fuel_level
        self.max_fuel = max_fuel
        self.ship_x = ship_x
        self.ship_y = ship_y
        self.ship_z = ship_z



    def fuel_up(self, amount:float):
        if self.fuel_level + amount > self.max_fuel:
            print("That would exceed the capacitiy of your tank!")
        else:
            self.fuel_level += amount
            print(f"{self.name} now has {self.fuel_level} fuel. ")

    def fly_to(self, planet):
        distance = math.sqrt((planet.planet_x - self.ship_x)**2 + (planet.planet_y - self.ship_y)**2 +(planet.planet_z - self.ship_z)**2)
        print(f"{distance} KMs to {planet.name}")
        if self.fuel_efficiency * self.fuel_level < distance:
            print(f"You do not have enough fuel to get there!")
        else:
            print(f"You traveled to {planet.name}")
            self.fuel_level -= distance / self.fuel_efficiency
            print(f"You have {self.fuel_level} Liters of Fuel remaining...")
            self.ship_x = planet.planet_x
            self.ship_y = planet.planet_y
            self.ship_z = planet.planet_z
            print(f"You are now at ({self.ship_x}, {self.ship_y})")

### Functions ###
def first_banner():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("=     ROCKET MAN    =")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print(f"|                o  |")
    print(f"|    ^              |")
    print(f"|   |||             |")
    print(f'|  / | \            |')
    print()

def banner():
    os.system('cls')
    print("=-=-=-=-=-=-=-=-=-=-=")
    print(f"=     ROCKET MAN    =      Coord: {usership.ship_x}, {usership.ship_y}, {usership.ship_z}")
    print("=-=-=-=-=-=-=-=-=-=-=")
    print(f"|                o  |      SHIP: {usership.name}")
    print(f"|    ^              |")
    print(f"|   |||             |      FUEL: {usership.fuel_level} / {usership.max_fuel} Liters")
    print(f'|  / | \            |      KM TO EMPTY: {usership.fuel_level * usership.fuel_efficiency}')
    print(f"|                   |")
    print("--------------------------------------------------------------------")


def actioner():
    userinput = ()
    while userinput != "leave":
        banner()
        userinput = input(f"Computer > What would you like to do? <stats> <leave> <fly> <refuel>\n{username} > ")
        if userinput == 'stats':
            print(f"{usership.name} is currently at the coordinate ({usership.ship_x},{usership.ship_y},{usership.ship_z})")
            print(f"{usership.fuel_level} Liters of Fuel and can travel {usership.fuel_level * usership.fuel_efficiency} Kilometers")
        if userinput == 'refuel':
            userfuelamount = int(input(f"Computer > How much fuel would you like to add?\n{username} > "))
            usership.fuel_up(userfuelamount)
        #print(f"Your ship's name is {usership.name}")

### Planet ###
class planet():
    def __init__(self, planet_name:str, planet_x:int, planet_y:int, planet_z:int, danger=0, resources=100, atmosphere="Clear Skies"):
        self.name = planet_name
        self.planet_x = planet_x
        self.planet_y = planet_y
        self.planet_z = planet_z
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self) -> str:
        return (
            f"{self.name} - Coordinates: ({self.planet_x}, {self.planet_y}, {self.planet_z}), "
            f"Danger: {self.danger}, Resources: {self.resources}, Atmosphere: {self.atmosphere}"
        )

    def planet_to_planet_distance(self,target):
        distance = math.sqrt ((self.planet_x - target.planet_x)**2 + (self.planet_y - target.planet_y)**2 + (self.planet_z - target.planet_z)**2)
        print(distance)

### DEFINE OBJECTS ###
mars = planet('mars', 10, 10, 10)
pluto = planet('Pluto', 30, 30 , 30)
ringo = spacecraft('ringo')


### EXECUTION ###
first_banner()
username = input(f"Computer > What is your name?\nYou > ")
name = input(f"Computer > Name your Spaceship!\n{username} > ")
usership = spacecraft(f'{name}')
banner()
actioner()
first_banner()
print("Computer > Goodbye.")
#ringo.fuel_up(10)
#ringo.fly_to(mars)
#print(mars)
#mars.planet_to_planet_distance(pluto)

