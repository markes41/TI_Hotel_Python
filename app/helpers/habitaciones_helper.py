from models.habitacion import Habitacion

class Habitaciones_Helper:
    def request_habitacion(request):
        precio = request.json["precio"]
        activa = request.json["activa"]
        reservada = request.json["reservada"]
        fecha_reserva = request.json["fecha_reserva"]

        habitacion = Habitacion(precio, activa, reservada, fecha_reserva)

        return habitacion