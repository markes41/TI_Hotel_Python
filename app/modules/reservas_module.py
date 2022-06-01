from flask import request
from services.reservas_service import Reservas_Service as service
from models.reserva import ReservaSchema as schema

class Reservas_Module:

    base_url = "/reservas"