from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Изменено на String
    password = db.Column(db.String(128), nullable=False)  # Изменено на String
