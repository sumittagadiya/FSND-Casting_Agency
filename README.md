# FSND-Casting_Agency
Udacity Full Stack Developer Nanodegree Project Capstone Projects

## Motivation
This is the last project of the Udacity-Full-Stack-Nanodegree Course. It covers following technical topics in a single app:

Database modeling with postgres & sqlalchemy check -> models.py

REST API  for CRUD Operations on database with Flask. check -> app.py)

Automated unit testing for test driven development with Unittest (check-> test_app.py)


Authorization & Role based Authentification with Auth0 (check Auth/auth.py)

Deployment on Heroku 

## Getting Started

### Installing Dependencies

#### Python 3 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Example in my code :

python3 -m venv env
source env/bin/activate

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies 

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [Flask-Migrate] (https://flask-migrate.readthedocs.io/en/latest/) is use for detecting changes in Database and migration of changes in Database.



- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup

Also set the following environmental variable for Auth0

```bash
# You can replace following with your details  This is my details and this token can be useful for running and testing my app, but this token might expired
export DATABASE_URL='postgres://postgres:1234@localhost:5432/casting'
export TEST_DATABASE_URL='postgres://postgres:1234@localhost:5432/test_casting'
export AUTH0_DOMAIN='tagadiya.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='casting'

export casting_assistant='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWM3MTBmZjUwMjAwMTM3ZjgwMzIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3MTkzLCJleHAiOjE1OTI0NzM1OTIsImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.UGN5AXZe4SQ9o2fZ6SK1vfuxzf2rAkuSbccujz64nO3Irj6BQuZtrsTEkIeAXq5PNEYrHC-QTX4I-rWh7KRNBLZuhJ5bolz6vtL-b5cDzQJoZCpoMJLQtNVMPTgwkXggn0lRsahi_ICULx9HuMki7YuKOtfRzYSzxHZWGobb04fyvFCWR-UHmhSj-xay4B_hnFqqA9rjAgkqZXqdQyOvjVouCya382YJJRpHtbavJ5yfzDqk_i_hv07sYLZXTh4FzjpzZIeTFrm3axPCyLc09B7-J_uhpCPqxY280otKMN3mEQeAgwXpfgv9A8l_h0kF8oVTaEACueWdJaiKzuHM8g' 

export casting_director='Bearer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWQ0ODBmZjUwMjAwMTM3ZjgxNGMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3MzYwLCJleHAiOjE1OTI0NzM3NTksImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.F_iVCn2zqDW3dB_zzMeZwL0G1oGtuSpDULa3VXONugJPPJqdxzvHgVhykzS8odx9PLe65FKPiWDie93YxwA_NpbnUcYGGTGBnWj7cmTDr0RXeDK2BDi5lkaWmS_p09zrU0NQoNQ7-lVuqS6qOcuYd0Oy4L-iRRQbUKgrmLg9q23HsQ9rnP6eU6gnKUVd3ZeG2Uz8EVCholiG2nq1D5cRcfc6nDHuvTQtSD3kzwVYjE6CXj4q4c0yxskAjXXxQzx2d8Q3aIPS3ou8OQs4InoWj45jxr6re9wZtFhYddQQXPg1CdYPmkcCtxtMVfxEOPTb1KQv4vMeVEkWUq5R2jKI7Q'

export producer='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJhU1ZlUFRRaXBFX2hVd2hNRUFqUyJ9.eyJpc3MiOiJodHRwczovL3RhZ2FkaXlhLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3NWUyOTkyMmQxMzAwMTkxODdmZWMiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTkyMzg3NDM5LCJleHAiOjE1OTI0NzM4MzgsImF6cCI6IjZzbkNUcXdVZFBKVzJNRExmSlBsOGFtcHAzWWVJUkpjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.YjztTrx8Jx5rqjFMUQdLxRcS_ksEl0X-c2QAJFkWdVDE2CgLTwTqZ8YSwAzwo6rd8WMk4Gqn9Kv1GVq0_4WPOhRqtURDjZoYoQ-2weL-pJilRunIIJV9rFFYmjebzwL7wXlgYeRr1LgkiXAXdzEMGN2oMyFeNVxzpAhqIDClhcYDtX_YBzh6w4fAAd1rstB5bNdEZa42tXJSdRuXOQT61DvPOqJcXhAZDAiPfmJ7kpH10zSpoZIu9rWaftChftkHCVLz27Sd-iiZWBVuaI_5mmw-5ujIOof81CPWO7i-eeTZey9RA1ElKe8-sVhHVkx34HxVycBbChlb7MuplTYKYQ'
```

please create database according to setting given or you can cahnge accordingly 

please run if working with new database setting No table

     python3 manage.py db init 
     
     python3 manage.py db migrate
     
     python3 manage.py db upgrade 
     

To run the server, execute: run this in your terminal where code is : python3 app.py

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain  # add this in environment variable
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `post:actors`
    - `get:actors`
    - `delete:actors`
    - `patch:actors`
    - `post:movies`
    - `get:movies`
    - `delete:movies`
    - `patch:movies`

6. Create new roles for:
    - Casting Assistant
      - Can view actors and movies

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
GET ...
POST ...
DELETE ...
PATCH ...

```
GET ‘/movies’ 
 
- Fetches a List of Movies Available
- Request Arguments: page , for fetching the data for particular page
- Returns: Returns Object with details about movie id, title, release_date and total_record

-Sample Request Format:

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



GET ‘/actors

- Fetches a List of Actors Available
- Request Arguments: page , for fetching the data for particular page
- Returns: Returns Object with details about movie id, age, gender, name and total_Record

-Sample Request Format: 

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
- Fetches a List of Movies for particular  id parameter in request
- Request Arguments: page (OPTIONAL) , for fetching the data for particular page
- Returns: Returns Object with details about actor details, id, release_date, title 

-Sample Request Format: 

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
- Fetches a List of Actors for particular  id parameter in request
- Request Arguments: page (OPTIONAL) , for fetching the data for particular page
- Returns: Returns Object with details about id, age, gender, movie details 

-Sample Request Format:

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
- Delete Movie based on specific Movie id
- Request Arguments: id (Required) -Movie Id
- Returns: object with status_code and success

Sample Request :

http://0.0.0.0:8080/movies/1

Response :

{
   "movie_id": 1,
   "status_code": 200,
   "success": true
}


DELETE ‘/actors/<int:id>’
- Delete Actor based on specific Actor id
- Request Arguments: id (Required) -Actor Id
- Returns: object with status_code and success

Sample Request  :

http://0.0.0.0:8080/actors/1

Response :

{
   "actor_id": 1,
   "status_code": 200,
   "success": true
 }


POST '/actors'
- This endpoint is used for creating new actor

Request body:
    {
    "name":"sapna pabbi",
    "age":28,
    "gender": "Female"
  }
    Add Authorization : 'Bearer TOKEN'
    
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
- EDIT  Movie for particular  id parameter in request
- Returns: Returns Object with updated movie record and status code 

Sample Request :

http://0.0.0.0:8080/movies/2

Add Authorization Header : 'Bearer Token'

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

   - Register 3 users - assign the Casting Assistant role to the first,Casting Director to the second and Executive Producer to the third
   - Sign into each account and make note of the JWT.
   - if you change the jwt please add in environment variable
   - Import the postman collection `Casting.postman_collection.json`
   - Right-clicking the collection folder ,select edit and navigate to the variables tab, update the JWT token for the three different roles i.e Casting Assistant, Casting Director and Executive Producer.
   - Run the collection to test the endpoints
   >_tip_: To ensure that the tests run correctly please update the ids for
    resources that require accessing a specific record by id, and make sure you create record and then check

9. Testing with pytest

   - You can also run unit tests by opening your terminal
   - run : python3 test_app.py



    
   






