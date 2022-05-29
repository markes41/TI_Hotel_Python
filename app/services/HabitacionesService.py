from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models.Habitacion import Habitacion, HabitacionSchema
from mkapp import db

class HabitacionesServices:

    def agregar_habitacion():
        precio = request.json["precio"]
        reservada = request.json["reservada"]
        fecha_reserva = request.json["fecha_Reserva"]
        estado = request.json["estado"]

        habitacion = Habitacion(precio, reservada, fecha_reserva, estado)

        db.session.add(habitacion)
        db.session.commit()
        return {"status": 200, "message": "Se agregó correctamente la habitación nueva."}

    def modificar_habitacion(id):
        precio = request.json["precio"]
        reservada = request.json["reservada"]
        fecha_reserva = request.json["fecha_Reserva"]
        estado = request.json["estado"]

        habitacion = Habitacion.query.get(id)
        habitacion.precio = precio
        habitacion.reservada = reservada
        habitacion.fecha_reserva = fecha_reserva
        habitacion.estado = estado    

        db.session.commit()
        return {"status": 200, "message": "Se modificó correctamente la habitación con id: "+str(id)}

    def eliminar_habitacion(id):
        habitacion = Habitacion.query.get(id)

        db.session.delete(habitacion)
        db.session.commit()
        return {"status": 200, "message": "Se eliminó correctamente el usuario con id: "+str(id)}

    def obtener_habitacion(id):
        habitacionSchema = HabitacionSchema()
        habitacion = Habitacion.query.get(id)
        return {"status": 200, "result": habitacionSchema.dumps(habitacion)} 

    def obtener_habitaciones():
        habitacionSchema = HabitacionSchema(many=True)
        habitaciones = Habitacion.query.all()
        return {"status": 200, "result": habitacionSchema.dumps(habitaciones)}         






