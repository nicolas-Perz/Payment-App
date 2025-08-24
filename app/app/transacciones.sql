-- Table structure for table `usuarios`
CREATE TABLE IF NOT EXISTS `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `dni` int NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`idusuarios`),
  UNIQUE KEY `dni_UNIQUE` (`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Esta tabla representa los usuarios existentes dentro del sistema';

-- Dumping data for table `usuarios`
INSERT INTO `usuarios` (`idusuarios`,`nombre`,`dni`,`email`) 
VALUES (1,'Nicolas',46703415,'nicolasperez4209@gmail.com'),
       (2,'Juan',46000000,'juan12345@gmail.com'),
       (3,'berserk',123456,'mesacastelasangre@gmail.com')
ON DUPLICATE KEY UPDATE 
    nombre=VALUES(nombre), dni=VALUES(dni), email=VALUES(email);


-- Table structure for table `cuentas`
CREATE TABLE IF NOT EXISTS `cuentas` (
  `idcuentas` int NOT NULL AUTO_INCREMENT,
  `monto` float NOT NULL,
  `idusuarios` int NOT NULL,
  PRIMARY KEY (`idcuentas`),
  KEY `idusuarios_idx` (`idusuarios`),
  CONSTRAINT `idusuarios` FOREIGN KEY (`idusuarios`) REFERENCES `usuarios` (`idusuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Esta tabla representa las cuentas (con sus registros/dinero) de los usuarios existentes.';

-- Dumping data for table `cuentas`
INSERT INTO `cuentas` (`idcuentas`,`monto`,`idusuarios`) 
VALUES (1,1000,1),(2,2000,2),(3,3000,3)
ON DUPLICATE KEY UPDATE 
    monto=VALUES(monto), idusuarios=VALUES(idusuarios);


-- Table structure for table `transacciones`
CREATE TABLE IF NOT EXISTS `transacciones` (
  `idtransacciones` int NOT NULL AUTO_INCREMENT,
  `idcuenta` int NOT NULL,
  `monto` float DEFAULT NULL,
  PRIMARY KEY (`idtransacciones`),
  KEY `idcuenta_idx` (`idcuenta`),
  CONSTRAINT `idcuenta` FOREIGN KEY (`idcuenta`) REFERENCES `cuentas` (`idcuentas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Esta tabla representa las transacciones/movimientos de las cuentas de cada usuario.';
