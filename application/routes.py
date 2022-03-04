from crypt import methods
from email import message
from flask import Flask, redirect, render_template, request, url_for
from application import app, db
from application.forms import RecipeForm, UserForm
from application.models import User, Recipe

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    message = ""
    userform = UserForm()

    if userform.validate_on_submit():
        user_name = User(user_name=userform.user_name.data)
        db.session.add(user_name)
        db.session.commit()
        #if validation is successful, redirect to /recipe
        # return redirect(url_for('recipe'))
        return f"Welcome {user_name}"
        
        # if len(user_name) == 0:
        #     message = "Please add a username to continue"

    # if validation isn't successful, redirect back to /home    
    return render_template('home.html', form=userform, message=message)

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    # message = ""
    recipeform = RecipeForm()

    if recipeform.validate_on_submit():
        recipe_name = Recipe(recipe_name=recipeform.recipe_name.data)
        db.session.add(recipe_name)
        db.session.commit()
        # if a recipe is added successfully, the user is redirected to the recipe log
        return render_template('log.html', form=recipeform)

        # if len(recipe_name) == 0:
        #     message = "Please add a new recipe to continue"
        # else:
        #     message = f'{recipe_name} was added to your recipe log'

    #if a recipe isn't added successfully, refresh the recipe page
    return render_template('recipe.html', form=recipeform), #message=message)

@app.route('/log')
def log():
    recipes = Recipe.query.all()
    return render_template('log.html', recipes=recipes)



