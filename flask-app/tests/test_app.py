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
        db.session.commit()
        db.drop_all()
        db.create_all()

        user1 = User(name="MsTest")
        # recipe1 = Recipe(name="Testghetti")
        # recipe2 = Recipe(name="Testeroni")
        # recipe3 = Recipe(name="Testonara")
        # recipe4 = Recipe(name="Testognese")
        # recipe5 = Recipe(name="Testake")

        db.session.add(user1)
        # db.session.add(recipe1)
        # db.session.add(recipe2)
        # db.session.add(recipe3)
        # db.session.add(recipe4)
        # db.session.add(recipe5)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestPages(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        response = self.client.get(url_for('user'))
        self.assertEqual(response.status_code, 200)

    def test_read(self):
        response = self.client.post(url_for('recipe'))
        self.assertIn(b'MsTest', response.data)
        # self.assertIn(b'Testghetti', response.data)