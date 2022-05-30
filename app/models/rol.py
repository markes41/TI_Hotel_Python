from sqlalchemy import false
from mkapp import db
from marshmallow import Schema, fields

class Rol( db.Model ):
    
    __tablename__ = 'Roles'

    id = db.Column(db.Integer, primary_key=True, nullable=false)
    nombre = db.Column(db.String(40), unique=True, nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre


class RolSchema(Schema):
    nombre = fields.Str()