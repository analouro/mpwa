from flask import Flask, request, render_template, redirect, url_for

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Welcome to M.E.A.L.'