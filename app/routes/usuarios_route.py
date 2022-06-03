from flask import Blueprint
from modules.usuarios_module import Usuarios_Module as Usuarios
from decorators.error.error_middleware import error_middleware
from decorators.auth.auth_middleware import token_required
from decorators.auth.roles_middleware import roles_middleware

usuarios_route = Blueprint('usuarios_route', __name__)

def get_blueprint():
    """"Retorna el blueprint para la usuarios_route principal"""
    return usuarios_route

@usuarios_route.route(Usuarios.base_url + '/agregar', methods=['POST'])
@error_middleware
def agregar_usuario():
	return Usuarios.agregar_usuario()

@usuarios_route.route(Usuarios.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
@error_middleware
def modificar_usuario(id):
	return Usuarios.modificar_usuario(id)

@usuarios_route.route(Usuarios.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
@error_middleware
def eliminar_usuario(id):
	return Usuarios.eliminar_usuario(id)

@usuarios_route.route(Usuarios.base_url + '/get/<int:id>', methods=['GET'])
@token_required
@error_middleware
def obtener_usuario(id):
	return Usuarios.obtener_usuario(id)

@usuarios_route.route(Usuarios.base_url + '/getUsuarios', methods=['GET'])
@token_required
@error_middleware
def obtener_usuarios():
	return Usuarios.obtener_usuarios()