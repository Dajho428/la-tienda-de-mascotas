import sqlite3

import jsonpickle

from tienda_Mascotas.Dominio.cliente import Cliente


class PersistenciaCliente:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_cliente()

    def __crear_tabla_cliente(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CLIENTE(codigoCliente text primary key, nombre text," \
                    " apellido text,cedula text," \
                    " genero text,direccion text,correo text,edad int,tiempoCliente) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_cliente(self, cliente: Cliente):
        cursor = self.con.cursor()
        query = "insert into CLIENTE(codigoCliente ," \
                " nombre , apellido, cedula ,genero, direccion, correo," \
                " edad,tiempoCliente) values(" \
                f" ?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (str(cliente.codigoCliente), cliente.nombre, cliente.apellido, str(cliente.cedula),
                               cliente.genero, cliente.direccion, cliente.correo, cliente.edad, cliente.tiempoCliente))
        self.con.commit()

    def consultar_tabla_cliente(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM CLIENTE"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Cliente(*row) for row in rows]

    def cargar_cliente(self, codigoCliente):
        cursor = self.con.cursor()
        query = "SELECT codigoCliente ,nombre ,  apellido ,cedula, genero , direccion, correo, edad, tiempoCliente FROM CLIENTE WHERE codigoCliente=?"
        clientes = cursor.execute(query, (codigoCliente,))
        cliente_encontrado = None
        for codigoCliene, nombre, apellido, cedula, genero, direccion, correo, edad, tiempoCliente in clientes:
            cliente_encontrado = Cliente(codigoCliente, nombre, apellido, cedula, genero, direccion, correo, edad,
                                         tiempoCliente)
        return cliente_encontrado

    def actualizar_cliente(self, cliente, codigoCliente):
        query = 'UPDATE CLIENTE SET  nombre=? ,  apellido=? ,cedula=?, genero=? , direccion=?, correo=?, edad=?, tiempoCliente=?' \
                'WHERE codigoCliente=?'
        cursor = self.con.cursor()
        cursor.execute(query, (cliente.nombre,
                               cliente.apellido,
                               cliente.cedula,
                               cliente.genero,
                               cliente.direccion,
                               cliente.correo,
                               cliente.edad,
                               cliente.tiempoCliente,
                               codigoCliente))
        self.con.commit()

    def eliminar_cliente(self, codigoCliente):
        query = "DELETE FROM CLIENTE WHERE codigoCliente=?"
        cursor = self.con.cursor()
        cursor.execute(query, (codigoCliente,))
        self.con.commit()

    @classmethod
    def save_json_cliente(cls, cliente):
        text_open = open("files/" + str(cliente.codigoCliente) + '.jsonCliente', mode='w')
        json_gui = jsonpickle.encode(cliente)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_cliente(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        cliente = jsonpickle.decode(json_gui)
        text_open.close()
        return cliente
