"""
Autograder tests for Problem Set 5 — Recursion & HTTP / APIs

Each test class tests either a custom class or a required function.
Tests run independently so students receive per-component feedback.

To run locally:
    pytest .github/python_tests/test_problem_set_5.py -v
"""

import copy
import os
import pytest
from conftest import load_student_module, assert_has_function
from random import randint
from unittest.mock import Mock

# ---------------------------------------------------------------------------
# Path to the student's submission (relative to the repo root)
# ---------------------------------------------------------------------------
_SOLUTION_MODE = os.environ.get("SOLUTION_MODE", "").lower() == "true"

STUDENT_FILE = (
    "Python/Weekly Problem Sets/Problem Set 5 solution.py"
    if _SOLUTION_MODE
    else "Python/Weekly Problem Sets/Problem Set 5 starter.py"
)


# ---------------------------------------------------------------------------
# Shared fixture — loads the student module once per test session
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def student():
    return load_student_module(STUDENT_FILE, "student_ps5")


# ===========================================================================
# Problem 1
# ===========================================================================
class TestRecursiveSquares:
    """Tests for problem 1, recursive squares"""

    def test_recursive_squares_exists(self, student):
        assert_has_function(student, "recursive_squares")

    def test_squares_empty_list(self, student):
        assert student.recursive_squares(0) == [], "When n = 0, the list should be empty"

    def test_squares_single(self, student):
        assert student.recursive_squares(1) == [1], "When n = 1, the list should be [1]"

    def test_squares_example(self, student):
        assert student.recursive_squares(5) == [
            1,
            4,
            9,
            16,
            25,
        ], "Failed the example of n=5"

    def test_squares_random(self, student):
        for i in range(5):
            n = randint(5, 15)
            ans = student.recursive_squares(n)
            assert len(ans) == n, f"Given n={n}, there should be {n} elements"
            assert ans[-1] == n**2, f"The last element for n={n} should be {n ** 2}"

    def test_squares_recursion(self, student):
        """Verify that recursive_squares() is implemented recursively by counting function calls"""
        n = 5
        expected_result = [1, 4, 9, 16, 25]

        # Track the number of times the function is called
        call_count = 0
        original_func = student.recursive_squares

        def wrapper(num):
            nonlocal call_count
            call_count += 1
            return original_func(num)

        # Temporarily replace the function with our wrapper
        student.recursive_squares = wrapper

        try:
            result = student.recursive_squares(n)
            assert (
                result == expected_result
            ), f"recursive_squares({n}) should return {expected_result}"

            # For n=5, recursion should call the function at least n+1 times
            # (for n=5, 4, 3, 2, 1, 0)
            expected_calls = n
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.recursive_squares = original_func


class TestPalindromeChecker:
    """Tests for problem 1, palindrome checker"""

    def test_palindrome_checker_exists(self, student):
        assert_has_function(student, "palindrome_checker")

    def test_palindrome_empty_string(self, student):
        assert student.palindrome_checker("") == True, "An empty string is a palindrome"

    def test_palindrome_examples(self, student):
        assert student.palindrome_checker("bacon") == False, "Bacon is not a palindrome"
        assert student.palindrome_checker("radar") == True, "Radar is a palindrome"

    def test_palindrome_even_length(self, student):
        for test_case, expected_result in {
            "leer": False,
            "noon": True,
            "deed": True,
            "fear": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_odd_length(self, student):
        for test_case, expected_result in {
            "vader": False,
            "radar": True,
            "level": True,
            "paper": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_sentences(self, student):
        cases = {
            "A man, a plan, a canal: Panama": False,
            "Able was I ere I saw Elba": True,
            "Eva, can I see bees in a cave?": False,
        }
        for test_case, expected_result in {
            "leer": False,
            "noon": True,
            "deed": True,
            "fear": False,
        }.items():
            assert (
                student.palindrome_checker(test_case) == expected_result
            ), f"'{test_case}' is {'' if expected_result else 'not '}a palindrome."

    def test_palindrome_recursion(self, student):
        """Verify that palindrome_checker() is implemented recursively by counting function calls"""
        test_string = "radar"
        expected_result = True

        # Track the number of times the function is called
        call_count = 0
        original_func = student.palindrome_checker

        def wrapper(s):
            nonlocal call_count
            call_count += 1
            return original_func(s)

        # Temporarily replace the function with our wrapper
        student.palindrome_checker = wrapper

        try:
            result = student.palindrome_checker(test_string)
            assert (
                result == expected_result
            ), f"palindrome_checker('{test_string}') should return {expected_result}"

            # For a string of length n, recursion should call the function at least ceil(n/2) + 1 times
            # (checking pairs until reaching base case)
            expected_calls = len(test_string) // 2
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.palindrome_checker = original_func


class TestListLength:
    """Tests for problem 1, flatten"""

    def test_length_exists(self, student):
        assert_has_function(student, "length")

    def test_length_empty_list(self, student):
        assert student.length([]) == 0, "Empty list length should be 0"

    def test_length_example_list(self, student):
        test_data = [1, 2, 3]
        expected_value = 3
        assert student.length(test_data) == 3, f"{test_data} should have length {expected_value}"

    def test_length_nested_list(self, student):
        test_data = [1, [15, 25], 3]
        expected_value = 3
        assert student.length(test_data) == 3, f"{test_data} should have length {expected_value}"

    def test_length_recursion(self, student):
        """Verify that length() is implemented recursively by counting function calls"""
        test_data = [1, 2, 3]
        expected_value = 3

        # Track the number of times the function is called
        call_count = 0
        original_length = student.length

        def wrapper(lst):
            nonlocal call_count
            call_count += 1
            return original_length(lst)

        # Temporarily replace the function with our wrapper
        student.length = wrapper

        try:
            result = student.length(test_data)
            assert result == expected_value, f"{test_data} should have length {expected_value}"

            # For a list of length n, recursion should call the function n+1 times
            # (once for each element + one final call with empty list)
            expected_calls = len(test_data)
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.length = original_length


@pytest.mark.challenge
class TestFlatten:
    """Tests for problem 1, flatten"""

    def test_flatten_exists(self, student):
        assert_has_function(student, "flatten")

    def test_flatten_empty(self, student):
        assert student.flatten([]) == [], "Empty list should be an empty list"

    def test_flatten_example(self, student):
        test_data = [1, [2, 3], [4], 5]
        expected_value = [1, 2, 3, 4, 5]
        assert (
            student.flatten(test_data) == expected_value
        ), f"{test_data} should return {expected_value}"

    def test_flatten_double(self, student):
        test_data = [1, [2, 3, [35]], [4], 5]
        expected_value = [1, 2, 3, 35, 4, 5]
        assert (
            student.flatten(test_data) == expected_value
        ), f"{test_data} should return {expected_value}"

    def test_flatten_more(self, student):
        test_cases = (
            ([[], [4], 5], [4, 5]),
            ([[1, 2], 3, 4], [1, 2, 3, 4]),
            ([[[1, 2], [3, 4]], 5, [6]], [1, 2, 3, 4, 5, 6]),
        )

        for test, ans in test_cases:
            assert student.flatten(test) == ans, f"{test} should return {ans}"

    def test_flatten_recursino(self, student):
        test_data = [1, [2, 3], [4], 5]
        expected_value = [1, 2, 3, 4, 5]

        # Track the number of times the function is called
        call_count = 0
        original_fn = student.flatten

        def wrapper(lst):
            nonlocal call_count
            call_count += 1
            return original_fn(lst)

        # Temporarily replace the function with our wrapper
        student.flatten = wrapper

        try:
            result = student.flatten(test_data)
            assert result == expected_value, f"{test_data} should return {expected_value}"

            # For a list of length n, recursion should call the function n+1 times
            # (once for each element + one final call with empty list)
            expected_calls = len(test_data)
            assert call_count >= 3, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.flatten = original_fn


# ===========================================================================
# Problem 2
# ===========================================================================
class TestFibonacci:
    """Tests for problem 2, fibonacci sequence"""

    def test_fibonacci_exists(self, student):
        assert_has_function(student, "fibonacci")

    def test_fibonacci_base_cases(self, student):
        assert student.fibonacci(0) == 0, "fibonacci(0) should return 0"
        assert student.fibonacci(1) == 1, "fibonacci(1) should return 1"

    def test_fibonacci_examples(self, student):
        assert student.fibonacci(6) == 8, "fibonacci(6) should return 8"

    def test_fibonacci_small_values(self, student):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_value in enumerate(expected):
            assert (
                student.fibonacci(i) == expected_value
            ), f"fibonacci({i}) should return {expected_value}"

    def test_fibonacci_larger_values(self, student):
        test_cases = {
            10: 55,
            12: 144,
            15: 610,
            20: 6765,
        }
        for n, expected in test_cases.items():
            assert student.fibonacci(n) == expected, f"fibonacci({n}) should return {expected}"

    def test_fibonacci_recursion(self, student):
        """Verify that fibonacci() is implemented recursively by counting function calls"""
        n = 5
        expected_result = 5

        # Track the number of times the function is called
        call_count = 0
        original_func = student.fibonacci

        def wrapper(num):
            nonlocal call_count
            call_count += 1
            return original_func(num)

        # Temporarily replace the function with our wrapper
        student.fibonacci = wrapper

        try:
            result = student.fibonacci(n)
            assert result == expected_result, f"fibonacci({n}) should return {expected_result}"

            # For fibonacci with multiple recursion, call count should be much higher than n
            # fibonacci(5) should make at least 10+ calls due to multiple recursion
            expected_calls = n * 2
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for multiple recursive implementation, but got {call_count}. "
                f"Make sure you're using multiple recursion (fibonacci(n-1) + fibonacci(n-2))!"
            )
        finally:
            # Restore the original function
            student.fibonacci = original_func


class TestCountWays:
    """Tests for problem 2, count ways to climb stairs"""

    def test_count_ways_exists(self, student):
        assert_has_function(student, "count_ways")

    def test_count_ways_base_cases(self, student):
        assert (
            student.count_ways(0) == 1
        ), "count_ways(0) should return 1 (one way to stay at ground)"
        assert student.count_ways(1) == 1, "count_ways(1) should return 1 (only one step)"

    def test_count_ways_examples(self, student):
        assert student.count_ways(3) == 3, "count_ways(3) should return 3"
        assert student.count_ways(4) == 5, "count_ways(4) should return 5"

    def test_count_ways_small_values(self, student):
        # The count_ways sequence is actually the Fibonacci sequence shifted by 1
        # count_ways(n) = fibonacci(n+1)
        expected = {
            2: 2,  # 1+1, 2
            5: 8,  # 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1
            6: 13,
            7: 21,
        }
        for n, expected_value in expected.items():
            assert (
                student.count_ways(n) == expected_value
            ), f"count_ways({n}) should return {expected_value}"

    def test_count_ways_larger_values(self, student):
        test_cases = {
            8: 34,
            10: 89,
            12: 233,
        }
        for n, expected in test_cases.items():
            assert student.count_ways(n) == expected, f"count_ways({n}) should return {expected}"

    def test_count_ways_recursion(self, student):
        """Verify that count_ways() is implemented recursively by counting function calls"""
        n = 5
        expected_result = 8

        # Track the number of times the function is called
        call_count = 0
        original_func = student.count_ways

        def wrapper(num):
            nonlocal call_count
            call_count += 1
            return original_func(num)

        # Temporarily replace the function with our wrapper
        student.count_ways = wrapper

        try:
            result = student.count_ways(n)
            assert result == expected_result, f"count_ways({n}) should return {expected_result}"

            # For multiple recursion, call count should be much higher than n
            expected_calls = n * 2
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for multiple recursive implementation, but got {call_count}. "
                f"Make sure you're using multiple recursion!"
            )
        finally:
            # Restore the original function
            student.count_ways = original_func


class TestGridPaths:
    """Tests for problem 2, grid paths"""

    def test_grid_paths_exists(self, student):
        assert_has_function(student, "grid_paths")

    def test_grid_paths_base_cases(self, student):
        assert student.grid_paths(1, 1) == 1, "grid_paths(1, 1) should return 1"
        assert (
            student.grid_paths(1, 5) == 1
        ), "grid_paths(1, n) should return 1 (only one path along edge)"
        assert (
            student.grid_paths(5, 1) == 1
        ), "grid_paths(m, 1) should return 1 (only one path along edge)"

    def test_grid_paths_examples(self, student):
        assert student.grid_paths(2, 2) == 2, "grid_paths(2, 2) should return 2"
        assert student.grid_paths(3, 3) == 6, "grid_paths(3, 3) should return 6"

    def test_grid_paths_small_grids(self, student):
        test_cases = {
            (2, 3): 3,
            (3, 2): 3,
            (2, 4): 4,
            (4, 2): 4,
            (3, 4): 10,
            (4, 3): 10,
        }
        for (m, n), expected in test_cases.items():
            assert (
                student.grid_paths(m, n) == expected
            ), f"grid_paths({m}, {n}) should return {expected}"

    def test_grid_paths_larger_grids(self, student):
        test_cases = {
            (4, 4): 20,
            (5, 5): 70,
            (3, 7): 28,
            (6, 4): 56,
        }
        for (m, n), expected in test_cases.items():
            assert (
                student.grid_paths(m, n) == expected
            ), f"grid_paths({m}, {n}) should return {expected}"

    def test_grid_paths_recursion(self, student):
        """Verify that grid_paths() is implemented recursively by counting function calls"""
        m, n = 3, 3
        expected_result = 6

        # Track the number of times the function is called
        call_count = 0
        original_func = student.grid_paths

        def wrapper(rows, cols):
            nonlocal call_count
            call_count += 1
            return original_func(rows, cols)

        # Temporarily replace the function with our wrapper
        student.grid_paths = wrapper

        try:
            result = student.grid_paths(m, n)
            assert (
                result == expected_result
            ), f"grid_paths({m}, {n}) should return {expected_result}"

            # For multiple recursion, call count should be higher than just m or n
            expected_calls = m + n
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for multiple recursive implementation, but got {call_count}. "
                f"Make sure you're using multiple recursion!"
            )
        finally:
            # Restore the original function
            student.grid_paths = original_func


@pytest.mark.challenge
class TestPermutations:
    """Tests for problem 2, permutations (challenge)"""

    def test_permutations_exists(self, student):
        assert_has_function(student, "permutations")

    def test_permutations_empty(self, student):
        result = student.permutations([])
        assert result == [[]], "permutations([]) should return [[]]"

    def test_permutations_single(self, student):
        result = student.permutations([1])
        assert len(result) == 1, "permutations([1]) should have 1 permutation"
        assert [1] in result, "permutations([1]) should contain [1]"

    def test_permutations_two_elements(self, student):
        result = student.permutations([1, 2])
        assert len(result) == 2, "permutations([1, 2]) should have 2 permutations (2!)"
        assert [1, 2] in result, "permutations([1, 2]) should contain [1, 2]"
        assert [2, 1] in result, "permutations([1, 2]) should contain [2, 1]"

    def test_permutations_three_elements(self, student):
        result = student.permutations([1, 2, 3])
        expected_perms = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        assert len(result) == 6, "permutations([1, 2, 3]) should have 6 permutations (3!)"
        for perm in expected_perms:
            assert perm in result, f"permutations([1, 2, 3]) should contain {perm}"

    def test_permutations_four_elements(self, student):
        result = student.permutations([1, 2, 3, 4])
        assert len(result) == 24, "permutations([1, 2, 3, 4]) should have 24 permutations (4!)"
        # Check a few specific permutations
        assert [1, 2, 3, 4] in result
        assert [4, 3, 2, 1] in result
        assert [2, 1, 4, 3] in result

    def test_permutations_unique(self, student):
        """Verify all permutations are unique"""
        result = student.permutations([1, 2, 3])
        # Convert to tuples for set comparison
        result_tuples = [tuple(perm) for perm in result]
        assert len(result_tuples) == len(set(result_tuples)), "All permutations should be unique"

    def test_permutations_recursion(self, student):
        """Verify that permutations() is implemented recursively by counting function calls"""
        test_data = [1, 2, 3]
        expected_count = 6

        # Track the number of times the function is called
        call_count = 0
        original_func = student.permutations

        def wrapper(lst):
            nonlocal call_count
            call_count += 1
            return original_func(lst)

        # Temporarily replace the function with our wrapper
        student.permutations = wrapper

        try:
            result = student.permutations(test_data)
            assert (
                len(result) == expected_count
            ), f"permutations({test_data}) should return {expected_count} permutations"

            # For multiple recursion with permutations, we expect many recursive calls
            expected_calls = len(test_data) * 2
            assert call_count >= expected_calls, (
                f"Expected at least {expected_calls} function calls for recursive implementation, but got {call_count}. "
                f"Make sure you're using recursion!"
            )
        finally:
            # Restore the original function
            student.permutations = original_func


# ===========================================================================
# Problem 3
# ===========================================================================
class TestGetUser:
    """Tests for problem 3, get_user function"""

    def test_get_user_exists(self, student):
        assert_has_function(student, "get_user")

    def test_get_user_valid(self, student):
        user = student.get_user(2)
        assert isinstance(user, dict), "get_user should return a dictionary"
        assert "id" in user, "User should have an 'id' field"
        assert user["id"] == 2, "User ID should match the requested ID"
        assert "email" in user, "User should have an 'email' field"
        assert "name" in user, "User should have a 'name' field"
        assert "username" in user, "User should have a 'username' field"

    def test_get_user_multiple(self, student):
        """Test multiple valid user IDs"""
        for user_id in [1, 3, 5]:
            user = student.get_user(user_id)
            assert isinstance(user, dict), f"get_user({user_id}) should return a dictionary"
            assert user.get("id") == user_id, f"User ID should be {user_id}"

    def test_get_user_invalid(self, student):
        """Test invalid user ID returns empty dict"""
        user = student.get_user(999)
        assert user == {}, "get_user with invalid ID should return empty dictionary"


class TestCreateUser:
    """Tests for problem 3, create_user function"""

    def test_create_user_exists(self, student):
        assert_has_function(student, "create_user")

    def test_create_user_basic(self, student):
        result = student.create_user("John Doe", "Developer")
        assert isinstance(result, dict), "create_user should return a dictionary"
        assert "name" in result, "Result should have a 'name' field"
        assert result["name"] == "John Doe", "Name should match the input"
        assert "job" in result, "Result should have a 'job' field"
        assert result["job"] == "Developer", "Job should match the input"
        assert "id" in result, "Result should have an 'id' field"

    def test_create_user_different_data(self, student):
        """Test creating users with different data"""
        test_cases = [
            ("Alice Smith", "Designer"),
            ("Bob Johnson", "Manager"),
            ("Carol White", "Engineer"),
        ]
        for name, job in test_cases:
            result = student.create_user(name, job)
            assert result["name"] == name, f"Name should be {name}"
            assert result["job"] == job, f"Job should be {job}"


class TestUpdateUser:
    """Tests for problem 3, update_user function"""

    def test_update_user_exists(self, student):
        assert_has_function(student, "update_user")

    def test_update_user_basic(self, student):
        result = student.update_user(2, "Jane Smith", "Manager")
        assert isinstance(result, dict), "update_user should return a dictionary"
        assert "name" in result, "Result should have a 'name' field"
        assert result["name"] == "Jane Smith", "Name should match the input"
        assert "job" in result, "Result should have a 'job' field"
        assert result["job"] == "Manager", "Job should match the input"

    def test_update_user_multiple(self, student):
        """Test updating different users"""
        for user_id in [1, 3, 5]:
            result = student.update_user(user_id, "Test User", "Tester")
            assert isinstance(result, dict), f"update_user({user_id}) should return a dictionary"
            assert result["name"] == "Test User", "Name should be updated"
            assert result["job"] == "Tester", "Job should be updated"


class TestDeleteUser:
    """Tests for problem 3, delete_user function"""

    def test_delete_user_exists(self, student):
        assert_has_function(student, "delete_user")

    def test_delete_user_valid(self, student):
        result = student.delete_user(2)
        assert isinstance(result, bool), "delete_user should return a boolean"
        assert result is True, "delete_user should return True for successful deletion"

    def test_delete_user_multiple(self, student):
        """Test deleting multiple users"""
        for user_id in [1, 3, 5, 10]:
            result = student.delete_user(user_id)
            assert result is True, f"delete_user({user_id}) should return True"


@pytest.mark.challenge
class TestGetUsersPage:
    """Tests for problem 3, get_all_users function (challenge)"""

    def test_get_users_page_exists(self, student):
        assert_has_function(student, "get_users_page")

    def test_get_users_basic(self, student):
        users = student.get_users_page()
        assert isinstance(users, list), "get_users_page should return a list"
        assert len(users) > 0, "Should return users"
        # Check that users are dictionaries with expected fields
        assert all("id" in user for user in users), "All users should have 'id' field"
        assert all("email" in user for user in users), "All users should have 'email' field"
        assert all("first_name" in user for user in users), "All users should have 'first_name' field"

    def test_get_users_ids(self, student):
        """Test that all user IDs are present"""
        users = student.get_users_page()
        user_ids = [user["id"] for user in users]
        expected_ids = list(range(1, 7))
        assert user_ids == expected_ids, "Should return users with IDs 1-6"


@pytest.mark.challenge
class TestPartialUpdateUser:
    """Tests for problem 3, partial_update_user function (challenge)"""

    def test_partial_update_user_exists(self, student):
        assert_has_function(student, "partial_update_user")

    def test_partial_update_single_field(self, student):
        result = student.partial_update_user(2, {"job": "Senior Developer"})
        assert isinstance(result, dict), "partial_update_user should return a dictionary"
        assert "job" in result, "Result should have a 'job' field"
        assert result["job"] == "Senior Developer", "Job should be updated"

    def test_partial_update_multiple_fields(self, student):
        updates = {"name": "John Smith", "job": "Team Lead"}
        result = student.partial_update_user(3, updates)
        assert isinstance(result, dict), "partial_update_user should return a dictionary"
        assert result["name"] == "John Smith", "Name should be updated"
        assert result["job"] == "Team Lead", "Job should be updated"

    def test_partial_update_different_users(self, student):
        """Test partial updates on different users"""
        for user_id in [1, 4, 7]:
            result = student.partial_update_user(user_id, {"job": "Updated Job"})
            assert isinstance(
                result, dict
            ), f"partial_update_user({user_id}) should return a dictionary"
            assert result["job"] == "Updated Job", "Job should be updated"


# ===========================================================================
# Problem 4
# ===========================================================================
class TestSearchMovie:
    """Tests for problem 4, search_movie function"""

    def test_search_movie_exists(self, student):
        assert_has_function(student, "search_movie")

    def test_search_movie_valid(self, student, mocker):
        """Test searching for a movie with valid API key"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 550,
                    "title": "Fight Club",
                    "release_date": "1999-10-15",
                    "overview": "A ticking-time-bomb insomniac...",
                    "vote_average": 8.4,
                }
            ]
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.search_movie("fake_api_key", "Fight Club")
        assert isinstance(result, dict), "search_movie should return a dictionary"
        assert result.get("id") == 550, "Should return the first result"
        assert result.get("title") == "Fight Club", "Title should match"

    def test_search_movie_multiple_results(self, student, mocker):
        """Test that only the first result is returned"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {"id": 1, "title": "Movie One"},
                {"id": 2, "title": "Movie Two"},
                {"id": 3, "title": "Movie Three"},
            ]
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.search_movie("fake_api_key", "Movie")
        assert result.get("id") == 1, "Should return the first result only"

    def test_search_movie_no_results(self, student, mocker):
        """Test when no movies are found"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": []}
        mocker.patch("requests.get", return_value=mock_response)

        result = student.search_movie("fake_api_key", "NonexistentMovie123456")
        assert result == {}, "Should return empty dict when no results"

    def test_search_movie_api_error(self, student, mocker):
        """Test handling API errors"""
        mock_response = Mock()
        mock_response.status_code = 401
        mocker.patch("requests.get", return_value=mock_response)

        result = student.search_movie("invalid_key", "Fight Club")
        assert result == {}, "Should return empty dict on API error"


class TestGetGithubUser:
    """Tests for problem 4, get_github_user function"""

    def test_get_github_user_exists(self, student):
        assert_has_function(student, "get_github_user")

    def test_get_github_user_valid(self, student, mocker):
        """Test getting a valid GitHub user"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "login": "octocat",
            "id": 1,
            "name": "The Octocat",
            "company": "GitHub",
            "blog": "https://github.blog",
            "location": "San Francisco",
            "email": None,
            "bio": "GitHub mascot",
            "public_repos": 8,
            "followers": 1000,
            "following": 5,
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_github_user("fake_token", "octocat")
        assert isinstance(result, dict), "get_github_user should return a dictionary"
        assert result.get("login") == "octocat", "Login should match"
        assert result.get("id") == 1, "ID should match"
        assert "public_repos" in result, "Should include public_repos"

    def test_get_github_user_different_users(self, student, mocker):
        """Test getting different users"""
        test_users = ["torvalds", "gvanrossum", "octocat"]
        for username in test_users:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "login": username,
                "id": 12345,
                "name": f"Test {username}",
            }
            mocker.patch("requests.get", return_value=mock_response)

            result = student.get_github_user("fake_token", username)
            assert result.get("login") == username, f"Login should be {username}"

    def test_get_github_user_not_found(self, student, mocker):
        """Test when user doesn't exist"""
        mock_response = Mock()
        mock_response.status_code = 404
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_github_user("fake_token", "nonexistentuser123456789")
        assert result == {}, "Should return empty dict when user not found"

    def test_get_github_user_invalid_token(self, student, mocker):
        """Test with invalid authentication token"""
        mock_response = Mock()
        mock_response.status_code = 401
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_github_user("invalid_token", "octocat")
        assert result == {}, "Should return empty dict with invalid token"


class TestCreateGist:
    """Tests for problem 4, create_gist function"""

    def test_create_gist_exists(self, student):
        assert_has_function(student, "create_gist")

    def test_create_gist_valid(self, student, mocker):
        """Test creating a gist successfully"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": "abc123def456",
            "url": "https://api.github.com/gists/abc123def456",
            "html_url": "https://gist.github.com/abc123def456",
            "files": {"test.py": {"filename": "test.py", "content": "print('Hello, World!')"}},
            "description": "Test gist",
            "public": True,
        }
        mocker.patch("requests.post", return_value=mock_response)

        result = student.create_gist("fake_token", "Test gist", "test.py", "print('Hello, World!')")
        assert isinstance(result, str), "create_gist should return a string"
        assert result == "abc123def456", "Should return the gist ID"

    def test_create_gist_different_files(self, student, mocker):
        """Test creating gists with different filenames and content"""
        test_cases = [
            ("example.js", "console.log('test');", "JavaScript example"),
            ("README.md", "# My Project", "Markdown readme"),
            ("config.json", '{"key": "value"}', "JSON config"),
        ]

        for filename, content, description in test_cases:
            mock_response = Mock()
            mock_response.status_code = 201
            mock_response.json.return_value = {"id": f"gist_{filename}"}
            mocker.patch("requests.post", return_value=mock_response)

            result = student.create_gist("fake_token", description, filename, content)
            assert result == f"gist_{filename}", f"Should return gist ID for {filename}"

    def test_create_gist_api_error(self, student, mocker):
        """Test handling API errors"""
        mock_response = Mock()
        mock_response.status_code = 401
        mocker.patch("requests.post", return_value=mock_response)

        result = student.create_gist("invalid_token", "Test", "test.txt", "content")
        assert result == "", "Should return empty string on API error"

    def test_create_gist_no_id_in_response(self, student, mocker):
        """Test when API doesn't return an ID"""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {}
        mocker.patch("requests.post", return_value=mock_response)

        result = student.create_gist("fake_token", "Test", "test.txt", "content")
        assert result == "", "Should return empty string when no ID in response"


class TestDeleteGist:
    """Tests for problem 4, delete_gist function"""

    def test_delete_gist_exists(self, student):
        assert_has_function(student, "delete_gist")

    def test_delete_gist_success(self, student, mocker):
        """Test successfully deleting a gist"""
        mock_response = Mock()
        mock_response.status_code = 204
        mocker.patch("requests.delete", return_value=mock_response)

        result = student.delete_gist("fake_token", "abc123def456")
        assert result is True, "delete_gist should return True on successful deletion"

    def test_delete_gist_multiple(self, student, mocker):
        """Test deleting multiple gists"""
        mock_response = Mock()
        mock_response.status_code = 204
        mocker.patch("requests.delete", return_value=mock_response)

        gist_ids = ["gist1", "gist2", "gist3"]
        for gist_id in gist_ids:
            result = student.delete_gist("fake_token", gist_id)
            assert result is True, f"Should return True for deleting {gist_id}"

    def test_delete_gist_not_found(self, student, mocker):
        """Test deleting a non-existent gist"""
        mock_response = Mock()
        mock_response.status_code = 404
        mocker.patch("requests.delete", return_value=mock_response)

        result = student.delete_gist("fake_token", "nonexistent")
        assert result is False, "Should return False when gist not found"

    def test_delete_gist_unauthorized(self, student, mocker):
        """Test deleting with invalid token"""
        mock_response = Mock()
        mock_response.status_code = 401
        mocker.patch("requests.delete", return_value=mock_response)

        result = student.delete_gist("invalid_token", "abc123")
        assert result is False, "Should return False with invalid token"

    def test_delete_gist_forbidden(self, student, mocker):
        """Test deleting a gist you don't own"""
        mock_response = Mock()
        mock_response.status_code = 403
        mocker.patch("requests.delete", return_value=mock_response)

        result = student.delete_gist("fake_token", "someone_elses_gist")
        assert result is False, "Should return False when forbidden"


@pytest.mark.challenge
class TestGetSpotifyTrackInfo:
    """Tests for problem 4, get_spotify_track_info function (challenge)"""

    def test_get_spotify_track_info_exists(self, student):
        assert_has_function(student, "get_spotify_track_info")

    def test_get_spotify_track_info_valid(self, student, mocker):
        """Test getting valid track information"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "3n3Ppam7vgaVa1iaRUc9Lp",
            "name": "Mr. Brightside",
            "artists": [{"name": "The Killers", "id": "0C0XlULifJtAgn6ZNCW2eu"}],
            "album": {"name": "Hot Fuss", "release_date": "2004-06-07"},
            "duration_ms": 222973,
            "popularity": 85,
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_spotify_track_info("fake_access_token", "3n3Ppam7vgaVa1iaRUc9Lp")
        assert isinstance(result, dict), "get_spotify_track_info should return a dictionary"
        assert result.get("name") == "Mr. Brightside", "Track name should match"
        assert result.get("artist") == "The Killers", "Artist name should match"
        assert result.get("album") == "Hot Fuss", "Album name should match"
        assert result.get("duration_ms") == 222973, "Duration should match"

    def test_get_spotify_track_info_multiple_artists(self, student, mocker):
        """Test track with multiple artists (should return first artist)"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "Collaboration Song",
            "artists": [{"name": "Artist One"}, {"name": "Artist Two"}, {"name": "Artist Three"}],
            "album": {"name": "Collab Album"},
            "duration_ms": 180000,
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_spotify_track_info("fake_access_token", "track123")
        assert result.get("artist") == "Artist One", "Should return the first artist"

    def test_get_spotify_track_info_different_tracks(self, student, mocker):
        """Test getting information for different tracks"""
        test_tracks = [
            ("track1", "Song A", "Band A", "Album A", 200000),
            ("track2", "Song B", "Band B", "Album B", 250000),
            ("track3", "Song C", "Band C", "Album C", 180000),
        ]

        for track_id, name, artist, album, duration in test_tracks:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "name": name,
                "artists": [{"name": artist}],
                "album": {"name": album},
                "duration_ms": duration,
            }
            mocker.patch("requests.get", return_value=mock_response)

            result = student.get_spotify_track_info("fake_token", track_id)
            assert result["name"] == name, f"Track name should be {name}"
            assert result["artist"] == artist, f"Artist should be {artist}"
            assert result["album"] == album, f"Album should be {album}"
            assert result["duration_ms"] == duration, f"Duration should be {duration}"

    def test_get_spotify_track_info_not_found(self, student, mocker):
        """Test when track doesn't exist"""
        mock_response = Mock()
        mock_response.status_code = 404
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_spotify_track_info("fake_token", "nonexistent_track")
        assert result == {}, "Should return empty dict when track not found"

    def test_get_spotify_track_info_invalid_token(self, student, mocker):
        """Test with invalid access token"""
        mock_response = Mock()
        mock_response.status_code = 401
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_spotify_track_info("invalid_token", "track123")
        assert result == {}, "Should return empty dict with invalid token"

    def test_get_spotify_track_info_missing_fields(self, student, mocker):
        """Test handling API response with missing fields"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "Incomplete Song"
            # Missing artists, album, duration_ms
        }
        mocker.patch("requests.get", return_value=mock_response)

        result = student.get_spotify_track_info("fake_token", "track123")
        assert result.get("name") == "Incomplete Song", "Should have name"
        assert result.get("artist") == "", "Should return empty string for missing artist"
        assert result.get("album") == "", "Should return empty string for missing album"
        assert result.get("duration_ms") == 0, "Should return 0 for missing duration"
