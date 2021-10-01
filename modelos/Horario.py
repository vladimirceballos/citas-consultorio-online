from app import db


class Horario (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.String(120), unique=False, nullable=False)
