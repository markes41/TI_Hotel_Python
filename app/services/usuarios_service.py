from models.usuario import Usuario, UsuarioSchema as schema
from mkapp import db

class Usuarios_Service:

    def obtener_usuario_login(usuario, clave):
        return Usuario.query.filter_by(
            usuario = usuario,
            clave = clave
        ).first()

    def agregar_usuario(usuario):
        db.session.add(usuario)
        db.session.commit()

        return {"status": 200, "message": "Se agregó correctamente el usuario."}

    def modificar_usuario(usuario):
        db.session.commit()
        return {"status": 200, "message": "Usuario modificado correctamente."}

    def eliminar_usuario(usuario):
        db.session.delete(usuario)
        db.session.commit()
        return {"status": 200, "message": "Usuario eliminado correctamente."}

    def obtener_usuario(id):
        return Usuario.query.get(id)