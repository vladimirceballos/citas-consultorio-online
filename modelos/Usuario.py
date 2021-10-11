from app import db 
from app import bcrypt


class Usuario (db.Model):
    
    __tablename__='usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(255), unique=False, nullable=False)
    documento = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(120), unique=False, nullable=False)
    genero = db.Column(db.String(120), unique=False, nullable=False)
    edad = db.Column(db.Integer, unique=False, nullable=False)
    contrasena = db.Column(db.String(120), unique=False, nullable=False)
    perfil = db.Column(db.Integer, db.ForeignKey(
        'perfil.id'), nullable=False)
    correo = db.Column(db.String(120), unique=False, nullable=False)
    telefono = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<Usuario: {}, {}>".format(self.id, self.nombre)

def __init__(self,documento,contrasena):
    self.documento=documento
    self.contrasena=bcrypt.generate_password_hash(contrasena).decode('utf8')
    self.id=3
    
    

@staticmethod
def crear_usuario(usuario):
    tipo_documento = usuario['tipo_documento']
    documento = int(usuario['documento'])
    nombre = usuario['nombre']
    genero = usuario['genero']
    edad = int(usuario['edad'])
    telefono = int(usuario['telefono'])
    correo = usuario['correo']
    contrasena = usuario['contrasena']

    usuario = Usuario(tipo_documento=tipo_documento,
                    documento=documento,
                    nombre=nombre,
                    genero=genero,
                    edad=edad,
                    contrasena=contrasena,
                    perfil=3,
                    correo=correo,
                    telefono=telefono)
    db.session.add(usuario)
    db.session.commit()
    return False

@staticmethod
def get_documento(documento_find):
    return Usuario.query.filter_by(documento=documento_find).first()

@staticmethod
def login(documento, contrasena):
    success= False
    user= Usuario.get_documento(documento)
    
    if (user):
        success= bcrypt.check_password_hash(user.contrasena, contrasena)
    
    return success