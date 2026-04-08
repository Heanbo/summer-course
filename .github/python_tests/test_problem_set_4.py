"""
Autograder tests for Problem Set 4 — Problem 1
Soldier Roster & Dispatch System

Each test class maps to one required function. Tests run independently so
students receive per-function feedback. Read the assertion messages — they
describe exactly what is expected.

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

# Safe fixture: calls process_reports() and skips any dependent test with a
# helpful message if the function hasn't been implemented yet (returns None).
@pytest.fixture
def roster_and_ranks(student):
    result = student.process_reports(REPORTS)
    if not (isinstance(result, tuple) and len(result) == 2):
        pytest.skip(
            "process_reports() did not return (roster, ranks) yet — implement that function first."
        )
    return result


REPORTS = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]

EXPECTED_NAMES = {"Santos", "Kowalski", "Okafor", "Briggs", "Nakamura", "Reyes"}
EXPECTED_AVAILABLE = ["Briggs", "Okafor", "Reyes", "Santos"]    # sorted
EXPECTED_RANKS = {"PRIVATE", "CORPORAL", "SERGEANT"}


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

    def test_roster_is_dict(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        assert isinstance(roster, dict), (
            "The first return value of process_reports() must be a dictionary.\n"
            "Each key is a soldier's name; each value is a dictionary of their details."
        )

    def test_roster_has_all_soldiers(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        missing = EXPECTED_NAMES - set(roster.keys())
        extra = set(roster.keys()) - EXPECTED_NAMES
        assert not missing and not extra, (
            f"Roster keys must be the six title-cased soldier names.\n"
            f"  Missing from your roster : {missing or 'none'}\n"
            f"  Unexpected in your roster: {extra or 'none'}\n"
            f"  Tip: use .title() on the name field from each report string."
        )

    def test_roster_entry_has_required_keys(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        required = {"rank", "fitness", "deployed"}
        for name, info in roster.items():
            missing_keys = required - set(info.keys())
            assert not missing_keys, (
                f"The roster entry for '{name}' is missing key(s): {missing_keys}.\n"
                f"Each entry must have exactly these keys: 'rank', 'fitness', 'deployed'."
            )

    def test_ranks_are_uppercase(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        for name, info in roster.items():
            rank = info.get("rank", "")
            assert rank == rank.upper(), (
                f"Ranks must be stored in UPPERCASE.\n"
                f"  '{name}' has rank '{rank}' — expected '{rank.upper()}'.\n"
                f"  Tip: use .upper() on the rank field."
            )

    def test_fitness_is_integer(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        for name, info in roster.items():
            assert isinstance(info.get("fitness"), int), (
                f"'fitness' must be stored as an integer, not a string.\n"
                f"  '{name}' has fitness value {repr(info.get('fitness'))}.\n"
                f"  Tip: wrap the parsed value in int()."
            )

    def test_fitness_values_correct(self, roster_and_ranks):
        expected = {
            "Santos": 91, "Kowalski": 74, "Okafor": 88,
            "Briggs": 55, "Nakamura": 82, "Reyes": 79,
        }
        roster, _ = roster_and_ranks
        for name, expected_fitness in expected.items():
            actual = roster.get(name, {}).get("fitness")
            assert actual == expected_fitness, (
                f"Fitness for '{name}' should be {expected_fitness}, got {repr(actual)}."
            )

    def test_deployed_is_boolean(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        for name, info in roster.items():
            assert isinstance(info.get("deployed"), bool), (
                f"'deployed' must be a boolean (True or False), not a string.\n"
                f"  '{name}' has deployed={repr(info.get('deployed'))}.\n"
                f"  Tip: use the expression  status_field == 'deployed'  which evaluates to True/False."
            )

    def test_deployed_values_correct(self, roster_and_ranks):
        roster, _ = roster_and_ranks
        assert roster["Kowalski"]["deployed"] is True, (
            "Kowalski's report says 'Status:deployed', so deployed should be True."
        )
        assert roster["Nakamura"]["deployed"] is True, (
            "Nakamura's report says 'Status:deployed', so deployed should be True."
        )
        assert roster["Santos"]["deployed"] is False, (
            "Santos's report says 'Status:available', so deployed should be False."
        )
        assert roster["Briggs"]["deployed"] is False, (
            "Briggs's report says 'Status:available', so deployed should be False."
        )

    def test_ranks_return_is_set(self, roster_and_ranks):
        _, ranks = roster_and_ranks
        assert isinstance(ranks, set), (
            "The second return value of process_reports() must be a set.\n"
            "A set naturally stores only unique values — use ranks.add(rank) inside the loop."
        )

    def test_ranks_values_correct(self, roster_and_ranks):
        _, ranks = roster_and_ranks
        assert ranks == EXPECTED_RANKS, (
            f"Unique ranks (uppercase) should be {EXPECTED_RANKS}.\n"
            f"Got: {ranks}"
        )


# ===========================================================================
# show_available()
# ===========================================================================
class TestShowAvailable:
    """Tests for show_available(roster) -> None  (prints available soldiers)"""

    def test_function_exists(self, student):
        assert_has_function(student, "show_available")

    def test_available_soldiers_are_printed(self, student, roster_and_ranks, capsys):
        roster, _ = roster_and_ranks
        student.show_available(roster)
        output = capsys.readouterr().out
        for name in EXPECTED_AVAILABLE:
            assert name in output, (
                f"'{name}' is available and should appear in show_available() output.\n"
                f"Your output was:\n{output}"
            )

    def test_deployed_soldiers_not_printed(self, student, roster_and_ranks, capsys):
        roster, _ = roster_and_ranks
        student.show_available(roster)
        output = capsys.readouterr().out
        for name in ("Kowalski", "Nakamura"):
            assert name not in output, (
                f"'{name}' is deployed and must NOT appear in show_available() output.\n"
                f"Your output was:\n{output}"
            )

    def test_output_is_alphabetically_sorted(self, student, roster_and_ranks, capsys):
        roster, _ = roster_and_ranks
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

    def test_dispatches_available_soldier(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        roster = copy.deepcopy(roster)   # isolate mutations between tests
        assert roster["Santos"]["deployed"] is False, "Test setup: Santos should start as not deployed."
        student.dispatch(roster, "Santos")
        assert roster["Santos"]["deployed"] is True, (
            "After calling dispatch(roster, 'Santos'), roster['Santos']['deployed'] should be True.\n"
            "Santos was available, so set deployed = True."
        )

    def test_dispatch_does_not_change_already_deployed(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        roster = copy.deepcopy(roster)
        student.dispatch(roster, "Kowalski")
        assert roster["Kowalski"]["deployed"] is True, (
            "Kowalski was already deployed — their deployed value should remain True after dispatch()."
        )

    def test_dispatch_already_deployed_prints_message(self, student, roster_and_ranks, capsys):
        roster, _ = roster_and_ranks
        roster = copy.deepcopy(roster)
        student.dispatch(roster, "Kowalski")
        output = capsys.readouterr().out.lower()
        assert "already" in output or "deployed" in output, (
            "When dispatching an already-deployed soldier, print a message to let the user know.\n"
            "Example: 'Kowalski is already deployed.'"
        )

    def test_dispatch_not_found_prints_message(self, student, roster_and_ranks, capsys):
        roster, _ = roster_and_ranks
        roster = copy.deepcopy(roster)
        student.dispatch(roster, "Nobody")
        output = capsys.readouterr().out.lower()
        assert "not found" in output or "nobody" in output, (
            "When the name is not in the roster, print a message indicating they were not found.\n"
            "Example: 'Nobody not found in roster.'"
        )

    def test_dispatch_case_insensitive_name(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        roster = copy.deepcopy(roster)
        student.dispatch(roster, "santos")   # all-lowercase input
        assert roster["Santos"]["deployed"] is True, (
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

    def test_returns_dict(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        assert isinstance(result, dict), (
            "fitness_report() must return a dictionary with keys 'high', 'medium', and 'low'."
        )

    def test_has_required_band_keys(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        for key in ("high", "medium", "low"):
            assert key in result, (
                f"fitness_report() result must contain the key '{key}'.\n"
                f"Your result had keys: {set(result.keys())}"
            )

    def test_high_band(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        assert set(result["high"]) == {"Santos", "Okafor", "Nakamura"}, (
            "High band (fitness >= 80) should contain Santos (91), Okafor (88), Nakamura (82).\n"
            f"Got: {result['high']}"
        )

    def test_medium_band(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        assert set(result["medium"]) == {"Kowalski", "Reyes"}, (
            "Medium band (60–79) should contain Kowalski (74) and Reyes (79).\n"
            f"Got: {result['medium']}"
        )

    def test_low_band(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        assert set(result["low"]) == {"Briggs"}, (
            "Low band (< 60) should contain only Briggs (55).\n"
            f"Got: {result['low']}"
        )

    def test_bands_are_alphabetically_sorted(self, student, roster_and_ranks):
        roster, _ = roster_and_ranks
        result = student.fitness_report(roster)
        for band in ("high", "medium", "low"):
            names = result[band]
            assert names == sorted(names), (
                f"Names in the '{band}' band must be sorted alphabetically.\n"
                f"Got: {names}\n"
                f"Tip: call .sort() on each band list before returning."
            )


# ---------------------------------------------------------------------------
# Problem 2 shared data
# ---------------------------------------------------------------------------

RECIPES = {
    "omelette":       ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":       ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":   ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese": ["bread", "cheese", "butter"],
}

PANTRY = {"eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"}


# ===========================================================================
# can_make()
# ===========================================================================
class TestCanMake:
    """Tests for can_make(recipe_ingredients, pantry_set) -> bool"""

    def test_function_exists(self, student):
        assert_has_function(student, "can_make")

    def test_returns_true_when_all_ingredients_present(self, student):
        result = student.can_make(RECIPES["omelette"], PANTRY)
        assert result is True, (
            "can_make() should return True for 'omelette' — all ingredients are in the pantry.\n"
            f"  Recipe    : {RECIPES['omelette']}\n"
            f"  Pantry    : {PANTRY}\n"
            f"  Your result: {result}"
        )

    def test_returns_true_for_grilled_cheese(self, student):
        result = student.can_make(RECIPES["grilled cheese"], PANTRY)
        assert result is True, (
            "can_make() should return True for 'grilled cheese' — bread, cheese, and butter are all in the pantry.\n"
            f"  Your result: {result}"
        )

    def test_returns_false_when_ingredients_missing(self, student):
        result = student.can_make(RECIPES["pancakes"], PANTRY)
        assert result is False, (
            "can_make() should return False for 'pancakes' — flour and sugar are not in the pantry.\n"
            f"  Recipe    : {RECIPES['pancakes']}\n"
            f"  Pantry    : {PANTRY}\n"
            f"  Your result: {result}"
        )

    def test_returns_false_for_tomato_pasta(self, student):
        result = student.can_make(RECIPES["tomato pasta"], PANTRY)
        assert result is False, (
            "can_make() should return False for 'tomato pasta' — pasta, tomatoes, and olive oil are missing.\n"
            f"  Your result: {result}"
        )

    def test_returns_bool_not_truthy(self, student):
        result = student.can_make(RECIPES["omelette"], PANTRY)
        assert isinstance(result, bool), (
            f"can_make() must return a bool (True or False), not {type(result).__name__}.\n"
            "Your loop should end with  return True  and return False on a miss."
        )

    def test_empty_recipe_always_makeable(self, student):
        result = student.can_make([], PANTRY)
        assert result is True, (
            "can_make() with an empty ingredient list should return True — nothing is missing.\n"
            f"  Your result: {result}"
        )

    def test_expanded_pantry_makes_pancakes_possible(self, student):
        bigger_pantry = PANTRY | {"flour", "sugar"}
        result = student.can_make(RECIPES["pancakes"], bigger_pantry)
        assert result is True, (
            "With flour and sugar added to the pantry, can_make() should return True for 'pancakes'.\n"
            f"  Your result: {result}"
        )


# ===========================================================================
# missing_ingredients()
# ===========================================================================
class TestMissingIngredients:
    """Tests for missing_ingredients(recipe_ingredients, pantry_set) -> list[str]"""

    def test_function_exists(self, student):
        assert_has_function(student, "missing_ingredients")

    def test_returns_list(self, student):
        result = student.missing_ingredients(RECIPES["pancakes"], PANTRY)
        assert isinstance(result, list), (
            f"missing_ingredients() must return a list, got {type(result).__name__}."
        )

    def test_correct_missing_for_pancakes(self, student):
        result = student.missing_ingredients(RECIPES["pancakes"], PANTRY)
        assert set(result) == {"flour", "sugar"}, (
            "For 'pancakes', the missing ingredients are flour and sugar.\n"
            f"  Your result: {result}"
        )

    def test_correct_missing_for_tomato_pasta(self, student):
        result = student.missing_ingredients(RECIPES["tomato pasta"], PANTRY)
        assert set(result) == {"pasta", "tomatoes", "olive oil"}, (
            "For 'tomato pasta', the missing ingredients are pasta, tomatoes, and olive oil.\n"
            f"  Your result: {result}"
        )

    def test_result_is_sorted(self, student):
        result = student.missing_ingredients(RECIPES["tomato pasta"], PANTRY)
        assert result == sorted(result), (
            "missing_ingredients() must return a sorted list.\n"
            f"  Your result  : {result}\n"
            f"  Sorted result: {sorted(result)}\n"
            "Tip: call .sort() on the list before returning, or use sorted()."
        )

    def test_empty_when_all_present(self, student):
        result = student.missing_ingredients(RECIPES["omelette"], PANTRY)
        assert result == [], (
            "missing_ingredients() should return an empty list when all ingredients are in the pantry.\n"
            f"  Your result: {result}"
        )

    def test_empty_recipe_returns_empty_list(self, student):
        result = student.missing_ingredients([], PANTRY)
        assert result == [], (
            "missing_ingredients() with an empty ingredient list should return [].\n"
            f"  Your result: {result}"
        )


# ===========================================================================
# check_recipes()
# ===========================================================================
class TestCheckRecipes:
    """Tests for check_recipes(recipes, pantry_set) -> None  (prints output)"""

    def test_function_exists(self, student):
        assert_has_function(student, "check_recipes")

    def test_makeable_recipes_shown(self, student, capsys):
        student.check_recipes(RECIPES, PANTRY)
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
        student.check_recipes(RECIPES, PANTRY)
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
        student.check_recipes(RECIPES, PANTRY)
        output = capsys.readouterr().out
        for ingredient in ("flour", "sugar", "pasta", "tomatoes"):
            assert ingredient in output, (
                f"'{ingredient}' is missing from the pantry and should appear in check_recipes() output.\n"
                f"Your output:\n{output}"
            )

    def test_unique_ingredient_count_printed(self, student, capsys):
        student.check_recipes(RECIPES, PANTRY)
        output = capsys.readouterr().out
        assert "13" in output, (
            "check_recipes() should print the count of unique ingredients across all recipes.\n"
            "There are 13 unique ingredients in the sample data — make sure that number appears in the output.\n"
            f"Your output:\n{output}"
        )


# ===========================================================================
# add_ingredients()   [Challenge]
# ===========================================================================
@pytest.mark.challenge
class TestAddIngredients:
    """Tests for add_ingredients(pantry_set, extra_ingredients) -> set[str]"""

    def test_function_exists(self, student):
        assert_has_function(student, "add_ingredients")

    def test_returns_set(self, student):
        result = student.add_ingredients(set(PANTRY), ["flour"])
        assert isinstance(result, set), (
            f"add_ingredients() must return a set, got {type(result).__name__}."
        )

    def test_new_ingredients_present(self, student):
        result = student.add_ingredients(set(PANTRY), ["flour", "sugar"])
        assert "flour" in result and "sugar" in result, (
            "add_ingredients() should add 'flour' and 'sugar' to the pantry set.\n"
            f"  Your result: {result}"
        )

    def test_original_ingredients_preserved(self, student):
        result = student.add_ingredients(set(PANTRY), ["flour"])
        assert PANTRY.issubset(result), (
            "add_ingredients() must keep the original pantry items — don't replace them.\n"
            f"  Original pantry: {PANTRY}\n"
            f"  Your result    : {result}"
        )

    def test_empty_extras_returns_unchanged(self, student):
        pantry_copy = set(PANTRY)
        result = student.add_ingredients(pantry_copy, [])
        assert result == PANTRY, (
            "add_ingredients() with an empty extras list should return the pantry unchanged.\n"
            f"  Your result: {result}"
        )
