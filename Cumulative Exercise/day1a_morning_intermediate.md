# 1. Day 1 - Morning - Intermediate
The intermediate exercises build on the basic exercises.  Stop and do those before starting here.

The intermediate exercises are much less prescriptive but should give you some ideas on techniques and problems to practice to further hone your skills.

- [1. Day 1 - Morning - Intermediate](#1-day-1---morning---intermediate)
- [2. Intermediate Exercises](#2-intermediate-exercises)
  - [2.1. Long-term Storage](#21-long-term-storage)
  - [2.2. Environment Variables](#22-environment-variables)
  - [2.3. Testing](#23-testing)
  - [2.4. Pre-commit](#24-pre-commit)


# 2. Intermediate Exercises
## 2.1. Long-term Storage
- Implement an endpoint that stores data in a database and provides it back to the user upon request (e.g. posts or articles)
- Implement an endpoint that receives that data

## 2.2. Environment Variables
- Utilize environment variables or a secrets manager to store your API key
- Utilize environment variables or a secrets manager to store your database access credentials

## 2.3. Testing
- Create appropriate, reusable fixtures for your test cases
- Determine best fixture scoping for your fixtures
- Mock the appropriate API calls so that your unit tests are independent of external services
- Create a series of integration tests to validate your code ties nicely with other services

## 2.4. Pre-commit
- Adjust your pre-commit hooks so that they only occur during specific stages (pre-commit, pre-push, pre-commit-merge, etc)
- Add a static security analyzer such as bandit
- Experiment with pre-commit 
