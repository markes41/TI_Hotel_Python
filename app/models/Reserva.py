from mkapp import db, ma
from models.habitacion import HabitacionSchema

class Reserva( db.Model ):
    
    __tablename__ = 'Reservas'

    id = db.Column(db.Integer, primary_key=True)
    id_habitacion = db.Column(db.Integer, db.ForeignKey('Habitaciones.id'))
    habitacion = db.relationship("Habitacion", backref="Reserva")
    fecha_desde = db.Column(db.DateTime, nullable=True)
    fecha_hasta = db.Column(db.DateTime, nullable=True)

    def __init__(self, id_habitacion, fecha_desde, fecha_hasta):
        self.id_habitacion = id_habitacion
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Reserva
        load_instance = True
        include_fk = True
    
    habitacion = ma.Nested(HabitacionSchema)