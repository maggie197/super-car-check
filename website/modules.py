#database Modules
from . import db
from flask_login import UserMixin

# create a db model
class User(db.Model, UserMixin): # UserMixin to access all the information about the currenty logged in user
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


    # example = db.relationship('example')