from mkapp import db, ma
class Habitacion( db.Model ):

    __tablename__ = 'Habitaciones'

    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Float, nullable=False)
    activa = db.Column(db.Boolean, nullable=False)
    reservada = db.Column(db.Boolean, nullable=False)

    def __init__(self, precio, activa, reservada, fecha_reserva):
        self.precio = precio
        self.activa = activa
        self.reservada = reservada

class HabitacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Habitacion
        load_instance = True