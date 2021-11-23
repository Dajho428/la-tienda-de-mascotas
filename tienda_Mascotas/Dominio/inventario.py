from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.venta import Venta


class Inventario:
    def __init__(self):
        self.mascotas = []
        self.clientes = []
        self.empleados = []
        self.alimentos = []
        self.accesorios = []
        self.ventas = []

    def agregar_mascota(self, mascota):
        if type(mascota) == Mascota:
            espec = Especificacion()
            espec.agregar_parametro('codigoMascota', mascota.codigoMascota)
            if len(list(self.buscar_mascota(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('la mascota ya existe')

    def buscar_mascota(self, especificacion):
        for g in self.mascotas:
            if g.cumple(especificacion):
                yield g

    def agregar_cliente(self, cliente):
        if type(cliente) == Cliente:
            espec = Especificacion()
            especCedula = Especificacion()
            espec.agregar_parametro('codigoCliente', cliente.codigoCliente)
            especCedula.agregar_parametro('cedula', cliente.cedula)
            if len(list(self.buscar_cliente(espec))) == 0 and len(list(self.buscar_cliente(especCedula))) == 0:
                self.clientes.append(cliente)
            else:
                raise Exception('El cliente ya existe')

    def buscar_cliente(self, especificacion):
        for g in self.clientes:
            if g.cumple(especificacion):
                yield g

    def agregar_empleado(self, empleado):
        if type(empleado) == Empleado:
            espec = Especificacion()
            especCedula = Especificacion()
            espec.agregar_parametro('codigo', empleado.codigo)
            especCedula.agregar_parametro('cedula', empleado.cedula)
            if len(list(self.buscar_empleado(espec))) == 0 and len(list(self.buscar_empleado(especCedula))) == 0:
                self.empleados.append(empleado)
            else:
                raise Exception('El empleado ya existe')

    def buscar_empleado(self, especificacion):
        for g in self.empleados:
            if g.cumple(especificacion):
                yield g

    def agregar_alimento(self, alimento):
        if type(alimento) == Alimento:
            espec = Especificacion()
            espec.agregar_parametro('codigoAlimento', alimento.codigoAlimento)
            if len(list(self.buscar_alimento(espec))) == 0:
                self.alimentos.append(alimento)
            else:
                raise Exception('El alimento ya existe')

    def buscar_alimento(self, especificacion):
        for g in self.alimentos:
            if g.cumple(especificacion):
                yield g

    def agregar_accesorio(self, accesorio):
        if type(accesorio) == Accesorio:
            espec = Especificacion()
            espec.agregar_parametro('codigoAccesorio', accesorio.codigoAccesorio)
            if len(list(self.buscar_accesorio(espec))) == 0:
                self.accesorios.append(accesorio)
            else:
                raise Exception('El accesorio ya existe')

    def buscar_accesorio(self, especificacion):
        for g in self.accesorios:
            if g.cumple(especificacion):
                yield g

    def agregar_venta(self, venta):
        if type(venta) == Venta:
            espec = Especificacion()
            espec.agregar_parametro('codigoVenta', venta.codigoVenta)
            if len(list(self.buscar_venta(espec))) == 0:
                self.ventas.append(venta)
            else:
                raise Exception('La venta ya existe')

    def buscar_venta(self, especificacion):
        for g in self.ventas:
            if g.cumple(especificacion):
                yield g
