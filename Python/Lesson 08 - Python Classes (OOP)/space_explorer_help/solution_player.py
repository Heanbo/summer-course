from solution_planet import Planet
from solution_spacecraft import Spacecraft


class Player:
    def __init__(self, name: str, starting_planet: Planet, difficulty: str = "Medium"):
        self.name = name
        self.current_planet = starting_planet
        self.distance_traveled = 0
        self.visited_planets = set([starting_planet])
        self.credits = {"Easy": 100, "Medium": 50, "Hard": 20}.get(difficulty, 50)
        self.mission_rewards = 0

    def visit_planet(self, planet: Planet) -> None:
        self.visited_planets.add(planet)
        self.distance_traveled += abs(self.current_planet - planet)
        self.current_planet = planet

    def buy_fuel(self, spacecraft: Spacecraft, price_per_unit: float = 2.0) -> None:
        print(f"You have {self.credits} credits.")
        try:
            amount = float(
                input(
                    f"Enter fuel amount to buy in kilounits (price: {price_per_unit}/kilounit): "
                )
            )
        except ValueError:
            print("Invalid input.")
            return
        cost = amount * price_per_unit
        if cost < 0:
            print("Stop tryin' to cheat.")
        elif self.credits >= cost:
            spacecraft.add_fuel(amount * 1000)
            self.credits -= cost
            print(f"Purchased {amount} units of fuel.")
        else:
            print("Not enough credits.")

    def complete_mission(self, planet: Planet) -> None:
        if not planet.can_do_mission(self.name):
            print(f"No more missions can be done at {planet.name}.")
            return
        outcome, reward = planet.mission_success()
        planet.record_mission(self.name)
        print(f"Mission outcome: {outcome}. Earned {reward} credits.")
        if outcome == "fail":
            penalty = 5 + int(planet.danger * 5)
            self.credits = max(0, self.credits - penalty)
            print(f"Mission failed! Lost {penalty} credits as penalty.")
        else:
            self.credits += reward
            self.mission_rewards += reward

    @property
    def score(self) -> float:
        return len(self.visited_planets) * 10 + self.credits + self.mission_rewards * 10

    def status(self) -> str:
        visited = ", ".join([p.name for p in self.visited_planets])
        return (
            f"Captain: {self.name}\n"
            f"Distance traveled: {self.distance_traveled:.2f} units\n"
            f"Visited planets: {visited}\n"
            f"Mission rewards: {self.mission_rewards}\n"
            f"Credits: {self.credits}\n"
            f"Score: {self.score}\n"
        )
