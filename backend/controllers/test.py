from flask import Blueprint, request
from modelsDb.model_usuario import Usuario

from modelsDb import conexion

apiUser= Blueprint('usertest', __name__, url_prefix='/usertest')

@apiUser.post('/prueba')
def testUser():
    email=r'roberto'
    password=r'12345'
    Usuario(email,password)
    conexion.session.commit()
    return (f'{email} cargado')



