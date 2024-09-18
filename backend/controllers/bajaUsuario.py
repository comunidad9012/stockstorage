from flask import Blueprint, request
from schemas.user_schema import userUnsuscribe
from modelsDb.model_usuario import Usuario
from modelsDb import conexion
from marshmallow import ValidationError


bajaUser= Blueprint('usertest1', __name__, url_prefix='/usertest1')

@bajaUser.post("/bajaUsuario")
def bajaUsuario():
    try:
        email=request.json["email"]

        user={"email": email}
        userValidation=userUnsuscribe().load(user)
        userVal=userValidation['email']
        usuario=conexion.session.query(Usuario).filter_by(email=userVal).first()

        if usuario:
       
            conexion.session.delete(usuario)
            conexion.session.commit()
            return(f'{email} eliminado')
        else:
            return (f'usuario {email} no encontrado')

    except ValidationError as badValidation:
        print(f'error {badValidation}')









