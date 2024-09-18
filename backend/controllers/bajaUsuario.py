from flask import Blueprint, request
from schemas.user_schema import userUnsuscribe
from modelsDb.model_usuario import Usuario
from modelsDb import conexion
from marshmallow import validationError


bajaUser= Blueprint('bajaUser', __name__, url_prefix='/bajaUser')

@bajaUser.post("/bajaUsuario")
def bajaUsuario():
    try:
        email=request.json("email")

        user={"email": email}
        userValidation=userUnsuscribe().load(user)
        userVal=Usuario(email=userValidation['email'])

        if userVal:
       
            conexion.session.delete(userVal)
            conexion.session.commit()
            return(f'{email} eliminado')
        else:
            return (f'usuario {email} no encontrado')

    except Exception as e:
        return (f'error {e}'),500









