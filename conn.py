import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    )  
    
    cur = conn.cursor()
    return cur

class Perfil:
    
    nombre=''
    descripcion=''
    cant_perfiles=0
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    cur= conn.cursor()
    
    
    #def __init__(self):
    #    pass
    
    
    #def __init__(self, nombre, descripcion):
    #    self.nombre = nombre
    #    self.descripcion = descripcion
    
    
    #def __init__(self, cant_perfiles):
    #    self.cant_perfiles = cant_perfiles
    
    
    #def __init__(self, nombre):
    #   self.nombre = nombre
        
        
    def list_perfiles(self):
        perfiles = []
        self.cur.execute('SELECT * FROM perfil')
        perfiles = self.cur.fetchall()
        self.cur.close()
        return perfiles
        
        
    def create_perfil(self):
        self.cur.execute('INSERT INTO perfil(nombre,descripcion) VALUES (%s,%s)', (self.nombre,self.descripcion))
        self.conn.commit()
        self.cur.close()
        
        
    def delete_perfil(self):
        self.cur.execute('DELETE FROM perfil(nombre, descripcion) WHERE idperfil=%s',(self.idperfil,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
    def consultar_citas(self):
        citas=[]
        self.cur.execute('SELECT * FROM citas')
        citas= self.cur.fetchall()
        #self.cur.close()
        #self.conn.close()
        # return citas
        for cita in citas:
            self.cur.execute('SELECT * FROM horarios WHERE idhorario =' +str(cita [4]))
            horario= self.cur.fetchall()
            
            print(horario, cita[3])
        self.cur.close()
        self.conn.close()
