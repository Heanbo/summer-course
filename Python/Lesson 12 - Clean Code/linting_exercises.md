# Hands-On: Code Formatting and Linting in Python

These exercises will help you learn to automatically format Python code using tools like `black`, and identify problems using linters like `pylint`.

- [Hands-On: Code Formatting and Linting in Python](#hands-on-code-formatting-and-linting-in-python)
  - [Hands-On #1](#hands-on-1)
    - [Exercise 0:](#exercise-0)
    - [Exercise 1: Format Code with `black`](#exercise-1-format-code-with-black)
    - [Exercise 2: Format an Entire Directory](#exercise-2-format-an-entire-directory)
    - [Exercise 3: Lint with `pylint`](#exercise-3-lint-with-pylint)
    - [Exercise 4: Type Check with `mypy`](#exercise-4-type-check-with-mypy)
    - [Exercise 5: Format and Lint as a Pre-Commit Hook](#exercise-5-format-and-lint-as-a-pre-commit-hook)
    - [Exercise 6: Add More Tools to Pre-Commit](#exercise-6-add-more-tools-to-pre-commit)


---

## Hands-On #1

### Exercise 0:

1. Clone the following repository:  https://github.com/shafe123/AI2C-python-formatting.git

1. Open the new repository as a folder in VS Code.

1. Install prerequisites via the terminal. (Optional, setup a virtual environment beforehand)
```bash
pip install black pylint pre-commit
```

### Exercise 1: Format Code with `black`

**Goal**: Use `black` to autoformat an unformatted Python script.

1. Install black by running the following command.

2. Look at the file called `messy.py`, it should resemble the following:

```python
def greet(name): print("Hello,"+name)
greet("world")
```

2. Run `black` on the messy.py file.

✅ *Check*: The file should now be properly formatted with consistent indentation and spacing.

🎯 *Extra*:  config VS Code to use black as its autoformatter on python files.

---

### Exercise 2: Format an Entire Directory

**Goal**: Use `black` to format all `.py` files in a project.

1. Inspect the remaining files and observe how they change after running black on the entire directory.

✅ *Check*: All Python files in the current directory and subdirectories are formatted.

---

### Exercise 3: Lint with `pylint`

**Goal**: Use `pylint` to get more detailed feedback.

1. Run `pylint` on `bad_style.py`.

✅ *Check*: You'll receive a score and detailed output for code quality, style, and possible bugs.

🎯 *Extra*:  Run pylint on the whole directory

---

### Exercise 4: Type Check with `mypy`

**Goal**: Use `mypy` to perform static type checking on your Python code.

1. Run `mypy` on `bad_style.py` to check for type-related issues.

✅ *Check*: You should see output indicating any type errors or warnings in the code.

🎯 *Extra*: Try adding type hints to fix some of the errors and run mypy again.

---

### Exercise 5: Format and Lint as a Pre-Commit Hook

**Goal**: Set up autoformatting and linting with `pre-commit` hooks.

1. Create a `.pre-commit-config.yaml` file with a configuration that includes the black formatter and mypy for type checking.

2. Install and run the pre-commit hooks. Note the output of the command.

3. Run the hooks again, did the output change?

✅ *Check*: Try committing and ensure that the files are formatted and checked before committing.

🤚 *Hint*: You can use `git restore *` to change all the files back to the original version that you pulled.

🎯 *Extra*:  Fix the errors and try committing again.

---

### Exercise 6: Add More Tools to Pre-Commit

**Goal**: Enhance your pre-commit workflow by adding additional code quality tools.

1. Update your `.pre-commit-config.yaml` to include more hooks, such as `isort` (for import sorting), `docformatter` (for docstring formatting), and other useful tools like:
   - `mypy` for type checking
   - `bandit` for security checks
   - `trailing-whitespace` and `end-of-file-fixer` from pre-commit-hooks
   - `check-yaml` and `check-json` for file validation
   - `codespell` for spelling checks

2. Reinstall the hooks to update them.

✅ *Check*: Try committing again. Now, in addition to formatting and linting, your code will be checked for types, security issues, spelling, trailing whitespace, and more.
