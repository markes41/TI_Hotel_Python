from mkapp import db, ma
class Usuario( db.Model ):
    
    __tablename__ = 'Usuarios'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, clave, usuario, rol):
        self.nombre = nombre
        self.clave = clave
        self.usuario = usuario
        self.rol = rol

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Usuario
        load_instance = True
        load_only = ("clave",)