# import libreries to use forms
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    # Usando las propias clases de Flask para generar el formulario
    # DataRequired // validacion de campos requeridos
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')