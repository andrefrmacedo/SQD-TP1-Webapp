from flask import Blueprint, render_template, request
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


@views.route('/backgroundDose', methods=['POST'])
def get_background_dose():

    weight = request.form['weight']
    data = n_voter(0, [weight])

    return render_template('response.html', data=data, type='Background Dose', details=False)


@views.route('/mealtimeStandard', methods=['POST'])
def get_mealtime_standard():
    return render_template('index.html')


@views.route('/mealtimePersonal', methods=['POST'])
def get_mealtime_personal():
    return render_template('index.html')