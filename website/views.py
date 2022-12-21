from flask import Blueprint, render_template
from markupsafe import escape

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/<username>')
def profile(username):
    return render_template('index.html', username=username)

