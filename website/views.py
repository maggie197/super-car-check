from flask import Blueprint, url_for
from markupsafe import escape

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return 'index'

@views.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

