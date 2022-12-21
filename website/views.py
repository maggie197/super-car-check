from flask import Blueprint, render_template, session, redirect, url_for
from markupsafe import escape

views = Blueprint('views', __name__)

@views.route('/')

def index():
    if "username" in session:
        username = session["username"]
        return render_template('index.html', username=username)
    else:
        return redirect(url_for("auth.login"))
