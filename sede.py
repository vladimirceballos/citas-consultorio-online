import conn
import psycopg2


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
pais=''
departamento=''
ciudad=''
comuna=''
direccion=''

    
    conn = psycopg2.connect(
        host = "ec2-52-0-93-3.compute-1.amazonaws.com",
        database = "d7fvitj0ia8476",
        user = "jjbocsmdipegxk",
        password = "3d71afcd6756199393a25037b52dd43d576770b44a15464c72947aec12865130"
    ) 
    
    def create_sede(self):
        self.cur.execute('INSERT INTO sede (pais,departamento,ciudad,comuna,direccion) VALUES (%s,%s,%s,%s,%s)', (self.pais, self.departamento, self.ciudad, self.comuna, self.direccion))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return idsede
        
    def delete_sede(self):
        self.cur.execute('DELETE FROM sede (pais, departamento,ciudad,comuna,direccion) WHERE idsede=%s',(self.idsede,))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        
    def consultar_sede(self):
        sedes=[]
        self.cur.execute('SELECT * FROM sede')
        sedes= self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return sedes