from flask import redirect, render_template, request, url_for
from application import app, db
from application.forms import UserForm, RecipeForm
from application.models import User, Recipe

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template ('layout.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    user_form = UserForm()

    if user_form.validate_on_submit():
        newuser = User(name=user_form.name.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('user.html', form=user_form)

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    user_recipe = RecipeForm()
    users= User.query.all()
    for user in users:
        user_recipe.recipe_user.choices.append((user.id, f'{user.name}'))

    if user_recipe.validate_on_submit():
        recipe = Recipe(name=user_recipe.name.data, user_id=user_recipe.recipe_user.data)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('recipe.html', form=user_recipe)

@app.route('/read', methods=['GET'])
def read():
    users = User.query.all()
    recipes = Recipe.query.all()

    return render_template('read.html', users=users, recipes=recipes)
