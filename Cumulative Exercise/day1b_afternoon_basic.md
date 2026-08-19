# 1. Day 1 - Afternoon
In this session you will accomplish the following steps:
1. !Create a GH Actions pipeline in a new branch
2. !Validate your pipeline with a pull request
3. Add a new feature -- branch, test cases, code, push, merge

## 1.1. Topics Covered
- GH Actions
  - On
  - Jobs
  - Steps
- Git branching
- GH Pull Request

## 1.2. Intermediate exercises
If you complete these exercises early, proceed to the intermediate level file.

## 1.3. Table of Contents
- [1. Day 1 - Afternoon](#1-day-1---afternoon)
  - [1.1. Topics Covered](#11-topics-covered)
  - [1.2. Intermediate exercises](#12-intermediate-exercises)
  - [1.3. Table of Contents](#13-table-of-contents)
- [2. Exercises](#2-exercises)
  - [2.1. !Create a GH Actions pipeline in a new branch](#21-create-a-gh-actions-pipeline-in-a-new-branch)
    - [2.1.1. Steps](#211-steps)
    - [2.1.2. Reference Material](#212-reference-material)
  - [2.2. !Validate your pipeline with a pull request](#22-validate-your-pipeline-with-a-pull-request)
  - [2.3. Add a new feature](#23-add-a-new-feature)
- [3. Congrats](#3-congrats)


# 2. Exercises

## 2.1. !Create a GH Actions pipeline in a new branch
### 2.1.1. Steps
1. Create a new branch that is reflected in both the local and remote repos
2. Build a CI pipeline using GH Actions
   1. Should run on any push or pull request to the main branch, or manually
   2. Checks formatting, linting, type checks, and unit tests for your web app.
   - Hint:  It's easiest to do this all in one job
   - Hint:  The easiest way to start with steps is to use the `run` instruction with the same commands you type in your terminal
3. Test your workflow by manually dispatching the workflow from the current branch

### 2.1.2. Reference Material
- [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [Simple GH steps](https://docs.github.com/en/actions/tutorials/build-and-test-code/python#installing-dependencies)
- [Jobs vs Steps](https://runs-on.com/github-actions/jobs-and-steps/)

## 2.2. !Validate your pipeline with a pull request
1. Open a pull request back to the main branch, observe the results of your new workflow in the pull request
2. Once the workflow passes, merge your new feature back into main

## 2.3. Add a new feature
1.  Identify a new feature for your web app.  Some ideas are listed below
    - Convert a lat/long to a weather forecast
    - Allow people to write and list comments (how will you store them?)
    - Provide a random image from a series of images (like a random photo album)
    - Display the latest news story from an RSS feed
2. Do the same checks / tests as you did for the other features
3. Do you need to change anything with your other commands or CI workflow for this new feature?

# 3. Congrats
If you made it this far, you've completed the basic exercises for the day.  You've built a small web app and implemented some common software engineering tools!  If you have time, consider doing the intermediate exercises.