from helpers.auth_middleware import token_required
from modules.authentication_module import AuthenticationModule as Auth
from modules.roles_module import Roles_Module as Roles
from modules.habitaciones_module import Habitaciones_Module as Habitaciones
from modules.usuarios_module import Usuarios_Module as Usuarios
from mkapp import app, db

# endpoints Login #
@app.route(Auth.base_url + '/login', methods=['POST'])
def login():
	return Auth.login()
###################

# endpoints Habitaciones #
@app.route(Habitaciones.base_url + '/agregar', methods=['POST'])
@token_required
def agregar_habitacion():
	return Habitaciones.agregar_habitacion()

@app.route(Habitaciones.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
def modificar_habitacion(id):
	return Habitaciones.modificar_habitacion(id)

@app.route(Habitaciones.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
def eliminar_habitacion(id):
	return Habitaciones.eliminar_habitacion(id)

@app.route(Habitaciones.base_url + '/get/<int:id>', methods=['GET'])
@token_required
def obtener_habitacion(id):
	return Habitaciones.obtener_habitacion(id)

@app.route(Habitaciones.base_url + '/getlistado', methods=['GET'])
@token_required
def obtener_habitaciones():
	return Habitaciones.obtener_habitaciones()
########################

# endpoints Roles #
@app.route(Roles.base_url + '/agregar', methods=['POST'])
@token_required
def agregar_rol():
	return Roles.agregar_rol()

@app.route(Roles.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
def modificar_rol(id):
	return Roles.modificar_rol(id)

@app.route(Roles.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
def eliminar_rol(id):
	return Roles.eliminar_rol(id)
#####################

# endpoints Usuarios #

@app.route(Usuarios.base_url + '/agregar', methods=['POST'])
def agregar_usuario():
	return Usuarios.agregar_usuario()

@app.route(Usuarios.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
def modificar_usuario():
	return Usuarios.modificar_usuario(id)

@app.route(Usuarios.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
def eliminar_usuario():
	return Usuarios.eliminar_usuario(id)

@app.route(Usuarios.base_url + '/get/<int:id>', methods=['GET'])
@token_required
def obtener_usuario(id):
	return Usuarios.obtener_usuario(id)
######################


@app.route('/', methods=['GET'])
def index():
	return "hola mundo nuevo"

# Crear tablas
db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")