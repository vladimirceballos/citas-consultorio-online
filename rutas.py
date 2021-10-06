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


@app.route('/agendamiento', methods=['GET', 'UPDATE'])
def show_appointment():
    if request.method == 'GET':
        cita = Cita.query.with_entities(Cita.id, Cita.horario, Cita.sede, Cita.profesional).filter(Cita.id_usuario==None)
        usuario=Usuario.query.filter_by(documento=1017220191)
        if len(usuario.all())>0:
            print(usuario.one().id)
        else:
            print("No registrado")
        print(cita)
        cita=cita.all()
        return render_template('list_citas.html',all_citas=cita)
    #print(cita)
    
    
    
def appointment():
    if request.method == 'UPDATE':
        result = agendar_cita(request.form)
        if result == True:
            return 'Appointment created successfully'
        else:
            return 'Error creating appointment'
    return render_template('')
