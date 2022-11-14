pipeline {
    agent any

    stages {
        stage('Job 1 - Stage 1') {
            steps {
                /* Pull code from Github repo */
                echo 'Stage 1: pulling code from Github repo ...'
                bat
                '''
                git init
                git remote add origin https://github.com/AmitLevy93/DevOps_HA_test_Amit.git
                git status
                git pull origin master
                '''
            }
        }
        stage('Job 1 - Stage 2') {
            steps {
                /* Build docker container of python with flask
                   (simple web app that talks the local docker engine) */
                echo 'Stage 2 - build docker image and run a container ...'
                bat
                '''
                cd python_flask_docker
                ::Create docker image from Dockerfile:
                docker image build -t python_flask_docker .
                ::List of docker images installed locally:
                docker image ls
                ::Creat a container from the image and run it:
                docker run -d --name python_flask_container -p 5000:5000 python_flask_docker
                ::List of all running containers:
                docker ps
                ::back to main project's directory:
                cd ..
                '''
            }
        }
        stage('Job 1 - Stage 3') {
            steps {
                echo 'Stage 3 - push docker image into Dockerhub ...'
                bat
                '''
                ::Login to DockerHub:
                docker login --username=amit93levy --password=<your-password>
                ::---add username and password (encrypted)---
                ::Push docker image into DockerHub:
                docker tag python_flask_docker amit93levy/python_flask_docker
                docker push amit93levy/python_flask_docker
                '''
                echo 'Go to: https://hub.docker.com/repository/docker/amit93levy/python_flask_docker'
            }
        }
        stage('Job 2 - Nginx docker file') {
            steps {
                bat
                '''
                cd nginx_reverse_proxy
                docker images
                docker ps
                ::Pull the latest nginx image from dockerhub and run it:
                docker run -d --name nginx-base -p 5001:80 nginx:latest
                ::Copy the file default.conf from nginx container to nginx_reverse_proxy local directory:
                docker cp nginx-base:/etc/nginx/conf.d/default.conf .
                ::Add proxy pass to default.conf
                type add_proxy_pass_to_conf_file.txt > default.conf
                ::Copy the local default.conf file to its location inside the container:
                docker cp default.conf nginx-base:/etc/nginx/conf.d/
                ::Testing/validating the file inside the container:
                docker exec nginx-base nginx -t
                ::Reload the file inside the container:
                docker exec nginx-base nginx -s reload
                ::Make a new docker image called "nginx-proxy" from the nginx container:
                docker commit nginx-base nginx-proxy
                '''
                echo 'go to: http://localhost:5001/app or http://localhost:5001'
            }
        }
        stage('Job 3 - Stage 1') {
            steps {
                echo 'Running the first container ....'
                bat
                '''
                docker run -d --name python_flask_container -p 5000:5000 python_flask_docker
                '''
            }
        }
        stage('Job 3 - Stage 2') {
            steps {
                echo 'Running the Second container ....'
                bat
                '''
                docker run -d --name nginx_proxy_container -p 5001:80 nginx-proxy
                '''
            }
        }
        stage('Job 3 - Stage 3') {
            steps {
                echo 'Testing....'
                bat
                '''
                curl http://localhost:5001/app
                '''
            }
        }
    }
}
