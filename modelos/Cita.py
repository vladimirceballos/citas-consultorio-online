from app import db
from modelos.Usuario import Usuario


class Cita(db.Model):
    
    __tablename__='cita'
    
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

def crear_cita(cita):
    horario = cita['horario']
    sede = cita['sede']
    profesional = cita['profesional']

    cita = Cita(horario=horario,
                    sede=sede,
                    profesional=profesional,)
    db.session.add(cita)
    db.session.commit()
    return False
    
    
def agendar_cita(cita):
    
    cita_seleccionada= Cita.query.filter_by(id=id_cita)
    cita_seleccionada.id_usuario=currentUsuario.id_usuario
    db.session.commit()
    
    
    