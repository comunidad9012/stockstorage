from flask import Flask
from flask_cors import CORS
from blueprints.rutas import apimain
from modelsDb import conexion
from flask_login import LoginManager

def create_app():
    app=Flask(__name__)
    #Esta linea lo que hace es ver si no esta creada la tabla, la crea
    app.secret_key = 'N8kikNDvPn' 
    login_manager = LoginManager()
    login_manager.init_app(app)
    conexion.Base.metadata.create_all(conexion.engine)
    CORS(app)
    
    app.register_blueprint(apimain)


    return app
