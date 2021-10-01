from app import db


class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.String(120), unique=False, nullable=False)
    sede = db.Column(db.String(120), unique=False, nullable=False)
    profesional = db.Column(db.String(120), unique=False, nullable=False)
    id_horario = db.Column(db.Integer, db.ForeignKey(
        'horario.id'), nullable=False)
    id_sede = db.Column(db.Integer, db.ForeignKey(
        'sede.id'), nullable=False)
    id_profesional = db.Column(db.Integer, db.ForeignKey(
        'profesional.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(
        'usuario.id'), nullable=True)
    asignada = db.Column(db.Boolean, unique=False, nullable=False)
    diagnostico = db.Column(db.String(120), unique=False, nullable=False)
    medicamentos = db.Column(db.String(120), unique=False, nullable=False)
