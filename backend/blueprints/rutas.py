from flask import Blueprint
from controllers.test import apiUser
from controllers.bajaUsuario import bajaUser

apimain= Blueprint('apimain', __name__, url_prefix='/apimain')


apimain.register_blueprint(apiUser)
apimain.register_blueprint(bajaUser)


