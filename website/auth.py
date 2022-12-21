from flask import Blueprint, render_template, request, redirect, url_for, session
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        session["username"] = username
        return redirect(url_for("views.index", username=username))

    else:
        if "username" in session:
            return redirect(url_for("views.index"))
        return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for("auth.login"))