import jwt
import json
from mkapp import app
from flask import request
from services.usuarios_service import UsuariosService

class AuthenticationModule:

    def __init__(self):
        self.crear_token()
        self.authenticated()
        self.login()

    def crear_token(self, payload):
        return jwt.encode(payload, app.config['JWT_SECRET'], algorithm="HS256")

    def authenticated(self, route):
        def inner(*args, **kwargs):
            try:
                token = request.headers["Authorization"][7:]
                payload = jwt.decode(token, app.config['JWT_SECRET'], algorithm=["HS256"])
                return route(*args, **kwargs)
            except jwt.DecodeError:
                return {"status": 401, "message": "El token se ha cambiado."}
            except jwt.InvalidSignatureError:
                return {"status": 401, "message": "El token es inválido."}
            except KeyError:
                return {"status": 401, "message": "El token es inexistente."}
        inner.__name__ = route.__name__
        return inner
    
    def login(self):
        try:
            usuario = request.json["usuario"]
            clave = request.json["clave"]

            result = UsuariosService.buscar_usuario_login(usuario, clave)

            if result.count() > 0:
                payload = json.dumps(result.__dict__)
                token = self.crear_token(payload)
                return {"status": 200, "message": "Se ha logeado correctamente.", "result": token}
        except:
            return {"status": 401, "message": "Ocurrió un problema al logear."}
