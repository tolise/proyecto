from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.views.ping import pingPong


db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/test'
    db = SQLAlchemy(app)

    from app import models

    app.register_blueprint(pingPong)
    return app
