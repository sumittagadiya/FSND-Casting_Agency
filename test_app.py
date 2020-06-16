import unittest
import os
from app import app, create_app
from models import db, Movie, Actor, setup_db, test_db_drop_and_create_all
import json
from datetime import date
import os

database_path = os.environ['TEST_DATABASE_URL']
#database_path='postgres://postgres:1234@localhost:5432/test_casting'
casting_assistant = os.environ['casting_assistant']
casting_director = os.environ['casting_director']
producer = os.environ['producer']

class Casting_TestCase(unittest.TestCase):
    def setUp(self):
        #app=create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        self.app = app.test_client()
        test_db_drop_and_create_all()

        self.actor = {
            "name": "Anil kapur",
            "age": 45,
            "gender": "male"
        }
        self.movie = {
            "title": "Season 24",
            "release_date":date.today(),
            "actor_id":2
        }

    def tearDown(self):
        """Executed after each test"""
        pass


    def test_get_movies_with_casting_assistant(self):
        resp = self.app.get('/movies',headers={'Authorization':casting_assistant})
        #print("test_response======>",resp)
        data = json.loads(resp.data)
        print("test get movies =====>",data)
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(data['total_record'],4)

    def test_get_movies_withoutAuth(self):
        resp = self.app.get('/movies')
        print("test get movies without auth",resp.data)
        self.assertEqual(resp.status_code, 401)

    def test_get_actors_with_casting_assistant(self):
        res = self.app.get('/actors',headers={'Authorization':casting_assistant})
        data = json.loads(res.data)
        print("test get actors=========>",data)
        self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['total_record'],4)  

    def test_get_actors_withoutAuth(self):
        res = self.app.get('/actors')
        print("Test get actors without auth",res)
        self.assertEqual(res.status_code, 401)

    def test_create_new_movie(self):
        res = self.app.post('/movies',json=self.movie,headers={'Authorization':producer})
        data = json.loads(res.data)
        print('test_create_movie ====>',data.items)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movie_auth_error(self):
        res = self.app.post('/movies',json=self.movie,headers={'Authorization':casting_director})
        data = json.loads(res.data)
        print("test create movie invalid auth =============>",data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], True)

    def test_create_new_Actor(self):
        res = self.app.post('/actors',json=self.actor,headers={'Authorization':casting_director})
        data = json.loads(res.data)
        print("test create actor=======>",data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor_auth_error(self):
        res = self.app.post('/actors', json=self.actor, headers={'Authorization':casting_assistant})
        data = json.loads(res.data)
        print("test create actor invalid auth==========>",data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], True)
    
    
    def test_delete_actors(self):
        res = self.app.delete('/actors/1',headers={'Authorization':casting_director})
        print("Deleted Actor======>",res)
        self.assertEqual(res.status_code, 200)

    def test_patch_movie_success(self):
        res = self.app.patch('/movies/2',headers={'Authorization':producer},json={"title": "Ready"})
        data = json.loads(res.data)
        print("patch movie=======>",data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movie_Auth_error(self):
        res = self.app.patch(
            '/movies/3',
            headers={'Authorization': casting_assistant},
             json={"title": "Ready"}
        )
        data = json.loads(res.data)
        print("test patch movie auth error=======>",data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], True)

    # delete Failure message 404 error
    def test_404_delete_if_actor_does_not_exist(self):
        res = self.app.delete(
            '/actors/2000',
            headers={'Authorization': producer}
        )
        data = json.loads(res.data)
        print("test error invalid delete items ====> ",data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # delete movie
    def test_delete_movie(self):
        res = self.app.delete('/movies/2',headers={'Authorization':producer})
        print("Deleted Movie======>",res)
        self.assertEqual(res.status_code, 200)

    def test_movie_delete_auth_error(self):
        res = self.app.delete(
            '/movies/2',
            headers={'Authorization':casting_director}
        )
        data = json.loads(res.data)
        print("test movie delete auth error=====>",data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], True)


if __name__ == '__main__':
    unittest.main()
    


    

