from flask import request
from services.reservas_service import Reservas_Service as service
from models.reserva import ReservaSchema as schema, Reserva
from datetime import datetime
from services.habitaciones_service import Habitaciones_Service as habitaciones_service


class Reservas_Module:

    base_url = "/reservas"

    def obtener_habitaciones_reservadas(id):
        habitaciones = service.obtener_habitaciones_reservadas(id)

        if len(habitaciones) == 0:
            return {"status": 200, "message": "No hay habitaciones reservadas."}

        sHabitaciones = schema(many=True)
        
        return {"status": 200, "result": sHabitaciones.dump(habitaciones)}

    def reservar_habitacion():
        
        id_habitacion = request.json["id_habitacion"]

        habitacion = habitaciones_service.obtener_habitacion(id_habitacion)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}, 404

        if habitacion.activa == False:
            return {"status": 200, "message": f"La habitación N°: {habitacion.id} se encuentra deshabilitada para ser reservada. Intente con otra."}, 200 

        if habitacion.reservada == True:
            return {"status": 200, "message": f"La habitación N°: {habitacion.id} ya se encuentra reservada."}, 200
        
        
        fecha_desde = request.json["fecha_desde"]
        fecha_hasta = request.json["fecha_hasta"]

        reserva = Reserva(habitacion.id, fecha_desde, fecha_hasta)

        result = service.agregar_reserva(reserva)

        if result:
            habitacion.reservada = True
            habitaciones_service.modificar_habitacion(habitacion)

        return {"status": 200, "message": f"Se reservó la habitación N°: {habitacion.id} correctamente."}, 200

    def obtener_reservas_by_fecha(fecha_str):
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')

        reservas = service.obtener_reservas_by_fecha(fecha)

        if len(reservas) == 0:
            return {"status": 404, "message": "No se encontraron registros."}, 404

        habitaciones_transformado = []

        for reserva in reservas:
            habitaciones_transformado.append({"num_habitacion": reserva.habitacion.id, "fecha_reserva": reserva.fecha_desde,
            "disponibilidad": "Disponible" if reserva.habitacion.reservada == False else "Ocupada"})

        return {"status": 200, "result": habitaciones_transformado}

        

        