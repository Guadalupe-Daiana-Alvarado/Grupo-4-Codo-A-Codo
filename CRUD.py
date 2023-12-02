
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import mysql.connector
from werkzeug.utils import secure_filename



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas
CORS(app, resources={r"/deportistas": {"origins": "*"}})

#--------------------------------------------------------------------
print ("\033[(H\033[J") 

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

        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS deportistas (
            id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
            Nombre VARCHAR(100) NOT NULL,
            Apellido VARCHAR(100) NOT NULL,
            Nacionalidad VARCHAR(100) NOT NULL,
            Deporte VARCHAR(100) NOT NULL,
            Cantidad_titulos INT,
            Comentarios VARCHAR(500))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    #Agregar deportista

    def agregar_deportista(self, nom, ape, nac, dep, cant, cmt):
        sql = f"INSERT INTO deportistas \
            (Nombre, Apellido, Nacionalidad, Deporte, Cantidad_titulos, Comentarios) \
            VALUES \
            ('{nom}', '{ape}', '{nac}', '{dep}', {cant}, '{cmt}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True    
    #Listar deportista

    def listar_productos(self):
            print("-"*50)
            for d in self.deportistas:
                print(f"Id.................: {d['id']}" )
                print(f"Nombre.............: {d['Nombre']}" )
                print(f"Apellido...........: {d['Apellido']}" )
                print(f"Nacionalidad.......: {d['Nacionalidad']}" )
                print(f"Deporte............: {d['Deporte']}" )
                print(f"Cantidad_titulos...: {d['Cantidad_titulos']}" )
                print(f"Comentarios........: {d['Comentarios']}" )
                print("-"*50)


    #Consultar deportista

    def consultar_producto(self, id):
            self.cursor.execute(f"SELECT * FROM deportistas WHERE Id = {id}")
            deportista_exist = self.cursor.fetchone()
            if deportista_exist:
                return deportista_exist


    #Eliminar deportista

    def eliminar_deportista(self, id):
        self.cursor.execute(f"DELETE FROM deportistas WHERE Id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0


    # Editar deportista

    def modificar_deportista(self, id, nuevo_nombre, nuevo_apellido, nuevo_deporte, nueva_nacionalidad, nuevos_titulos, nueva_descripcion):

        sql = "UPDATE deportistas SET Nombre = %s, Apellido = %s, Deporte = %s, Nacionalidad = %s, Cantidad_titulos = %s, Comentarios = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_deporte, nueva_nacionalidad, nuevos_titulos, nueva_descripcion, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
            
    def listar_deportistas(self):
        self.cursor.execute("SELECT * FROM deportistas")
        lista_deportistas = self.cursor.fetchall()
        return lista_deportistas

 # -------------------------------------------------------------------
lista_deportistas = Listado(host='localhost', user='root', password='', database='miapp')
"""
lista_deportistas.agregar_deportista ('Valentino', 'Rossi', 'Italiano', 'Motociclismo', 9, 'De los 9 títulos, 7 fueron en la máxima categoría')
lista_deportistas.agregar_deportista ('Lionel', 'Messi', 'Argentino', 'Futbol', 43, 'Jugó más de 20 años en el Barcelona siempre con el número 10')
lista_deportistas.agregar_deportista ( 'Serena', 'Williams', 'Estadounidense', 'Tenis', 73, 'Es la única tenista en haber completado el Golden Slam de carrera en las dos modalidades, individuales y dobles')
"""
lista_deportistas.consultar_producto(1)




# Ruta para obtener la lista de deportistas
@app.route('/deportistas', methods=['GET'])
def obtener_deportistas():
    deportistas = lista_deportistas.listar_deportistas()
    return jsonify(deportistas)

# Ruta para agregar un deportista
@app.route('/deportistas', methods=['POST'])
def agregar_deportista():
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Nacionalidad = request.form['Nacionalidad']
    Deporte = request.form['Deporte']  
    Cantidad_titulos = request.form['Cantidad_titulos']
    Comentarios = request.form['Comentarios']
    print("*"*20)

    if lista_deportistas.agregar_deportista( Nombre, Apellido, Nacionalidad, Deporte, Cantidad_titulos,Comentarios):
        return jsonify({"mensaje": "Producto agregado"}), 201
    else:
        return jsonify({"mensaje": "Producto ya existe"}), 400

# Ruta para obtener detalles de un deportista por ID
@app.route('/deportistas/<int:id>', methods=['GET'])
def obtener_deportista(id):
    deportista = lista_deportistas.consultar_producto(id)
    return jsonify(deportista)

# Ruta para eliminar un deportista por ID
@app.route('/deportistas/<int:id>', methods=['DELETE'])
def eliminar_deportista(id):
    success = lista_deportistas.eliminar_deportista(id)
    return jsonify({'success': success})

# Ruta para modificar un deportista por ID
@app.route('/deportistas/<int:id>', methods=['PUT'])
def modificar_deportista(id):
    new_nombre = request.form['Nombre']
    new_apellido = request.form['Apellido']
    new_deporte = request.form['Deporte']
    new_nacionalidad = request.form['Nacionalidad']
    new_titulos = request.form['Cantidad_titulos']
    new_descripcion = request.form['Comentarios']

    if lista_deportistas.modificar_deportista(id,new_nombre, new_apellido,new_deporte, new_nacionalidad, new_titulos, new_descripcion):
        return jsonify({"mensaje": "deportista modificado"}), 200
    else:
        return jsonify({"mensaje": "deportista no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
