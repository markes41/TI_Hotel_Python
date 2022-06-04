from models.reserva import Reserva
from mkapp import db
class Reservas_Service:
    def obtener_habitaciones_reservadas():
        return Reserva.query.all()

    def obtener_reserva_by_id(id):
        return Reserva.query.get(id)
    
    def agregar_reserva(reserva):
        db.session.add(reserva)
        db.session.commit()
        return True

    def obtener_reservas_by_fecha(fecha):
        return Reserva.query.filter_by(fecha_reserva == fecha).all()