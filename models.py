#----------------
# Imports
#----------------

import os
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
import json
from datetime import date


# Database Setup 

# Use production database.

database_path = os.environ['DATABASE_URL']

# If you want run locally you can give path as follow.
#database_path = "postgres://{}:{}@{}/{}".format('postgres','1234','localhost:5432', 'casting')
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    '''Binds a Flask Application and a SQLAlchemy '''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_create_all():
    '''drop existing database and create new fresh database'''   
    db.drop_all()
    db.create_all()
    db_initialize_records()

def test_db_drop_create_all():
    '''drop existing database and create new fresh database'''  
    db.drop_all()
    db.create_all()
    db_initialize_records()


# Movies Model 

class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    release_date = Column(DateTime, nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id', ondelete="CASCADE"))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actor': self.Actor.short()            
        }

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


# Actors Model 

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    movies = db.relationship(
        'Movie',
        backref='Actor',
        lazy=True, 
        cascade="save-update,delete, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': [movie.short() for movie in self.movies]
        }


def db_initialize_records():
    '''initialize own records'''

    new_actor_1 = (Actor(
        name='Emraan Hashmi',
        gender='Male',
        age=39
        ))

    new_actor_2 = (Actor(
        name='salman khan',
        gender='Male',
        age=50
        ))

    new_actor_3 = (Actor(
        name='Hrithik Roshan',
        gender='Male',
        age=40
        ))

    new_actor_4 = (Actor(
        name='Tony Starc',
        gender='Male',
        age=45
        ))

    new_actor_1.insert()
    new_actor_2.insert()
    new_actor_3.insert()
    new_actor_4.insert()

    # Create record for new movie
    new_movie_1 = (Movie(
        title='Jannat',
        release_date=date.today(),
        actor_id=new_actor_1.id
        ))

    new_movie_2 = (Movie(
        title='Partner',
        release_date=date.today(),
        actor_id=new_actor_2.id
        ))

    new_movie_3 = (Movie(
        title='Super 30',
        release_date=date.today(),
        actor_id=new_actor_3.id
        ))
    new_movie_4 = (Movie(
        title='Avengers-End game',
        release_date=date.today(),
        actor_id=new_actor_4.id
        ))
    
    new_movie_1.insert()
    new_movie_2.insert()
    new_movie_3.insert()
    new_movie_4.insert()

    db.session.commit()


