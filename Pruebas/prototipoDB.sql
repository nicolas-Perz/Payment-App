DROP database if exists prototipoDB;

CREATE DATABASE prototipoDB;
USE prototipoDB;


CREATE TABLE IF NOT EXISTS transacciones (
    id INT AUTO_INCREMENT,
    descripcion varchar(50),
    monto float,
    PRIMARY KEY (id)
);