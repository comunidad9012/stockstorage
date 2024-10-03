from flask import Blueprint, request, jsonify
from schemas.user_schema import userRegisterSchema
from modelsDb.model_usuario import Usuario
from marshmallow import ValidationError
from modelsDb import conexion
from flask_login import login_user

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.post('/')
def loginUser(): 
    try:

        email = request.json.get('email')
        password = request.json.get('password')
        newUser = {
            "email": email,
            "password": password
        }
        userValidation = userRegisterSchema().load(newUser)
        user = conexion.session.query(Usuario).filter_by(email=userValidation['email']).first()

        if user and user.password:
            login_user(user)
            return jsonify({'message': 'Logueado correctamente'})
        else:
            return jsonify({'message': 'Credenciales incorrectas'})

    except ValidationError as badValidation:
        return jsonify({'error': str(badValidation)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
