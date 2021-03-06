from flask import render_template, request, redirect, url_for
from modelos.Usuario import Usuario, crear_usuario
from modelos.Perfil import Perfil
from modelos.Horario import Horario
from modelos.Cita import Cita
from modelos.Profesional import Profesional
from modelos.Sede import Sede
from flask_bcrypt import Bcrypt
from app import app
from flask import Flask

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        result = crear_usuario(request.form)
        if result == True:
            return redirect (url_for('login'))
        else:
            return 'Error creating user'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        documento=request.form["documento"]
        contrasena=request.form["contrasena"]
        valida_usuario=Usuario.login(documento,contrasena)
        if (valida_usuario):
            return redirect (url_for('/agendamiento'))
    elif request.method=='GET':
        return render_template('login.html')



@app.route('/agendamiento', methods=['GET', 'POST'])
def show_appointment():
    if request.method == 'GET':
        cita = Cita.query.with_entities(Cita.id, Cita.horario, Cita.sede, Cita.profesional).filter(Cita.id_usuario==None)
        usuario=Usuario.query.filter_by(documento=request.form['documento'])
        print(cita.all())
        return render_template('list_citas.html',all_citas=cita)
    
    
    
def appointment():
    if request.method == 'POST':
        id_cita=request.form['id_cita']
        id_usuario=request.form['id_usuario']
        result = Cita.agendar_cita(id_cita,id_usuario)
        if result == True:
            return 'Appointment created successfully'
        else:
            return 'Error creating appointment'
    return render_template('')


@app.route('/profesional', methods= ['POST', 'GET'])
def show_historial():
    if request.method == 'GET':
        result = Cita.list_historial(request.form)
    return render_template('')
        
        
def agregar_historial():
    if request.method == 'PUT':
        result = Cita.add_historial
        
        

