from flask_swagger_ui import get_swaggerui_blueprint
from mkapp import app, db
from routes import auth_route, habitaciones_route, usuarios_route, reservas_route

### Especificaciones swagger documentación API ###
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python - API Hotel Flask"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
###################################################

####### ROUTES ENDPOINTS #######

# Authorization
app.register_blueprint(auth_route.get_blueprint())

# Habitaciones
app.register_blueprint(habitaciones_route.get_blueprint())

# Usuarios
app.register_blueprint(usuarios_route.get_blueprint())

# Reservas
app.register_blueprint(reservas_route.get_blueprint())

###############################

db.create_all()

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)