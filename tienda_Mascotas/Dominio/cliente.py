import uuid

import jsonpickle

from tienda_Mascotas.Dominio.persona import Persona


class Cliente(Persona):
    def __init__(self, codigoCliente, nombre, apellido, cedula, genero, direccion, correo, edad, tiempoCliente):
        super().__init__(nombre, apellido, cedula, genero, direccion, correo, edad)
        self.codigoCliente = codigoCliente
        self.tiempoCliente = tiempoCliente

    def __repr__(self):
        representacion = "Cliente:" + " " + str(self.nombre) + " " + str(
            self.apellido) + " " + "Identificado con cedula:" + " " + str(self.cedula)
        return representacion

    def cumple(self, especificacion):
        dict_cliente = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_cliente or dict_cliente[k] != especificacion.get_value(k):
                return False
        return True

    def modificarTiempoCliente(self, nuevoTiempo):
        self.tiempoCliente = nuevoTiempo

    def guardar(self, cliente):
        from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente
        persitencia_cliente = PersistenciaCliente()
        persitencia_cliente.guardar_cliente(cliente)

    def guardar_actualizar(self):
        self._actualizar(self.codigoCliente)

    def _actualizar(self, codigoCliente):
        from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente
        persitencia_cliente = PersistenciaCliente()
        persitencia_cliente.actualizar_cliente(self, codigoCliente)

    def update(self, dict_params):
        self.codigoCliente = dict_params.get('codigoCliente', self.codigoCliente)
        self.nombre = dict_params.get('nombre', self.nombre)
        self.apellido = dict_params.get('apellido', self.apellido)
        self.cedula = dict_params.get('cedula', self.cedula)
        self.genero = dict_params.get('genero', self.genero)
        self.direccion = dict_params.get('direccion', self.direccion)
        self.correo = dict_params.get('correo', self.correo)
        self.edad = dict_params.get('edad', self.edad)
        self.tiempoCliente = dict_params.get('tiempoCliente', self.tiempoCliente)

    def eliminar(self, codigoCliente):
        from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente
        persisten_cliente = PersistenciaCliente()
        persisten_cliente.eliminar_cliente(codigoCliente)
