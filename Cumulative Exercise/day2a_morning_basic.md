# 1. Day 2 - Morning
In this session you will accomplish the following steps:
1. !Build a docker image in a new branch
2. Update your pipeline to build & push the image
3.  Merge your changes in

## 1.1. Topics Covered
- Dockerfiles
- Docker images, Docker build
- GitHub Container Registry

## 1.2. Intermediate exercises
If you complete these exercises early, proceed to the intermediate level file.

## 1.3. Table of Contents
- [1. Day 2 - Morning](#1-day-2---morning)
  - [1.1. Topics Covered](#11-topics-covered)
  - [1.2. Intermediate exercises](#12-intermediate-exercises)
  - [1.3. Table of Contents](#13-table-of-contents)
- [2. Exercises](#2-exercises)
  - [2.1. !Build a docker image](#21-build-a-docker-image)
    - [2.1.1. Steps](#211-steps)
    - [2.1.2. Reference Material](#212-reference-material)
  - [2.2. Update your pipeline to build \& push](#22-update-your-pipeline-to-build--push)
    - [2.2.1. Steps](#221-steps)
    - [2.2.2. Reference Material](#222-reference-material)
- [3. Congrats](#3-congrats)

# 2. Exercises
Make sure your docker engine is running before starting these exercises

## 2.1. !Build a docker image
### 2.1.1. Steps
1. Create a new branch that is reflected in both the local and remote repos
2. Write a dockerfile that containerizes your web app
  - Start simple with just a basic python container
  - Build up from there
  - Your `RUN` commands will be similar to how your run your web app locally
  - For `ENTRYPOINT`/`CMD`, you will need to use the `--host` and `--port` arguments with `uvicorn`.
3. Build the dockerfile using the `docker buildx build` command. 
  - You should give your image a tag
  - You should specify the build directory as `web_app/`
  - Depending on where you placed the dockerfile, you may need to specify the path to the dockerfile
4. Run the image locally and validate that it works
  - Make sure to expose a port when you run the container (the `EXPOSE` instruction in the Dockerfile is not automatic)
  - Don't forget to rebuild your image on changes!!
  - If something is failing, you can check the `docker container logs`
  - Test your endpoints and see that they function properly
  - You should be able to remove the container and start a new container with no issues


### 2.1.2. Reference Material
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [FastAPI example](https://fastapi.tiangolo.com/deployment/docker/#dockerfile)
- [Best practices](https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)
- [Docker buildx build](https://docs.docker.com/reference/cli/docker/buildx/build/#file)

## 2.2. Update your pipeline to build & push
### 2.2.1. Steps
1. Update your CI workflow
  - You can use a pre-built Action
  - Or use multiple run steps
  - You may need to adjust the permissions of your workflow
  - Do you want to place this in a new job or in a separate step?
2. Push your changes and validate that they work.
  - If the workflow does not run automatically on the new branch, you can manually run it from the Actions page.
  - You should see a new package in GitHub (repo -> right sidebar)

### 2.2.2. Reference Material
- [GH Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [push-to-ghcr Action](https://github.com/macbre/push-to-ghcr#input-parameters)
- [Package Permissions](https://docs.github.com/en/packages/managing-github-packages-using-github-actions-workflows/publishing-and-installing-a-package-with-github-actions#publishing-a-package-using-an-action)

# 3. Congrats
You've now built your own web app and published the package to a container registry.  This is a complete Cont. Integration, Cont. Delivery pipeline!  If you have time, consider doing the intermediate exercises.