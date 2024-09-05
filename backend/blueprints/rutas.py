from flask import Blueprint
from controllers.test import apiUser

apimain= Blueprint('apimain', __name__, url_prefix='/apimain')
apimain.register_blueprint(apiUser)


