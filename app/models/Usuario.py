from mkapp import db
from marshmallow import Schema, fields

class Usuario( db.Model ):
    
    __tablename__ = 'Usuarios'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(50), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('Roles.id'))

    def __init__(self, nombre, clave, usuario, rol):
        self.nombre = nombre
        self.clave = clave
        self.usuario = usuario
        self.rol = rol

class UsuarioSchema(Schema):
    usuario = fields.Str()
    nombre = fields.Int()
    rol = fields.Str()