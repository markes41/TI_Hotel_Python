from services.HabitacionesService import HabitacionesService
from mkapp import app, db

# endpoints Habitación
@app.route('/habitacion/agregar', methods=['POST'])
def agregar_habitacion():
	return HabitacionesService.agregar_habitacion()

@app.route('/habitacion/modificar/<int:id>', methods=['PUT'])
def modificar_habitacion(id):
	return HabitacionesService.modificar_habitacion(id)

@app.route('/habitacion/eliminar/<int:id>', methods=['DELETE'])
def eliminar_habitacion(id):
	return HabitacionesService.eliminar_habitacion(id)

@app.route('/habitacion/get/<int:id>', methods=['GET'])
def obtener_habitacion(id):
	return HabitacionesService.obtener_habitacion(id)

@app.route('/habitaciones/', methods=['GET'])
def obtener_habitaciones():
	return HabitacionesService.obtener_habitaciones()

# Crear tablas
db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")