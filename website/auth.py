from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/home')
def homepage():
    return 'Hello, World'