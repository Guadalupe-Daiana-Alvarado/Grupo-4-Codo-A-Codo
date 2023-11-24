#--------------------------------------------------------------------
# Instalo las cosas necesarias

import mysql.connector

#--------------------------------------------------------------------

print("\033[H\033[J") # Limpiar la consola

class Listado:
    deportistas = [] 
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS deportistas (
            Nombre VARCHAR(100) NOT NULL,
            Apellido VARCHAR(100) NOT NULL,
            Deporte VARCHAR(100) NOT NULL,
            Cantidad de títulos o campeonatos INT,
            Comentarios VARCHAR(500))''')
        self.conn.commit()






 # -------------------------------------------------------------------
lista_deportistas = Listado(host='localhost', user='root', password='', database='miapp')