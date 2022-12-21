from flask import Blueprint, render_template
from markupsafe import escape

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/<username>')
def index(username=""):
    return render_template('index.html', username=username)

