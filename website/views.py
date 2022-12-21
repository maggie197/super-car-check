from flask import Blueprint,request, render_template, session, redirect, url_for, flash
from markupsafe import escape
from .modules import User
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=["POST", "GET"])

def index():
    email = None
    if "username" in session:
        username = session["username"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user =User.query.filter_by(name=username).first()
            found_user.email = email
            db.session.commit()
        else:
            if "email" in session:
                email = session["email"]

        return render_template('index.html', email=email, username=username)
    else:
        flash("You are not logged in!", "error")
        return redirect(url_for("auth.login"))
