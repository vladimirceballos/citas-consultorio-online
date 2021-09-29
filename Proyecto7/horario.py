class Horario:
    hora=''
    dia=0
    mes=0
    ano=0
    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    
    def create_horario(self):
        self.cur.execute('INSERT INTO horario (hora,dia,mes,ano) VALUES (%s,%s,%s,%s)', (self.hora,self.dia,self.mes,self.ano))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return id
        
    def delete_horario(self):
        self.cur.execute('DELETE FROM horario (hora, dia, mes, ano) WHERE idhorario=%s',(self.idhorario,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
        
    def consultar_horario(self):
        horarios=[]
        self.cur.execute('SELECT * FROM horario')
        citas= self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return horarios
        