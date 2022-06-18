from flask import request
from services.habitaciones_service import Habitaciones_Service as service
from models.habitacion import HabitacionSchema as schema

class Habitaciones_Module:

    base_url = "/habitaciones"

    def agregar_habitacion():
        sHabitacion = schema()
        habitacion = sHabitacion.load(request.json)

        if(habitacion.precio < 0):
            return {"status": 404, "message": "El precio debe ser mayor a 0."}, 404

        return service.agregar_habitacion(habitacion)

    def modificar_habitacion(id):
        hab_original = service.obtener_habitacion(id)

        if hab_original is None:
            return {"status": 404, "message": "Registro no encontrado."}

        hab_original.precio = request.json["precio"]

        if(hab_original.precio < 0):
            return {"status": 404, "message": "Introduzca un precio válido."}, 404

        return service.modificar_habitacion(hab_original)

    def eliminar_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}, 404

        return service.eliminar_habitacion(habitacion)

    def obtener_habitaciones():
        habitaciones = None

        if len(habitaciones) == 0:
            return {"status": 404, "message": "No hay habitaciones disponibles."}, 404

        habitacionSchema = schema(many=True)
        return {"status": 200, "result": habitacionSchema.dump(habitaciones)}

    def obtener_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}, 404

        habitacionSchema = schema()
        return {"status": 200, "result": habitacionSchema.dump(habitacion)}

    def deshabilitar_habitacion(id):
        habitacion = service.obtener_habitacion(id)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}, 404

        habitacion.activa = False

        return service.modificar_habitacion(habitacion)

    def obtener_habitaciones_precio(precio):

        habitaciones = service.obtener_habitaciones_precio(precio)

        if len(habitaciones) == 0:
            return {"status": 404, "message": "No se encontraron registros."}, 404
        
        habitacionSchema = schema(many=True)
        return {"status": 200, "result": habitacionSchema.dump(habitaciones)}