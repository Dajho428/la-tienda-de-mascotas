from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Infraestructura.persistencia_accesorio import Persistencia_accesorio
from tienda_Mascotas.Infraestructura.persistencia_alimento import Persistencia_alimento
from tienda_Mascotas.Infraestructura.persistencia_cliente import Persistencia_cliente
from tienda_Mascotas.Infraestructura.persistencia_empleado import Persistencia_empleado
from tienda_Mascotas.Infraestructura.persistencia_mascota import Persistencia_mascota
from tienda_Mascotas.Infraestructura.persistencia_venta import Persistencia_venta


class Controlador_inventario():
    def __init__(self):
        self.saverMascota = Persistencia_mascota()
        self.saverMascota.connect()
        self.saverAccesorios = Persistencia_accesorio()
        self.saverAccesorios.connect()
        self.saverAlimentos = Persistencia_alimento()
        self.saverAlimentos.connect()
        self.saverCliente = Persistencia_cliente()
        self.saverCliente.connect()
        self.saverEmpleado = Persistencia_empleado()
        self.saverEmpleado.connect()
        self.saverVenta = Persistencia_venta()
        self.saverVenta.connect()

    def generarInventario(self):

        inventario = Inventario()
        mascotas = self.saverMascota.consultar_tabla_mascota()
        alimentos = self.saverAlimentos.consultar_tabla_alimento()
        accesorios = self.saverAccesorios.consultar_tabla_accesorio()
        clientes = self.saverCliente.consultar_tabla_cliente()
        empleados = self.saverEmpleado.consultar_tabla_empleado()
        for mascota in mascotas:
            inventario.agregar_mascota(mascota)
        for alimento in alimentos:
            inventario.agregar_alimento(alimento)
        for accesorio in accesorios:
            inventario.agregar_accesorio(accesorio)
        for cliente in clientes:
            inventario.agregar_cliente(cliente)
        for empleado in empleados:
            inventario.agregar_empleado(empleado)
        return inventario
