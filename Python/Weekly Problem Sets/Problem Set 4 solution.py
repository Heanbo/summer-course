"""Problem Set 4 — Solution with Custom Classes

This script demonstrates object-oriented programming using custom classes
to solve data management problems.

Topics: classes, __init__ methods, instance attributes, instance methods,
dictionaries, sets, string methods
"""


# ── Problem 1 ─────────────────────────────────────────────────────────────────
class Soldier:
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self) -> None:
        """Mark this soldier as deployed."""
        self.deployed = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    roster = {}
    ranks = set()

    for report in report_list:
        parts = []
        for part in report.split("|"):
            parts.append(part.strip())

        # Expecting format: NAME | Rank | Fitness:NN | Status:state
        name = parts[0].title()
        rank = parts[1].upper()
        fitness_field = int(parts[2].split(":", 1)[1].strip())
        status_field = parts[3].split(":", 1)[1].strip().lower()

        soldier = Soldier(
            name=name,
            rank=rank,
            fitness=fitness_field,
            deployed=(status_field == "deployed"),
        )

        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available_soldiers = []

    for name, soldier in roster.items():
        if not soldier.deployed:
            available_soldiers.append(name)

    available_soldiers.sort()
    print(f"Available soldiers: {available_soldiers}\n")


def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    display_name = name.title()
    print(f"Dispatching {display_name}...", end=" ")

    soldier = roster.get(display_name)
    if soldier is None:
        print(f"{display_name} not found in roster.")
        return

    if not soldier.deployed:
        soldier.dispatch()
        print("Done. Status set to deployed.")
    else:
        print(f"{display_name} is already deployed.")


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    bands = {"high": [], "medium": [], "low": []}

    for name, soldier in roster.items():
        if soldier.fitness >= 80:
            bands["high"].append(name)
        elif 60 <= soldier.fitness <= 79:
            bands["medium"].append(name)
        else:
            bands["low"].append(name)

    for level in bands.values():
        level.sort()

    return bands


# ── Problem 2 ─────────────────────────────────────────────────────────────────
class Recipe:
    """Represents a recipe with a name and list of ingredients."""

    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set: set[str]) -> bool:
        """Check if all ingredients are in the pantry."""
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                return False
        return True

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        """Return sorted list of missing ingredients."""
        missing = []
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                missing.append(ingredient)
        missing.sort()
        return missing


class Pantry:
    """Represents a pantry with a set of ingredients."""

    def __init__(self, items: list[str]):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        for ingredient in extra_ingredients:
            self.items.add(ingredient)

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        return ingredient in self.items

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        return self.items


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    recipes = []
    for name, ingredients in recipe_data.items():
        recipes.append(Recipe(name, ingredients))
    return recipes


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    print("=== RECIPE CHECKER ===")

    all_ingredients = set()
    pantry_set = pantry.get_items()

    for recipe in recipes:
        for ingredient in recipe.ingredients:
            all_ingredients.add(ingredient)

        if recipe.can_make(pantry_set):
            print(f"{recipe.name:<14}: CAN MAKE ✓")
        else:
            missing = recipe.missing_ingredients(pantry_set)
            print(f"{recipe.name:<14}: MISSING — {missing}")

    unique = list(all_ingredients)
    unique.sort()
    print(f"\nAll unique ingredients ({len(unique)}): {unique}")


# ── Problem 3 ─────────────────────────────────────────────────────────────────
class LyricAnalyzer:
    """Analyzes song lyrics for word frequency."""

    def __init__(self, lyrics: str):
        self.original_lyrics = lyrics
        # Process lyrics: normalize, remove punctuation, split
        processed = lyrics.lower()
        processed = processed.replace(",", "")
        processed = processed.replace(".", "")
        processed = processed.replace("'", "")
        processed = processed.replace("!", "")
        processed = processed.replace("?", "")
        self.words = processed.split()

    def count_words(self) -> dict[str, int]:
        """Return dictionary mapping words to their counts."""
        word_count = {}
        for word in self.words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    def unique_word_count(self) -> int:
        """Return the number of unique words."""
        return len(set(self.words))

    def most_common_word(self) -> tuple[str, int]:
        """Return (word, count) for the most frequent word."""
        word_count = self.count_words()
        most_common = None
        max_count = 0

        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                most_common = word

        return (most_common, max_count)

    def print_report(self) -> None:
        """Print complete word analysis report."""
        print("=== WORD COUNT ===")
        word_count = self.count_words()

        # Get sorted list of words
        words_sorted = list(word_count.keys())
        words_sorted.sort()

        for word in words_sorted:
            print(f"{word:10}: {word_count[word]}")

        print(f"\nUnique words: {self.unique_word_count()}")

        most_common, count = self.most_common_word()
        print(f"Most common word: '{most_common}' — {count} times")

    def filter_stopwords(self, stop_words: set[str]) -> None:
        """Remove stop words from the word list."""
        filtered = []
        for word in self.words:
            if word not in stop_words:
                filtered.append(word)
        self.words = filtered


# ── Problem 4 ─────────────────────────────────────────────────────────────────
class Animal:
    """Represents a zoo animal with species, age, and origin."""

    def __init__(self, name: str, species: str, age: int, origin: str):
        self.name = name
        self.species = species
        self.age = age
        self.origin = origin

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.age} years, from {self.origin})"

    def get_info(self) -> None:
        """Print detailed information about the animal."""
        print(f"Name:    {self.name}")
        print(f"Species: {self.species}")
        print(f"Age:     {self.age}")
        print(f"Origin:  {self.origin}")


def build_registry(raw_data: list[str]) -> dict[str, Animal]:
    """Parse raw data strings and return dictionary of Animal objects."""
    registry = {}

    for entry in raw_data:
        parts = []
        for part in entry.split(","):
            parts.append(part.strip())

        name = parts[0]
        species = parts[1]
        age = int(parts[2])
        origin = parts[3]

        animal = Animal(name, species, age, origin)
        registry[name] = animal

    return registry


def analyze_registry(registry: dict[str, Animal]) -> None:
    """Analyze and print statistics about the zoo registry."""
    print(f"=== ZOO REGISTRY BUILT ===")
    print(f"{len(registry)} animals registered.\n")

    # Collect unique species
    species_set = set()
    origin_set = set()

    for animal in registry.values():
        species_set.add(animal.species)
        origin_set.add(animal.origin)

    print(f"Unique species: {species_set}")
    print(f"Animals come from {len(origin_set)} distinct regions.\n")


def group_by_species(registry: dict[str, Animal]) -> dict[str, list[Animal]]:
    """Group animals by species and return the groupings."""
    by_species = {}

    for animal in registry.values():
        if animal.species not in by_species:
            by_species[animal.species] = []
        by_species[animal.species].append(animal)

    return by_species


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
            soldier = roster.get(name.title())
            status = "deployed" if soldier.deployed else "available"
            print(f"  {name:8}: {status}")

        print("\nFitness report:")
        report = fitness_report(roster)
        for band in ("high", "medium", "low"):
            print(f"  {band.title():6}: {report[band]}")

    elif TESTING_PROBLEM == 2:
        recipe_data = {
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
        pantry_items = [
            "eggs",
            "butter",
            "salt",
            "pepper",
            "cheese",
            "milk",
            "bread",
            "garlic",
        ]

        recipes = create_recipes(recipe_data)
        pantry = Pantry(pantry_items)

        check_recipes(recipes, pantry)

        raw = input("\nExtra ingredients you have (comma-separated): ")
        extras = []
        for item in raw.split(","):
            extras.append(item.strip())
        pantry.add_ingredients(extras)

        print()
        check_recipes(recipes, pantry)

    elif TESTING_PROBLEM == 3:
        lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""

        analyzer = LyricAnalyzer(lyrics)
        analyzer.print_report()

        print("\n=== WITH STOPWORDS FILTERED ===")
        stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}
        analyzer.filter_stopwords(stop_words)
        analyzer.print_report()

    elif TESTING_PROBLEM == 4:
        raw_data = [
            "Simba, lion, 7, Africa",
            "Pebbles, penguin, 3, Antarctica",
            "Kovu, lion, 4, Africa",
            "Bubbles, dolphin, 12, Ocean",
            "Mango, parrot, 6, South America",
            "Nala, lion, 5, Africa",
            "Splash, dolphin, 8, Ocean",
            "Crackers, parrot, 2, South America",
        ]

        registry = build_registry(raw_data)
        analyze_registry(registry)

        name_input = input("Enter an animal name to look up: ")
        name = name_input.strip().title()

        if name in registry:
            print()
            registry[name].get_info()
        else:
            print(f"\n{name} not found in registry.")

        print("\n=== ANIMALS BY SPECIES ===")
        by_species = group_by_species(registry)
        for species, animals in by_species.items():
            names = []
            for animal in animals:
                names.append(animal.name)
            print(f"{species:8}: {', '.join(names)}")

    else:
        print("There are only 4 problems!")
