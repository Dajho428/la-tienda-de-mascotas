from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.cliente import Cliente
import uuid
import random


def test_buscar_cliente():
    nombresClientes = ['Pedro', 'Franco', 'Mauricio', 'Camila', 'Catalina']
    apellidosClientes = {
        'Pedro': ['Sanchez', 'Ramirez', 'Pelaez', 'Veracruz', 'Torres', 'Beltran', 'Almehida', 'Gonzales'],
        'Franco': ['Caceres', 'Almehida', 'Marulanda', 'Jimenez', 'Cortazar'],
        'Mauricio': ['Peleaz', 'Arbelaez', 'Guiñez', 'Peralta'],
        'Camila': ['Hincapie', 'Castro', 'Fernandez'],
        'Catalina': ['Giraldo', 'Henao', 'Betancur', 'Barrientos']
    }
    direccionesClientes = ['Cra 15 #8-62', 'Cra 18 #4-86', 'Cra 22 #7-25', 'Cra 8 #1-12', 'Cra 20 #8-87']
    correoCliente = "correoCliente@hotmail.com"
    tiempoCliente = "4 años"
    generosClientes = ['Masculino', 'Femenino']
    inventario = Inventario()
    for nombreCliente in nombresClientes:
        for apellidoCliente in apellidosClientes[nombreCliente]:
            direccionCliente = random.choice(direccionesClientes)
            codigoCliente = uuid.uuid4()
            edadCliente = random.randint(1, 100)
            cedula = uuid.uuid4()
            generoCliente = random.choice(generosClientes)
            inventario.agregar_cliente(
                Cliente(codigoCliente, nombreCliente, apellidoCliente, cedula, generoCliente, direccionCliente,
                        correoCliente, edadCliente, tiempoCliente))
    especificacion = Especificacion()
    especificacion.agregar_parametro('apellido', 'Sanchez')
    for cliente in inventario.buscar_cliente(especificacion):
        assert cliente is not None
    assert len(list(inventario.buscar_cliente(especificacion))) > 0
    print(list(inventario.buscar_cliente(especificacion)))
    print(inventario.clientes)


def test_fuzzing_buscar_cliente():
    nombresClientes = ['Pedro', 'Franco', 'Mauricio', 'Camila', 'Catalina']
    apellidosClientes = {
        'Pedro': ['Sanchez', 'Ramirez', 'Pelaez', 'Veracruz', 'Torres', 'Beltran', 'Almehida', 'Gonzales'],
        'Franco': ['Caceres', 'Almehida', 'Marulanda', 'Jimenez', 'Cortazar'],
        'Mauricio': ['Peleaz', 'Arbelaez', 'Guiñez', 'Peralta'],
        'Camila': ['Hincapie', 'Castro', 'Fernandez'],
        'Catalina': ['Giraldo', 'Henao', 'Betancur', 'Barrientos']
    }
    direccionesClientes = ['Cra 15 #8-62', 'Cra 18 #4-86', 'Cra 22 #7-25', 'Cra 8 #1-12', 'Cra 20 #8-87']
    correoCliente = "correoCliente@hotmail.com"
    generosClientes = ['Masculino', 'Femenino']
    cantidad_clientes = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_clientes):
        direccionCliente = random.choice(direccionesClientes)
        codigoCliente = uuid.uuid4()
        edadCliente = random.randint(1, 100)
        cedula = uuid.uuid4()
        generoCliente = random.choice(generosClientes)
        nombreCliente = random.choice(nombresClientes)
        apellidoCliente = random.choice(apellidosClientes[nombreCliente])
        tiempoCliente = "4 años"
        if i % 10 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('nombre', nombreCliente)
            especificacion.agregar_parametro('apellido', apellidoCliente)
            especificaciones.append(especificacion)
        cliente = Cliente(codigoCliente, nombreCliente, apellidoCliente, cedula, generoCliente, direccionCliente,
                          correoCliente, edadCliente, tiempoCliente)
        inventario.agregar_cliente(cliente)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_cliente(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_cliente(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('nombre', 'hola hola')
    print(inventario.clientes)
    assert len(list(inventario.buscar_cliente(esp_fake))) == 0
    cliente = Cliente(codigoCliente, nombreCliente, apellidoCliente, cedula, generoCliente, direccionCliente,
                      correoCliente, edadCliente, tiempoCliente)
    try:
        inventario.agregar_cliente(cliente)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_buscar_cliente()
    test_fuzzing_buscar_cliente()
