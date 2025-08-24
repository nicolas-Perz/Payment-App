DROP database if exists transacciones;

CREATE DATABASE transacciones;
USE transacciones;

CREATE TABLE usuarios (
  idusuarios INT AUTO_INCREMENT,
  nombre varchar(45),
  dni INT,
  email varchar(45),
  PRIMARY KEY (idusuarios),
  UNIQUE KEY dni_UNIQUE (dni)
);

CREATE TABLE cuentas (
  idcuentas INT AUTO_INCREMENT,
  monto float,
  idusuarios INT,
  PRIMARY KEY (idcuentas),
  FOREIGN KEY (idusuarios) REFERENCES usuarios(idusuarios)
);

CREATE TABLE transacciones (
  idtransacciones INT AUTO_INCREMENT,
  idcuenta INT,
  monto float DEFAULT NULL,
  PRIMARY KEY (idtransacciones),
  KEY idcuenta_idx (idcuenta),
  FOREIGN KEY (idcuenta) REFERENCES cuentas(idcuentas)
);

/* INSERT!
INSERT INTO usuarios VALUES (1,'Nicolas',46703415,'nicolasperez4209@gmail.com'),
       (2,'Juan',46000000,'juan12345@gmail.com'),
       (3,'berserk',123456,'mesacastelasangre@gmail.com');

INSERT INTO cuentas (idcuentas,monto,idusuarios) 
VALUES (1,1000,1),(2,2000,2),(3,3000,3)
ON DUPLICATE KEY UPDATE 
    monto=VALUES(monto), idusuarios=VALUES(idusuarios);
