from sqlalchemy import String, Integer, Column, create_engine, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import os
import json
from datetime import date

#----------------------------------------------------------------------------#
# Database Setup 
#----------------------------------------------------------------------------#

# Use Production Database.

database_path = os.environ['DATABASE_URL']

# If run locally, key does not exist, so use locally set database instead.
#database_path = "postgres://{}:{}@{}/{}".format('postgres','1234','localhost:5432', 'casting')
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    '''binds a flask application and a SQLAlchemy service'''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all():
    '''drops the database tables and starts fresh
    can be used to initialize a clean database
    '''   
    db.drop_all()
    db.create_all()
    db_init_records()

def test_db_drop_and_create_all():
    '''drops the database tables and starts fresh
    can be used to initialize a clean database
    '''   
    db.drop_all()
    db.create_all()
    db_init_records()


#----------------------------------------------------------------------------#
# Movies Model 
# Attribute : title, release_date
#----------------------------------------------------------------------------#

class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    release_date = Column(DateTime, nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id', ondelete="CASCADE"))
    # fee = Column(Integer)

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


#----------------------------------------------------------------------------#
# Actors Model 
# Attribute : name, age, gender
#----------------------------------------------------------------------------#

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


def db_init_records():
    '''this will initialize the database with some test records.'''

    new_actor = (Actor(
        name='Emraan Hashmi',
        gender='Male',
        age=39
        ))

    new_actor1 = (Actor(
        name='salman khan',
        gender='Male',
        age=50
        ))

    new_actor2 = (Actor(
        name='Hrithik Roshan',
        gender='Male',
        age=40
        ))

    new_actor3 = (Actor(
        name='Tony Starc',
        gender='Male',
        age=45
        ))

    new_actor.insert()
    new_actor1.insert()
    new_actor2.insert()
    new_actor3.insert()

    # Create record for new movie
    new_movie = (Movie(
        title='Jannat',
        release_date=date.today(),
        actor_id=new_actor.id
        ))

    new_movie1 = (Movie(
        title='Partner',
        release_date=date.today(),
        actor_id=new_actor1.id
        ))

    new_movie2 = (Movie(
        title='Super 30',
        release_date=date.today(),
        actor_id=new_actor2.id
        ))
    new_movie3 = (Movie(
        title='Avengers-End game',
        release_date=date.today(),
        actor_id=new_actor3.id
        ))
    
    new_movie.insert()
    new_movie1.insert()
    new_movie2.insert()
    new_movie3.insert()

    db.session.commit()


