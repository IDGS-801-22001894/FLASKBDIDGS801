from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, DateField, RadioField
from wtforms import validators
from wtforms.validators import DataRequired
from datetime import datetime

class UserForm2(Form):
    id=IntegerField('id',
    [validators.number_range(min=1, max=20,message='valor no valido')])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4,max=20, message='requiere min=4 max=20')
    ])
   
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email=EmailField('correo',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
 