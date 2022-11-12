pipeline {
    agent any

    stages {
        stage('Job 1') {
            steps {
                /* Pull code from Github repo */
                println('Part 1: pulling code from Github repo ...')
                batchFile(
                    '''
                    git init
                    git remote add origin https://github.com/AmitLevy93/DevOps_HA_test_Amit.git
                    git status
                    git pull origin master
                    '''
                    )
                /* Build docker container of python with flask
                   (simple web app that talks the local docker engine) */
                println('Part 2 - build docker image and run a container ...')
                batchFile(
                    '''
                    cd python_flask_docker
                    ::Create docker image from Dockerfile:
                    docker image build -t python_flask_docker .
                    ::List of docker images installed locally:
                    docker image ls
                    ::Creat a container from the image and run it:
                    docker run -p 5000:5000 -d python_flask_docker
                    ::List of all running containers:
                    docker ps
                    '''
                    )
                println('Part 3 - push docker image into Dockerhub ...')
                batchFile(
                    '''
                    ::Login to DockerHub:
                    docker login --username=amit93levy --password=<your-password>
                    ::---add username and password (encrypted)---
                    ::Push docker image into DockerHub:
                    docker tag python_flask_docker amit93levy/python_flask_docker
                    docker push amit93levy/python_flask_docker
                    '''
                )
                println('Go to: https://hub.docker.com/repository/docker/amit93levy/python_flask_docker')
            }
        }
        stage('Job 2 - Nginx docker file') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Job 3 - run') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
