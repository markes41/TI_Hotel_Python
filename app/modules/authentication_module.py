import jwt
import json
from mkapp import app
from flask import request
from services.usuarios_service import Usuarios_Service as usu_service

class AuthenticationModule:

    base_url = "/authentication"

    def __init__(self):
        self.crear_token()
        self.authenticated()
        self.login()

    def crear_token(self, payload):
        return jwt.encode(payload, app.config['JWT_SECRET'], algorithm="HS256")
    
    def login(self):
        try:
            usuario = request.json["usuario"]
            clave = request.json["clave"]

            result = usu_service.buscar_usuario_login(usuario, clave)

            if result.count() > 0:
                payload = json.dumps(result.__dict__)
                token = self.crear_token(payload)
                return {"status": 200, "message": "Se ha conectado correctamente.", "result": token}
            else:
                return {"status": 401, "message": "Credenciales inválidas"}
        except:
            return {"status": 401, "message": "Ocurrió un problema al realizar el login."}
