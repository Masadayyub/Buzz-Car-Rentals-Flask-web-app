from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from Api import app

db = SQLAlchemy(app)
ma = Marshmallow(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.String(120))

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc


class userSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'desc')

class user_table(db.Model):
    email = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password


class user_tableSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password')

class user_booking(db.Model):
    email = db.Column(db.String(80), primary_key=True)
    id = db.Column(db.Integer)
    carname = db.Column(db.String(80))
    cardescription = db.Column(db.String(80))

    def __init__(self, email, id, carname, cardescription):
        self.email = email
        self.id = id
        self.carname = carname
        self.cardescription = cardescription


class user_bookingSchema(ma.Schema):
    class Meta:
        fields = ('email', 'id', 'carname', 'cardescription')

db.create_all()
