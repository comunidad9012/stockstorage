from flask import Blueprint
from controllers.controller_user import blueprintRegister
from controllers.bajaUsuario import bajaUser
from controllers.controller_login import loginBlueprint


apimain= Blueprint('apimain', __name__, url_prefix='/apimain')


apimain.register_blueprint(blueprintRegister)
apimain.register_blueprint(loginBlueprint)


