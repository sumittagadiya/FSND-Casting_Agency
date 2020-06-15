import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db, db_drop_and_create_all
from auth.auth import AuthError, requires_auth
import sys


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  return app


app = create_app()
#db_drop_and_create_all() # uncomment this if you want to start a new database on app refresh
RECORD_PER_PAGE = 10

#----------------------------------------------------------------------------#
  #  API Endpoints
  #  ----------------------------------------------------------------
  #  NOTE:  For explanation of each endpoint, please have look at the README.md file. 
  #         DOC Strings only contain short description and list of test classes 
  #----------------------------------------------------------------------------#

  #----------------------------------------------------------------------------#
  # Endpoint /actors GET/POST/DELETE/PATCH
  #----------------------------------------------------------------------------#

''' 
GET : get all movies 
'''


@app.route("/movies", methods=["GET"])
@requires_auth("get:movies")
def get_movies(payload):
  #page_num = request.args.get('page',1,type=int)
  #print(page_num)
  movies = Movie.query.paginate(per_page=RECORD_PER_PAGE, error_out=True)
  print("movies ====> ", movies)
  if len(movies.items) == 0:
    abort(404)
  else:
    return jsonify({
      "success" : True,
      "status_code": 200,
      "movies": [movie.short() for movie in movies.items],
      "total_record": movies.total
      }), 200

"""
GET : get movie details 
"""

@app.route("/movies/<int:id>/details", methods=["GET"])
@requires_auth("get:movies")
def get_movie_details(payload,id):
  movie = Movie.query.filter_by(id=id).one_or_none()
  if movie is None:
    abort(404)
  else:
    try:
      return jsonify({
        "status_code": 200,
        "success": True,
        "movie": movie.format()
      }), 200
    except BaseException:
      print(sys.exc_info())
      abort(500)

'''
GET : get all actors (/actors/actor_id/details)
'''

@app.route("/actors/<int:id>/details",methods=["GET"])
@requires_auth("get:actors")
def get_actor_details(payload,id):
 # print("Actor id ===>", id)
  actor = Actor.query.get(id)
  if actor is None:
    abort(404)
  else:
    try:
      return jsonify({
        "status_code": 200,
        "success": True,
        'actor': actor.format()
      }), 200

    except BaseException:
      print(sys.exc_info())
      abort(500)

'''
GET/actors: get all actors
'''

@app.route("/actors",methods=["GET"])
@requires_auth("get:actors")
def get_actors(payload):
  page_num = request.args.get('page',1,type=int)
  print(page_num)
  actors = Actor.query.paginate(per_page=RECORD_PER_PAGE,error_out=True)
  if len(actors.items) == 0:
        abort(404)
  else:
    return jsonify({
      "success": True,
      "status_code": 200,
      "actors": [actor.short() for actor in actors.items],
      "total_record": actors.total
      }), 200

'''
  POST : /actors
  create a new Actor Record
  {
    "name":name of actor,
    "age": age of actor,
    "gender": gender
  }
'''

@app.route("/actors",methods=["POST"])
@requires_auth("post:actors")
def create_new_actor(payload):
  body = request.get_json()
  name = body.get("name")
  age = body.get("age")
  gender = body.get("gender")
  actor = Actor(name=name,age=age,gender=gender)

  try:
    actor.insert()
    return jsonify({
      "success": True,
      "status_code": 200,
      "message": "{} created".format(actor.name),
      "actor":actor.short()
    }), 200
  except BaseException:
    print(sys.exc_info())
    abort(400)

'''
  POST : /movies
  create a new Movie Record
  {
    "title":"name of movie",
    "release_date": "release date",
    "actor_id": "Actor Id"
  }
'''

@app.route("/movies",methods=["POST"])
@requires_auth("post:movies")
def create_new_movie(payload):
  body = request.get_json()
  new_title = body.get("title")
  new_release_date = body.get("release_date")
  new_actor_id = body.get("actor_id")

  movie = Movie(title=new_title,release_date=new_release_date,actor_id=new_actor_id)
  try:
    movie.insert()
    return jsonify({
      "success": True,
      "status_code": 200,
      "message": "{} created".format(movie.title),
      "Movie": movie.short()
    }), 200
  except BaseException:
    print(sys.exc_info())
    abort(400)

'''
PATCH /movies/id
update perticular movie record
'''

@app.route("/movies/<int:id>",methods=["PATCH"])
@requires_auth("patch:movies")
def edit_movie(payload,id):
  movie = Movie.query.filter_by(id=id).one_or_none()
  print("Movie to be patched",movie)
  if movie is None:
    abort(404)
  else:
    try:
      body = request.get_json()
      title = body.get("title")
      release_date = body.get("release_date")
      actor_id = body.get("actor_id")

      if title:
        movie.title = title
      if release_date:
        movie.release_date = release_date
      if actor_id:
        movie.actor_id = actor_id
      movie.update()
      return jsonify({
        "success": True,
        "status_code":200,
        'movie':movie.short()
      }), 200

    except BaseException:
      print(sys.exc_info())
      abort(500)


"""
PATCH /actors/id
update actor record
"""


@app.route("/actors/<int:id>", methods=["PATCH"])
@requires_auth("patch:actors")
def edit_actor(payload, id):
  print("patch actor id",id)
  actor = Actor.query.filter_by(id=id).one_or_none()
  if actor is None:
    abort(404)
  else:
    try:
      req_body = request.get_json()
      name = req_body.get("name")
      age = req_body.get("age")
      gender = req_body.get("gender")
      if name:
        actor.name = name
      if age:
        actor.age = age
      if gender:
        actor.gender = gender
      actor.update()
      return jsonify({
        'status_code': 200,
        'success':  True,
        'actor': actor.short()
      }), 200
    except BaseException:
      print(sys.exc_info())
      abort(500)



'''
DELETE /actors/id
delete actor record
'''

@app.route("/actors/<int:id>",methods=["DELETE"])
@requires_auth("delete:actors")
def remove_actor(payload,id):
  actor = Actor.query.filter_by(id=id).one_or_none()
  if actor is None:
    abort(404)
  else:
    try:
      actor.delete()
      return jsonify({
        "success": True,
        "status_code": 200,
        "actor_id": id
      }), 200
    except BaseException:
      print(sys.exc_info())
      abort(500)

'''
DELETE /movies/id
delete Movie record
'''

@app.route("/movies/<int:id>",methods=["DELETE"])
@requires_auth("delete:movies")
def remove_movie(payload,id):
  movie = Movie.query.filter_by(id=id).one_or_none
  if movie is None:
    abort(404)
  else:
    try:
      movie.delete()
      return jsonify({
        "success": True,
        "status_code":200,
        "movie_id": id
      }), 200
    except BaseException:
      print(sys.exc_info())
      abort(500)

 #----------------------------------------------------------------------------#
 # Error Handlers
 #----------------------------------------------------------------------------#


@app.errorhandler(400)
def bad_request(error):
  return jsonify({
      "success": False,
      "status_code": 400,
      "message": "request format error"
    }), 400


@app.errorhandler(500)
def server_request_processing_error(error):
    return jsonify({
      "success": False,
      "status_code": 500,
      "message": "Internal server error"
    }), 500


@app.errorhandler(404)
def ressource_not_found(error):
  return jsonify({
    "success": False,
    "status_code": 404,
    "error": "Resources_not_found"
  }), 404


@app.errorhandler(AuthError)
def auth_error(error):
  return jsonify({
    "success": True,
    "error":error.status_code,
    "message":error.error['description']
  }), error.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



