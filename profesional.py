class Profesional(db.Model):
    id_profesional=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(120), unique=False, nullable=False)
    ocupacion=db.Column(db.String(120), unique=False, nullable=False)
    cita_id=db.Column(db.Integer, db.ForeignKey('cita.id'), nullable=False)
    
    