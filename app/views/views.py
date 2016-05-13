from flask import Blueprint, render_template
from ..voter import n_voter

views = Blueprint('views', __name__, url_prefix="")


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/mealstandard')
def meal_standard():
    return render_template('mealstandard.html')


@views.route('/mealpersonal')
def meal_personal():
    return render_template('mealpersonal.html')


@views.route('/background')
def background():
    return render_template('background.html')
