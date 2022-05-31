from functools import wraps
import jwt
from flask import request
from mkapp import app
from services.usuarios_service import Usuarios_Service as service

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return { "message": "No se ha encontrado el token de autorización."}, 404
        try:
            data = jwt.decode(token, app.config["JWT_SECRET"], algorithms=["HS256"])

            usu = service.obtener_usuario(data["id"])["result"]

            if usu is None:
                return { "message": "Token inválido.", "error": "No autorizado"}, 401
        except Exception as e:
            return {"message": "Ha ocurrido un error al válidar el token", "error": str(e)}, 500

        return f(*args, **kwargs)

    return decorated