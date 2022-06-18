
# Api Hotel - Taller Integrador

Para la correcta utilización de la aplicación se deberá instalar los paquetes correspondientes que utiliza el proyecto. Los mismos están detallados en el archivo requeriments.txt. 

## 1. Configuración con Docker

El proyecto está configurado para ser corrido con docker, el mismo creará un entorno virtual con todas las dependencias instaladas y la base de datos levantada. Se deberá correr el comando para crear los contendores e imágenes correspondientes.

```bash
  docker compose up
```

## 2. Documentación y prueba de endpoints.

Para testear los endpoints se utilizó Swagger OpenAPI 3.0, al mismo se puede ingresar, una vez levantado el proyecto en docker, mediante la siguiente url.

```bash
  http://localhost:8080/api/docs/
```

## 3. Autorización mediante JWT.

Ingresando a la dirección de la documentación del proyecto, se podrá realizar el login para que el sistema nos brinde un token de autorización con el cual se podrá consumir ciertos endpoints, según el rol que hayamos elegido.

## 4. Roles existentes.

- Administrador (puede ingresar a cualquier endpoint).
- Empleado (puede ingresar a ciertos métodos de habitaciones y usuarios).
- Cliente (puede ingresar a ciertos métodos de reservas)
