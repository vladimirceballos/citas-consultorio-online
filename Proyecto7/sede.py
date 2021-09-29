class Sede:
    pais=''
    ciudad=''
    departamento=''
    comuna=''
    direccion=''
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
nombre=''
ocupacion=''
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    def create_profesional(self):
        self.cur.execute('INSERT INTO profesional (nombre,ocupacion) VALUES (%s,%s)', (self.nombre,self.ocupacion))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return id
        
    def delete_profesional(self):
        self.cur.execute('DELETE FROM profesional (nombre, ocupacion) WHERE idprofesional=%s',(self.idprofesional,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
    def consultar_profesional(self):
        profesionales=[]
        self.cur.execute('SELECT * FROM profesional')
        citas= self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return profesionales