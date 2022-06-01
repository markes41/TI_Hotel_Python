from flask import request
from services.habitaciones_service import Habitaciones_Service as service
from models.habitacion import HabitacionSchema as schema

class Habitaciones_Module:

    base_url = "/habitaciones"

    def agregar_habitacion():
        sHabitacion = schema()
        habitacion = sHabitacion.load(request.json)

        return service.agregar_habitacion(habitacion)

    def modificar_habitacion(id):
        hab_original = service.obtener_habitacion(id)

        if hab_original is None:
            return {"status": 404, "message": "Registro no encontrado."}

        sHabitacion = schema()
        hab_modificada = sHabitacion.load(request.json)

        hab_original.precio = hab_modificada.precio
        hab_original.reservada = hab_modificada.reservada
        hab_original.activa = hab_modificada.activa

        return service.modificar_habitacion(hab_original)

    def eliminar_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}

        return service.eliminar_habitacion(habitacion)

    def obtener_habitaciones():
        habitaciones = service.obtener_habitaciones()

        if habitaciones is None:
            return {"status": 404, "message": "Registro no encontrado."}

        habitacionSchema = schema(many=True)
        return {"status": 200, "result": habitacionSchema.dump(habitaciones)}

    def obtener_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}

        habitacionSchema = schema()
        return {"status": 200, "result": habitacionSchema.dump(habitacion)}

    def deshabilitar_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}

        habitacion.activa = False

        return service.modificar_habitacion(habitacion)