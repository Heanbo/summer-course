# 1. Day 1 - Morning
In this session you will accomplish the following steps:
1. !Build a small web app in python
2. !Add test cases to your web app
3. !Format, lint, and type check your code
4. Add pre-commit checks locally and push your code

Throughout this exercise, pay special attention to where you are creating files.
Creating a file in the wrong directory may cause the tools that you are using 
to miss those files.

## 1.1. Topics Covered
- FastAPI
- Unit tests
- Formatting and Linting
- Pre-commit checks
- Git repositories, pushing

## 1.2. Intermediate exercises
If you complete these exercises early, proceed to the intermediate level file.

## 1.3. Table of Contents
- [1. Day 1 - Morning](#1-day-1---morning)
  - [1.1. Topics Covered](#11-topics-covered)
  - [1.2. Intermediate exercises](#12-intermediate-exercises)
  - [1.3. Table of Contents](#13-table-of-contents)
- [2. Exercises](#2-exercises)
  - [2.1. !Project Setup](#21-project-setup)
    - [2.1.1. Steps](#211-steps)
    - [2.1.2. Reference material](#212-reference-material)
  - [2.2. !Building a small web app](#22-building-a-small-web-app)
    - [2.2.1. Steps](#221-steps)
    - [2.2.2. Reference material](#222-reference-material)
  - [2.3. !Best Practices](#23-best-practices)
    - [2.3.1. Format, lint, and type checking](#231-format-lint-and-type-checking)
    - [2.3.2. Unit tests](#232-unit-tests)
    - [2.3.3. Reference Material](#233-reference-material)
  - [2.4. Pre-commit Checks](#24-pre-commit-checks)
    - [2.4.1. Steps](#241-steps)
    - [2.4.2. Reference Material](#242-reference-material)
- [3. Congrats](#3-congrats)


# 2. Exercises

## 2.1. !Project Setup
In this phase, you will setup your environment so that you can complete the follow-on tasks:

### 2.1.1. Steps
1. Create a repository in GitHub
2. Track the remote repository locally, or clone the remote repository locally
3. Create a virtual environment in your repository
4. Create a `requirements.txt` file to specify the `fastapi` and `uvicorn` dependencies
5. Activate the virtual environment and install the dependencies in the environment
6. Add any relevant folders or files to the `.gitignore` file
7. Push the current setup to your repository

### 2.1.2. Reference material
- [Quick FastAPI start](https://www.tutorialspoint.com/fastapi/fastapi_hello_world.htm)
- [venvs / requirements](https://docs.python.org/3/tutorial/venv.html)
- [git init vs clone](https://github.com/git-guides/git-init)

## 2.2. !Building a small web app
Now it's time to build a small web app.  We'll start with testing it locally and worry about other 
details later.

### 2.2.1. Steps
1. Create a new folder called `web_app` to store the web app files.
2. Create a new file called `main.py` for your fastapi code.
3. Using fastapi within `main.py`, create a simple web page at the root URL `/` that responds to 
`GET` Requests
4. Start your web server and navigate to the root to validate the basic infrastructure works
5. Add another another `POST` endpoint that takes `city`, and `state` as inputs and returns the `lat`/`long`
    - You can "consume" another API to do this conversion for you
    - Make sure to add some validation to the inputs (what if the user provides no state? etc)
    - It's generally bad practice to hard code API keys in your source control, but it's fine for this practice.  Alternatively, use the `dotenv` package to load a `.env` file.
    - Make sure to add some validation or retries when you call the other API (what if they never 
respond? etc)
    - Hint: it's easier to use path parameters here

### 2.2.2. Reference material
- [Quick FastAPI start](https://www.tutorialspoint.com/fastapi/fastapi_hello_world.htm)
- [Free name to lat/long API](https://geocode.maps.co/docs/endpoints/)
- [Later reading: async keyword](https://realpython.com/async-io-python/)

## 2.3. !Best Practices
You may have to add some new tools for this section.  Be sure to add them to your 
`requirements.txt` file.
### 2.3.1. Format, lint, and type checking
1. Format and lint your code using black and pylint (you'll want to ignore your venv folder)
2. Run mypy on your code (you'll want to ignore your venv folder)

### 2.3.2. Unit tests
1. Add unit tests to your code (typically this would be in the `web_app/tests/` folder)
2. Determine the code coverage of your unit tests
3. How should you "test" your code with the other API?  How do you make the tests
reproducible without relying on the other service? (no need to implement but think about)
4. Validate your changes and push your code

### 2.3.3. Reference Material
- [Sample Black config file](./samples/.black)
- [Sample pylint config file](./samples/.pylintrc)
- [Sample pytest config file](./samples/pytest.ini)
- [Sample mypy config file](./samples/mypy.ini)
- [Pytest unit testing](https://docs.pytest.org/en/stable/how-to/assert.html)

## 2.4. Pre-commit Checks
You may have to add some new tools for this section.  Be sure to add them to your 
`requirements.txt` file.

### 2.4.1. Steps
1. Create a new branch
2. Write your pre-commit config file (`.pre-commit-config.yaml`)
    - black
    - pylint
    - mypy
    - pytest
3. Install the pre-commit hooks to your repo
4. Run the hooks against all files in the repo (by default it only runs against
changed files)
5. Commit and push your changes (your pre-commit tools should run here)
    - Some tools fix the files (mostly formatters) so you can simply re-run
    - Other tools you need to go back and fix the issues before re-running

### 2.4.2. Reference Material
- [Pre-commit sample config](https://github.com/PramodKumarYadav/pre-commit-hook-for-python/blob/main/.pre-commit-config.yaml)


# 3. Congrats
If you made it this far, you've completed the basic exercises for the morning.  Enjoy the well-earned taste of success!  If you have time, consider doing the intermediate exercises.