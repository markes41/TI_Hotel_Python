from models.Usuario import Usuario, UsuarioSchema
from mkapp import db

class UsuariosService:
    def agregar_usuario():
        usuario = request.json["usuario"]
        clave = request.json["clave"]
        nombre = request.json["nombre"]

        usuario = Usuario()

        db.session.add(habitacion)
        db.session.commit()
        return {"status": 200, "message": "Se agregó correctamente la habitación nueva."}