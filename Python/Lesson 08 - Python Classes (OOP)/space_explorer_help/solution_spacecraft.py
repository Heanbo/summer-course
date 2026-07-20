class Spacecraft:
    def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, amount: float) -> None:
        self.fuel_level += amount

    def calculate_required_fuel(self, distance: float) -> float:
        return distance / self.fuel_efficiency

    def check_fuel(self, distance: float) -> bool:
        return self.fuel_level >= self.calculate_required_fuel(distance)

    def launch(self, distance: float) -> None:
        if self.check_fuel(distance):
            self.fuel_level -= self.calculate_required_fuel(distance)
            print(f"{self.name} has successfully traveled {distance} units!")
        else:
            print(f"{self.name} does not have enough fuel to travel {distance} units.")

if __name__ == "__main__":
    test_craft = Spacecraft("Testing", 1000, 0.50)  # new spacecraft
    print(test_craft.calculate_required_fuel(100))  # should be 200
    print(test_craft.check_fuel(1000))              # should be false
    test_craft.launch(500)                          # should work
    print(test_craft.fuel_level)                    # should be 0

if __name__ == "__main__":
    test_craft = Spacecraft("Testing", 1000, 0.50)  # new spacecraft
    print(test_craft.calculate_required_fuel(100))  # should be 200
    print(test_craft.check_fuel(1000))              # should be false
    test_craft.launch(500)                          # should work
    print(test_craft.fuel_level)                    # should be 0