import imp
from flask import Blueprint
from modules.reservas_module import Reservas_Module  as Reservas
from decorators.error.error_middleware import error_middleware
from decorators.auth.auth_middleware import token_required
from decorators.auth.roles_middleware import roles_middleware

reservas_route = Blueprint('reservas_route', __name__)

def get_blueprint():
    """"Retorna el blueprint para la app principal"""
    return reservas_route

@reservas_route.route(Reservas.base_url + '/getReservas', methods=['GET'])
@token_required
@error_middleware
@roles_middleware("Empleado")
def obtener_reservas():
	return Reservas.obtener_habitaciones_reservadas()

@reservas_route.route(Reservas.base_url + '/reservarHabitacion/<int:id>/<int:cantidad_dias>', methods=['POST'])
@token_required
@error_middleware
@roles_middleware("Cliente")
def reservar_habitacion(id, cantidad_dias):
	return Reservas.reservar_habitacion(id, cantidad_dias)

@reservas_route.route(Reservas.base_url + '/obtenerHabitacionesByDia', methods=['GET'])
def obtener_habitacion_by_dia():
	return Reservas.obtener_reservas_by_dia()