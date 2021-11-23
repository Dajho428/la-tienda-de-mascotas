import sqlite3

from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.venta import Venta


class PersistenciaVenta:
    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_mascotas.sqlite")

    def connect(self):
        self.__crear_tabla_venta()

    def __crear_tabla_venta(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE VENTA(codigoVenta Integer PRIMARY KEY Autoincrement , cantidadVenta Integer," \
                    " precioUnidad float, precioTotal float,nombreProducto text, codigoCliente text," \
                    " codigo text,FOREIGN KEY(codigoCliente) references CLIENTE(codigoCliente)," \
                    "FOREIGN KEY(codigo) references EMPLEADO(codigo)) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_venta(self, venta: Venta,codigoCliente,codigoEmpleado):
        cursor = self.con.cursor()
        query = "insert into VENTA( cantidadVenta ," \
                " precioUnidad , precioTotal ,nombreProducto ," \
                " codigoCliente,codigo) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (venta.cantidadVenta, venta.precioUnidad, venta.precioTotal,
                               venta.nombreProducto, str(codigoCliente), str(codigoEmpleado)))
        self.con.commit()

    def consultar_tabla_venta(self, inventario: Inventario):
        cursor = self.con.cursor()
        venta = cursor.execute(
            "select codigoVenta,cantidadVenta,precioUnidad,precioTotal,"
            "nombreProducto, codigoCliente,codigo"
            " from VENTA")
        ventas = []
        for codigoVenta, cantidadVenta, precioUnidad, precioTotal, \
            nombreProducto, codigoCliente, codigo in venta:
            espcCliente = Especificacion()
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            espcEmpleado = Especificacion()
            espcEmpleado.agregar_parametro("codigo", codigo)
            clientes = list(inventario.buscar_cliente(espcCliente))
            empleados = list(inventario.buscar_empleado(espcEmpleado))
            venta_cargada = Venta(clientes[0], empleados[0], nombreProducto, cantidadVenta, precioUnidad, precioTotal)
            venta_cargada.codigoVenta = codigoVenta
            ventas.append(venta_cargada)
        return ventas

    def cargar_venta(self, codigoVenta):
        cursor = self.con.cursor()
        query = "SELECT codigoVenta ,cantidadVenta,precioUnidad,precioTotal,nombreProducto, codigoCliente,codigo FROM VENTA WHERE codigoVenta=?"
        ventas = cursor.execute(query, (codigoVenta,))
        venta_encontrada = None
        for codigoVenta, cantidadVenta, precioUnidad, precioTotal, nombreProducto, codigoCliente, codigo in ventas:
            venta_encontrada = Venta(codigoVenta, cantidadVenta, precioUnidad, precioTotal, nombreProducto,
                                     codigoCliente, codigo)
        return venta_encontrada
