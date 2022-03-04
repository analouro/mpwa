from flask import Flask, redirect, render_template, request, url_for
from application import app, db
from application.forms import RecipeForm, UserForm
from application.models import User, Recipe

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    userform = UserForm()

    if request.method == 'POST':
        if userform.validate_on_submit():
            user_name = User(user_name=userform.user_name.data)
            db.session.add(user_name)
            db.session.commit()
            return redirect(url_for('recipe'))

    #if the username isn't validated, return to home      
    return render_template('home.html', form=userform)

@app.route('/recipe', methods=['GET', 'POST'])
#@app.route('/recipe/<name>', methods=['GET', 'POST'])
def recipe():

    # if request.method == 'GET':
        return render_template('recipe.html')
    # # userform = UserForm
    # user = User.query.get(1)
    # user.user_name = name
    # db.session.commit()
    # return user.user_name
    # # name.user_name = name

    # if request.method == 'GET':
    #     userform.user_name.data = user.user_name
    #     return render_template('recipe.html', form=userform)
        
    # return render_template ('recipe.html')
    # recipeform = RecipeForm()

    # if recipeform.validate_on_submit():
    #     user_name = User.query.filter_by()
    #     recipe_name = Recipe(recipe_name=recipeform.recipe_name.data)
    #     db.session.add(recipe_name)
    #     db.session.commit()
    #     # if a recipe is added successfully, the user is redirected to the recipe log
    #     return render_template('log.html', form=recipeform)

        # if len(recipe_name) == 0:
        #     message = "Please add a new recipe to continue"
        # else:
        #     message = f'{recipe_name} was added to your recipe log'

    #if a recipe isn't added successfully, refresh the recipe page
    # return render_template('recipe.html', form=recipeform, user=user_name

# @app.route('/log')
# def log():
#     recipes = Recipe.query.all()
#     return render_template('log.html', recipes=recipes)