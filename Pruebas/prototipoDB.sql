DROP database if exists prototipoDB;

CREATE DATABASE prototipoDB;
USE prototipoDB;


CREATE TABLE IF NOT EXISTS transacciones (
    id INT AUTO_INCREMENT,
    descripcion varchar(50),
    monto float,
    PRIMARY KEY (id)
);

INSERT INTO usuarios VALUES (1,'Nicolas',46703415,'nicolasperez4209@gmail.com'),
       (2,'Juan',46000000,'juan12345@gmail.com'),
       (3,'berserk',123456,'mesacastelasangre@gmail.com');