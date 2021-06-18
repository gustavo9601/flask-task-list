from flask import request, redirect, render_template, session, url_for, flash
from app import create_app
from app.forms import LoginForm

# import librerias para pruebas
import unittest

"""
execute in console

export FLASK_APP=current_name_file_init.py => export || set
export FLASK_DEBUG=1 => export || set
export FLASK_ENV=development => export || set
flask run

echo FLASK_ENV=development // se puede imprimir el valor de la variable por consola
"""

app = create_app()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/form-login', methods=['GET', 'POST'])
def form_login():
    login_form = LoginForm()
    # session.get('username') // obteniendo valores de la session encriptada
    username = session.get('username') if session.get('username') else None

    context = {
        'login_form': login_form,
        'username': username
    }

    if request.method == 'POST' and login_form.validate_on_submit():
        # Obteniendo valores enviados
        username = login_form.username.data
        session['username'] = username

        # Creando un mensaje flash
        flash('Nombre de usuario se registro en la sesion :)')

        return redirect(url_for('form_login'))

    return render_template('form.html', **context)


"""
Handling errors 
"""


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def error_500(error):
    return render_template('500.html')


"""
Commands in console
"""


@app.cli.command()
def test():
    # desde consola flask test
    # flask name_function

    # Especificando el directorio donde debe buscar los test
    tests = unittest.TestLoader().discover('./tests')
    # todos los archivos debeb empexar por test_{name_test}.py
    # Ejecutando todos los test encontrados en el directorio anterior
    unittest.TextTestRunner().run(tests)
