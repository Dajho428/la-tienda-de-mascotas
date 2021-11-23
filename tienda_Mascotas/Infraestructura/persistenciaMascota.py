import sqlite3
import jsonpickle

from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Infraestructura.configuracion import Configuracion


class PersistenciaMascota:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_mascota()

    def __crear_tabla_mascota(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MASCOTA(codigoMascota text primary key, tipoMascota text," \
                    " raza text, nombre text,edad int," \
                    " precio float,cantidad int) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_mascota(self, mascota: Mascota):
        cursor = self.con.cursor()
        query = "insert into MASCOTA(codigoMascota , tipoMascota ," \
                " raza , nombre ,edad ," \
                " precio,cantidad) values(" \
                f" ?,?,?,?,?,?,?)"
        cursor.execute(query, (str(mascota.codigoMascota), mascota.tipoMascota, mascota.raza, mascota.nombre,
                               mascota.edad, mascota.precio, mascota.cantidad))
        self.con.commit()

    def consultar_tabla_mascota(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM MASCOTA"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Mascota(*row) for row in rows]

    def cargar_mascota(self, codigoMascota):
        cursor = self.con.cursor()
        query = "SELECT codigoMascota , tipoMascota , raza , nombre ,edad , precio,cantidad FROM MASCOTA WHERE codigoMascota=?"
        mascotas = cursor.execute(query, (codigoMascota,))
        mascota_encontrada = None
        for codigoMascota, tipoMascota, raza, nombre, edad, precio, cantidad in mascotas:
            mascota_encontrada = Mascota(codigoMascota, tipoMascota, raza, nombre, edad, precio, cantidad)
        return mascota_encontrada

    def actualizar_mascota(self, mascota, codigoMascota):
        query = 'UPDATE MASCOTA SET  tipoMascota=? , raza=? , nombre=? ,edad=? , precio=?,cantidad=?' \
                'WHERE codigoMascota=?'
        cursor = self.con.cursor()
        cursor.execute(query, (mascota.tipoMascota,
                               mascota.raza,
                               mascota.nombre,
                               mascota.edad,
                               mascota.precio,
                               mascota.cantidad,
                               codigoMascota))
        self.con.commit()

    def eliminar_mascota(self, codigoMascota):
        query = "DELETE FROM MASCOTA WHERE codigoMascota=?"
        cursor = self.con.cursor()
        cursor.execute(query, (codigoMascota,))
        self.con.commit()

    @classmethod
    def save_json_mascota(cls, mascota):
        text_open = open("files/" + str(mascota.codigoMascota) + '.jsonMascota', mode='w')
        json_gui = jsonpickle.encode(mascota)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_mascota(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        mascota = jsonpickle.decode(json_gui)
        text_open.close()
        return mascota

    @classmethod
    def save_json_configuracion(cls, configuracion: Configuracion):
        text_open = open("files/" + str(configuracion.codigoUnico) + '.json', mode='w')
        json_gui = jsonpickle.encode(configuracion)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_configuracion(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        configuracion = jsonpickle.decode(json_gui)
        text_open.close()
        return configuracion
