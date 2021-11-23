import sqlite3

import jsonpickle

from tienda_Mascotas.Dominio.accesorio import Accesorio


class PersistenciaAccesorio:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_accesorio()

    def __crear_tabla_accesorio(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ACCESORIO(codigoAccesorio text primary key,nombreAccesorio text, precioAccesorio float," \
                    " cantidadAccesorio int,descripcionAccesorio text," \
                    " usoAccesorio text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_accesorio(self, accesorio: Accesorio):
        cursor = self.con.cursor()
        query = "insert into ACCESORIO(codigoAccesorio , nombreAccesorio ," \
                " precioAccesorio , cantidadAccesorio ,descripcionAccesorio," \
                " usoAccesorio) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(accesorio.codigoAccesorio), accesorio.nombreAccesorio, accesorio.precio,
                               accesorio.cantidad, accesorio.descripcionAccesorio, accesorio.usoAccesorio))
        self.con.commit()

    def consultar_tabla_accesorio(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM ACCESORIO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Accesorio(*row) for row in rows]

    def cargar_accesorio(self, codigoAccesorio):
        cursor = self.con.cursor()
        query = "SELECT codigoAccesorio , nombreAccesorio , precioAccesorio , cantidadAccesorio ,descripcionAccesorio , usoAccesorio FROM ACCESORIO WHERE codigoAccesorio=?"
        accesorios = cursor.execute(query, (codigoAccesorio,))
        accesorio_encontrado = None
        for codigoAccesorio, nombreAccesorio, precioAccesorio, cantidadAccesorio, descripcionAccesorio, usoAccesorio in accesorios:
            accesorio_encontrado = Accesorio(codigoAccesorio, nombreAccesorio, precioAccesorio, cantidadAccesorio,
                                             descripcionAccesorio, usoAccesorio)
        return accesorio_encontrado

    def actualizar_accesorio(self, accesorio, codigoAccesorio):
        query = 'UPDATE ACCESORIO SET  nombreAccesorio=? , precioAccesorio=? , cantidadAccesorio=? ,descripcionAccesorio=? , usoAccesorio=?' \
                'WHERE codigoAccesorio=?'
        cursor = self.con.cursor()
        cursor.execute(query, (accesorio.nombreAccesorio,
                               accesorio.precio,
                               accesorio.codigoAccesorio,
                               accesorio.descripcionAccesorio,
                               accesorio.usoAccesorio,
                               codigoAccesorio))
        self.con.commit()

    def eliminar_accesorio(self, codigoAccesorio):
        query = "DELETE FROM ACCESORIO WHERE codigoAccesorio=?"
        cursor = self.con.cursor()
        cursor.execute(query, (codigoAccesorio,))
        self.con.commit()

    @classmethod
    def save_json_accesorio(cls, accesorio):
        text_open = open("files/" + str(accesorio.codigoAccesorio) + '.jsonAccesorio', mode='w')
        json_gui = jsonpickle.encode(accesorio)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_accesorio(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        accesorio = jsonpickle.decode(json_gui)
        text_open.close()
        return accesorio
