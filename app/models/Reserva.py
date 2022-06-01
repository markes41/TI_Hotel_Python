from sqlalchemy import false
from mkapp import db, ma

class Reserva( db.Model ):
    
    __tablename__ = 'Reservas'

    id = db.Column(db.Integer, primary_key=True)
    id_habitacion = db.Column(db.integer, db.ForeignKey('Habitaciones.Id'))
    habitacion = db.relationship("Habitacion", backref=db.backref("Habitacion", uselist=False))
    fecha_reserva = db.Column(db.DateTime, nullable=True)
    cantidad_dias = db.Column(db.Integer, nullable=false)

    def __init__(self, id_habitacion, habitacion, fecha_reserva, cantidad_dias):
        self.id_habitacion = id_habitacion
        self.habitacion = habitacion
        self.fecha_reserva = fecha_reserva
        self.cantidad_dias = cantidad_dias

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Reserva
        load_instance = True
        include_fk = True
