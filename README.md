# Udacity-Capstone-Project

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/mroluseyi/Udacity-Capstone-Project/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/mroluseyi/Udacity-Capstone-Project/tree/master)



PROJECT OVERVIEW:
This project was created to show the use of a CI/CD pipeline to create a simple app written in python to show 'Hello ...' message when receiving request. Docker images were pushed to Docker hub, Hadolint was installed to lint the dockerfile, connect to the kubernetes cluster and deployed the docker image to it using rolling deployment.


STEPS:
- Create Makefile
- Create Dockerfile and Lint Dockerfile
- Build and upload Docker image to Docker hub
- Create cluster and node group in AWS EKS
- Install kubectl
- deploy app to AWS EKS cluster
- Create CI/CD to run this commands after testing locally

TECHNOLOGIES USED:
- Docker
- Kubectl
- Eksctl
- CircleCI
- GitHub
- AWS