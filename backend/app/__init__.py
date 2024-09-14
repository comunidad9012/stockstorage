from flask import Flask
from flask_cors import CORS
from blueprints.rutas import apimain
from modelsDb import conexion

def create_app():
    app=Flask(__name__)
    #Esta linea lo que hace es ver si no esta creada la tabla, la crea
    conexion.Base.metadata.create_all(conexion.engine)
    CORS(app)
    
    app.register_blueprint(apimain)


    return app
