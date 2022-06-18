from models.habitacion import Habitacion
from mkapp import db

class Habitaciones_Service:

    def agregar_habitacion(habitacion):
        db.session.add(habitacion)
        db.session.commit()

        return {"status": 200, "message": "Se agregó correctamente la nueva habitación."}

    def modificar_habitacion(habitacion):
        db.session.commit()
        return {"status": 200, "message": "Habitación modificada correctamente."}

    def eliminar_habitacion(habitacion):
        db.session.delete(habitacion)
        db.session.commit()
        return {"status": 200, "message": "Habitación eliminada correctamente."}

    def obtener_habitacion(id):
        return Habitacion.query.get(id)
    
    def obtener_habitaciones_precio(precio_elegido):
        return Habitacion.query.filter(
            Habitacion.precio < precio_elegido
        ).all()

    def obtener_habitaciones():
        return Habitacion.query.filter(
            Habitacion.activa == True
        ).all()
