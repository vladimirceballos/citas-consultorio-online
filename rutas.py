from flask import render_template, request

from modelos.Usuario import Usuario, crear_usuario
from modelos.Perfil import Perfil
from modelos.Horario import Horario
from modelos.Cita import Cita
from modelos.Profesional import Profesional
from modelos.Sede import Sede

from app import app


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        result = crear_usuario(request.form)
        if result == True:
            return 'User created successfully'
        else:
            return 'Error creating user'
    return render_template('register.html')


@app.route('/users')
def get_users():
    usuarios = Usuario.query.all()
    print(usuarios)
    return render_template('usuarios.html', usuarios=usuarios)
