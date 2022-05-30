from flask import request
from services.roles_service import Roles_Service as service
from models.rol import Rol

class Roles_Module:

    base_url = '/roles'

    def agregar_rol():
        nombre = request.json["nombre"]
        rol = Rol(nombre)

        return service.agregar_rol(rol)

    def modificar_rol(id):
        rol = service.obtener_rol(id)
        nombre = request.json["nombre"]
        rol.nombre = nombre

        return service.modificar_rol(rol)
    
    def eliminar_rol(id):
        rol = service.obtener_rol(id)

        return service.eliminar_rol(rol)



