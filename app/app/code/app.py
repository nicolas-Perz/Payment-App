from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from Transaccion import *

app = Flask(__name__)

# Conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'transacciones' #nombre de la base de datos

# Conecto la base de datos a MySQL
conexion_db = MySQL(app)





# ------------------------------------------------------------------------- #
# Vista inicio
@app.route('/')
def index():
    user_Cuenta = Cuenta('Necesita loguearse',0,'Sin correo electronico','***',0)
    return render_template('index.html', user_cuenta = user_Cuenta)



# ------------------------------------------------------------------------- #
# Vista registro de usuario
@app.route('/registrarse', methods=['POST'])
def registrarse():
    cursor_db = conexion_db.connection.cursor()

    if(request.method == 'POST'):
        # Capturo los datos enviados por el formulario form-registrarse
        user_Nombre = request.form['userNombre']
        user_DNI = request.form['userDNI']
        user_Email = request.form['userEmail']
        user_Password = request.form['userPassword']
        user_Cuenta = Cuenta(user_Nombre,user_DNI,user_Email,user_Password,0)

        # Inserto el nuevo usuario en la base de datos
        sql = "INSERT INTO transacciones.usuarios (nombre,dni,email,contrasena) VALUES (%s,%s,%s,%s)"
        cursor_db.execute(sql, [user_Nombre,user_DNI,user_Email,user_Password])
        
        # Mediante el DNI del usuario, busco en la tabla usuarios su id para generar su registro en la tabla cuentas
        sql = "SELECT idusuarios FROM transacciones.usuarios WHERE dni = %s"
        cursor_db.execute(sql, [user_DNI])

        # user_ID originalmente es una tupla pero solo interesa el primer dato [0]
        user_ID = cursor_db.fetchone()
        user_ID = user_ID[0]

        sql = "INSERT INTO transacciones.cuentas (monto,idusuarios) VALUES (%s,%s)"
        cursor_db.execute(sql, [0,user_ID])

        conexion_db.connection.commit()
    return render_template('index.html', user_cuenta = user_Cuenta)

@app.route('/depositar',methods=['POST'])
def transferir():

<<<<<<< HEAD



# ------------------------------------------------------------------------- #
# Vista login de usuario
@app.route('/login', methods=['POST'])
def login():
    cursor_db = conexion_db.connection.cursor()
    
    if(request.method == 'POST'):
        # Capturo los datos (dni y contraseña) enviados desde el form-login
        login_DNI = request.form['loginDNI']
        login_Password = request.form['loginPassword']

        sql = "SELECT * FROM transacciones.usuarios WHERE dni = %s"
        cursor_db.execute(sql, [login_DNI])
        user_Datos = cursor_db.fetchone()

        if(user_Datos):
            # Guardo todos los datos por separado para trabajar con ellos
            user_ID,user_Nombre,user_DNI,user_Email,user_Password = user_Datos

            sql = "SELECT monto FROM transacciones.cuentas WHERE idusuarios = %s"
            cursor_db.execute(sql, [user_ID])

            # user_Monto originalmente es una tupla pero solo interesa el primer dato [0]
            user_Monto = cursor_db.fetchone()
            user_Monto = user_Monto[0]

            if(login_Password == user_Password):
                user_Cuenta = Cuenta(user_Nombre,user_DNI,user_Email,user_Password,user_Monto)
            else:
                user_Cuenta = Cuenta("Error de login", 0, "Sin correo electrónico", '***', 0)
        else:
            Cuenta("Error de login", 0, "Sin correo electrónico", '***', 0)
    return render_template('index.html', user_cuenta = user_Cuenta)
=======
    cursor_db = conexion_db.connection.cursor()
    if request.method == 'POST':
        data = {
            #'userSearch': request.form['userSearch'],
            'userMonto': request.form['userMonto'],
        }
    sql = f"INSERT INTO cuentas (monto) VALUES ('{data['userMonto']}')"
    cursor_db.execute(sql)
    conexion_db.connection.commit()
    cuentas = cursor_db.fetchall()
    print(cuentas)
    print('holis')
    return render_template('index.html',data=data)
>>>>>>> 3a904b26f4a0b21507fab83171649360c5f25419

if __name__ == '__main__':
    app.run(debug=True, port=5000)