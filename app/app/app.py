from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from Transaccion import *

app = Flask(__name__)

#Conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'transacciones' #nombre de la base de datos

conexion_db = MySQL(app) #Crear vinculo entre la aplicación y MySQL    

@app.route('/')
def index():
    data = {
        'userNombre': 'Sin usuario',
        'userDinero': 0
    }
    return render_template('index.html',data=data)

@app.route('/login',methods=['POST'])
def login():

    cursor_db = conexion_db.connection.cursor()
    if request.method == 'POST':
        data = {
            'userNombre': request.form['userNombre'],
            'userDNI': request.form['userDNI'],
            'userEmail': request.form['userEmail']
        }
    sql = f"INSERT INTO usuarios (nombre,dni,email) VALUES ('{data['userNombre']}','{data['userDNI']}','{data['userEmail']}')"
    cursor_db.execute(sql)
    conexion_db.connection.commit()
    usuarios = cursor_db.fetchall()
    print(usuarios)
    print('holis')
    return render_template('index.html',data=data)






if __name__ == '__main__':
    app.run(debug=True, port=5000)


''' -------------------------------------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():

    usuario_dinero = 1000
    if request.method == 'POST':
        monto_ingresado = request.form.get('userIngresar',type=int)
        if monto_ingresado:
            usuario_dinero += monto_ingresado
        else:
            monto_ingresado = request.form.get('retirar',type=int)
            if monto_ingresado:
                usuario_dinero -= monto_ingresado

    cursos = ['python','java','c++']
    data = {
        'titulo':'Menu principal',
        'saludo':'Bienvenido!',
        'cursos':cursos,
        'cursos_cant':len(cursos),
        'usuario_dinero': usuario_dinero
    }

    return render_template('index.html', data=data)
'''