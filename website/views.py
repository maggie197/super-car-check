from flask import Blueprint
from markupsafe import escape

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> Hello </h1>"

@views.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
