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
            return redirect(url_for('users'))

    #if the username isn't validated, return to home      
    return render_template('home.html', form=userform)

@app.route('/users', methods=['GET'])
def users():
    user_name = User.query.all()
    return render_template('users.html', user_name=user_name )