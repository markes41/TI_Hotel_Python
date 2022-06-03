from flask import Blueprint
from modules.usuarios_module import Usuarios_Module  as Usuarios
from decorators.error.error_middleware import error_middleware

auth_route = Blueprint('auth_route', __name__)

def get_blueprint():
    """"Retorna el blueprint para la app principal"""
    return auth_route

@auth_route.route('/auth/login', methods=['POST'])
@error_middleware
def login():
	auth = Auth()
	return auth.login()
    