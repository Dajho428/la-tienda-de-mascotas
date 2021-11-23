import uuid

import jsonpickle

from tienda_Mascotas.Dominio.elementoCompra import ElementoCompra


class Accesorio(ElementoCompra):
    def __init__(self, codigoAccesorio, nombre, precio,cantidad,
                 descripcionAccesorio,usoAccesorio):
        super().__init__(cantidad, precio)
        self.codigoAccesorio = codigoAccesorio
        self.nombreAccesorio = nombre
        self.descripcionAccesorio = descripcionAccesorio
        self.usoAccesorio = usoAccesorio

    def __repr__(self):
        representacion = "Accesorio:" + " " + self.nombreAccesorio + " " + "Con precio:" + " " + str(
            self.precio) + " " + "Y uso de:" + " " + str(self.usoAccesorio)
        return representacion

    def cumple(self, especificacion):
        dict_accesorio = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_accesorio or dict_accesorio[k] != especificacion.get_value(k):
                return False
        return True

    def guardar(self, accesorio):
        from tienda_Mascotas.Infraestructura.persistenciaAccesorio import PersistenciaAccesorio
        persitencia_accesorio = PersistenciaAccesorio()
        persitencia_accesorio.guardar_accesorio(accesorio)

    def guardar_actualizar(self):
        self._actualizar(self.codigoAccesorio)

    def _actualizar(self, codigoAccesorio):
        from tienda_Mascotas.Infraestructura.persistenciaAccesorio import PersistenciaAccesorio
        persitencia_accesorio = PersistenciaAccesorio()
        persitencia_accesorio.actualizar_accesorio(self, codigoAccesorio)

    def update(self, dict_params):
        self.codigoAccesorio = dict_params.get('codigoAccesorio', self.codigoAccesorio)
        self.nombreAccesorio = dict_params.get('nombreAccesorio', self.nombreAccesorio)
        self.precio = dict_params.get('precioAccesorio', self.precio)
        self.cantidad = dict_params.get('cantidadAccesorio', self.cantidad)
        self.descripcionAccesorio = dict_params.get('descripcionAccesorio', self.descripcionAccesorio)
        self.usoAccesorio = dict_params.get('usoAccesorio', self.usoAccesorio)

    def eliminar(self, codigoAccesorio):
        from tienda_Mascotas.Infraestructura.persistenciaAccesorio import PersistenciaAccesorio
        persisten_accesorio = PersistenciaAccesorio()
        persisten_accesorio.eliminar_accesorio(codigoAccesorio)
