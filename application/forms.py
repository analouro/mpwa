from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from application import app
from application.models import User
from application.models import Recipe

# class to enter username
class UserForm(FlaskForm):
    user_name = StringField('Enter Username')
    submit_name = SubmitField('Add Username')

# class to enter recipe name
class RecipeForm(FlaskForm):
    recipe_name = StringField('Enter the name of your Recipe')
    submit_recipe = SubmitField('Add Recipe')

