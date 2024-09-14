from flask import Blueprint, request
from modelsDb.model_usuario import Usuario

from modelsDb import conexion

apiUser= Blueprint('usertest', __name__, url_prefix='/usertest')

@apiUser.post('/prueba')
def testUser():
    email=request.json['email']
    password=request.json['password']
    new_user=Usuario(email,password)
    conexion.session.add(new_user)
    conexion.session.commit()
    return (f'{email} cargado')



