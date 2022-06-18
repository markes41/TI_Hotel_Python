from flask import Blueprint
from modules.habitaciones_module import Habitaciones_Module as Habitaciones
from decorators.error.error_middleware import error_middleware
from decorators.auth.auth_middleware import token_required
from decorators.auth.roles_middleware import roles_middleware

habitaciones_route = Blueprint('habitaciones_route', __name__)

def get_blueprint():
    """"Retorna el blueprint para la app principal"""
    return habitaciones_route

@habitaciones_route.route(Habitaciones.base_url + '/agregar', methods=['POST'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def agregar_habitacion():
	return Habitaciones.agregar_habitacion()

@habitaciones_route.route(Habitaciones.base_url + '/modificar/<int:id>', methods=['PUT'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def modificar_habitacion(id):
	return Habitaciones.modificar_habitacion(id)

@habitaciones_route.route(Habitaciones.base_url + '/eliminar/<int:id>', methods=['DELETE'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def eliminar_habitacion(id):
	return Habitaciones.eliminar_habitacion(id)

@habitaciones_route.route(Habitaciones.base_url + '/get/<int:id>', methods=['GET'])
@token_required
@error_middleware
def obtener_habitacion(id):
	return Habitaciones.obtener_habitacion(id)

@habitaciones_route.route(Habitaciones.base_url + '/getHabitaciones', methods=['GET'])
@token_required
@error_middleware
def obtener_habitaciones():
	return Habitaciones.obtener_habitaciones()

@habitaciones_route.route(Habitaciones.base_url + '/deshabilitar/<int:id>', methods=['GET'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def deshabilitar_habitacion(id):
	return Habitaciones.deshabilitar_habitacion(id)

@habitaciones_route.route(Habitaciones.base_url + '/get/precio/<precio>', methods=['GET'])
@token_required
@error_middleware
@roles_middleware("Cliente")
def obtener_habitaciones_precio(precio):
	return Habitaciones.obtener_habitaciones_precio(precio)

