"""
Shared pytest configuration for all Problem Set autograders.

Each test file defines its own `student` fixture that calls `load_student_module()`
with the path to that problem set's starter file.  This keeps every problem set
self-contained while sharing the import infrastructure.

Usage in a test file
--------------------
    import pytest
    from conftest import load_student_module

    STUDENT_FILE = "Python/Weekly Problem Sets/Problem Set 4 starter.py"

    @pytest.fixture(scope="module")
    def student():
        return load_student_module(STUDENT_FILE, "student_ps4")
"""

import importlib.util
import sys
from pathlib import Path

import pytest


# Repo root is three levels up from this file:
#   .github/python_tests/conftest.py  →  .github/python_tests  →  .github  →  repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _candidate_paths(relative_path: str) -> list[Path]:
    """
    Return an ordered list of file paths to try for a given starter path.

    Given "Python/Weekly Problem Sets/Problem Set 4 starter.py" this produces:
      1. .../Problem Set 4.py           (with ' starter' stripped — checked first)
      2. .../Problem Set 4 starter.py   (exact name as specified — fallback)
    """
    primary = REPO_ROOT / relative_path
    stem = primary.stem  # e.g. "Problem Set 4 starter"
    short_stem = stem.replace(" starter", "").replace(" Starter", "")
    short = primary.with_stem(short_stem)
    candidates = [short] if short != primary else []
    candidates.append(primary)
    return candidates


def load_student_module(relative_path: str, module_name: str):
    """
    Import a student's Python file by its repo-relative path and return the module.

    Parameters
    ----------
    relative_path : str
        Path to the student file relative to the repo root, using forward slashes.
        Spaces in the path are fine (e.g. "Python/Weekly Problem Sets/Problem Set 4 starter.py").
        If the exact file is not found, the loader also tries the same name with
        ' starter' removed (e.g. "Problem Set 4.py") before failing.
    module_name : str
        Unique internal name for sys.modules (e.g. "student_ps4").  Use a different
        name for each problem set so they don't collide when all tests run together.

    Raises
    ------
    pytest.fail  —  with a student-readable message if the file is missing or has a
                    syntax error, so the test run fails cleanly instead of crashing.
    """
    candidates = _candidate_paths(relative_path)
    file_path = next((p for p in candidates if p.exists()), None)

    if file_path is None:
        names = "  or  ".join(f"'{p.name}'" for p in candidates)
        pytest.fail(
            "\n\nStudent file not found. Expected one of:\n"
            + "".join(f"  • {p}\n" for p in candidates)
            + f"\nMake sure your file is named {names} "
            f"and is saved in '{candidates[0].parent}'.",
            pytrace=False,
        )

    print(f"\n[autograder] Loading student file: {file_path}")

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module

    try:
        spec.loader.exec_module(module)
    except SyntaxError as exc:
        pytest.fail(
            f"\n\nSyntax error in '{relative_path}':\n  {exc}\n"
            f"Fix the syntax error and push again.",
            pytrace=False,
        )
    except Exception as exc:
        pytest.fail(
            f"\n\nYour script raised an error when imported:\n  {type(exc).__name__}: {exc}\n"
            f"Make sure all top-level code is inside an 'if __name__ == \"__main__\":' block.",
            pytrace=False,
        )

    return module


def assert_has_function(module, func_name: str):
    """
    Assert that `module` exposes a callable named `func_name`.

    Provides a clear student-facing message when a required function is missing
    or not yet implemented (still `pass`).
    """
    assert hasattr(module, func_name) and callable(getattr(module, func_name)), (
        f"\n\nFunction '{func_name}()' was not found in your submission.\n"
        f"Check that:\n"
        f"  1. The function is defined at the top level (not inside another function).\n"
        f"  2. The spelling and capitalisation exactly match '{func_name}'.\n"
        f"  3. The function body is not still 'pass' with no return value."
    )
