from mkapp import db
from marshmallow import Schema, fields

class Habitacion( db.Model ):

    __tablename__ = 'Habitaciones'

    id = db.Column(db.Integer, primary_key=True)
    fecha_reserva = db.Column(db.String(20), unique=True, nullable=False)
    precio = db.Column(db.String(50), nullable=False)
    activa = db.Column(db.String(50), nullable=False)
    reservada = db.Column(db.String(50), nullable=False)

    def __init__(self, precio, activa, reservada, fecha_reserva):
        self.fecha_reserva = fecha_reserva
        self.precio = precio
        self.activa = activa
        self.reservada = reservada

class HabitacionSchema(Schema):
    usuario = fields.Str()
    edad = fields.Int()