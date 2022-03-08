from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import User, Recipe

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='today',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        user1 = User(name="MsTest")
        user2 = User(name="MrTest")
        user3 = User(name="BabyTest")

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestViews(TestBase):
    def test_read(self):
        response = self.client.post(url_for('recipe'))
        self.assertIn(b'MsTest', response.data)

class TestViews(TestBase):
    def test_recipe(self):
        response = self.client.post(url_for('recipe'))
        self.assertIn(b'MsTest', response.data)



# class TestViews(TestBase):
#     def test_recipe_post(self):
#         response = self.client.post(url_for('recipe'))
#         self.assertIn(b'RecipeX', response.data)

# class TestViews(TestBase):
#     def test_read_get(self):
#         response = self.client.get(url_for('read'))
#         self.assertEqual(response.status_code, 200)