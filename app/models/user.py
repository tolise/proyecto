from flask_sqlalchemy import SQLAlchemy
from app import db



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    apellido = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

