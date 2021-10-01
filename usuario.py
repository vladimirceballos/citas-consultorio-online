from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Usuario (db.Model):
    tipo_documento = db.Column(db.String(255), unique=False, nullable=False)
    documento = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    genero = db.Column(db.String(120), unique=False, nullable=False)
    edad = db.Column(db.Integer, unique=False, nullable=False)
    contrasena = db.Column(db.String(120), unique=False, nullable=False)
    perfil = db.Column(db.Integer, db.ForeignKey('perfil.id_perfil'), nullable=False)
    cita = db.Column(db.Integer, db.ForeignKey('cita.id_cita'), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.Integer, unique=True, nullable=False)
    id_usuario= db.Column(db.Integer, primary_key=True)

def crear_usuario(self):
    user1 = Usuario(tipo_documento="",documento=0,nombre="",genero="",edad=0,contrasena="",perfil=1,correo="",telefono=0)
    user1.save()