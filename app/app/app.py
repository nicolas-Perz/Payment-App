from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)