import jwt
from mkapp import app
from flask import request
from services.usuarios_service import Usuarios_Service as usu_service
from models.usuario import UsuarioSchema as schema

class AuthModule():

    base_url = "/auth"

    def crear_token(self, payload):
        return jwt.encode(payload, app.config['JWT_SECRET'], algorithm="HS256")
    
    def login(self):
        usuario = request.json["usuario"]
        clave = request.json["clave"]

        result = usu_service.obtener_usuario_login(usuario, clave)

        usu = schema().dump(result)

        if usu != {}:
            auth = AuthModule()
            token = auth.crear_token(usu)
            return {"status": 200, "message": "Se ha conectado correctamente.", "token": token}
        else:
            return {"status": 404, "message": "Credenciales inválidas."}