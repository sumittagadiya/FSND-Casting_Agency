# ---------------#
# Imports -------#
# ---------------#

import json
import os
import unittest
from app import app, create_app
from models import Movie,Actor,test_db_drop_create_all

from datetime import date
import os

database_path = os.environ['TEST_DATABASE_URL']
#database_path='postgres://postgres:1234@localhost:5432/test_casting'  (incase of locally run)
assistant = os.environ['assistant']
director = os.environ['director']
producer = os.environ['producer']

class Casting_Agency_TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        self.app = app.test_client()
        test_db_drop_create_all()

        
    def tearDown(self):
        """Executed after each test"""
        pass


    # test get movies with authorization
    def test_get_movies_authorized(self):
        resp = self.app.get('/movies',headers={'Authorization':assistant})
        data = json.loads(resp.data)
        print("test get movies with auth ----------------->",data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])


    # test get movies without authorization header
    def test_get_movies_unauthorized(self):
        resp = self.app.get('/movies')
        data = json.loads(resp.data)
        print("test get movies without auth ------------------------>",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])
 

    # test get all actors with authorization
    def test_get_actors_authorized(self):
        resp = self.app.get('/actors',headers={'Authorization':assistant})
        data = json.loads(resp.data)
        print("test get actors with auth-------------------------------->",data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])
          

    # test get actors without authorization header
    def test_get_actors_unauthorized(self):
        resp = self.app.get('/actors')
        data = json.loads(resp.data)
        print("Test get actors without auth-------------------------------->",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])

    # test post movie with valid authorization
    def test_add_new_movie_valid_authorized(self):
        data = {"title": "Season 24", "release_date": date.today(),"actor_id":2}
        resp = self.app.post('/movies',json=data,headers={'Authorization':producer})
        data = json.loads(resp.data)
        print('test create movie with valid auth------------------------------->',data.items)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])


    # test post movie with invalid authorization
    def test_add_new_movie_invalid_authorized(self):
        data1 = {"title": "Season 24", "release_date": date.today(),"actor_id":2}
        resp = self.app.post('/movies',json=data1,headers={'Authorization':director})
        data = json.loads(resp.data)
        print("test create movie invalid auth ------------------------->",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])


    # test post actor with valid authorization
    def test_add_Actor_valid_authorized(self):
        actor_data = {"name": "Anil kapur","age": 45,"gender": "male"}
        resp = self.app.post('/actors',json=actor_data,headers={'Authorization':director})
        data = json.loads(resp.data)
        print("test create actor valid authorized ------------------------->",data.items)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])


    # test post actor invalid authorization
    def test_add_Actor_invalid_authorized(self):
        actor_data = {"name": "Anil kapur","age": 45,"gender": "male"}
        resp = self.app.post('/actors', json=actor_data, headers={'Authorization':assistant})
        data = json.loads(resp.data)
        print("test create actor invalid auth-------------------------------->",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])
    

    # test patch movie with valid authorization
    def test_patch_movie_valid_authorized(self):
        resp = self.app.patch('/movies/2',headers={'Authorization':producer},json={"title": "Ready"})
        data = json.loads(resp.data)
        print("patch movie valid authorized---------------------------------->",data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])
    

    # test patch movie invalid authorization
    def test_patch_movie_invalid_authorized(self):
        resp = self.app.patch('/movies/3',headers={'Authorization': assistant},json={"title": "Ready"})
        data = json.loads(resp.data)
        print("patch movie invalid authorized----------------------->",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])


    # test delete actor with valid authorization
    def test_remove_actors_valid_authorized(self):
        resp = self.app.delete('/actors/1',headers={'Authorization':director})
        data = json.loads(resp.data)
        print("Delete Actor valid Authorized------------------------>",data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])
  

    # test delete actor invalid authorization
    def test_remove_actors_invalid_authorized(self):
        resp = self.app.delete('/actors/1',headers={'Authorization':assistant})
        data = json.loads(resp.data)
        print("Delete Actor invalid authorized ----------------------------->",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])


    # test delete actor id not found
    def test_remove_actor_id_not_found(self):
        resp = self.app.delete('/actors/1500',headers={'Authorization': producer})
        data = json.loads(resp.data)
        print("test delete actor id not found --------------------------> ",data)
        self.assertEqual(resp.status_code, 404)
        self.assertFalse(data['success'])

    # test delete movie valid authorized
    def test_remove_movie_valid_authorized(self):
        resp = self.app.delete('/movies/2',headers={'Authorization':producer})
        data = json.loads(resp.data)
        print("Test delete movie valid authorized------------------->",data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['success'])

    # test delete movie with invalid auth
    def test_delete_movie_invalid_authorized(self):
        resp = self.app.delete('/movies/2',headers={'Authorization':director})
        data = json.loads(resp.data)
        print("test movie delete invalid authorized------------------------>",data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(data['success'])

    
    # test delete movie id not found
    def test_delete_movie_id_not_found(self):
        res = self.app.delete('/movies/2000',headers={'Authorization':producer})
        data = json.loads(res.data)
        print("test delete movie id not found------------------------------->",data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


if __name__ == '__main__':
    unittest.main()
    


    

