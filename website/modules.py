#database Modules
from . import db

# create a db model
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email


    # example = db.relationship('example')