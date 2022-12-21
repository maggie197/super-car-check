from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .modules import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        session["username"] = username

        found_user =User.query.filter_by(name=username).first()
        if found_user:
            session["email"] = found_user.email

        else:
            username = User(username, "") 
            db.session.add(username)
            db.session.commit()

        return redirect(url_for("views.index", username=username))
        
    else:
        if "username" in session:
            return redirect(url_for("views.index"))
        return render_template('login.html')

@auth.route('/logout')
def logout():
    if "username" in session:
        username = session["username"]
        flash(f"You have been logged out, {username}", "info")

    session.pop("username", None)
    session.pop("email", None)

    return redirect(url_for("auth.login"))