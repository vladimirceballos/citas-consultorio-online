class Usuario:
    tipo_documento=''
    documento= 0
    nombre=''
    genero=''
    edad=0
    contraseña=''
    perfil=''
    cita=''
    correo=''
    telefono=0
    historial=''
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 