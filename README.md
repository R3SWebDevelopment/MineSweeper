# Mine Swipper

This project us the https://github.com/R3SWebDevelopment/django_skeleton repository for project setting

This project is the back end (API) for the game mine swipper.

For reference the commits for this project start after commit e72a6ac6f6f4d288196612467260c1817bd4cdb4

# Django Skeleton

This project is already setup to be executed on a docker container.

### Docker containers:
1. db: Container that execute a postgres 9.6 or above database
1. redis: Container with a default configuration for redis services
1. celery: Container with a default configuration for celery services
1. web: Container that run the django project

### Initialize project
1. sudo docker-compose build
1. sudo docker-compose up -d
1. sudo docker-compose exec web bash
1. cd django_skeleton
1. ./manage.py migrate
1. ./manage.py push_fixtures

### Access point
Front End: 
Back End: 

## Instruccions

# minesweeper-API
API test

We ask that you complete the following challenge to evaluate your development skills. Please use the programming language and framework discussed during your interview to accomplish the following task.

## The Game
Develop the classic game of [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game))

## Show your work

1.  Create a Public repository
2.  Commit each step of your process so we can follow your thought process.

## What to build
The following is a list of items (prioritized from most important to least important) we wish to see:
* Design and implement  a documented RESTful API for the game (think of a mobile app for your API)
* Implement an API client library for the API designed above. Ideally, in a different language, of your preference, to the one used for the API
* When a cell with no adjacent mines is revealed, all adjacent squares will be revealed (and repeat)
* Ability to 'flag' a cell with a question mark or red flag
* Detect when game is over
* Persistence
* Time tracking
* Ability to start a new game and preserve/resume the old ones
* Ability to select the game parameters: number of rows, columns, and mines
* Ability to support multiple users/accounts
 
## Deliverables we expect:
* URL where the game can be accessed and played (use any platform of your preference: heroku.com, aws.amazon.com, etc)
* Code in a public Github repo
* README file with the decisions taken and important notes

## Time Spent
You do not need to fully complete the challenge. We suggest not to spend more than 5 hours total, which can be done over the course of 2 days.  Please make commits as often as possible so we can see the time you spent and please do not make one commit.  We will evaluate the code and time spent.
 
What we want to see is how well you handle yourself given the time you spend on the problem, how you think, and how you prioritize when time is insufficient to solve everything.

Please email your solution as soon as you have completed the challenge or the time is up.