from flask import Flask, render_template, request, jsonify
#importar la libreria para conectar con MySQL
from flask_mysqldb import MySQL


app = Flask(__name__)

#Funciones before y after request, sirven para ejecutar funcionas tanto antes de la peticion como despues
@app.before_request
def before_request():
    print("Antes de la peticion")
    
@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response

#todo lo necesario para conectar con la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #si no tendre acceso denegado
app.config['MYSQL_DB'] = 'prototipodb'

conexion = MySQL(app)

@app.route('/')
def index():
    #lo que vamos a poner en esta funcion, son variables con el contenido que podremos mostrar como plantilla gracias a Jinja2, empezsamos creando un arreglo a modo de lista
    cursos = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
    #creamos un diccionario con el contenido que queremos mostrar en la plantilla
    data = {
        'titulo': 'Mis Cursos',
        'bienvenida': 'Bienvenido a mi sitio web de cursos',
        'cursos': cursos,
        'numero_cursos': len(cursos) #obtenemos el numero de cursos con "len()" que devuelve la longitud de este arreglo 
    }
    return render_template('index.html', data = data)


#URL DINAMICAS
@app.route('/contacto/<nombre>/<int:edad>') #se define la ruta con los parametros que se van a recibir
def contacto(nombre,edad): #se definen los parametros que se van a recibir
    #creamos un diccionario con el contenido que queremos mostrar en la plantilla, en este caso nombre y edad
    datos = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    #y le devolvemos a la plantilla lo que queremos mostrar
    return render_template('contacto.html', nombre=nombre, datos = datos)

#QUERY STRINGS, hace referencia a los parametros que se envian en la URL despues del signo de interrogacion "?"
#en vez de pasarle por arroba, hago que se ejecute en el if __name__ == '__main__' (el bloque que se ejecuta si el archivo se ejecuta directamente)
def query_string():
    print(request)  
    print(request.args) #args es un diccionario con los parametros que se envian en la URL
    print(request.args.get('param1')) #get obtiene el valor del parametro 'param1'
    print(request.args.get('param2')) #get obtiene el valor del parametro 'param2'
    return "Ok"

#CONEXION A LA BASE DE DATOS
@app.route('/transacciones')
def listar_transacciones():
    #creamos un diccionario vacio que agarre lo que estamos obteniendo de la base de datos
    data = {}
    try: #try y except para manejar errores, con un cursor hacemos la consulta SELECT a la base de datos
        #creamos un cursor que es lo que nos permite ejecutar consultas SQL
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM `transacciones`"
        #a partir de la conexion, obtenemos el cursor y ejecutamos la consulta SQL
        cursor.execute(sql)
        transaccion = cursor.fetchall()
        #print(transaccion)
        data['transacciones'] = transaccion
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje'] = f"Error: {str(ex)}"

    #devolvemos la informacion en formato JSON para que ambas partes sepan leerla
    return jsonify(data)




#lo que hace este bloque es que si el archivo se ejecuta directamente, se ejecuta la aplicacion de Flask
if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True, port=5000)