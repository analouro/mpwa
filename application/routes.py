from flask import Flask
from application import app

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to M.E.A.L.'