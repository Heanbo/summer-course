import os
from solution_spacecraft import Spacecraft
from solution_planet import Planet
from solution_player import Player
import random


def choose_difficulty() -> str | None:
    while True:
        level = input("Choose difficulty (Easy, Medium, Hard): ").capitalize()
        if level in ["Easy", "Medium", "Hard"]:
            return level
        print("Invalid choice. Please enter Easy, Medium, or Hard.")


def setup_spacecraft(difficulty: str) -> Spacecraft:
    if difficulty == "Easy":
        return Spacecraft("Apollo 11", 600, 2.5)
    elif difficulty == "Medium":
        return Spacecraft("Voyager 1", 400, 2.0)
    else:
        return Spacecraft("Vostok 1", 250, 1.5)


def create_planets() -> list[Planet]:
    return [
        Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
        Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
        Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
        Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
        Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
        Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
        Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
        Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
        Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
        Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
    ]


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("=== Welcome to the Space Explorer Game ===")
    player_name = input("Enter your name, Captain: ")
    difficulty = ""
    while not difficulty:
        difficulty = choose_difficulty()
    all_planets = create_planets()

    spacecraft = setup_spacecraft(difficulty)
    current_planet = all_planets[0] # Start at Earth
    player = Player(player_name, current_planet, difficulty)

    shuffled_planets = all_planets[1:]
    random.shuffle(shuffled_planets)
    visible_planets = shuffled_planets[:2]
    not_visible_planets = shuffled_planets[2:]

    while not_visible_planets:
        clear_screen()
        print(f"Captain: {player.name}")
        print(f"Fuel: {spacecraft.fuel_level:.2f} units | Credits: {player.credits}")
        print(f"Current planet: {current_planet.name}")
        print("\nAvailable planets to travel to:")
        for idx, planet in enumerate(visible_planets, 1):
            print(f"{idx}. {planet}")

        print("\nWhat would you like to do?")
        print("1. Travel to a planet")
        print("2. Buy fuel")
        print("3. Start mission on current planet")
        print("4. End mission.")
        action = input("Enter the number of your choice: ")

        if action == "1":
            try:
                choice = int(input("Choose a planet to travel to by number: ")) - 1
                if not (0 <= choice < len(visible_planets)):
                    raise ValueError
            except ValueError:
                print("Invalid selection.")
                input("Press Enter to continue...")
                continue

            destination = visible_planets.pop(choice)
            distance = destination - current_planet

            if not spacecraft.check_fuel(distance):
                print("Not enough fuel to travel. Try buying more.")
                input("Press Enter to continue...")
                visible_planets.insert(choice, destination)
            else:
                spacecraft.launch(distance)
                player.visit_planet(destination)
                player.complete_mission(destination)
                current_planet = destination
                # Reveal two more planets if possible
                if not_visible_planets:
                    visible_planets.append(not_visible_planets.pop(0))
                if not_visible_planets:
                    visible_planets.append(not_visible_planets.pop(0))
        elif action == "2":
            player.buy_fuel(spacecraft)
            input("Press Enter to continue...")
        elif action == "3":
            player.complete_mission(current_planet)
            input("Press Enter to continue...")
        elif action == "4":
            break
        else:
            print("Invalid action. Please choose 1, 2, or 3.")
            input("Press Enter to continue...")

    clear_screen()
    print("\n=== Mission Summary ===")
    print(player.status())


if __name__ == "__main__":
    main()
