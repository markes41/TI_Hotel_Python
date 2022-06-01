from flask import request
from services.usuarios_service import Usuarios_Service as service
from models.usuario import UsuarioSchema as schema

class Usuarios_Module:

    base_url = "/usuarios"

    def agregar_usuario():
        uSchema = schema()
        usu = uSchema.load(request.json)

        return service.agregar_usuario(usu)
    
    def modificar_usuario(self, id):
        usu_original = service.obtener_usuario(id)

        if usu_original is None:
            return {"status": 404, "message": "Usuario no encontrado."}

        uSchema = schema()
        usu_nuevo = uSchema.load(request.json)


        usu_original.nombre = usu_nuevo.nombre
        usu_original.clave = usu_nuevo.clave
        usu_original.usuario = usu_nuevo.usuario
        usu_original.rol = usu_nuevo.rol

        return service.modificar_usuario(usu_original)

    def eliminar_usuario(id):
        usu = service.obtener_usuario(id)

        if usu is None:
            return {"status": 404, "message": "Registro no encontrado."}
        
        return service.eliminar_usuario(usu)
        

    def obtener_usuario(id):
        usu = service.obtener_usuario(id)
        uSchema = schema()
        
        if usu is None:
            return {"status": 404, "message": "Registro no encontrado."}
        
        return {"status": 200, "result": uSchema.dump(usu)}
