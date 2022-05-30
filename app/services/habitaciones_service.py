from mkapp import db
from models.habitacion import Habitacion, HabitacionSchema

class Habitaciones_Service:

    def agregar_habitacion(habitacion):
        db.session.add(habitacion)
        db.session.commit()

        return {"status": 200, "message": "Se agregó correctamente la habitación nueva."}

    def modificar_habitacion(habitacion):
        db.session.commit()
        return {"status": 200, "message": "Se modificó correctamente la habitación con id: "+str(habitacion.id)}

    def eliminar_habitacion(habitacion):
        db.session.delete(habitacion)
        db.session.commit()
        return {"status": 200, "message": "Se eliminó correctamente el usuario con id: "+str(habitacion.id)}

    def obtener_habitacion(id):
        habitacionSchema = HabitacionSchema()
        habitacion = Habitacion.query.get(id)
        return {"status": 200, "result": habitacionSchema.dumps(habitacion)} 

    def obtener_habitaciones():
        habitacionSchema = HabitacionSchema(many=True)
        habitaciones = Habitacion.query.all()
        return {"status": 200, "result": habitacionSchema.dumps(habitaciones)}         






