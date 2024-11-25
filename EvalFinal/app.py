from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el menú principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el Ejercicio 1 (Cálculo de compras)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        if 18 <= edad < 30:
            descuento = 0.15
        elif edad >= 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'monto_descuento': monto_descuento,
            'total_a_pagar': total_a_pagar
        }

    return render_template('ejercicio1.html', resultado=resultado)

# Ruta para el Ejercicio 2 (Inicio de sesión)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        if nombre == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido Administrador Juan'
        elif nombre == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido Usuario Pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
