from services.habitaciones_service import HabitacionesService
from modules.habitaciones_module import HabitacionesModule
from modules.authentication_module import authenticated, AuthenticationModule
from mkapp import app, db

# endpoints Login

@app.route('/auth/login', methods=['POST'])
def login():
	return AuthenticationModule.login()

#################

# endpoints Habitación
@app.route('/habitacion/agregar', methods=['POST'])
@authenticated
def agregar_habitacion():
	return HabitacionesService.agregar_habitacion()

@app.route('/habitacion/modificar/<int:id>', methods=['PUT'])
@authenticated
def modificar_habitacion(id):
	return HabitacionesService.modificar_habitacion(id)

@app.route('/habitacion/eliminar/<int:id>', methods=['DELETE'])
@authenticated
def eliminar_habitacion(id):
	return HabitacionesService.eliminar_habitacion(id)

@app.route('/habitacion/get/<int:id>', methods=['GET'])
@authenticated
def obtener_habitacion(id):
	return HabitacionesService.obtener_habitacion(id)

@app.route('/habitaciones/', methods=['GET'])
@authenticated
def obtener_habitaciones():
	return HabitacionesService.obtener_habitaciones()

# Crear tablas
db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")