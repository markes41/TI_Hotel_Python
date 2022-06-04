from models.reserva import Reserva
from mkapp import db
from sqlalchemy import and_, or_

class Reservas_Service:
    def obtener_habitaciones_reservadas(id):
        return Reserva.query.filter_by(id_habitacion = id).all()

    def obtener_reserva_by_id(id):
        return Reserva.query.get(id)
    
    def agregar_reserva(reserva):
        db.session.add(reserva)
        db.session.commit()
        return True

    def obtener_reservas_by_fecha(fecha):
        return Reserva.query.filter(
            and_(fecha >= Reserva.fecha_desde, fecha <= Reserva.fecha_hasta)
        ).all()

        