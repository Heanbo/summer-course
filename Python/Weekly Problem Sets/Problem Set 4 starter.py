# problem 1
def process_reports(report_list: list[str]) -> tuple:
    pass


def show_available(roster: dict[str, dict[str, object]]) -> None:
    pass


def dispatch(roster: dict[str, dict[str, object]], name: str) -> None:
    pass


def fitness_report(roster: dict[str, dict[str, object]]) -> dict[str, list[str]]:
    pass


# problem 2
def can_make(recipe_ingredients: list[str], pantry_set: set[str]) -> bool:
    pass


def missing_ingredients(
    recipe_ingredients: list[str], pantry_set: set[str]
) -> list[str]:
    pass


def check_recipes(recipes: dict[str, list[str]], pantry_set: set[str]) -> None:
    pass


def add_ingredients(pantry_set: set[str], extra_ingredients: list[str]) -> set[str]:
    pass


# problem 3

# problem 4

# This will only execute if this script is executed directly, not imported
if __name__ == "__main__":
    # you can use this variable to test problems independently
    # while you're working locally
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

        # add your own testing here for problem 1

    elif TESTING_PROBLEM == 2:
        recipes = {
            "omelette": ["eggs", "butter", "salt", "pepper", "cheese"],
            "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "salt"],
            "tomato pasta": [
                "pasta",
                "tomatoes",
                "garlic",
                "olive oil",
                "salt",
                "pepper",
            ],
            "grilled cheese": ["bread", "cheese", "butter"],
        }
        pantry = [
            "eggs",
            "butter",
            "salt",
            "pepper",
            "cheese",
            "milk",
            "bread",
            "garlic",
        ]

        # add your own testing here for problem 2

    elif TESTING_PROBLEM == 3:
        pass

    elif TESTING_PROBLEM == 4:
        pass

    else:
        print("There are only 4 problems!")
