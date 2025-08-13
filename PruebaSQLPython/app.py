from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def obtener_conexion():
    return sqlite3.connect("transacciones.db")

@app.route("/")
def index():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, descripcion, monto FROM transacciones")
    transacciones = cursor.fetchall()
    conexion.close()

    html = "<h1>Lista de transacciones</h1><ul>"
    for t in transacciones:
        html += f"<li>{t[1]} — ${t[2]}</li>"
    html += "</ul>"

    html += """
    <h2>Nueva transacción</h2>
    <form method='POST' action='/agregar'>
        Descripción: <input type='text' name='descripcion'><br>
        Monto: <input type='number' step='0.01' name='monto'><br>
        <input type='submit' value='Agregar'>
    </form>
    """
    return html

@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form["descripcion"]
    monto = float(request.form["monto"])

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO transacciones (descripcion, monto) VALUES (?, ?)",
        (descripcion, monto)
    )
    conexion.commit()
    conexion.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
