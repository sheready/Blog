from flask import Flask, render_template
from app.forms import LoginForm
from app import app


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')