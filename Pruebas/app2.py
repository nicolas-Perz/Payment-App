from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/contacto/<nombre>')
def contacto(nombre):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
    }
    return render_template('contacto.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True, port=5000)