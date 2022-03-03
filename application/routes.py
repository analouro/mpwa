from crypt import methods
from flask import Flask, render_template, request
from application import app
from application.forms import UserForm

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
