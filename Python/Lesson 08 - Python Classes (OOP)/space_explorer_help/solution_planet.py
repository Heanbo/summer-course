import random
from solution_spacecraft import Spacecraft

class Planet:
    def __init__(
        self,
        name: str,
        coordinates: tuple[float, float, float],
        danger: float,
        resources: float,
        atmosphere: str,
    ):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
        # Maximum missions allowed: fewer for higher danger
        self.max_missions = max(1, 4 - int(self.danger))
        self.missions_done: dict[str, int] = {}

    def __str__(self) -> str:
        return (
            f"{self.name} - Coordinates: ({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]}), "
            f"Danger: {self.danger}, Resources: {self.resources}, Atmosphere: {self.atmosphere}"
        )

    def __sub__(self, other) -> float:
        diff = tuple(coord_1 - coord_2 for coord_1, coord_2 in zip(self.coordinates, other.coordinates))
        return (diff[0] ** 2 + diff[1] ** 2 + diff[2] ** 2) ** 0.5

    def can_do_mission(self, player_name: str) -> bool:
        return self.missions_done.get(player_name, 0) < self.max_missions

    def record_mission(self, player_name: str) -> None:
        self.missions_done[player_name] = self.missions_done.get(player_name, 0) + 1

    def mission_success(self) -> tuple[str, float]:
        chance = max(0.2, 1.0 - 0.15 * self.danger)
        roll = random.random()
        if roll < chance:
            return "success", self.resources
        elif roll < chance + 0.2:
            return "partial", self.resources // 2
        else:
            return "fail", 0


if __name__ == "__main__":
    test_planet = Planet("Test World", (1, 2, 3), 5, 100, "A spooky world in the orbit of Nimbus I")
    second_planet = Planet("Second World", (3, 4, 5), 4, 200, "A not so spooky world in the orbit of Nimbus I")
    print(test_planet)
    print(test_planet - second_planet)
    
    test_craft = Spacecraft("Testing", 1000, 0.50)  # new spacecraft
    print(test_craft.calculate_required_fuel(test_planet - second_planet))  # should be 200