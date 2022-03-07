from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from application.models import User, Recipe


# class to enter username
class UserForm(FlaskForm):
    name = StringField('Enter User', validators=[DataRequired(), Length(min=2,max=50)])
    # recipe_name = StringField('Add Recipe', validators=[DataRequired(), Length(min=2,max=100)])
    # user_id = SelectField('User', choices=[])
    submit = SubmitField('Submit')

# # class to enter recipe name
class RecipeForm(FlaskForm):
    name = StringField('Add Recipe:', validators=[DataRequired(), Length(min=2,max=100)])
    recipe_user = SelectField ('Pick a user:', choices=[],validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    name = StringField('Add Recipe:', validators=[DataRequired(), Length(min=2,max=100)])
    submit = SubmitField('Update')