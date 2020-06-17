# Casting Agency
Casting Agency is a company that is responsible for creating movies and managing movies and actors with different roles. there are three different roles which are Assistant role, Director Role and Producer role,all have different permissions to perform actions on database

Here is hosted heroku [Link](https://casting-agency-fsnd-capstone.herokuapp.com)

## Motivation

This is my Last project of Full stack nano degree program by Udacity

Database model located in  models.py

REST API  for CRUD Operations check app.py

Automated unit testing check  unit_test.py


Authorization & Role based Authentification with Auth0 check Auth/auth.py

Deployment on Heroku 

## Getting Started

### Installing Dependencies

#### Python 3 

Install letest version of [python3] (https://www.python.org/downloads/)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

In my code i have created conda virtual enviornment because of some issues in my machine.
check [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to create virtual enviornment in conda

Example in my code :

conda create -n myenv python=3.6

source activate myenv

For python virtual enviornment setup you can do following in your terminal

python3 -m venv env source env/bin/activate

for more details check [this] (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies 

Once you have your virtual environment setup and running, you can install dependencies by hitting

```
pip install -r requirements.txt

```

This will install all of the required packages which are in `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [Flask-Migrate] (https://flask-migrate.readthedocs.io/en/latest/) is use for detecting changes in Database and migration of changes in Database.



- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup

Set the following environmental variable for Auth0 in setup.sh file if you run project locally and for heroku you can set all this variables in heroku dashboard.

```bash
# you have to replace following details with your setup.
export DATABASE_URL='postgres://postgres:1234@localhost:5432/casting'
export TEST_DATABASE_URL='postgres://postgres:1234@localhost:5432/test_casting'
export AUTH0_DOMAIN='tagadiya.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='casting'

export assistant='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWM3MTBmZjUwMjAwMTM3ZjgwMzIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3MTkzLCJleHAiOjE1OTI0NzM1OTIsImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.UGN5AXZe4SQ9o2fZ6SK1vfuxzf2rAkuSbccujz64nO3Irj6BQuZtrsTEkIeAXq5PNEYrHC-QTX4I-rWh7KRNBLZuhJ5bolz6vtL-b5cDzQJoZCpoMJLQtNVMPTgwkXggn0lRsahi_ICULx9HuMki7YuKOtfRzYSzxHZWGobb04fyvFCWR-UHmhSj-xay4B_hnFqqA9rjAgkqZXqdQyOvjVouCya382YJJRpHtbavJ5yfzDqk_i_hv07sYLZXTh4FzjpzZIeTFrm3axPCyLc09B7-J_uhpCPqxY280otKMN3mEQeAgwXpfgv9A8l_h0kF8oVTaEACueWdJaiKzuHM8g' 

export director='Bearer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWQ0ODBmZjUwMjAwMTM3ZjgxNGMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3MzYwLCJleHAiOjE1OTI0NzM3NTksImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.F_iVCn2zqDW3dB_zzMeZwL0G1oGtuSpDULa3VXONugJPPJqdxzvHgVhykzS8odx9PLe65FKPiWDie93YxwA_NpbnUcYGGTGBnWj7cmTDr0RXeDK2BDi5lkaWmS_p09zrU0NQoNQ7-lVuqS6qOcuYd0Oy4L-iRRQbUKgrmLg9q23HsQ9rnP6eU6gnKUVd3ZeG2Uz8EVCholiG2nq1D5cRcfc6nDHuvTQtSD3kzwVYjE6CXj4q4c0yxskAjXXxQzx2d8Q3aIPS3ou8OQs4InoWj45jxr6re9wZtFhYddQQXPg1CdYPmkcCtxtMVfxEOPTb1KQv4vMeVEkWUq5R2jKI7Q'

export producer='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWUyOTkyMmQxMzAwMTkxODdmZWMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3NDM5LCJleHAiOjE1OTI0NzM4MzgsImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.YjztTrx8Jx5rqjFMUQdLxRcS_ksEl0X-c2QAJFkWdVDE2CgLTwTqZ8YSwAzwo6rd8WMk4Gqn9Kv1GVq0_4WPOhRqtURDjZoYoQ-2weL-pJilRunIIJV9rFFYmjebzwL7wXlgYeRr1LgkiXAXdzEMGN2oMyFeNVxzpAhqIDClhcYDtX_YBzh6w4fAAd1rstB5bNdEZa42tXJSdRuXOQT61DvPOqJcXhAZDAiPfmJ7kpH10zSpoZIu9rWaftChftkHCVLz27Sd-iiZWBVuaI_5mmw-5ujIOof81CPWO7i-eeTZey9RA1ElKe8-sVhHVkx34HxVycBbChlb7MuplTYKYQ'
```

please create database according to your settings. 

please run following command if you are working with new database setting .

     python3 manage.py db init 
     
     python3 manage.py db migrate
     
     python3 manage.py db upgrade 
     

to run server :hit python3 app.py in your working directory 

### Setup Auth0 Details

1. Create a new Auth0 Account
2. Select a unique tenant domain  # this will be used in our environment variable
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    
    - `get:actors`
    - `get:movies`
    - `post:actors`
    - `post:movies`
    - `patch:actors`
    - `patch:movies`
    - `delete:actors`
    - `delete:movies`
    

6. Create new roles for:
    - Assistant
      - Can view all actors and all movies

    - Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies

    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database

7. Endpoints

    | Functionality            | Endpoint                      | Casting assistant  |  Casting Director  | Executive Producer |
    | ------------------------ | ----------------------------- | :----------------: | :----------------: | :----------------: |
    | Fetches a list of actors | GET /actors                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a list of movies | GET /movies                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a specific actor | GET /actors/&lt;id&gt;        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches a specific movie | GET /movies/&lt;id&gt;        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
    | Creates an actor         | POST /actor                   |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Fetches Movie actors     | GET /movies/&lt;id&gt;/actors |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Patches an actor         | PATCH /actors/&lt;id&gt;      |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Delete an Actor          | DELETE /actors/&lt;id&gt;     |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
    | Creates a movie          | POST /movies                  |        :x:         |        :x:         | :heavy_check_mark: |
    | Deletes a movie          | DELETE /movies/&lt;id&gt;     |        :x:         |        :x:         | :heavy_check_mark: |


## Authentication

The API has three registered users:

1. Assistant

```
email: assistant@gmail.com
password: Assistant@123
```

2. Director

```
email: director.casting@gmail.com
password: Director@123
```

3. Producer

```
email: executive.producer@gmail.com
password: Executive@123
```

The Auth0 domain and api audience can be found in `setup.sh`.



# Endpoints

GET
POST
PATCH
DELETE


```
GET ‘/movies’ 
 
- Fetches a List of all Available Movies
- Request Arguments: you can give id number to fetch particular movie eg. /movies/2
- Returns: It will return Object with details about movie id, title, release_date and total_record

Request:

http://0.0.0.0:8080/movies

Response:
{
  "movies": [
    {
      "id": 1,
      "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
      "title": "Jannat"
    },
    {
      "id": 2,
      "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
      "title": "Partner"
    },
    {
      "id": 3,
      "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
      "title": "Super 30"
    },
    {
      "id": 4,
      "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
      "title": "Avengers-End game"
    }
  ],
  "status_code": 200,
  "success": true,
  "total_record": 4
}



GET ‘/actors’

- Fetches a List of all Available Actors
- Request Arguments: we can fetch perticular actor details by giving existing actor id
- Returns: Returns Object with details about movie id, age, gender, name and total_Record

Request : 

http://0.0.0.0:8080/actors

Response:

{
  "actors": [
    {
      "age": 39,
      "gender": "Male",
      "id": 1,
      "name": "Emraan Hashmi"
    },
    {
      "age": 50,
      "gender": "Male",
      "id": 2,
      "name": "salman khan"
    },
    {
      "age": 40,
      "gender": "Male",
      "id": 3,
      "name": "Hrithik Roshan"
    },
    {
      "age": 45,
      "gender": "Male",
      "id": 4,
      "name": "Tony Starc"
    }
  ],
  "status_code": 200,
  "success": true,
  "total_record": 4
}



GET ‘/movies/<int:id>’
- Get a List of Movies for given id  in request
- Request Arguments: Can give particular id to get details.
- Returns: Returns Object with details about actor details,release_date, id, title 

Request: 

http://0.0.0.0:8080/movies/3/details

Response:
{
  "movie": {
    "actor": {
      "age": 40,
      "gender": "Male",
      "id": 3,
      "name": "Hrithik Roshan"
    },
    "id": 3,
    "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
    "title": "Super 30"
  },
  "status_code": 200,
  "success": true
}


GET ‘/actors/<int:id>’
- get a List of Actors for specific id parameter in request.
- Request Arguments: give specific id in request to get details of that actor id.
- Returns: Returns Object with details about id, age, gender, movie details.

Request :

http://0.0.0.0:8080/actors/4/details

Response:

{
  "actor": {
    "age": 45,
    "gender": "Male",
    "id": 4,
    "movies": [
      {
        "id": 4,
        "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
        "title": "Avengers-End game"
      }
    ],
    "name": "Tony Starc"
  },
  "status_code": 200,
  "success": true
}

DELETE ‘/movies/<int:id>’
- Delete Movie with specific Movie id
- Request Arguments: movie id you want to delete.
- Returns: object with status_code and success.

Request :

http://0.0.0.0:8080/movies/1

Response :

{
   "movie_id": 1,
   "status_code": 200,
   "success": true
}


DELETE ‘/actors/<int:id>’
- Delete Actor with specific Actor id
- Request Arguments: specific actor id which you want to test
- Returns: object with status_code and success

Request  :

http://0.0.0.0:8080/actors/1

Response :

{
   "actor_id": 1,
   "status_code": 200,
   "success": true
}


POST '/actors'
- This endpoint is used for creating new actor
- Request argument : Nothing
- returns : object with status code and success and json body.

Request body:
{
  "name":"sapna pabbi",
  "age":28,
  "gender": "Female"
}
Give Authorization : 'Bearer TOKEN'
    
Returns:

  {
    "actor": {
      "age": 28,
      "gender": "Female",
      "id": 5,
      "name": "sapna pabbi"
    },
    "message": "sapna pabbi created",
    "status_code": 200,
    "success": true
  }
  

POST: /Movies
- This endpoint is used for creating new Movie
- returns : Object with status code, success and json body
Sample Request :

http://0.0.0.0:8080/movies
 
Request body:
{
    "title":"Inside Age",
    "release_date": "{{current_timestamp}}",
    "actor_id":2
  }

Add Authorization : 'Bearer TOKEN'
  
Returns:
   
   {
  "Movie": {
    "id": 5,
    "release_date": "Wed, 17 Jun 2020 09:12:09 GMT",
    "title": "Inside Age"
  },
  "message": "Inside Age created",
  "status_code": 200,
  "success": true
}


PATCH ‘/movies/<int:id>’
- EDIT  Movie for given particular id parameter in request
- Returns: Returns Object with updated movie record and status code 

Request :

http://0.0.0.0:8080/movies/2

Give Authorization Header : 'Bearer Token'

Request body:
{
    "title":"Inaside age 2"
}

Response:

{
  "movie": {
    "id": 2,
    "release_date": "Wed, 17 Jun 2020 00:00:00 GMT",
    "title": "Inaside age 2"
  },
  "status_code": 200,
  "success": true
}

```

8. Test your endpoints with [Postman](https://getpostman.com).

   - Register 3 users and assign the Assistant role to the first user ,Casting Director to the second user and Producer to the third
   - Sign into each account and make note of the JWT token.
   - if you change the jwt please add in environment variable to get desired results.
   - Import the postman collection `Casting.postman_collection.json`
   - Right-clicking the collection folder ,select edit and navigate to the variables tab, update the JWT token for the three different roles i.e Assistant, Director and Producer.
   - Run the collection to test the endpoints
   >_tip_: To ensure that the tests run correctly please update the ids for
    resources that require accessing a specific record by id, and make sure you create record and then check
  >_tip_: if you get error then please try to get new token by login into auth0 account.

9. Testing with pytest

   - You can also run unit tests by opening your terminal
   - run : python3 test_app.py
 

10. For Deployment on Heroku follow below considered steps 

   - cd into your project directory
   - run following commands first just for assure.
   ```
    1. python manage.py db init
    2. python manage.py db migrate
    3. python manage.py db upgrade
    4. pip freeze > requirements.txt
    5. commit and push all your changes on github
    6. heroku create name_of_your_app
    7. git remote add heroku heroku_git_url
    8. heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
    9. heroku config --app name_of_your_application
    10.Go to heroku dashboard and go to app > setting > Reveal Config Vars and configure all environment variables which are given in setup.sh
    11.git push heroku master
    12.heroku run python manage.py db upgrade --app name_of_your_application

   ```
   And now you have a live application! Open the application from your Heroku Dashboard and see it work live! Make additional requests using curl or Postman as you build your application and make more complex endpoints.


    
   






