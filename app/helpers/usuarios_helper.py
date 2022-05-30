from models.usuario import Usuario

class Usuarios_Helper:

    def request_usuario(request):
        nombre = request.json["nombre"]
        clave = request.json["clave"]
        usuario = request.json["usuario"]
        rol = request.json["rol"]

        usu = Usuario(nombre, clave, usuario, rol)

        return usu