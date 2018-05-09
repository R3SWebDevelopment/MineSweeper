#Mine Swipper

This project us the https://github.com/R3SWebDevelopment/django_skeleton repository for project setting

This project is the back end (API) for the game mine swipper.

For reference the commits for this project start after commit e72a6ac6f6f4d288196612467260c1817bd4cdb4

#Django Skeleton

This project is already setup to be executed on a docker container.

###Docker containers:
1. db: Container that execute a postgres 9.6 or above database
1. redis: Container with a default configuration for redis services
1. celery: Container with a default configuration for celery services
1. web: Container that run the django project

###Initialize project
1. sudo docker-compose build
1. sudo docker-compose up -d
1. sudo docker-compose exec web bash
1. cd django_skeleton
1. ./manage.py migrate
1. ./manage.py push_fixtures