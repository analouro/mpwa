from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from application.models import User, Recipe


# form to enter username
class UserForm(FlaskForm):
    name = StringField('Enter User', validators=[DataRequired(), Length(min=2,max=50)])
    submit = SubmitField('Submit')

# form to enter recipe name
class RecipeForm(FlaskForm):
    name = StringField('Add Recipe:', validators=[DataRequired(), Length(min=2,max=100)])
    recipe_user = SelectField ('Pick a user:', choices=[],validators=[DataRequired()])
    submit = SubmitField('Submit')

# form to update recipe name
class UpdateForm(FlaskForm):
    name = StringField('', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Update')