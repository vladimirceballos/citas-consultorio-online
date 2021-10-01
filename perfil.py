class Perfil (db.Model):
    id_perfil=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(120), unique=False, nullable=False)
    descripcion=db.Column(db.String(120), unique=False, nullable=False)
    id_usuario=db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    