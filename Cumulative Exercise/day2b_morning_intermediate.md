# 1. Day 2 - Morning - Intermediate
The intermediate exercises build on the basic exercises.  Stop and do those before starting here.

The intermediate exercises are much less prescriptive but should give you some ideas on techniques and problems to practice to further hone your skills.

- [1. Day 2 - Morning - Intermediate](#1-day-2---morning---intermediate)
- [2. Intermediate Exercises](#2-intermediate-exercises)
  - [2.1. Docker image](#21-docker-image)
  - [2.2. Docker compose](#22-docker-compose)
  - [2.3. Update build pipeline](#23-update-build-pipeline)


# 2. Intermediate Exercises
## 2.1. Docker image
- Update your code to use environment variables for the host address and port numbers
- Update your docker image to use those same environment variables
- Utilize a different user than `root` in your docker image
- Run a `docker scout` scan on your image and resolve any vulnerabilities

## 2.2. Docker compose
- If you implemented long-term storage previously, utilize docker compose to startup a database container alongside your image
- Put the two containers in their own network using docker compose
- Name the database volume explicitly in docker compose
- Test your app using docker compose locally

## 2.3. Update build pipeline
- Utilize an image scanner like `docker scout` to scan your image after being built in the pipeline
- Add an SBOM and security report to your pipeline artifacts
- Write a smoke test using docker compose in your pipeline (this can be fragile)
