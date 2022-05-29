from models.usuario import Usuario, UsuarioSchema
from mkapp import db

class UsuariosService:
    def buscar_usuario_login(usuario, clave):
        result = Usuario.query.filter_by(
            usuario = usuario,
            clave = clave
        )

        return result
