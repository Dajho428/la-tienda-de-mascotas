import sqlite3

import jsonpickle

from tienda_Mascotas.Dominio.alimento import Alimento


class PersistenciaAlimento:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_alimento()

    def __crear_tabla_alimento(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE ALIMENTO(codigoAlimento text primary key,tipoAlimento text, nombreProducto text," \
                    " cantidadAlimento int," \
                    " cantidadContenido text,precio float) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_alimento(self, alimento: Alimento):
        cursor = self.con.cursor()
        query = "insert into ALIMENTO(codigoAlimento , tipoAlimento ," \
                " nombreProducto , cantidadAlimento ,cantidadContenido," \
                " precio) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(alimento.codigoAlimento), alimento.tipoAlimento, alimento.nombreProducto,
                               alimento.cantidadAlimento, alimento.cantidadContenido, alimento.precio))
        self.con.commit()

    def consultar_tabla_alimento(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM ALIMENTO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Alimento(*row) for row in rows]

    def cargar_alimento(self, codigoAlimento):
        cursor = self.con.cursor()
        query = "SELECT codigoAlimento , tipoAlimento , nombreProducto , cantidadAlimento ,cantidadContenido, precio FROM ALIMENTO WHERE codigoAlimento=?"
        alimentos = cursor.execute(query, (codigoAlimento,))
        alimento_encontrado = None
        for codigoAlimento, tipoAlimento, nombreProducto, cantidadAlimento, cantidadContenido, precio in alimentos:
            alimento_encontrado = Alimento(codigoAlimento, tipoAlimento, nombreProducto, cantidadAlimento,
                                           cantidadContenido, precio)
        return alimento_encontrado

    def actualizar_alimento(self, alimento, codigoAlimento):
        query = 'UPDATE ALIMENTO SET  tipoAlimento=? , nombreProducto=? , cantidadAlimento=? ,cantidadContenido=?, precio=?' \
                'WHERE codigoAlimento=?'
        cursor = self.con.cursor()
        cursor.execute(query, (alimento.tipoAlimento,
                               alimento.nombreProducto,
                               alimento.cantidadAlimento,
                               alimento.cantidadContenido,
                               alimento.precio,
                               codigoAlimento))
        self.con.commit()

    def eliminar_alimento(self, codigoAlimento):
        query = "DELETE FROM ALIMENTO WHERE codigoAlimento=?"
        cursor = self.con.cursor()
        cursor.execute(query, (codigoAlimento,))
        self.con.commit()

    @classmethod
    def save_json_alimento(cls, alimento):
        text_open = open("files/" + str(alimento.codigoAlimento) + '.jsonAlimento', mode='w')
        json_gui = jsonpickle.encode(alimento)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_alimento(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        alimento = jsonpickle.decode(json_gui)
        text_open.close()
        return alimento
