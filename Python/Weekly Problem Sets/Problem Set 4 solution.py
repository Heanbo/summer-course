"""Problem Set 4 — Problem 1 solution
Soldier Roster & Dispatch System
This script parses a list of raw personnel report strings, builds a roster
dictionary, prints summary information, and implements a `dispatch` function
that updates a soldier's status from "available" to "deployed".
The demonstration code is wrapped in an `if __name__ == "__main__":` block
so autograders can import the functions without executing the demo.
"""


def process_reports(report_list: list[str]) -> tuple:
    roster = {}
    ranks = set()
    for report in report_list:
        parts = []
        for part in report.split("|"):
            parts.append(part.strip())

        # Expecting format: NAME | Rank | Fitness:NN | Status:state
        name = parts[0].title()
        rank = parts[1].upper()

        # Parse fitness and status fields
        fitness_field = int(parts[2].split(":", 1)[1].strip())
        status_field = parts[3].split(":", 1)[1].strip().lower()

        roster[name] = {
            "rank": rank,
            "fitness": int(fitness_field),
            "deployed": status_field == "deployed",
        }

        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, dict[str, object]]) -> None:
    available_soldiers = []

    for name, info in roster.items():
        if not info.get("deployed", False):
            available_soldiers.append(name)

    available_soldiers.sort()
    print(f"Available soldiers: {available_soldiers}\n")


def dispatch(roster: dict[str, dict[str, object]], name: str) -> None:
    """Set a soldier's status to 'deployed' if available.
    Prints an informative message when the soldier is deployed, already
    deployed, or not found.
    """
    display_name = name.title()
    print(f"Dispatching {display_name}...", end=" ")

    soldier = roster.get(display_name)
    if soldier is None:
        print(f"{display_name} not found in roster.")
        return

    if not soldier.get("deployed", False):
        soldier["deployed"] = True
        print("Done. Status set to deployed.")
    else:
        print(f"{display_name} is already deployed.")


def fitness_report(roster: dict[str, dict[str, object]]) -> dict[str, list[str]]:
    bands = {"high": [], "medium": [], "low": []}

    for name, info in roster.items():
        fitness_level = info.get("fitness", 0)
        if fitness_level >= 80:
            bands["high"].append(name)
        elif 60 <= fitness_level <= 79:
            bands["medium"].append(name)
        else:
            bands["low"].append(name)

    for level in bands.values():
        level.sort()

    return bands


# ── Problem 2 ─────────────────────────────────────────────────────────────────

def can_make(recipe_ingredients: list[str], pantry_set: set[str]) -> bool:
    for ingredient in recipe_ingredients:
        if ingredient not in pantry_set:
            return False
    return True


def missing_ingredients(recipe_ingredients: list[str], pantry_set: set[str]) -> list[str]:
    missing = []
    for ingredient in recipe_ingredients:
        if ingredient not in pantry_set:
            missing.append(ingredient)
    missing.sort()
    return missing


def check_recipes(recipes: dict[str, list[str]], pantry_set: set[str]) -> None:
    print("=== RECIPE CHECKER ===")

    all_ingredients = set()

    for recipe_name, ingredients in recipes.items():
        for ingredient in ingredients:
            all_ingredients.add(ingredient)

        if can_make(ingredients, pantry_set):
            print(f"{recipe_name:<14}: CAN MAKE ✓")
        else:
            missing = missing_ingredients(ingredients, pantry_set)
            print(f"{recipe_name:<14}: MISSING — {missing}")

    unique = list(all_ingredients)
    unique.sort()
    print(f"\nAll unique ingredients ({len(unique)}): {unique}")


def add_ingredients(pantry_set: set[str], extra_ingredients: list[str]) -> set[str]:
    for ingredient in extra_ingredients:
        pantry_set.add(ingredient)
    return pantry_set


if __name__ == "__main__":
    TESTING_PROBLEM = 1

    if TESTING_PROBLEM == 1:
        reports = [
            "SANTOS | Private | Fitness:91 | Status:available",
            "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
            "OKAFOR | Sergeant | Fitness:88 | Status:available",
            "BRIGGS | Private | Fitness:55 | Status:available",
            "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
            "REYES | Sergeant | Fitness:79 | Status:available",
        ]

        roster, ranks = process_reports(reports)

        print("=== ROSTER LOADED ===")
        print(f"{len(roster)} soldiers on record.")
        print(f"Ranks on file: {ranks}\n")

        show_available(roster)

        dispatch(roster, "Santos")
        dispatch(roster, "Kowalski")
        print("\nUpdated status:")
        for name in ["Santos", "Kowalski"]:
            info = roster.get(name.title())
            status = "deployed" if info.get("deployed") else "available"
            print(f"  {name:8}: {status}")

        print("\nFitness report:")
        report = fitness_report(roster)
        for band in ("high", "medium", "low"):
            print(f"  {band.title():6}: {report[band]}")

    elif TESTING_PROBLEM == 2:
        recipes = {
            "omelette":       ["eggs", "butter", "salt", "pepper", "cheese"],
            "pancakes":       ["flour", "eggs", "milk", "butter", "sugar", "salt"],
            "tomato pasta":   ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
            "grilled cheese": ["bread", "cheese", "butter"],
        }
        pantry = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]
        pantry_set = set(pantry)

        check_recipes(recipes, pantry_set)

        raw = input("\nExtra ingredients you have (comma-separated): ")
        extras = []
        for item in raw.split(","):
            extras.append(item.strip())
        pantry_set = add_ingredients(pantry_set, extras)

        print()
        check_recipes(recipes, pantry_set)

    elif TESTING_PROBLEM == 3:
        pass

    elif TESTING_PROBLEM == 4:
        pass

    else:
        print("There are only 4 problems!")

