from flask import Blueprint, render_template, request, redirect, url_for, session
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        return redirect(url_for("views.index", username=username))

    else:
        return render_template('login.html')

@auth.route('/logout')
def logout():
    return "Logged out"