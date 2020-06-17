import os
import sys
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from auth.auth import AuthError, requires_auth
from models import setup_db,Movie, Actor, db_drop_create_all


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={'/': {"origins": "*"}}) #Set up CORS. Allow '*' for origins.
  return app

app = create_app()
#db_drop_create_all() # uncomment this if you want to start a new database on app refresh

RECORD_PER_PAGE = 10
def paginated_records(request,records,RECORD_PER_PAGE):
  page=request.args.get('page',1,type=int)
  start=(page - 1)*RECORD_PER_PAGE
  end=start+RECORD_PER_PAGE
  records = [record.short() for record in records]
  current_records = records[start:end]
  return current_records

#  API Endpoints
# Endpoint  GET/POST/DELETE/PATCH

'''default endpoint'''
@app.route('/', methods=['POST', 'GET'])
def health():
  return jsonify("Healthy")



''' 
get all movies with Authorization header
'''


@app.route("/movies", methods=["GET"])
@requires_auth("get:movies")
def get_movies_list(payload):
  movies = Movie.query.all()
  total_movies = len(movies)
  print("movies ====> ", movies)
  # Get paginated movies
  current_movies =  paginated_records(request, movies, RECORD_PER_PAGE)
  if (len(current_movies) == 0):
    abort(404)
  else:
    return jsonify({
      "success" : True,
      "status_code": 200,
      "movies": [current_movies],
      "total_record": total_movies
      }), 200

# get movie details for perticular movie id

@app.route("/movies/<int:movie_id>/details", methods=["GET"])
@requires_auth("get:movies")
def get_movie_details_given_id(payload,movie_id):
  movie = Movie.query.get(movie_id)
  if not movie:
    abort(404)
  else:
    try:
      return jsonify({
        "status_code": 200,
        "success": True,
        "movie": movie.format()
      }), 200
    except Exception:
      abort(500)

'''
get particular actor details
'''

@app.route("/actors/<int:actor_id>/details",methods=["GET"])
@requires_auth("get:actors")
def get_particular_actor(payload,actor_id):
 # print("Actor id ===>", id)
  actor = Actor.query.get(actor_id)
  if not actor:
    abort(404)
  else:
    try:
      return jsonify({
        "status_code": 200,
        "success": True,
        'actor': actor.format()
      }), 200

    except Exception:
      abort(500)

'''
get list of all actors
'''

@app.route("/actors",methods=["GET"])
@requires_auth("get:actors")
def get_actors_list(payload):
  actors = Actor.query.all()
  total_actors = len(actors)
  print("Actors =========>",actors)
  # get paginated actors
  current_actors =  paginated_records(request, actors, RECORD_PER_PAGE)
  if (len(current_actors) == 0):
    abort(404)
  else:
    return jsonify({
      "success": True,
      "status_code": 200,
      "actors": [current_actors],
      "total_record": total_actors
      }), 200

'''
 POST: Create new actor with given details
'''

@app.route("/actors",methods=["POST"])
@requires_auth("post:actors")
def add_new_actor(payload):
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
      "message": "{} added".format(actor.name),
      "Added actor":actor.short()
    }), 200
  except Exception:
    abort(400)

'''
POST : Add new movie with required details
'''

@app.route("/movies",methods=["POST"])
@requires_auth("post:movies")
def add_new_movie(payload):
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
      "message": "{} added".format(movie.title),
      "Added Movie": movie.short()
    }), 200
  except Exception:
    abort(400)

'''
PATCH : Update perticular movie details
'''

@app.route("/movies/<int:movie_id>",methods=["PATCH"])
@requires_auth("patch:movies")
def update_movie(payload,movie_id):
  movie = Movie.query.get(movie_id)
  print("Movie to be patched",movie)
  if not movie :
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

    except Exception:
      abort(500)


"""
PATCH : update particular actor details
"""


@app.route("/actors/<int:actor_id>", methods=["PATCH"])
@requires_auth("patch:actors")
def edit_actor(payload, actor_id):
  print("patch actor id",id)
  actor = Actor.query.get(actor_id)
  if not actor :
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
    except Exception:
      abort(500)



'''
DELETE : delete particular actor
'''

@app.route("/actors/<int:actor_id>",methods=["DELETE"])
@requires_auth("delete:actors")
def delete_actor(payload,actor_id):
  actor = Actor.query.get(actor_id)
  if not actor :
    abort(404)
  else:
    try:
      actor.delete()
      return jsonify({
        "success": True,
        "status_code": 200,
        "actor_id": "{} deleted".format(actor_id)
      }), 200
    except Exception:
      abort(500)

'''
DELETE : delete perticular movie record
'''

@app.route("/movies/<int:movie_id>",methods=["DELETE"])
@requires_auth("delete:movies")
def delete_movie(payload,movie_id):
  movie = Movie.query.get(movie_id)
  if not movie :
    abort(404)
  else:
    try:
      #print("===============>",movie.title)
      movie.delete()
      return jsonify({
        "success": True,
        "status_code":200,
        "movie_id": "{} deleted".format(movie_id)
      }), 200
    except Exception:
      abort(500)

 #----------------------------------------------------------------------------#
 # Error Handlers
 #----------------------------------------------------------------------------#


@app.errorhandler(400)
def bad_request(error):
  return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal server error"
    }), 500


@app.errorhandler(404)
def not_found(error):
  return jsonify({
    "success": False,
    "error": 404,
    "error": "Resource not found"
  }), 404

@app.errorhandler(401)
def not_authorized(error):
  return jsonify({
    "success": False,
    "error": 401,
    "message": 'Unathorized'
    }), 401

@app.errorhandler(AuthError)
def auth_error(error):
  return jsonify({
    "success": False,
    "error":error.status_code,
    "message":error.error['description']
  }), error.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



