from flask import Blueprint
from modules.reservas_module import Reservas_Module  as Reservas
from decorators.error.error_middleware import error_middleware
from decorators.auth.auth_middleware import token_required
from decorators.auth.roles_middleware import roles_middleware

reservas_route = Blueprint('reservas_route', __name__)

def get_blueprint():
    """"Retorna el blueprint para la app principal"""
    return reservas_route

@reservas_route.route(Reservas.base_url + '/reservarHabitacion', methods=['POST'])
@token_required
@error_middleware
@roles_middleware("Cliente")
def reservar_habitacion():
	return Reservas.reservar_habitacion()

@reservas_route.route(Reservas.base_url + '/getHabitacionesByFecha/<fecha_desde>/<fecha_hasta>', methods=['GET'])
@error_middleware
@token_required
@roles_middleware("Cliente")
def obtener_habitacion_by_dia(fecha_desde, fecha_hasta):
	return Reservas.obtener_reservas_by_fecha(fecha_desde, fecha_hasta)

@reservas_route.route(Reservas.base_url + '/getReservasByHabitacion/<int:id>', methods=['GET'])
@error_middleware
@token_required
@roles_middleware("Cliente")
def obtener_reservas_by_Habitacion(id):
	return Reservas.obtener_reservas_by_habitacion(id)

@reservas_route.route(Reservas.base_url + '/getEstadoHabitaciones/<fecha>', methods=['GET'])
@error_middleware
@token_required
@roles_middleware("Cliente")
def obtener_estado_habitaciones(fecha):
	return Reservas.obtener_estado_habitaciones(fecha)