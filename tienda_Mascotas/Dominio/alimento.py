import uuid

import jsonpickle

from tienda_Mascotas.Dominio.elementoCompra import ElementoCompra


class Alimento(ElementoCompra):
    def __init__(self, codigoAlimento, tipoAlimento, nombre, cantidadAlimento,
                 cantidadContenido, precio):

        super().__init__(cantidadAlimento, precio)
        self.codigoAlimento = codigoAlimento
        self.tipoAlimento = tipoAlimento
        self.nombreProducto = nombre
        self.cantidadAlimento = cantidadAlimento
        self.cantidadContenido = cantidadContenido
        self.precio = precio

    def __repr__(self):
        representacion = "Codigo:" + " " + str(self.codigoAlimento) + " " + "Nombre:" + str(
            self.nombreProducto) + " " + "Alimento para:" + str(self.tipoAlimento) + "" \
                                                                                     "Con un precio de:" + " " + str(
            self.precio)
        return representacion

    def cumple(self, especificacion):
        dict_alimento = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_alimento or dict_alimento[k] != especificacion.get_value(k):
                return False
        return True

    def guardar(self, alimento):
        from tienda_Mascotas.Infraestructura.persistenciaAlimento import PersistenciaAlimento
        persitencia_alimento = PersistenciaAlimento()
        persitencia_alimento.guardar_alimento(alimento)

    def guardar_actualizar(self):
        self._actualizar(self.codigoAlimento)

    def _actualizar(self, codigoAlimento):
        from tienda_Mascotas.Infraestructura.persistenciaAlimento import PersistenciaAlimento
        persitencia_alimento = PersistenciaAlimento()
        persitencia_alimento.actualizar_alimento(self, codigoAlimento)

    def update(self, dict_params):
        self.codigoAlimento = dict_params.get('codigoAlimento', self.codigoAlimento)
        self.tipoAlimento = dict_params.get('tipoAlimento', self.tipoAlimento)
        self.nombreProducto = dict_params.get('nombreProducto', self.nombreProducto)
        self.cantidadAlimento = dict_params.get('cantidadAlimento', self.cantidadAlimento)
        self.cantidadContenido = dict_params.get('cantidadContenido', self.cantidadContenido)
        self.precio = dict_params.get('precio', self.precio)

    def eliminar(self, codigoAlimento):
        from tienda_Mascotas.Infraestructura.persistenciaAlimento import PersistenciaAlimento
        persisten_alimento = PersistenciaAlimento()
        persisten_alimento.eliminar_alimento(codigoAlimento)
