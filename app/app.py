from decorators.auth.auth_middleware import token_required
from decorators.error.error_middleware import error_middleware
from decorators.auth.roles_middleware import roles_middleware
from modules.authentication_module import AuthModule as Auth
from modules.habitaciones_module import Habitaciones_Module as Habitaciones
from modules.usuarios_module import Usuarios_Module as Usuarios
from mkapp import app, db


# endpoints Login #
@app.route(Auth.base_url + '/login', methods=['POST'])
@error_middleware
def login():
	auth = Auth()
	return auth.login()
###################

# endpoints Habitaciones #
@app.route(Habitaciones.base_url + '/agregar', methods=['POST'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def agregar_habitacion():
	return Habitaciones.agregar_habitacion()

@app.route(Habitaciones.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def modificar_habitacion(id):
	return Habitaciones.modificar_habitacion(id)

@app.route(Habitaciones.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def eliminar_habitacion(id):
	return Habitaciones.eliminar_habitacion(id)

@app.route(Habitaciones.base_url + '/get/<int:id>', methods=['GET'])
@token_required
@error_middleware
def obtener_habitacion(id):
	return Habitaciones.obtener_habitacion(id)

@app.route(Habitaciones.base_url + '/getlistado', methods=['GET'])
@token_required
@error_middleware
def obtener_habitaciones():
	return Habitaciones.obtener_habitaciones()

@app.route(Habitaciones.base_url + '/deshabilitar/<int:id>', methods=['GET'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def deshabilitar_habitacion(id):
	return Habitaciones.deshabilitar_habitacion(id)
########################

# endpoints Usuarios #
@app.route(Usuarios.base_url + '/agregar', methods=['POST'])
@error_middleware
def agregar_usuario():
	return Usuarios.agregar_usuario()

@app.route(Usuarios.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
@error_middleware
def modificar_usuario(id):
	usu = Usuarios()
	return usu.modificar_usuario(id)

@app.route(Usuarios.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
@error_middleware
def eliminar_usuario(id):
	return Usuarios.eliminar_usuario(id)

@app.route(Usuarios.base_url + '/get/<int:id>', methods=['GET'])
@token_required
@error_middleware
def obtener_usuario(id):
	return Usuarios.obtener_usuario(id)
######################

@app.route('/init', methods=["POST"])
@error_middleware
def crear_tablas():
	db.create_all()
	return {"message": "Se crearon las tablas correctamente."}

# Crear tablas
db.create_all()
##############

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)