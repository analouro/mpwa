from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from application import app
from application.models import User
from application.models import Recipe

# class to enter username
class UserForm(FlaskForm):
    user_name = StringField('Enter Username', validators=[DataRequired(), Length(min=2,max=50)])
    recipe_name = StringField('Add Recipe', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Submit')

# # class to enter recipe name
# class RecipeForm(FlaskForm):
#     recipe_name = StringField('Add Recipe Name', validators=[DataRequired(), Length(min=2,max=100)])
#     submit_recipe = SubmitField('Add Recipe')

