
class Cita(db.Model):
    id_cita= db.Column(db.Integer, primary_key=True)
    horario=db.Column(db.String(120), unique=False, nullable=False)
    ubicacion=db.Column(db.String(120), unique=False, nullable=False)
    profesional=db.Column(db.String(120), unique=False, nullable=False)
    id_horario=db.Column(db.Integer, db.ForeignKey('horario.id_horario'), nullable=False)
    id_ubicacion=db.Column(db.Integer, db.ForeignKey('ubicacion.id_profesional'), nullable=False)
    id_profesional=db.Column(db.Integer, db.ForeignKey('profesional.id_profesional'), nullable=False)
    id_usuario=db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    asignada=db.Column(db.Boolean, unique=False, nullable=False)
    diagnostico=db.Column(db.String(120), unique=False, nullable=False)
    medicamentos=db.Column(db.String(120), unique=False, nullable=False)
    
