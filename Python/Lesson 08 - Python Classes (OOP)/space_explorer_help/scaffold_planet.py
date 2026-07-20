import random

class Planet:
    def __init__(
        self,
        name: str,
        coordinates: tuple[float, float, float],
        danger: float,
        resources: float,
        atmosphere: str,
    ):
        # assign the arguments as instance variables (use self.whatever)
        # Maximum missions allowed: fewer for higher danger

    def __str__(self) -> str:
        # when you print out a planet object, what do you want it to look like?
        # return that string
        pass

    def __sub__(self, other) -> float:
        # calculate the distance between this planet object (self) and another planet object (other)
        pass

    def can_do_mission(self) -> bool:
        # can the player do anymore missions here?
        pass

    def record_mission(self, player_name: str) -> None:
        # record when a player has done missions here
        pass

    def mission_success(self) -> tuple[str, float]:
        # calculate a mission's outcome
        # should return a mission status and the number of resources gathered
        pass
