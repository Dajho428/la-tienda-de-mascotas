import uuid
from tienda_Mascotas.Dominio.elemento_compra import Elemento_compra


class Mascota(Elemento_compra):
    def __init__(self, codigoMascota, tipoMascota, raza, nombre, edad, precio, cantidad):

        super().__init__(cantidad, precio)
        self.tipoMascota = tipoMascota
        self.codigoMascota = codigoMascota
        self.raza = raza
        self.edad = edad
        self.nombre = nombre

    def __repr__(self):
        representacion = "La mascota es un:" + " " + str(self.tipoMascota) + " " + "De raza:" + " " + str(
            self.raza) + " " \
                         "Con edad:" + " " + str(self.edad) + " " + "Y un precio de:" + " " + str(self.precio)
        return representacion

    def cumpleaños(self, nueva_Edad):
        self.edad = nueva_Edad

    def cumple(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True

    def guardar(self, mascota):
        from tienda_Mascotas.Infraestructura.persistencia_mascota import Persistencia_mascota
        persitencia_mascota = Persistencia_mascota()
        persitencia_mascota.guardar_mascota(mascota)

    def guardar_actualizar(self):
        self._actualizar(self.codigoMascota)

    def _actualizar(self, codigoMascota):
        from tienda_Mascotas.Infraestructura.persistencia_mascota import Persistencia_mascota
        persitencia_mascota = Persistencia_mascota()
        persitencia_mascota.actualizar_mascota(self, codigoMascota)

    def update(self, dict_params):
        self.codigoMascota = dict_params.get('codigoMascota', self.codigoMascota)
        self.tipoMascota = dict_params.get('tipoMascota', self.tipoMascota)
        self.raza = dict_params.get('raza', self.raza)
        self.nombre = dict_params.get('nombre', self.nombre)
        self.edad = dict_params.get('edad', self.edad)
        self.precio = dict_params.get('precio', self.precio)
        self.cantidad = dict_params.get('cantidad', self.cantidad)

    def eliminar(self, codigoMascota):
        from tienda_Mascotas.Infraestructura.persistencia_mascota import Persistencia_mascota
        persisten_mascota = Persistencia_mascota()
        persisten_mascota.eliminar_mascota(codigoMascota)

    def actualizarStock(self,cantidad):
        self.cantidad=self.cantidad-cantidad



