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
                println('Part 2 - build and push docker container into Dockerhub ...')
                batchFile(
                    '''
                    
                    '''
                    )
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