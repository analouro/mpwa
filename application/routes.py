from crypt import methods
from tokenize import Name
from flask import Flask, redirect, render_template, request, url_for
from application import app, db
from application.forms import UserForm
from application.models import User, Recipe

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UserForm()

    if request.method == 'POST':
        user = form.user_name.data
        recipe = form.recipe_name.data

        new = User(user_name=user, recipe_name=recipe)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('read'))
    
    return render_template('home.html', form=form)

@app.route('/read', methods=['GET'])
def read():
    users = User.query.all()
    recipes = User.query.all()

    return render_template('read.html', users=users, recipes=recipes)
