from scaffold_planet import Planet
from scaffold_spacecraft import Spacecraft


class Player:
    def __init__(self, name: str, starting_planet: Planet, difficulty: str = "Medium"):
        # store arguments as instance variables

        # keep track of other metrics such as credits, distance traveled, and mission rewards
        pass
        

    def visit_planet(self, planet: Planet) -> None:
        # update the player's variables when they move to a new planet
        pass

    def buy_fuel(self, spacecraft: Spacecraft, price_per_unit: float = 2.0) -> None:
        # handle the player buying fuel for their spacecraft
        pass

    def complete_mission(self, planet: Planet) -> None:
        # attempt to do a mission
        pass

    @property
    def score(self) -> float:
        # return the player's score

    def status(self) -> str:
        # return the game stats for display later
        pass