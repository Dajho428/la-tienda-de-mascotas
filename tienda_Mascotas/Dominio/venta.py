class Venta():
    def __init__(self, codigoCliente, codigo, nombreProducto, cantidadVenta, precioUnidad, precioTotal):
        self.codigoVenta = None
        self.codigoCliente = codigoCliente
        self.nombreProducto = nombreProducto
        self.codigo = codigo#Codigo Empleado
        self.cantidadVenta = cantidadVenta
        self.precioUnidad = precioUnidad
        self.precioTotal = precioTotal

    def __repr__(self):
        representacion = str(
            self.codigoVenta) + " " + "Venta realizada por el empleado:" + " " + self.codigoEmpleado.nombre + "\n" \
                         + "venta realiza al cliente:" + " " + self.codigoCliente.nombre + " " + "con cedula: " + str(
            self.codigoCliente.cedula) + "\n" \
                         + "producto vendido: " + self.nombreProducto + " " + "cantidad: " + str(
            self.cantidadVenta) + "\n" \
                         + "precio unidad: " + str(self.precioUnidad) + " " + "precio total: " + str(self.precioTotal)
        return representacion

    def cumple(self, especificacion):
        dict_venta = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_venta or dict_venta[k] != especificacion.get_value(k):
                return False
        return True

    def guardar(self, venta,codigoCliente,codigoEmpleado):
        from tienda_Mascotas.Infraestructura.persistenciaVenta import PersistenciaVenta
        persitencia_venta = PersistenciaVenta()
        persitencia_venta.guardar_venta(venta,codigoCliente,codigoEmpleado)
