from . import auth
from app.forms import LoginForm
from flask import render_template, request, session, redirect, flash, url_for


# @auth // name of bluprint
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if request.method == 'POST' and login_form.validate_on_submit():
        # Obteniendo valores enviados
        username = login_form.username.data
        session['username'] = username


        # Creando un mensaje flash
        flash('Nombre de usuario se registro en la sesion :)')

        return redirect(url_for('index'))

    return render_template('login.html', **context)
