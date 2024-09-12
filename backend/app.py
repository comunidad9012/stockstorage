from flask import Flask, jsonify
from flask import Blueprint, request, current_app, jsonify,current_app
from sqlalchemy.ext.declarative import declarative_base


#aca traigo el modelo y la base de datos
from modelsDb import conexion
from modelsDb.modelosDb import Usuario

app = Flask(__name__)

@app.route("/")
def inicio():
    return("hola mundo")
    
#Esta linea lo que hace es ver si no esta creada la tabla, la crea
conexion.Base.metadata.create_all(conexion.engine)
print(type(conexion.engine))



#ingresar datos
def run():
    usuario=Usuario("rosa@gmail.com", "12356")
    conexion.session.add(usuario)
    print(usuario.id)
    conexion.session.commit()
#run()

#CONSULTAS DE EJEMPLO DE SQLALCHEMY
# consulta=conexion.session.query(Usuario).all()
# for i in consulta:
#     print(i.email)

#consulta=conexion.session.query(Usuario).count()

#filtrar datos
#miNombre=conexion.session.query(Usuario).filter_by(username='genaro').first()
#print(miNombre.username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

