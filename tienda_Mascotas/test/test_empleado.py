from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.empleado import Empleado
import uuid
import random


def test_buscar_empleado():
    nombresEmpleados = ['Pedro', 'Franco', 'Mauricio', 'Camila', 'Catalina']
    apellidosEmpleados = {
        'Pedro': ['Sanchez', 'Ramirez', 'Pelaez', 'Veracruz', 'Torres', 'Beltran', 'Almehida', 'Gonzales'],
        'Franco': ['Caceres', 'Almehida', 'Marulanda', 'Jimenez', 'Cortazar'],
        'Mauricio': ['Peleaz', 'Arbelaez', 'Guiñez', 'Peralta'],
        'Camila': ['Hincapie', 'Castro', 'Fernandez'],
        'Catalina': ['Giraldo', 'Henao', 'Betancur', 'Barrientos']
    }
    cargos = ['Gerente', 'auxiliar', 'empleado medio tiempo']
    direccionesEmpleados = ['Cra 15 #8-62', 'Cra 18 #4-86', 'Cra 22 #7-25', 'Cra 8 #1-12', 'Cra 20 #8-87']
    correoEmpleado = "correoEmpleado@hotmail.com"
    horarioEmpleado = "10 a 9"
    generosEmpleado = ['Masculino', 'Femenino']
    inventario = Inventario()
    for nombreEmpleado in nombresEmpleados:
        for apellidoEmpleado in apellidosEmpleados[nombreEmpleado]:
            direccionEmpleado = random.choice(direccionesEmpleados)
            codigoEmpleado = uuid.uuid4()
            salarioEmpleado = random.randint(1000, 10000)
            edadEmpleado = random.randint(1, 100)
            cargo = random.choice(cargos)
            cedula = uuid.uuid4()
            generoEmpleado = random.choice(generosEmpleado)
            inventario.agregar_empleado(Empleado(codigoEmpleado, nombreEmpleado, cedula, apellidoEmpleado, cargo,
                                                 salarioEmpleado, generoEmpleado, edadEmpleado, direccionEmpleado,
                                                 correoEmpleado, horarioEmpleado))
    especificacion = Especificacion()
    especificacion.agregar_parametro('apellido', 'Sanchez')
    for empleado in inventario.buscar_empleado(especificacion):
        assert empleado is not None
    assert len(list(inventario.buscar_empleado(especificacion))) > 0
    print(list(inventario.buscar_empleado(especificacion)))
    print(inventario.empleados)


def test_fuzzing_buscar_empleado():
    nombresEmpleados = ['Pedro', 'Franco', 'Mauricio', 'Camila', 'Catalina']
    apellidosEmpleados = {
        'Pedro': ['Sanchez', 'Ramirez', 'Pelaez', 'Veracruz', 'Torres', 'Beltran', 'Almehida', 'Gonzales'],
        'Franco': ['Caceres', 'Almehida', 'Marulanda', 'Jimenez', 'Cortazar'],
        'Mauricio': ['Peleaz', 'Arbelaez', 'Guiñez', 'Peralta'],
        'Camila': ['Hincapie', 'Castro', 'Fernandez'],
        'Catalina': ['Giraldo', 'Henao', 'Betancur', 'Barrientos']
    }
    cargos = ['Gerente', 'auxiliar', 'empleado medio tiempo']
    direccionesEmpleados = ['Cra 15 #8-62', 'Cra 18 #4-86', 'Cra 22 #7-25', 'Cra 8 #1-12', 'Cra 20 #8-87']
    correoEmpleado = "correoEmpleado@hotmail.com"
    horarioEmpleado = "10 a 9"
    generosEmpleado = ['Masculino', 'Femenino']
    cantidad_empleados = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_empleados):
        direccionEmpleado = random.choice(direccionesEmpleados)
        codigoEmpleado = uuid.uuid4()
        salarioEmpleado = random.randint(1000, 10000)
        edadEmpleado = random.randint(1, 100)
        cedula = uuid.uuid4()
        generoEmpleado = random.choice(generosEmpleado)
        cargo = random.choice(cargos)
        nombreEmpleado = random.choice(nombresEmpleados)
        apellidoEmpleado = random.choice(nombreEmpleado)
        if i % 10 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('nombre', nombreEmpleado)
            especificacion.agregar_parametro('apellido', apellidoEmpleado)
            especificaciones.append(especificacion)
        empleado = Empleado(codigoEmpleado, nombreEmpleado, cedula, apellidoEmpleado, cargo,
                            salarioEmpleado, generoEmpleado, edadEmpleado, direccionEmpleado,
                            correoEmpleado, horarioEmpleado)
        inventario.agregar_empleado(empleado)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_empleado(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_empleado(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('nombre', 'hola hola')
    print(inventario.empleados)
    assert len(list(inventario.buscar_empleado(esp_fake))) == 0
    empleado = Empleado(codigoEmpleado, nombreEmpleado, cedula, apellidoEmpleado, cargo,
                        salarioEmpleado, generoEmpleado, edadEmpleado, direccionEmpleado,
                        correoEmpleado, horarioEmpleado)
    try:
        inventario.agregar_empleado(empleado)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_buscar_empleado()
    test_fuzzing_buscar_empleado()
