from flask import Flask, jsonify
from flask import Blueprint, request, current_app, jsonify,current_app

#aca traigo el modelo y la base de datos
from modelsDb import conexion
from modelsDb.modelosDb import Usuario

app = Flask(__name__)


#logica para crear la base de datos en sqlalchemy

#Esta linea lo que hace es ver si no esta creada la tabla, la crea
conexion.Base.metadata.create_all(conexion.engine)

#ingresar datos
def run():
    papa=Usuario("felix")
    conexion.session.add(papa)
    print(papa.id)
    conexion.session.commit()
#run()

consulta=conexion.session.query(Usuario).all()
#print(consulta)
consulta=conexion.session.query(Usuario).count()

#filtrar datos
miNombre=conexion.session.query(Usuario).filter_by(username='genaro').first()
#print(miNombre.username)



