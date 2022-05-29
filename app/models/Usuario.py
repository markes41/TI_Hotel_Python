from mkapp import db
from marshmallow import Schema, fields

class Usuario( db.Model ):
    
    __tablename__ = 'Usuarios'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    clave = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, clave, usuario):
        self.nombre = nombre
        self.clave = clave
        self.usuario = usuario


class UsuarioSchema(Schema):
    usuario = fields.Str()
    nombre = fields.Int()