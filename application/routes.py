from crypt import methods
from flask import Flask, render_template, request
from application import app
from application.forms import RecipeForm, UserForm
from application.models import User, Recipe

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    message = ""
    form = UserForm()

    if request.method == 'POST':
        user_name = form.user_name.data
        
        if len(user_name) == 0:
            message = "Please add a username to continue"
        else:
            message = f'Welcome {user_name}'
    
    return render_template('home.html', form=form, message=message)

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    message = ""
    form = RecipeForm()

    if request.method == 'POST':
        recipe_name = form.recipe_name.data

        if len(recipe_name) == 0:
            message = "Please add a new recipe to continue"
        else:
            message = f'{recipe_name} was added to your recipe log'
    
    return render_template('recipe.html', form=form, message=message)

@app.route('/log')
def log():
    recipes = Recipe.query.all()
    return render_template('log.html', recipes=recipes)



