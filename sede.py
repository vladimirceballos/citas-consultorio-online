

class Sede(db.Model):
    pais= db.Column(db.String(120), unique=False, nullable=False)
    ciudad= db.Column(db.String(120), unique=False, nullable=False)
    departamento=db.Column(db.String(120), unique=False, nullable=False)
    comuna=db.Column(db.String(120), unique=False, nullable=True)
    direccion=db.Column(db.String(120), unique=False, nullable=False)
    id_sede= db.Column(db.Integer, primary_key=True)
    cita_id=db.Column(db.Integer, db.ForeignKey('cita.id'), nullable=False)
    
