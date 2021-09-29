import conn
import psycopg2

class Cita:
    horario=''
    ubicacion=''
    profesional=''
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    #def __init__(self):
    #    pass
    
    #def __init__(self,horario,ubicacion,profesional):
    #    self.horario = horario
    #   self.ubicacion =ubicacion
    #    self.profesional = profesional
        
    cur = conn.cursor()

    def create_cita(self):
        self.cur.execute('INSERT INTO citas (horario,ubicacion,profesional) VALUES (%s,%s,%s)', (self.horario,self.ubicacion,self.profesional))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return id
        
    def delete_cita(self):
        self.cur.execute('DELETE FROM citas (horario, ubicacion, profesional) WHERE idcita=%s',(self.idcita,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
    def consultar_citas(self):
        citas=[]
        self.cur.execute('SELECT * FROM citas')
        citas= self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return citas
        