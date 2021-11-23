import sqlite3

import jsonpickle

from tienda_Mascotas.Dominio.empleado import Empleado


class PersistenciaEmpleado:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_empleado()

    def __crear_tabla_empleado(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE EMPLEADO(codigo text primary key, nombre text,cedula text," \
                    " apellido text, cargo text,salario float," \
                    " genero text,edad int,direccion text,correo text,horario text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_empleado(self, empleado: Empleado):
        cursor = self.con.cursor()
        query = "insert into EMPLEADO(codigo ," \
                " nombre , cedula, apellido ,cargo , salario, genero, edad, direccion, correo, horario ) values(" \
                f" ?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (str(empleado.codigo), empleado.nombre, str(empleado.cedula), empleado.apellido,
                               empleado.cargo, empleado.salario, empleado.genero, empleado.edad, empleado.direccion,
                               empleado.correo, empleado.horario))
        self.con.commit()

    def consultar_tabla_empleado(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM EMPLEADO"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Empleado(*row) for row in rows]

    def cargar_empleado(self, codigoEmpleado):
        cursor = self.con.cursor()
        query = "SELECT codigo ,nombre , cedula, apellido ,cargo , salario, genero, edad, direccion, correo, horario FROM EMPLEADO WHERE codigo=?"
        empleados = cursor.execute(query, (codigoEmpleado,))
        empleado_encontrado = None
        for codigo, nombre, cedula, apellido, cargo, salario, genero, edad, direccion, correo, horario in empleados:
            empleado_encontrado = Empleado(codigo, nombre, cedula, apellido, cargo, salario, genero, edad, direccion,
                                           correo, horario)
        return empleado_encontrado

    def actualizar_empleado(self, empleado, codigoEmpleado):
        query = 'UPDATE EMPLEADO SET  nombre=? , cedula=?, apellido=? ,cargo=? , salario=?, genero=?, edad=?, direccion=?, correo=?, horario=?' \
                'WHERE codigo=?'
        cursor = self.con.cursor()
        cursor.execute(query, (empleado.nombre,
                               empleado.cedula,
                               empleado.apellido,
                               empleado.cargo,
                               empleado.salario,
                               empleado.genero,
                               empleado.edad,
                               empleado.direccion,
                               empleado.correo,
                               empleado.horario,
                               codigoEmpleado))
        self.con.commit()

    def eliminar_empleado(self, codigoEmpleado):
        query = "DELETE FROM EMPLEADO WHERE codigo=?"
        cursor = self.con.cursor()
        cursor.execute(query, (codigoEmpleado,))
        self.con.commit()

    @classmethod
    def save_json_empleado(cls, empleado):
        text_open = open("files/" + str(empleado.codigo) + '.jsonEmpleado', mode='w')
        json_gui = jsonpickle.encode(empleado)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_empleado(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        empleado = jsonpickle.decode(json_gui)
        text_open.close()
        return empleado
