------------------------ TABLA USUARIOS ------------------------
CREATE TABLE Usuarios(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Usuario VARCHAR(100) UNIQUE NOT NULL,
    Clave VARCHAR(100) NOT NULL,
    Rol INTEGER NOT NULL,
)

INSERT INTO Usuarios(Usuario, Clave, Rol)
VALUES ('Marcos', '123', 1)

INSERT INTO Usuarios(Usuario, Clave, Rol)
VALUES ('Gabriel', '123', 2)

INSERT INTO Usuarios(Usuario, Clave, Rol)
VALUES ('Luciano', '123', 2)

----------------------------------------------------------------

------------------------ TABLA ROLES ---------------------------
CREATE TABLE Roles(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Nombre VARCHAR UNIQUE NOT NULL
)

INSERT INTO Roles(Nombre)
VALUES ('Empleado desde init')

INSERT INTO Roles(Nombre)
VALUES ('Cliente')

----------------------------------------------------------------

--------------------- TABLA HABITACIONES -----------------------
CREATE TABLE Habitaciones(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Precio DOUBLE PRECISION,
    Reservada BOOLEAN NOT NULL,
    Fecha_Reserva DATE NOT NULL,
    Estado BOOLEAN NOT NULL
);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Estado)
VALUES (950.50, true, '2022-05-26', false);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Estado)
VALUES (500, true, '2022-05-20', false);

INSERT INTO Habitaciones(Precio, Reservada, Fecha_Reserva, Estado)
VALUES (1500, true, '2022-05-23', false);

----------------------------------------------------------------

----------------------- TABLA RESERVAS -------------------------

CREATE TABLE Reservas(
    Id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    Habitacion_Id INTEGER,
    Fecha_Desde DATE NOT NULL,
    Fecha_Hasta DATE NOT NULL,
    Estado BOOLEAN NOT NULL,
    CONSTRAINT FK_Habitacion
        FOREIGN KEY(Habitacion_Id)
                REFERENCES Habitaciones(Id)
);

INSERT INTO Reservas(Habitacion_Id, Fecha_Desde, Fecha_Hasta, Estado)
VALUES (3, '2022-05-20', '2022-05-26', true);

INSERT INTO Reservas(Habitacion_Id, Fecha_Desde, Fecha_Hasta, Estado)
VALUES (2, '2022-05-26', '2022-06-06', true);
----------------------------------------------------------------