from mkapp import db, ma
from models.habitacion import HabitacionSchema

class Reserva( db.Model ):
    
    __tablename__ = 'Reservas'

    id = db.Column(db.Integer, primary_key=True)
    id_habitacion = db.Column(db.Integer, db.ForeignKey('Habitaciones.id'))
    habitacion = db.relationship("Habitacion", backref="Reserva")
    fecha_reserva = db.Column(db.DateTime, nullable=True)
    cantidad_dias = db.Column(db.Integer, nullable=False)

    def __init__(self, id_habitacion, fecha_reserva, cantidad_dias):
        self.id_habitacion = id_habitacion
        self.fecha_reserva = fecha_reserva
        self.cantidad_dias = cantidad_dias

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Reserva
        load_instance = True
        include_fk = True
    
    habitacion = ma.Nested(HabitacionSchema)