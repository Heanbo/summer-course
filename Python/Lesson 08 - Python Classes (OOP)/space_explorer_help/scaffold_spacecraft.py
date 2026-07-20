class Spacecraft:
    def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
        # store the arguments as instance variables
        pass

    def add_fuel(self, amount: float) -> None:
        # add fuel to the spacecraft's fuel stores
        pass

    def calculate_required_fuel(self, distance: float) -> float:
        # calculate the fuel needed to go a specific distance
        pass

    def check_fuel(self, distance: float) -> bool:
        # see if the current fuel level will go the specified distance
        pass

    def launch(self, distance: float) -> None:
        # handle a launch happening
        pass


if __name__ == "__main__":
    # run your tests here...