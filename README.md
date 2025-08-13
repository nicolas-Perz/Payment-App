# Payment-App
Mini proyecto principiante de un gestor de transacciones. Aplicación web (que en un futuro podriamos portear a escritorio) que vía sesiones de diferentes usuarios permita ingresar, retirar y analizar movimientos de cantidades de dinero.

Tecnologías:
Python (código general)
Flask (biblioteca de Python para interactuar con una página web y una database)
SQL (motor de la base de datos)
SQLite (libreria ligera incluida en Python para hacer de puente entre este mismo y SQL)

Acciones:
Crear un usuario propio.
Login de usuarios creados.
Logout del usuario actual.
Ingreso de dinero en el usuario actual.
Retiro de dinero en el usuario actual.
Transferencia de dinero en el usuario actual a uno ya existente.
Historial de últimos movimientos monetarios independiente de cada usuario.

Cosas que podriamos incluir a futuro:
Generar facturas que incluyan una información más completa de cada transacción y/o usuario.
Aplicar descuentos basados en tarjetas ficticias.
Visualizar de forma gráfica un análisis de los movimientos de cada usuario independientemente (Ej. % de ganacias/perdidas en general o los últimos 10 movimientos)
