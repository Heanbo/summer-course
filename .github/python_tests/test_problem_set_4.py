"""
Autograder tests for Problem Set 4 — Custom Classes & OOP

Each test class tests either a custom class or a required function.
Tests run independently so students receive per-component feedback.

To run locally:
    pytest .github/python_tests/test_problem_set_4.py -v
"""

import copy
import os
import pytest
from conftest import load_student_module, assert_has_function


# ---------------------------------------------------------------------------
# Path to the student's submission (relative to the repo root)
# ---------------------------------------------------------------------------
_SOLUTION_MODE = os.environ.get("SOLUTION_MODE", "").lower() == "true"

STUDENT_FILE = (
    "Python/Weekly Problem Sets/Problem Set 4 solution.py"
    if _SOLUTION_MODE
    else "Python/Weekly Problem Sets/Problem Set 4 starter.py"
)


# ---------------------------------------------------------------------------
# Shared fixture — loads the student module once per test session
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def student():
    return load_student_module(STUDENT_FILE, "student_ps4")


# ---------------------------------------------------------------------------
# Sample data used across all tests
# ---------------------------------------------------------------------------
REPORTS = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]

EXPECTED_NAMES = {"Santos", "Kowalski", "Okafor", "Briggs", "Nakamura", "Reyes"}
EXPECTED_AVAILABLE = ["Briggs", "Okafor", "Reyes", "Santos"]  # sorted
EXPECTED_RANKS = {"PRIVATE", "CORPORAL", "SERGEANT"}


# ===========================================================================
# Problem 1: Soldier class
# ===========================================================================
class TestSoldierClass:
    """Tests for the Soldier class"""

    def test_class_exists(self, student):
        assert hasattr(student, "Soldier"), "Soldier class not found in your file."

    def test_can_instantiate(self, student):
        soldier = student.Soldier("Test", "PRIVATE", 75, False)
        assert soldier is not None, "Could not create a Soldier instance."

    def test_has_required_attributes(self, student):
        soldier = student.Soldier("Santos", "PRIVATE", 91, False)
        assert hasattr(soldier, "name"), "Soldier must have a 'name' attribute."
        assert hasattr(soldier, "rank"), "Soldier must have a 'rank' attribute."
        assert hasattr(soldier, "fitness"), "Soldier must have a 'fitness' attribute."
        assert hasattr(soldier, "deployed"), "Soldier must have a 'deployed' attribute."

    def test_attributes_stored_correctly(self, student):
        soldier = student.Soldier("Santos", "PRIVATE", 91, False)
        assert soldier.name == "Santos"
        assert soldier.rank == "PRIVATE"
        assert soldier.fitness == 91
        assert soldier.deployed is False

    def test_dispatch_method_exists(self, student):
        soldier = student.Soldier("Santos", "PRIVATE", 91, False)
        assert hasattr(soldier, "dispatch"), "Soldier must have a 'dispatch()' method."

    def test_dispatch_method_sets_deployed(self, student):
        soldier = student.Soldier("Santos", "PRIVATE", 91, False)
        soldier.dispatch()
        assert soldier.deployed is True, "dispatch() should set deployed to True."

    def test_str_method_exists(self, student):
        soldier = student.Soldier("Santos", "PRIVATE", 91, False)
        result = str(soldier)
        assert isinstance(result, str), "__str__() must return a string."
        assert len(result) > 0, "__str__() should return a non-empty string."


# ===========================================================================
# process_reports()
# ===========================================================================
class TestProcessReports:
    """Tests for process_reports(report_list) -> (roster_dict, ranks_set)"""

    def test_function_exists(self, student):
        assert_has_function(student, "process_reports")

    def test_returns_two_values(self, student):
        result = student.process_reports(REPORTS)
        assert isinstance(result, tuple) and len(result) == 2, (
            "process_reports() must return exactly two values as a tuple: "
            "(roster_dict, ranks_set).  "
            "Example:  return roster, ranks"
        )

    def test_roster_is_dict(self, student):
        roster, _ = student.process_reports(REPORTS)
        assert isinstance(roster, dict), (
            "The first return value of process_reports() must be a dictionary.\n"
            "Each key is a soldier's name; each value is a Soldier object."
        )

    def test_roster_has_all_soldiers(self, student):
        roster, _ = student.process_reports(REPORTS)
        missing = EXPECTED_NAMES - set(roster.keys())
        extra = set(roster.keys()) - EXPECTED_NAMES
        assert not missing and not extra, (
            f"Roster keys must be the six title-cased soldier names.\n"
            f"  Missing from your roster : {missing or 'none'}\n"
            f"  Unexpected in your roster: {extra or 'none'}\n"
            f"  Tip: use .title() on the name field from each report string."
        )

    def test_roster_values_are_soldier_objects(self, student):
        roster, _ = student.process_reports(REPORTS)
        for name, soldier in roster.items():
            assert hasattr(soldier, "name") and hasattr(soldier, "rank"), (
                f"Roster values must be Soldier objects.\n"
                f"  '{name}' has value of type {type(soldier).__name__}"
            )

    def test_soldier_attributes_correct(self, student):
        roster, _ = student.process_reports(REPORTS)
        santos = roster.get("Santos")
        assert santos.rank == "PRIVATE", f"Santos rank should be PRIVATE, got {santos.rank}"
        assert santos.fitness == 91, f"Santos fitness should be 91, got {santos.fitness}"
        assert santos.deployed is False, f"Santos deployed should be False, got {santos.deployed}"

    def test_deployed_values_correct(self, student):
        roster, _ = student.process_reports(REPORTS)
        assert roster["Kowalski"].deployed is True, "Kowalski should be deployed."
        assert roster["Nakamura"].deployed is True, "Nakamura should be deployed."
        assert roster["Santos"].deployed is False, "Santos should not be deployed."
        assert roster["Briggs"].deployed is False, "Briggs should not be deployed."

    def test_ranks_return_is_set(self, student):
        _, ranks = student.process_reports(REPORTS)
        assert isinstance(ranks, set), (
            "The second return value of process_reports() must be a set.\n"
            "A set naturally stores only unique values — use ranks.add(rank) inside the loop."
        )

    def test_ranks_values_correct(self, student):
        _, ranks = student.process_reports(REPORTS)
        assert ranks == EXPECTED_RANKS, (
            f"Unique ranks (uppercase) should be {EXPECTED_RANKS}.\n" f"Got: {ranks}"
        )


# ===========================================================================
# show_available()
# ===========================================================================
class TestShowAvailable:
    """Tests for show_available(roster) -> None  (prints available soldiers)"""

    def test_function_exists(self, student):
        assert_has_function(student, "show_available")

    def test_available_soldiers_are_printed(self, student, capsys):
        roster, _ = student.process_reports(REPORTS)
        student.show_available(roster)
        output = capsys.readouterr().out
        for name in EXPECTED_AVAILABLE:
            assert name in output, (
                f"'{name}' is available and should appear in show_available() output.\n"
                f"Your output was:\n{output}"
            )

    def test_deployed_soldiers_not_printed(self, student, capsys):
        roster, _ = student.process_reports(REPORTS)
        student.show_available(roster)
        output = capsys.readouterr().out
        for name in ("Kowalski", "Nakamura"):
            assert name not in output, (
                f"'{name}' is deployed and must NOT appear in show_available() output.\n"
                f"Your output was:\n{output}"
            )

    def test_output_is_alphabetically_sorted(self, student, capsys):
        roster, _ = student.process_reports(REPORTS)
        student.show_available(roster)
        output = capsys.readouterr().out
        positions = {name: output.find(name) for name in EXPECTED_AVAILABLE}
        order = sorted(positions, key=lambda n: positions[n])
        assert order == EXPECTED_AVAILABLE, (
            f"show_available() must print names in alphabetical order.\n"
            f"Expected order : {EXPECTED_AVAILABLE}\n"
            f"Detected order : {order}\n"
            f"Tip: call .sort() on the list of available names before printing."
        )


# ===========================================================================
# dispatch()
# ===========================================================================
class TestDispatch:
    """Tests for dispatch(roster, name) -> None"""

    def test_function_exists(self, student):
        assert_has_function(student, "dispatch")

    def test_dispatches_available_soldier(self, student):
        roster, _ = student.process_reports(REPORTS)
        assert roster["Santos"].deployed is False, "Test setup: Santos should start as not deployed."
        student.dispatch(roster, "Santos")
        assert roster["Santos"].deployed is True, (
            "After calling dispatch(roster, 'Santos'), Santos.deployed should be True.\n"
            "Santos was available, so set deployed = True."
        )

    def test_dispatch_does_not_change_already_deployed(self, student):
        roster, _ = student.process_reports(REPORTS)
        student.dispatch(roster, "Kowalski")
        assert roster["Kowalski"].deployed is True, (
            "Kowalski was already deployed — their deployed value should remain True after dispatch()."
        )

    def test_dispatch_already_deployed_prints_message(self, student, capsys):
        roster, _ = student.process_reports(REPORTS)
        student.dispatch(roster, "Kowalski")
        output = capsys.readouterr().out.lower()
        assert "already" in output or "deployed" in output, (
            "When dispatching an already-deployed soldier, print a message to let the user know.\n"
            "Example: 'Kowalski is already deployed.'"
        )

    def test_dispatch_not_found_prints_message(self, student, capsys):
        roster, _ = student.process_reports(REPORTS)
        student.dispatch(roster, "Nobody")
        output = capsys.readouterr().out.lower()
        assert "not found" in output or "nobody" in output, (
            "When the name is not in the roster, print a message indicating they were not found.\n"
            "Example: 'Nobody not found in roster.'"
        )

    def test_dispatch_case_insensitive_name(self, student):
        roster, _ = student.process_reports(REPORTS)
        student.dispatch(roster, "santos")  # all-lowercase input
        assert roster["Santos"].deployed is True, (
            "dispatch() should work regardless of how the caller capitalises the name.\n"
            "Tip: use name.title() inside dispatch() to normalise the input."
        )


# ===========================================================================
# fitness_report()   [Challenge]
# ===========================================================================
@pytest.mark.challenge
class TestFitnessReport:
    """Tests for fitness_report(roster) -> {'high': [...], 'medium': [...], 'low': [...]}"""

    def test_function_exists(self, student):
        assert_has_function(student, "fitness_report")

    def test_returns_dict(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        assert isinstance(result, dict), (
            "fitness_report() must return a dictionary with keys 'high', 'medium', and 'low'."
        )

    def test_has_required_band_keys(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        for key in ("high", "medium", "low"):
            assert key in result, (
                f"fitness_report() result must contain the key '{key}'.\n"
                f"Your result had keys: {set(result.keys())}"
            )

    def test_high_band(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        assert set(result["high"]) == {"Santos", "Okafor", "Nakamura"}, (
            "High band (fitness >= 80) should contain Santos (91), Okafor (88), Nakamura (82).\n"
            f"Got: {result['high']}"
        )

    def test_medium_band(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        assert set(result["medium"]) == {"Kowalski", "Reyes"}, (
            "Medium band (60–79) should contain Kowalski (74) and Reyes (79).\n"
            f"Got: {result['medium']}"
        )

    def test_low_band(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        assert set(result["low"]) == {"Briggs"}, (
            "Low band (< 60) should contain only Briggs (55).\n" f"Got: {result['low']}"
        )

    def test_bands_are_alphabetically_sorted(self, student):
        roster, _ = student.process_reports(REPORTS)
        result = student.fitness_report(roster)
        for band in ("high", "medium", "low"):
            names = result[band]
            assert names == sorted(names), (
                f"Names in the '{band}' band must be sorted alphabetically.\n"
                f"Got: {names}\n"
                f"Tip: call .sort() on each band list before returning."
            )


# ===========================================================================
# Problem 2: Recipe class
# ===========================================================================
RECIPE_DATA = {
    "omelette": ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta": ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese": ["bread", "cheese", "butter"],
}

PANTRY_ITEMS = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]


class TestRecipeClass:
    """Tests for the Recipe class"""

    def test_class_exists(self, student):
        assert hasattr(student, "Recipe"), "Recipe class not found in your file."

    def test_can_instantiate(self, student):
        recipe = student.Recipe("test", ["eggs", "milk"])
        assert recipe is not None, "Could not create a Recipe instance."

    def test_has_required_attributes(self, student):
        recipe = student.Recipe("omelette", ["eggs", "butter"])
        assert hasattr(recipe, "name"), "Recipe must have a 'name' attribute."
        assert hasattr(recipe, "ingredients"), "Recipe must have an 'ingredients' attribute."

    def test_can_make_method_exists(self, student):
        recipe = student.Recipe("test", ["eggs"])
        assert hasattr(recipe, "can_make"), "Recipe must have a 'can_make()' method."

    def test_can_make_returns_true_when_available(self, student):
        recipe = student.Recipe("omelette", RECIPE_DATA["omelette"])
        pantry_set = set(PANTRY_ITEMS)
        result = recipe.can_make(pantry_set)
        assert result is True, "can_make() should return True when all ingredients are available."

    def test_can_make_returns_false_when_missing(self, student):
        recipe = student.Recipe("pancakes", RECIPE_DATA["pancakes"])
        pantry_set = set(PANTRY_ITEMS)
        result = recipe.can_make(pantry_set)
        assert result is False, "can_make() should return False when ingredients are missing."

    def test_missing_ingredients_method_exists(self, student):
        recipe = student.Recipe("test", ["eggs"])
        assert hasattr(
            recipe, "missing_ingredients"
        ), "Recipe must have a 'missing_ingredients()' method."

    def test_missing_ingredients_returns_list(self, student):
        recipe = student.Recipe("pancakes", RECIPE_DATA["pancakes"])
        pantry_set = set(PANTRY_ITEMS)
        result = recipe.missing_ingredients(pantry_set)
        assert isinstance(result, list), "missing_ingredients() must return a list."

    def test_missing_ingredients_correct(self, student):
        recipe = student.Recipe("pancakes", RECIPE_DATA["pancakes"])
        pantry_set = set(PANTRY_ITEMS)
        result = recipe.missing_ingredients(pantry_set)
        assert set(result) == {
            "flour",
            "sugar",
        }, f"Missing ingredients for pancakes should be flour and sugar, got {result}"

    def test_missing_ingredients_sorted(self, student):
        recipe = student.Recipe("pancakes", RECIPE_DATA["pancakes"])
        pantry_set = set(PANTRY_ITEMS)
        result = recipe.missing_ingredients(pantry_set)
        assert result == sorted(result), "missing_ingredients() must return a sorted list."


# ===========================================================================
# Pantry class
# ===========================================================================
class TestPantryClass:
    """Tests for the Pantry class"""

    def test_class_exists(self, student):
        assert hasattr(student, "Pantry"), "Pantry class not found in your file."

    def test_can_instantiate(self, student):
        pantry = student.Pantry(["eggs", "milk"])
        assert pantry is not None, "Could not create a Pantry instance."

    def test_has_method_exists(self, student):
        pantry = student.Pantry(PANTRY_ITEMS)
        assert hasattr(pantry, "has"), "Pantry must have a 'has()' method."

    def test_has_method_works(self, student):
        pantry = student.Pantry(PANTRY_ITEMS)
        assert pantry.has("eggs") is True, "Pantry.has('eggs') should return True."
        assert pantry.has("flour") is False, "Pantry.has('flour') should return False."

    def test_add_ingredients_method_exists(self, student):
        pantry = student.Pantry(PANTRY_ITEMS)
        assert hasattr(
            pantry, "add_ingredients"
        ), "Pantry must have an 'add_ingredients()' method."

    def test_add_ingredients_works(self, student):
        pantry = student.Pantry(list(PANTRY_ITEMS))
        pantry.add_ingredients(["flour", "sugar"])
        assert pantry.has("flour") is True, "After adding flour, pantry.has('flour') should be True."
        assert pantry.has("sugar") is True, "After adding sugar, pantry.has('sugar') should be True."

    def test_get_items_method_exists(self, student):
        pantry = student.Pantry(PANTRY_ITEMS)
        assert hasattr(pantry, "get_items"), "Pantry must have a 'get_items()' method."

    def test_get_items_returns_set(self, student):
        pantry = student.Pantry(PANTRY_ITEMS)
        result = pantry.get_items()
        assert isinstance(result, set), "get_items() must return a set."


# ===========================================================================
# create_recipes()
# ===========================================================================
class TestCreateRecipes:
    """Tests for create_recipes(recipe_data) -> list[Recipe]"""

    def test_function_exists(self, student):
        assert_has_function(student, "create_recipes")

    def test_returns_list(self, student):
        result = student.create_recipes(RECIPE_DATA)
        assert isinstance(result, list), "create_recipes() must return a list."

    def test_list_contains_recipe_objects(self, student):
        result = student.create_recipes(RECIPE_DATA)
        for item in result:
            assert hasattr(item, "name") and hasattr(item, "ingredients"), (
                f"create_recipes() must return a list of Recipe objects.\n"
                f"Found item of type {type(item).__name__}"
            )

    def test_correct_number_of_recipes(self, student):
        result = student.create_recipes(RECIPE_DATA)
        assert len(result) == len(RECIPE_DATA), (
            f"create_recipes() should return {len(RECIPE_DATA)} Recipe objects, got {len(result)}"
        )


# ===========================================================================
# check_recipes()
# ===========================================================================
class TestCheckRecipes:
    """Tests for check_recipes(recipes, pantry) -> None  (prints output)"""

    def test_function_exists(self, student):
        assert_has_function(student, "check_recipes")

    def test_makeable_recipes_shown(self, student, capsys):
        recipes = student.create_recipes(RECIPE_DATA)
        pantry = student.Pantry(PANTRY_ITEMS)
        student.check_recipes(recipes, pantry)
        output = capsys.readouterr().out
        assert "omelette" in output.lower(), (
            "check_recipes() output should mention 'omelette' (it can be made).\n"
            f"Your output:\n{output}"
        )
        assert "grilled cheese" in output.lower(), (
            "check_recipes() output should mention 'grilled cheese' (it can be made).\n"
            f"Your output:\n{output}"
        )

    def test_missing_recipes_shown(self, student, capsys):
        recipes = student.create_recipes(RECIPE_DATA)
        pantry = student.Pantry(PANTRY_ITEMS)
        student.check_recipes(recipes, pantry)
        output = capsys.readouterr().out
        assert "pancakes" in output.lower(), (
            "check_recipes() output should mention 'pancakes' (ingredients are missing).\n"
            f"Your output:\n{output}"
        )
        assert "tomato pasta" in output.lower(), (
            "check_recipes() output should mention 'tomato pasta' (ingredients are missing).\n"
            f"Your output:\n{output}"
        )

    def test_missing_ingredients_appear_in_output(self, student, capsys):
        recipes = student.create_recipes(RECIPE_DATA)
        pantry = student.Pantry(PANTRY_ITEMS)
        student.check_recipes(recipes, pantry)
        output = capsys.readouterr().out
        for ingredient in ("flour", "sugar", "pasta", "tomatoes"):
            assert ingredient in output, (
                f"'{ingredient}' is missing from the pantry and should appear in check_recipes() output.\n"
                f"Your output:\n{output}"
            )

    def test_unique_ingredient_count_printed(self, student, capsys):
        recipes = student.create_recipes(RECIPE_DATA)
        pantry = student.Pantry(PANTRY_ITEMS)
        student.check_recipes(recipes, pantry)
        output = capsys.readouterr().out
        assert "13" in output, (
            "check_recipes() should print the count of unique ingredients across all recipes.\n"
            "There are 13 unique ingredients in the sample data — make sure that number appears in the output.\n"
            f"Your output:\n{output}"
        )


# ===========================================================================
# Pantry.add_ingredients()   [Challenge]
# ===========================================================================
@pytest.mark.challenge
class TestPantryAddIngredients:
    """Challenge tests for Pantry.add_ingredients() method"""

    def test_add_single_ingredient(self, student):
        pantry = student.Pantry(list(PANTRY_ITEMS))
        pantry.add_ingredients(["flour"])
        assert pantry.has("flour") is True, (
            "After adding 'flour', pantry.has('flour') should return True."
        )

    def test_add_multiple_ingredients(self, student):
        pantry = student.Pantry(list(PANTRY_ITEMS))
        pantry.add_ingredients(["flour", "sugar", "olive oil"])
        assert pantry.has("flour") is True, "Pantry should contain 'flour' after adding."
        assert pantry.has("sugar") is True, "Pantry should contain 'sugar' after adding."
        assert pantry.has("olive oil") is True, "Pantry should contain 'olive oil' after adding."

    def test_original_ingredients_preserved(self, student):
        pantry = student.Pantry(list(PANTRY_ITEMS))
        pantry.add_ingredients(["flour"])
        for ingredient in PANTRY_ITEMS:
            assert pantry.has(ingredient) is True, (
                f"Original ingredient '{ingredient}' should still be in pantry after adding new items."
            )

    def test_duplicate_ingredients_handled(self, student):
        pantry = student.Pantry(["eggs", "milk"])
        pantry.add_ingredients(["eggs", "flour"])  # eggs is a duplicate
        assert pantry.has("eggs") is True, "Pantry should still contain 'eggs'."
        assert pantry.has("flour") is True, "Pantry should contain newly added 'flour'."

    def test_empty_list_doesnt_break(self, student):
        pantry = student.Pantry(list(PANTRY_ITEMS))
        original_items = pantry.get_items()
        pantry.add_ingredients([])
        assert pantry.get_items() == original_items, (
            "Adding an empty list should not change the pantry contents."
        )

    def test_makes_recipes_available(self, student):
        """Integration test: adding ingredients should make new recipes available"""
        recipes = student.create_recipes(RECIPE_DATA)
        pantry = student.Pantry(list(PANTRY_ITEMS))
        
        # Pancakes should not be makeable initially
        pancake_recipe = [r for r in recipes if r.name == "pancakes"][0]
        assert pancake_recipe.can_make(pantry.get_items()) is False, (
            "Pancakes should not be makeable before adding flour and sugar."
        )
        
        # Add the missing ingredients
        pantry.add_ingredients(["flour", "sugar"])
        
        # Now pancakes should be makeable
        assert pancake_recipe.can_make(pantry.get_items()) is True, (
            "Pancakes should be makeable after adding flour and sugar."
        )


# ===========================================================================
# Problem 3: LyricAnalyzer class
# ===========================================================================
SAMPLE_LYRICS = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""


class TestLyricAnalyzerClass:
    """Tests for the LyricAnalyzer class"""

    def test_class_exists(self, student):
        assert hasattr(student, "LyricAnalyzer"), "LyricAnalyzer class not found in your file."

    def test_can_instantiate(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert analyzer is not None, "Could not create a LyricAnalyzer instance."

    def test_has_words_attribute(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(analyzer, "words"), "LyricAnalyzer must have a 'words' attribute."
        assert isinstance(analyzer.words, list), "'words' should be a list."

    def test_count_words_method_exists(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(analyzer, "count_words"), "LyricAnalyzer must have a 'count_words()' method."

    def test_count_words_returns_dict(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        result = analyzer.count_words()
        assert isinstance(result, dict), "count_words() must return a dictionary."

    def test_count_words_correct(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        result = analyzer.count_words()
        # "we" and "will" appear 6 times each in the sample
        assert result.get("we") == 6, "The word 'we' appears 6 times in the sample lyrics."
        assert result.get("will") == 6, "The word 'will' appears 6 times in the sample lyrics."

    def test_unique_word_count_method_exists(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(
            analyzer, "unique_word_count"
        ), "LyricAnalyzer must have a 'unique_word_count()' method."

    def test_unique_word_count_returns_int(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        result = analyzer.unique_word_count()
        assert isinstance(result, int), "unique_word_count() must return an integer."

    def test_most_common_word_method_exists(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(
            analyzer, "most_common_word"
        ), "LyricAnalyzer must have a 'most_common_word()' method."

    def test_most_common_word_returns_tuple(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        result = analyzer.most_common_word()
        assert isinstance(result, tuple) and len(result) == 2, (
            "most_common_word() must return a tuple of (word, count)."
        )

    def test_print_report_method_exists(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(analyzer, "print_report"), "LyricAnalyzer must have a 'print_report()' method."

    def test_print_report_produces_output(self, student, capsys):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        analyzer.print_report()
        output = capsys.readouterr().out
        assert len(output) > 0, "print_report() should produce some output."
        assert "we" in output.lower(), "print_report() should include word counts."


# ===========================================================================
# LyricAnalyzer.filter_stopwords()   [Challenge]
# ===========================================================================
@pytest.mark.challenge
class TestFilterStopwords:
    """Challenge tests for LyricAnalyzer.filter_stopwords() method"""

    def test_method_exists(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        assert hasattr(
            analyzer, "filter_stopwords"
        ), "LyricAnalyzer must have a 'filter_stopwords()' method."

    def test_removes_stopwords(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        stop_words = {"we", "you", "your"}
        original_count = len(analyzer.words)
        analyzer.filter_stopwords(stop_words)
        new_count = len(analyzer.words)
        assert new_count < original_count, (
            "After filtering stopwords, the word list should be shorter."
        )

    def test_stopwords_actually_removed(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        stop_words = {"we", "will"}
        analyzer.filter_stopwords(stop_words)
        word_count = analyzer.count_words()
        assert "we" not in word_count, (
            "'we' should not appear in word count after being filtered out."
        )
        assert "will" not in word_count, (
            "'will' should not appear in word count after being filtered out."
        )

    def test_non_stopwords_preserved(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        stop_words = {"we", "you", "your"}
        analyzer.filter_stopwords(stop_words)
        word_count = analyzer.count_words()
        # Words that should still be there
        assert "rock" in word_count, "'rock' should still be in the word list."
        assert "big" in word_count, "'big' should still be in the word list."

    def test_empty_stopwords_no_change(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        original_count = len(analyzer.words)
        analyzer.filter_stopwords(set())  # Empty set
        new_count = len(analyzer.words)
        assert new_count == original_count, (
            "Filtering with an empty stopword set should not change the word list."
        )

    def test_changes_most_common_word(self, student):
        """Integration test: filtering stopwords should change the most common word"""
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        
        # Before filtering, "we" or "will" should be most common (both appear 6 times)
        original_most_common, original_count = analyzer.most_common_word()
        assert original_most_common in ["we", "will"], (
            f"Most common word should be 'we' or 'will' before filtering, got '{original_most_common}'"
        )
        
        # Filter out the stop words
        stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got", "will"}
        analyzer.filter_stopwords(stop_words)
        
        # After filtering, a different word should be most common
        filtered_most_common, filtered_count = analyzer.most_common_word()
        assert filtered_most_common != "we" and filtered_most_common != "will", (
            f"After filtering, most common word should not be 'we' or 'will', got '{filtered_most_common}'"
        )
        # "big" and "rock" both appear 3 times and could be most common after filtering
        assert filtered_most_common in ["big", "rock"], (
            f"After filtering stopwords, 'big' or 'rock' should be most common (3 times), got '{filtered_most_common}'"
        )
        assert filtered_count == 3, (
            f"Most common word after filtering should appear 3 times, got {filtered_count}"
        )

    def test_unique_word_count_decreases(self, student):
        analyzer = student.LyricAnalyzer(SAMPLE_LYRICS)
        original_unique = analyzer.unique_word_count()
        
        stop_words = {"we", "will", "you", "your", "a"}
        analyzer.filter_stopwords(stop_words)
        
        new_unique = analyzer.unique_word_count()
        assert new_unique < original_unique, (
            f"Unique word count should decrease after filtering.\n"
            f"  Before: {original_unique}\n"
            f"  After:  {new_unique}"
        )


# ===========================================================================
# Problem 4: Animal class
# ===========================================================================
RAW_DATA = [
    "Simba, lion, 7, Africa",
    "Pebbles, penguin, 3, Antarctica",
    "Kovu, lion, 4, Africa",
    "Bubbles, dolphin, 12, Ocean",
    "Mango, parrot, 6, South America",
    "Nala, lion, 5, Africa",
    "Splash, dolphin, 8, Ocean",
    "Crackers, parrot, 2, South America",
]


class TestAnimalClass:
    """Tests for the Animal class"""

    def test_class_exists(self, student):
        assert hasattr(student, "Animal"), "Animal class not found in your file."

    def test_can_instantiate(self, student):
        animal = student.Animal("Test", "dog", 5, "USA")
        assert animal is not None, "Could not create an Animal instance."

    def test_has_required_attributes(self, student):
        animal = student.Animal("Simba", "lion", 7, "Africa")
        assert hasattr(animal, "name"), "Animal must have a 'name' attribute."
        assert hasattr(animal, "species"), "Animal must have a 'species' attribute."
        assert hasattr(animal, "age"), "Animal must have an 'age' attribute."
        assert hasattr(animal, "origin"), "Animal must have an 'origin' attribute."

    def test_attributes_stored_correctly(self, student):
        animal = student.Animal("Simba", "lion", 7, "Africa")
        assert animal.name == "Simba"
        assert animal.species == "lion"
        assert animal.age == 7
        assert animal.origin == "Africa"

    def test_str_method_exists(self, student):
        animal = student.Animal("Simba", "lion", 7, "Africa")
        result = str(animal)
        assert isinstance(result, str), "__str__() must return a string."
        assert len(result) > 0, "__str__() should return a non-empty string."

    def test_get_info_method_exists(self, student):
        animal = student.Animal("Simba", "lion", 7, "Africa")
        assert hasattr(animal, "get_info"), "Animal must have a 'get_info()' method."

    def test_get_info_produces_output(self, student, capsys):
        animal = student.Animal("Simba", "lion", 7, "Africa")
        animal.get_info()
        output = capsys.readouterr().out
        assert len(output) > 0, "get_info() should produce some output."
        assert "Simba" in output, "get_info() should display the animal's name."


# ===========================================================================
# build_registry()
# ===========================================================================
class TestBuildRegistry:
    """Tests for build_registry(raw_data) -> dict[str, Animal]"""

    def test_function_exists(self, student):
        assert_has_function(student, "build_registry")

    def test_returns_dict(self, student):
        result = student.build_registry(RAW_DATA)
        assert isinstance(result, dict), "build_registry() must return a dictionary."

    def test_correct_number_of_animals(self, student):
        result = student.build_registry(RAW_DATA)
        assert len(result) == len(RAW_DATA), (
            f"build_registry() should create {len(RAW_DATA)} Animal objects, got {len(result)}"
        )

    def test_registry_values_are_animal_objects(self, student):
        result = student.build_registry(RAW_DATA)
        for name, animal in result.items():
            assert hasattr(animal, "name") and hasattr(animal, "species"), (
                f"Registry values must be Animal objects.\n"
                f"  '{name}' has value of type {type(animal).__name__}"
            )

    def test_animal_data_parsed_correctly(self, student):
        result = student.build_registry(RAW_DATA)
        simba = result.get("Simba")
        assert simba is not None, "Registry should contain 'Simba'."
        assert simba.species == "lion", f"Simba should be a lion, got {simba.species}"
        assert simba.age == 7, f"Simba should be 7 years old, got {simba.age}"
        assert simba.origin == "Africa", f"Simba should be from Africa, got {simba.origin}"


# ===========================================================================
# analyze_registry()
# ===========================================================================
class TestAnalyzeRegistry:
    """Tests for analyze_registry(registry) -> None"""

    def test_function_exists(self, student):
        assert_has_function(student, "analyze_registry")

    def test_produces_output(self, student, capsys):
        registry = student.build_registry(RAW_DATA)
        student.analyze_registry(registry)
        output = capsys.readouterr().out
        assert len(output) > 0, "analyze_registry() should produce some output."
        assert "8" in output, "Output should mention 8 animals."


# ===========================================================================
# group_by_species()   [Challenge]
# ===========================================================================
@pytest.mark.challenge
class TestGroupBySpecies:
    """Tests for group_by_species(registry) -> dict[str, list[Animal]]"""

    def test_function_exists(self, student):
        assert_has_function(student, "group_by_species")

    def test_returns_dict(self, student):
        registry = student.build_registry(RAW_DATA)
        result = student.group_by_species(registry)
        assert isinstance(result, dict), "group_by_species() must return a dictionary."

    def test_groups_lions_correctly(self, student):
        registry = student.build_registry(RAW_DATA)
        result = student.group_by_species(registry)
        lions = result.get("lion", [])
        lion_names = {animal.name for animal in lions}
        assert lion_names == {"Simba", "Kovu", "Nala"}, (
            f"Lions should be Simba, Kovu, and Nala. Got: {lion_names}"
        )

    def test_groups_dolphins_correctly(self, student):
        registry = student.build_registry(RAW_DATA)
        result = student.group_by_species(registry)
        dolphins = result.get("dolphin", [])
        dolphin_names = {animal.name for animal in dolphins}
        assert dolphin_names == {"Bubbles", "Splash"}, (
            f"Dolphins should be Bubbles and Splash. Got: {dolphin_names}"
        )
