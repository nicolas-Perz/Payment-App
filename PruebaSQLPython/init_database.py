import sqlite3

# Conectarse (o crear) la base de datos
conexion = sqlite3.connect("transacciones.db")

# Leer el archivo database.sql
with open("database.sql", "r", encoding="utf-8") as f:
    db = f.read()

# Ejecutar el script SQL
conexion.executescript(db)

# Guardar y cerrar
conexion.commit()
conexion.close()

print("✅ Base de datos inicializada con database.sql")