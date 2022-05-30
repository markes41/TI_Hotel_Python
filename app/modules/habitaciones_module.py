from flask import request
from models.habitacion import Habitacion
from services.habitaciones_service import Habitaciones_Service as service
from helpers.habitaciones_helper import Habitaciones_Helper as helper

class Habitaciones_Module:

    base_url = "/Habitaciones"

    def agregar_habitacion():
        habitacion = helper.request_habitacion(request)

        return service.agregar_habitacion(habitacion)

    def modificar_habitacion(id):
        hab_modificada = helper.request_habitacion(request)

        hab_original = Habitacion.query.get(id)
        hab_original.precio = hab_modificada.precio
        hab_original.reservada = hab_modificada.reservada
        hab_original.fecha_reserva = hab_modificada.fecha_reserva
        hab_original.estado = hab_modificada.estado  

        return service.modificar_habitacion(hab_original)

    def eliminar_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        return service.eliminar_habitacion(habitacion)

    def obtener_habitaciones():
        return service.obtener_habitaciones()

    def obtener_habitacion(id):
        return service.obtener_habitacion(id)