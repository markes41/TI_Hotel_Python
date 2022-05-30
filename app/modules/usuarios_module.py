from flask import request
from services.usuarios_service import Usuarios_Service as service
from helpers.usuarios_helper import Usuarios_Helper as helper

class Usuarios_Module:

    base_url = "/Usuarios"

    def agregar_usuario():
        usu = helper.request_usuario(request)

        return service.agregar_usuario(usu)
    
    def modificar_usuario(id):
        usu_nuevo = helper.request_usuario(request)

        usu_original = service.obtener_usuario(id)

        usu_original.nombre = usu_nuevo.nombre
        usu_original.clave = usu_nuevo.clave
        usu_original.usuario = usu_nuevo.usuario
        usu_original.rol = usu_nuevo.rol

        return service.modificar_usuario(usu_original)

    def eliminar_usuario(id):
        usu = service.obtener_usuario(id)

        return service.eliminar_usuario(usu)

    def obtener_usuario(id):
        return service.obtener_usuario(id)
