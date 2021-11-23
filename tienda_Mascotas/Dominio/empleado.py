import uuid

import jsonpickle

from tienda_Mascotas.Dominio.persona import Persona


class Empleado(Persona):
    def __init__(self, codigo, nombre, cedula, apellido, cargo, salario, genero, edad, direccion, correo,
                 horario):

        super().__init__(nombre, apellido, cedula, genero, direccion, correo, edad)
        self.codigo = codigo
        self.cargo = cargo
        self.horario = horario
        self.salario = salario

    def __repr__(self):
        representacion = "Empleado:" + str(self.nombre) + " " + str(self.apellido) + " " + "Con cargo de:" + str(
            self.cargo)
        return representacion

    def ascenso(self, nuevoCargo):
        self.cargo = nuevoCargo

    def aumento(self, nuevoSalario):
        self.salario = nuevoSalario

    def cambioHorarioLaboral(self, nuevoHorario):
        self.horario = nuevoHorario

    def cumple(self, especificacion):
        dict_empleado = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_empleado or dict_empleado[k] != especificacion.get_value(k):
                return False
        return True

    def guardar(self, empleado):
        from tienda_Mascotas.Infraestructura.persistenciaEmpleado import PersistenciaEmpleado
        persitencia_empleado = PersistenciaEmpleado()
        persitencia_empleado.guardar_empleado(empleado)

    def guardar_actualizar(self):
        self._actualizar(self.codigo)

    def _actualizar(self, codigo):
        from tienda_Mascotas.Infraestructura.persistenciaEmpleado import PersistenciaEmpleado
        persitencia_empleado = PersistenciaEmpleado()
        persitencia_empleado.actualizar_empleado(self, codigo)

    def update(self, dict_params):
        self.codigo = dict_params.get('codigo', self.codigo)
        self.nombre = dict_params.get('nombre', self.nombre)
        self.cedula = dict_params.get('cedula', self.cedula)
        self.apellido = dict_params.get('apellido', self.apellido)
        self.cargo = dict_params.get('cargo', self.cargo)
        self.salario = dict_params.get('salario', self.salario)
        self.genero = dict_params.get('genero', self.genero)
        self.edad = dict_params.get('edad', self.edad)
        self.direccion = dict_params.get('direccion', self.direccion)
        self.correo = dict_params.get('correo', self.correo)
        self.horario = dict_params.get('horario', self.horario)

    def eliminar(self, codigoEmpleado):
        from tienda_Mascotas.Infraestructura.persistenciaEmpleado import PersistenciaEmpleado
        persisten_empleado = PersistenciaEmpleado()
        persisten_empleado.eliminar_empleado(codigoEmpleado)
