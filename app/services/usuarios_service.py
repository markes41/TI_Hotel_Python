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
        return {"status": 200, "message": "Se modificó correctamente la habitación con id: "+str(id)}

    def eliminar_usuario(usuario):
        db.session.delete(usuario)
        db.session.commit()
        return {"status": 200, "message": "Se eliminó correctamente la habitación con id: "+str(id)}

    def obtener_usuario(id):
        usuarioSchema = schema()
        usuario = Usuario.query.get(id)
        return {"status": 200, "result": usuarioSchema.dump(usuario)}

    def obtener_usuarios():
        usuarioSchema = schema(many=True)
        usuarios = Usuario.query.all()
        return {"status": 200, "result": usuarioSchema.dump(usuarios)}