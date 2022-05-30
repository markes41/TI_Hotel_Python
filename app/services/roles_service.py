from models.rol import Rol, RolSchema
from mkapp import db

class Roles_Service:

    def agregar_rol(rol):
        db.session.add(rol)
        db.commit()
        return {"status": 200, "message": "Se agregó el rol "+ str(rol.rol)+" exitosamente."}

    def modificar_rol(rol):
        db.commit(rol)
        return {"status": 200, "message": "Se modificó correctamente el rol " + str(rol.rol)}

    def eliminar_rol(rol):
        db.session.delete(rol)
        db.session.commit()
        return {"status": 200, "message": "Se eliminó correctamente el rol " + str(rol.rol)}
    
    def obtener_rol(id):
        rolSchema = RolSchema()
        rol = Rol.query.get(id)
        return {"status": 200, "result": rolSchema.dumps(rol)} 