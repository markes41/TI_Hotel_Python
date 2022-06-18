------------------------ TABLA USUARIOS ------------------------
CREATE TABLE Usuarios(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Usuario VARCHAR(100) UNIQUE NOT NULL,
    Nombre VARCHAR(100) UNIQUE NOT NULL,
    Clave VARCHAR(100) NOT NULL,
    Rol VARCHAR(50) NOT NULL,
);

INSERT INTO Usuarios(Usuario, Nombre, Clave, Rol)
VALUES ('msequeira', 'Marcos', '123', 'Administrador');

INSERT INTO Usuarios(Usuario, Nombre, Clave, Rol)
VALUES ('gniglio', 'Gabriel','123', 'Empleado');

INSERT INTO Usuarios(Usuario,Nombre,  Clave, Rol)
VALUES ('lescobar', 'Luciano', '123', 'Cliente');

----------------------------------------------------------------

--------------------- TABLA HABITACIONES -----------------------
CREATE TABLE Habitaciones(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Precio DOUBLE PRECISION,
    Reservada BOOLEAN NOT NULL,
    Activa BOOLEAN NOT NULL
);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Activa)
VALUES (950.50, true, '2022-05-26', false);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Activa)
VALUES (500, true, '2022-05-20', false);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Activa)
VALUES (1500, true, '2022-05-23', false);

----------------------------------------------------------------

----------------------- TABLA RESERVAS -------------------------

CREATE TABLE Reservas(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Id_Habitacion INTEGER,
    Fecha_Desde DATE NOT NULL,
    Fecha_Hasta DATE NOT NULL,
    CONSTRAINT FK_Habitacion
        FOREIGN KEY(Habitacion_Id)
                REFERENCES Habitaciones(Id)
);

INSERT INTO Reservas(Habitacion_Id, Fecha_Desde, Fecha_Hasta, Estado)
VALUES (3, '2022-05-20', '2022-05-26');

INSERT INTO Reservas(Habitacion_Id, Fecha_Desde, Fecha_Hasta, Estado)
VALUES (2, '2022-05-26', '2022-06-06');
----------------------------------------------------------------