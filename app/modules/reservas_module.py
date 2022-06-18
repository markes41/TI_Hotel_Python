from flask import request
from models.reserva import ReservaSchema
from models.habitacion import HabitacionSchema
from services.reservas_service import Reservas_Service as service
from models.reserva import ReservaSchema as schema, Reserva
from services.habitaciones_service import Habitaciones_Service as habitaciones_service
from datetime import datetime, date
from mkapp import app

class Reservas_Module:

    base_url = "/reservas"

    def reservar_habitacion():
        fecha_desde = datetime.strptime(request.json["fecha_desde"], app.config['DATE_FORMAT'])
        fecha_hasta = datetime.strptime(request.json["fecha_hasta"], app.config['DATE_FORMAT'])

        if fecha_desde > fecha_hasta:
            return {"status": 404, "message": "La fecha de inicio no puede ser mayor a la fecha final."}, 404
        
        if fecha_desde < datetime.today() or fecha_hasta < datetime.today():
            return {"status": 404, "message": "Las fechas elegidas no pueden ser menores a la fecha actual."}, 404
        
        
        id_habitacion = request.json["id_habitacion"]

        habitacion = habitaciones_service.obtener_habitacion(id_habitacion)

        if habitacion is None:
            return {"status": 404, "message": "Registro no encontrado."}, 404

        if habitacion.activa == False:
            return {"status": 200, "message": f"La habitación N°: {habitacion.id} se encuentra deshabilitada para ser reservada. Intente con otra."}, 200

        reservas = service.obtener_habitaciones_reservadas(id_habitacion)
        

        reservasFiltred = [x for x in reservas if x.fecha_desde <= fecha_desde <= x.fecha_hasta or x.fecha_desde <= fecha_hasta <= x.fecha_hasta]

        if len(reservasFiltred) > 0:
            return {"status": 200, "message": f"La habitación N°: {habitacion.id} se encuentra reservada para la fecha solicitada. Intente con una fecha distinta."}, 200

        reserva = Reserva(habitacion.id, fecha_desde, fecha_hasta)

        result = service.agregar_reserva(reserva)

        if result:
            habitacion.reservada = True
            habitaciones_service.modificar_habitacion(habitacion)

        return {"status": 200, "message": f"Se reservó la habitación N°: {habitacion.id} correctamente."}, 200

        
    def obtener_reservas_by_fecha(fecha_inicio, fecha_fin):
        fecha_desde = datetime.strptime(fecha_inicio, app.config['DATE_FORMAT'])
        fecha_hasta = datetime.strptime(fecha_fin, app.config['DATE_FORMAT'])

        if fecha_desde > fecha_hasta:
            return {"status": 404, "message": "La fecha de inicio no puede ser mayor a la fecha final."}, 404

        reservas = service.obtener_reservas_by_fecha(fecha_desde, fecha_hasta)
        habitaciones = habitaciones_service.obtener_habitaciones()
        
        sHabitaciones = HabitacionSchema(many = True)

        if len(reservas) == 0:
            return {"status": 200, "result": sHabitaciones.dump(habitaciones)}

        id_habitaciones = []
        for reserva in reservas:
            if not reserva.id_habitacion in id_habitaciones:
                id_habitaciones.append(reserva.id_habitacion)

        habitaciones_libres = []

        for id in id_habitaciones:
            habitaciones_libres = list(filter(lambda m: m.id != id, habitaciones))
        

        return {"status": 200, "result": sHabitaciones.dump(habitaciones_libres)}

    def obtener_reservas_by_habitacion(id_habitacion):
        reservas = service.obtener_habitaciones_reservadas(id_habitacion)

        if len(reservas) == 0:
            return {"status": 404, "message": "No se encontraron reservas para esta habitación."}, 404

        sReservas = ReservaSchema(many = True)

        return {"status": 200, "result": sReservas.dump(reservas)}
    
    def obtener_estado_habitaciones(fecha_str):
        fecha = datetime.strptime(fecha_str, app.config['DATE_FORMAT'])
        reservas = service.obtener_reservas(fecha)

        if len(reservas) == 0:
            return {"status": 404, "message": "No existen reservas."}, 404

        id_habitaciones = []
        for reserva in reservas:
            if not reserva.id_habitacion in id_habitaciones:
                id_habitaciones.append(reserva.id_habitacion)

        habitaciones = habitaciones_service.obtener_habitaciones()

        habitaciones_estado = []

        for habitacion in habitaciones:
            if habitacion.id in id_habitaciones:
                habitaciones_estado.append(
                    {
                        "nro_habitacion": habitacion.id,
                        "estado": "Ocupada",
                        "precio": habitacion.precio
                    }
                )
            else:
                habitaciones_estado.append(
                    {
                        "nro_habitacion": habitacion.id,
                        "estado": "Disponible",
                        "precio": habitacion.precio
                    }
                )

        return {"status": 200, "result": habitaciones_estado}
