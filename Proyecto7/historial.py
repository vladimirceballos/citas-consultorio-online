class Historial:
    historia=''
    medicamentos=''
    citas=''
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    def create_historial(self):
        self.cur.execute('INSERT INTO historiaclinica (historia,medicamentos,citas) VALUES (%s,%s,%s)', (self.historia,self.medicamentos,self.citas))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        

    def consultar_historial(self):  
        historial=[]
        self.cur.execute('SELECT * FROM historiaclinica')
        citas= self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return historial
    