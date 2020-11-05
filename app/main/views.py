from flask import render_template, url_for
from . import main


@main.route('/')
@main.route('/home')
def index():

    title = Home
    return render_template('index.html', title=title)

@main.route('/about')
def about():

    title =About
    return render_template('about.html', title=title)

@main.route('/menu')
def menu():

    title = Home
    return render_template('menu.html', title=title)

