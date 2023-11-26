--------------------------------------------------------------------
# Instalo las cosas necesarias

# Instalar con pip install Flask
# Instalar con pip install flask-cors
# Instalar con pip install mysql-connector-python

import mysql.connector
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask import request

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
            id INT,
            Nombre VARCHAR(100) NOT NULL,
            Apellido VARCHAR(100) NOT NULL,
            Nacionalidad VARCHAR(100) NOT NULL,
            Deporte VARCHAR(100) NOT NULL,
            Cantidad_titulos INT,
            Comentarios VARCHAR(500))''')
        self.conn.commit()


#Agregar deportista

def agregar_deportista(self, cod, nom, ape, nac, dep, cant, cmt):
        self.cursor.execute(f"SELECT * FROM deportistas WHERE id = {cod}")
        deportista_exist = self.cursor.fetchone()
        if deportista_exist:
            return False

        sql = f"INSERT INTO deportistas \
               (id, Nombre, Apellido, Nacionalidad, Deporte, Cantidad_titulos, Comentarios) \
               VALUES \
               ({cod}, '{nom}', '{ape}', '{nac}', '{dep}', {cant}, '{cmt}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

#Listar deportista

def listar_productos(self):
        print("-"*50)
        for deportista in self.deportistas:
            print(f"Id.................: {producto['id']}" )
            print(f"Nombre.............: {producto['Nombre']}" )
            print(f"Apellido...........: {producto['Apellido']}" )
            print(f"Nacionalidad.......: {producto['Nacionalidad']}" )
            print(f"Deporte............: {producto['Deporte']}" )
            print(f"Cantidad_titulos...: {producto['Cantidad_titulos']}" )
            print(f"Comentarios........: {producto['Comentarios']}" )
            print("-"*50)


#Consultar deportista

def consultar_producto(self, id):
        self.cursor.execute(f"SELECT * FROM depotistas WHERE Id = {id}")
        deportista_exist = self.cursor.fetchone()
        if deportista_exist:
            return deportista_exist


#Eliminar deportista

    def eliminar_deportista(self, id):
        self.cursor.execute(f"DELETE FROM deportista WHERE Id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0


# Editar deportista

def modificar_producto(self, cod, nom, ape, nac, dep, cant, cmt):
        sql = f"UPDATE productos SET \
                Nombre = '{nom}',\
                Apellido = '{ape}',\
                Nacionalidad = '{nac}',\
                Deporte = '{dep}',\
                Cantidad_titulos = {cant},\
                Comentarios = '{cmt}'\
                WHERE Id = {id}"
        self.cursor.execute(sql)
        self.conn.commit()
        return True



 # -------------------------------------------------------------------
lista_deportistas = Listado(host='localhost', user='root', password='', database='miapp')

lista_deportistas.agregar_deportista (1, 'Valentino', 'Rossi', 'Italiano', 'Motociclismo', 9, 'De los 9 títulos, 7 fueron en la máxima categoría')
lista_deportistas.agregar_deportista (2, 'Lionel', 'Messi', 'Argentino', 'Futbol', 43, 'Jugó más de 20 años en el Barcelona siempre con el número 10')
lista_deportistas.agregar_deportista (3, 'Serena', 'Williams', 'Estadounidense', 'Tenis', 73, 'Es la única tenista en haber completado el Golden Slam de carrera en las dos modalidades, individuales y dobles')



