from flask import Flask
from flask_cors import CORS
from blueprints.rutas import apimain

def create_app():
    app=Flask(__name__)
    CORS(app)


    app.register_blueprint(apimain)


    return app
