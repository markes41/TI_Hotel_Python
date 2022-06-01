from functools import wraps
import jwt
from flask import request
from mkapp import app

def roles_middleware(rol):
    def rol_decorated(func):
        @wraps(func)
        def rol_inner(*args, **kwargs):
            try:
                if "Authorization" in request.headers:
                    token = request.headers["Authorization"].split(" ")[1]
                if not token:
                    return { "message": "No se ha encontrado el token de autorización."}, 404

                data = jwt.decode(token, app.config["JWT_SECRET"], algorithms=["HS256"])

                if data["rol"] != rol:
                    return { "message": "Módulo sólo habilitado para " + str(rol) + "s."}, 401

                return func(*args, **kwargs)
            except Exception as e:
                return {"status": 500, "message": "Ocurrió un error en la aplicación.", "error": str(e)}
        return rol_inner
    return rol_decorated
