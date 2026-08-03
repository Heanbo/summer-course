# Problem Set 4 — Custom Classes & Object-Oriented Programming

**Topics covered:** custom classes, `__init__` methods, instance attributes, instance methods, working with lists of objects, dictionaries, sets, string methods

**Autograder note:** When using automated tests, it often requires exact function names, parameter lists, and return types. Do not rename functions or change parameter names/order; avoid extra print statements unless the instructions ask for them; prefer returning values over printing when specified. Wrap any demonstration or test code in an `if __name__ == "__main__":` block so autograders can import your functions cleanly.

Work on a new branch named `python/problem-set-4` for this problem set.  Your submitted script must be named `Problem Set 4 starter.py` or `Problem Set 4.py` for it to be picked up by the autograder.  Once you have passed all tests, you can merge your code back into main.

You may need to enable those workflows in GitHub Actions.  The workflows will not run automatically before they have been enabled.

## Submitting Your Work
As stated above, you should create a new branch and checkout that branch for this problem set called `python/problem-set-4`.  The general flow is shown below.

1. Fork the `AFC-AI2C/summer-course` repo (you only need to do this once)
   - This will create your own personal repo at `<github-username>/summer-course`
   - You have full ownership of that repo
2. Clone your personal repo locally (you only need to do this once)
3. Create and switch to a new branch called `python/problem-set-4`
4. Perform your work in either `Problem Set 4 starter.py` or a new file called `Problem Set 4.py`
5. Commit your changes
6. Push your changes
7. Review the output in GitHub Actions.  You can click into each run separately to see feedback
8. Fix any issues and repeat steps 5-7.
9. Once complete for all problems, you can merge your work back into main.

---

## Problem 1 — Soldier Roster & Dispatch System 🪖

*HQ needs a searchable roster of available soldiers. Your program will parse incoming personnel reports using custom classes to represent each soldier.*

**You are given the following personnel reports as raw strings:**

```python
reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]
```

**Your task:**

- **Create a `Soldier` class** with the following:
  - An `__init__` method that accepts `name`, `rank`, `fitness`, and `deployed` parameters
  - Store these as instance attributes using `self.name`, `self.rank`, `self.fitness`, and `self.deployed`
  - Add a `dispatch()` method that sets `self.deployed = True`
  - Add a `__str__` method that returns a formatted string with the soldier's information (e.g., `"Santos (PRIVATE, fitness: 91, deployed: False)"`)

- Create a function named `process_reports()` that:
  - Takes a list of report strings as input
  - Returns two values: a dictionary of `Soldier` objects (keyed by name), and a set of unique ranks
  - Use a `for` loop to parse each report string with `.split("|")`, `.strip()`, and `.split(":")`
  - Use `.title()` on names, `.upper()` on ranks, and `.lower()` on status values to normalise the data
  - Create a `Soldier` object for each report and add it to the roster dictionary
  - Collect all unique ranks in a set

- Write a function `show_available(roster)` that:
  - Takes the roster dictionary (containing `Soldier` objects) as input
  - Prints all soldiers where `deployed` is `False`, sorted alphabetically by name
  - Use `.sort()` on the list of available names

- Write a function `dispatch(roster, name)` that:
  - Takes the roster dictionary and a soldier's name
  - Calls the `.dispatch()` method on the appropriate `Soldier` object
  - Prints a message if they are already deployed or not found

**Expected output (partial):**

```
=== ROSTER LOADED ===
6 soldiers on record.
Ranks on file: {'PRIVATE', 'CORPORAL', 'SERGEANT'}

Available soldiers: ['Briggs', 'Okafor', 'Reyes', 'Santos']

Dispatching Santos...   Done. Status set to deployed.
Dispatching Kowalski... Kowalski is already deployed.

Updated status:
  Santos   : deployed
  Kowalski : deployed
```

### Challenge

Write a function `fitness_report(roster)` that builds and returns a dictionary with three keys — `"high"`, `"medium"`, and `"low"` — each mapping to a list of soldier names in that fitness band (high ≥ 80, medium 60–79, low < 60). Access the `fitness` attribute from each `Soldier` object using a `for` loop. Use `.append()` to build each list and `.sort()` to sort the names. Print the full report.

---

## Problem 2 — Recipe Ingredient Checker 🍳

*You're building a tool that helps cooks figure out what they can make with what's in their kitchen, and what they're missing.*

**You are given the following recipes and pantry:**

```python
recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]
```

**Your task:**

- **Create a `Recipe` class** with the following:
  - An `__init__` method that accepts `name` and `ingredients` (a list of strings)
  - Store these as instance attributes
  - Add a `can_make(pantry_set)` method that returns `True` if all ingredients are in the pantry set, `False` otherwise
  - Add a `missing_ingredients(pantry_set)` method that returns a **sorted list** of ingredients not in the pantry

- **Create a `Pantry` class** with the following:
  - An `__init__` method that accepts a list of ingredient strings
  - Store the ingredients internally as a **set** for efficient lookups
  - Add an `add_ingredients(extra_ingredients)` method that adds new ingredients to the pantry
  - Add a `has(ingredient)` method that returns `True` if the ingredient is in the pantry

- Create a function `create_recipes(recipe_data)` that:
  - Takes the recipe dictionary shown above
  - Returns a list of `Recipe` objects

- Create a function `check_recipes(recipes, pantry)` that:
  - Takes a list of `Recipe` objects and a `Pantry` object
  - Uses a `for` loop to check each recipe
  - Prints whether each recipe can be made and — if not — what's missing
  - At the end, print a list of all **unique ingredients** across all recipes, sorted alphabetically

**Expected output:**

```
=== RECIPE CHECKER ===
omelette       : CAN MAKE ✓
pancakes       : MISSING — ['flour', 'sugar']
tomato pasta   : MISSING — ['olive oil', 'pasta', 'tomatoes']
grilled cheese : CAN MAKE ✓

All unique ingredients (13): ['bread', 'butter', 'cheese', 'eggs', ...]
```

### Challenge

In your `__main__` block, ask the user for a comma-separated list of extra ingredients, parse them with `.split(",")` and `.strip()`, add them to the pantry using the `.add_ingredients()` method, then call `check_recipes()` again and print which recipes became newly available.

---

## Problem 3 — Song Lyric Word Counter 🎵

*Pick your favourite song and paste a few verses as a string in your code. Your program will analyse the lyrics using a custom class.*

**Your task:**

- **Create a `LyricAnalyzer` class** with the following:
  - An `__init__` method that accepts a lyrics string
  - Store the lyrics as an instance attribute
  - In `__init__`, process the lyrics: use `.lower()` to normalise, `.replace()` to strip punctuation, and `.split()` to create a list of words
  - Store the processed word list as `self.words`
  - Add a `count_words()` method that builds and returns a dictionary mapping each word to its count
  - Add a `unique_word_count()` method that returns the number of unique words (hint: use a set)
  - Add a `most_common_word()` method that returns a tuple of `(word, count)` for the most frequently used word
  - Add a `print_report()` method that prints all words alphabetically with their counts, the unique word count, and the most common word

- In your `__main__` block:
  - Create a multi-line string variable called `lyrics` with your chosen song lyrics. Here is an example:
  
```python
lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""
```

  - Create a `LyricAnalyzer` object with your lyrics
  - Call the `.print_report()` method

**Expected output (partial, using example lyrics):**

```
=== WORD COUNT ===
a          : 4
all        : 1
be         : 1
big        : 3
...
we         : 6
will       : 6
...

Unique words: 26
Most common word: 'we' — 6 times
```

### Challenge

Add a `filter_stopwords(stop_words)` method to your `LyricAnalyzer` class that:
- Takes a set of stop words (common filler words to ignore)
- Creates a new filtered word list excluding stop words
- Updates `self.words` with the filtered list

Use this set for filtering:
```python
stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}
```

After filtering, call `.print_report()` again to see the most common *meaningful* word.

---

## Problem 4 — Zoo Animal Registry 🦁

*You've just been hired as the data manager for a city zoo. Your job is to build and query a registry of animals using custom classes.*

**You are given the following raw data as a list of comma-separated strings:**

```python
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
```

**Your task:**

- **Create an `Animal` class** with the following:
  - An `__init__` method that accepts `name`, `species`, `age`, and `origin`
  - Store these as instance attributes
  - Add a `__str__` method that returns a formatted string like: `"Bubbles (dolphin, 12 years, from Ocean)"`
  - Add a `get_info()` method that prints the animal's details in a readable format

- Create a function `build_registry(raw_data)` that:
  - Takes the list of comma-separated strings
  - Uses a `for` loop with `.split(",")` and `.strip()` to parse each entry
  - Creates an `Animal` object for each entry
  - Returns a dictionary where keys are animal names and values are `Animal` objects

- Create a function `analyze_registry(registry)` that:
  - Takes the registry dictionary of `Animal` objects
  - Prints the total number of animals
  - Uses a set to collect and print all **unique species**
  - Uses a set to collect and print how many distinct **origins** the zoo's animals come from

- In your `__main__` block:
  - Build the registry
  - Call `analyze_registry()`
  - Ask the user to enter an animal's name
  - Use `.strip()` and `.title()` to clean the input
  - Look up the animal in the registry and call its `.get_info()` method (or print "not found")

**Example output (partial):**

```
=== ZOO REGISTRY BUILT ===
8 animals registered.

Unique species: {'lion', 'penguin', 'dolphin', 'parrot'}
Animals come from 4 distinct regions.

Enter an animal name to look up: bubbles

Name:    Bubbles
Species: dolphin
Age:     12
Origin:  Ocean
```

### Challenge

Write a function `group_by_species(registry)` that takes the registry dictionary and returns a new dictionary where each key is a species name and the value is a list of `Animal` objects of that species. Then use a `for` loop to print each species with its animal names using `", ".join()`:

```
lion    : Simba, Kovu, Nala
dolphin : Bubbles, Splash
...
```

---

## References

- [Python classes](https://docs.python.org/3/tutorial/classes.html)
- [Python `__init__` method](https://docs.python.org/3/tutorial/classes.html#class-objects)
- [Python dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)