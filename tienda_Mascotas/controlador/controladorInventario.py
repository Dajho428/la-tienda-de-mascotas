from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Infraestructura.persistenciaAccesorio import PersistenciaAccesorio
from tienda_Mascotas.Infraestructura.persistenciaAlimento import PersistenciaAlimento
from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente
from tienda_Mascotas.Infraestructura.persistenciaEmpleado import PersistenciaEmpleado
from tienda_Mascotas.Infraestructura.persistenciaMascota import PersistenciaMascota
from tienda_Mascotas.Infraestructura.persistenciaVenta import PersistenciaVenta


class ControladorInventario():
    def __init__(self):
        self.saverMascota = PersistenciaMascota()
        self.saverMascota.connect()
        self.saverAccesorios = PersistenciaAccesorio()
        self.saverAccesorios.connect()
        self.saverAlimentos = PersistenciaAlimento()
        self.saverAlimentos.connect()
        self.saverCliente = PersistenciaCliente()
        self.saverCliente.connect()
        self.saverEmpleado = PersistenciaEmpleado()
        self.saverEmpleado.connect()
        self.saverVenta = PersistenciaVenta()
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
