import os
import random


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def choose_difficulty():
    while True:
        level = input("Choose difficulty (Easy, Medium, Hard): ").capitalize()
        if level in ["Easy", "Medium", "Hard"]:
            return level
        print("Invalid choice. Please enter Easy, Medium, or Hard.")


def setup_spacecraft(difficulty):
    if difficulty == "Easy":
        return {"name": "Apollo 11", "fuel_level": 600, "fuel_efficiency": 2.5}
    elif difficulty == "Medium":
        return {"name": "Voyager 1", "fuel_level": 400, "fuel_efficiency": 2.0}
    else:
        return {"name": "Vostok 1", "fuel_level": 250, "fuel_efficiency": 1.5}


def create_planets():
    # Each planet is a dict
    return [
        {
            "name": "Earth",
            "coordinates": (149.6, 0.0, 0.0),
            "danger": 0,
            "resources": 0,
            "atmosphere": "Earth-like",
        },
        {
            "name": "Mars",
            "coordinates": (227.9, 0.0, 1.0),
            "danger": 1,
            "resources": 20,
            "atmosphere": "Thin",
        },
        {
            "name": "Jupiter",
            "coordinates": (778.5, 50.0, 12.0),
            "danger": 3,
            "resources": 40,
            "atmosphere": "Gas Giant",
        },
        {
            "name": "Saturn",
            "coordinates": (1434.0, -80.0, -20.0),
            "danger": 2,
            "resources": 35,
            "atmosphere": "Gas Giant",
        },
        {
            "name": "Uranus",
            "coordinates": (2871.0, 30.0, 40.0),
            "danger": 2,
            "resources": 45,
            "atmosphere": "Icy",
        },
        {
            "name": "Neptune",
            "coordinates": (4495.0, -25.0, 70.0),
            "danger": 4,
            "resources": 50,
            "atmosphere": "Icy",
        },
        {
            "name": "Pluto",
            "coordinates": (5906.0, 120.0, -90.0),
            "danger": 5,
            "resources": 60,
            "atmosphere": "Frozen",
        },
        {
            "name": "Eris",
            "coordinates": (10100.0, 200.0, -130.0),
            "danger": 4,
            "resources": 55,
            "atmosphere": "Frozen",
        },
        {
            "name": "Kepler-22b",
            "coordinates": (600000.0, 0.0, 0.0),
            "danger": 3,
            "resources": 70,
            "atmosphere": "Earth-like",
        },
        {
            "name": "Proxima b",
            "coordinates": (402080.0, 30.0, 10.0),
            "danger": 5,
            "resources": 80,
            "atmosphere": "Unknown",
        },
    ]


def planet_str(planet):
    return (
        f"{planet['name']} - Coordinates: ({planet['coordinates'][0]}, {planet['coordinates'][1]}, {planet['coordinates'][2]}), "
        f"Danger: {planet['danger']}, Resources: {planet['resources']}, Atmosphere: {planet['atmosphere']}"
    )


def planet_distance(p1, p2):
    diff = tuple(x - y for x, y in zip(p1["coordinates"], p2["coordinates"]))
    return (diff[0] ** 2 + diff[1] ** 2 + diff[2] ** 2) ** 0.5


def max_missions(planet):
    if planet["name"] == "Earth":
        return 0
    return max(1, 4 - int(planet["danger"]))


def can_do_mission(planet, player_name, planet_missions):
    return planet_missions.get((planet["name"], player_name), 0) < max_missions(planet)


def record_mission(planet, player_name, planet_missions):
    key = (planet["name"], player_name)
    planet_missions[key] = planet_missions.get(key, 0) + 1


def mission_success(planet):
    chance = max(0.2, 1.0 - 0.15 * planet["danger"])
    roll = random.random()
    if roll < chance:
        return "success", planet["resources"]
    elif roll < chance + 0.2:
        return "partial", planet["resources"] // 2
    else:
        return "fail", 0


def buy_fuel(player, spacecraft, price_per_unit=2.0):
    print(f"You have {player['credits']} credits.")
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
    elif player["credits"] >= cost:
        spacecraft["fuel_level"] += amount * 1000
        player["credits"] -= cost
        print(f"Purchased {amount} units of fuel.")
    else:
        print("Not enough credits.")


def complete_mission(player, planet, planet_missions):
    if not can_do_mission(planet, player["name"], planet_missions):
        print(f"No more missions can be done at {planet['name']}.")
        return
    outcome, reward = mission_success(planet)
    record_mission(planet, player["name"], planet_missions)
    print(f"Mission outcome: {outcome}. Earned {reward} credits.")
    if outcome == "fail":
        penalty = 5 + int(planet["danger"] * 5)
        player["credits"] = max(0, player["credits"] - penalty)
        print(f"Mission failed! Lost {penalty} credits as penalty.")
    else:
        player["credits"] += reward
        player["mission_rewards"] += reward


def player_status(player):
    visited = ", ".join([p for p in player["visited_planets"]])
    score = (
        len(player["visited_planets"]) * 10
        + player["credits"]
        + player["mission_rewards"] * 10
    )
    return (
        f"Captain: {player['name']}\n"
        f"Distance traveled: {player['distance_traveled']:.2f} units\n"
        f"Visited planets: {visited}\n"
        f"Mission rewards: {player['mission_rewards']}\n"
        f"Credits: {player['credits']}\n"
        f"Score: {score}\n"
    )


def main():
    print("=== Welcome to the Space Explorer Game ===")
    player_name = input("Enter your name, Captain: ")
    difficulty = ""
    while not difficulty:
        difficulty = choose_difficulty()
    all_planets = create_planets()

    spacecraft = setup_spacecraft(difficulty)
    credits_start = {"Easy": 100, "Medium": 50, "Hard": 20}[difficulty]
    player = {
        "name": player_name,
        "current_planet": all_planets[0],
        "distance_traveled": 0,
        "visited_planets": set([all_planets[0]["name"]]),
        "credits": credits_start,
        "mission_rewards": 0,
    }
    planet_missions = {}

    shuffled_planets = all_planets[1:]
    random.shuffle(shuffled_planets)
    visible_planets = shuffled_planets[:2]
    not_visible_planets = shuffled_planets[2:]

    while not_visible_planets or visible_planets:
        clear_screen()
        print(f"Captain: {player['name']}")
        print(
            f"Fuel: {spacecraft['fuel_level']:.2f} units | Credits: {player['credits']}"
        )
        print(f"Current planet: {player['current_planet']['name']}")
        print("\nAvailable planets to travel to:")
        for idx, planet in enumerate(visible_planets, 1):
            print(f"{idx}. {planet_str(planet)}")

        print("\nWhat would you like to do?")
        print("1. Travel to a planet")
        print("2. Buy fuel")
        print("3. Start mission on current planet")
        print("4. End mission.")
        action = input("Enter the number of your choice: ")

        if action == "1":
            if not visible_planets:
                print("No planets available to travel to.")
                input("Press Enter to continue...")
                continue
            try:
                choice = int(input("Choose a planet to travel to by number: ")) - 1
                if not (0 <= choice < len(visible_planets)):
                    raise ValueError
            except ValueError:
                print("Invalid selection.")
                input("Press Enter to continue...")
                continue

            destination = visible_planets.pop(choice)
            distance = planet_distance(destination, player["current_planet"])
            required_fuel = distance / spacecraft["fuel_efficiency"]

            if spacecraft["fuel_level"] < required_fuel:
                visible_planets.append(destination)
                print("Not enough fuel to travel. Try buying more.")
                input("Press Enter to continue...")
            else:
                spacecraft["fuel_level"] -= required_fuel
                print(
                    f"{spacecraft['name']} has successfully traveled {distance:.2f} units!"
                )
                player["visited_planets"].add(destination["name"])
                player["distance_traveled"] += abs(distance)
                player["current_planet"] = destination
                # Reveal two more planets if possible
                if not_visible_planets:
                    visible_planets.append(not_visible_planets.pop(0))
                if not_visible_planets:
                    visible_planets.append(not_visible_planets.pop(0))
                input("Press Enter to continue...")
        elif action == "2":
            buy_fuel(player, spacecraft)
            input("Press Enter to continue...")
        elif action == "3":
            complete_mission(player, player["current_planet"], planet_missions)
            input("Press Enter to continue...")
        elif action == "4":
            break
        else:
            print("Invalid action. Please choose 1, 2, 3, or 4.")
            input("Press Enter to continue...")

    clear_screen()
    print("\n=== Mission Summary ===")
    print(player_status(player))


if __name__ == "__main__":
    main()
