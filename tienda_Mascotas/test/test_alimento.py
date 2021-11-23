from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.alimento import Alimento
import uuid
import random


def test_buscar_alimento():
    tipoAlimentos = ['perro', 'gato', 'conejo', 'hamster', 'loro']
    nombreProductos = {
        'perro': ['dogchao', 'perritos', 'dusky', 'happyfood', 'dogyomo', 'My dog food'],
        'gato': ['cat food', 'whiskas', 'happy food cat', 'cat yomy', 'happy cat ', 'My cat food'],
        'conejo': ['la comida del conejo', 'Alimento conejo', 'rabbit food', 'rabbit yomi', 'delicias del conejo'],
        'hamster': ['la comida del hamster', 'alimento hamster', 'Hamster yomi', 'las delicias del hamster'],
        'loro': ['alpiste', 'semillas', 'comida Condoritos', 'lo mejor del condorito', 'comida de aves']
    }
    inventario = Inventario()
    for tipoAlimento in tipoAlimentos:
        for nombreProducto in nombreProductos[tipoAlimento]:
            cantidadAlimento = random.randint(10, 100)
            cantidadContenido = random.randint(500, 1000)
            precio = random.randint(1000, 10000)
            codigoAlimento = uuid.uuid4()
            inventario.agregar_alimento(
                Alimento(codigoAlimento, tipoAlimento, nombreProducto, cantidadAlimento, cantidadContenido, precio))
    especificacion = Especificacion()
    especificacion.agregar_parametro('tipoAlimento', 'perro')
    for alimento in inventario.buscar_alimento(especificacion):
        assert alimento is not None
    assert len(list(inventario.buscar_alimento(especificacion))) > 0
    print(list(inventario.buscar_alimento(especificacion)))
    print(inventario.alimentos)


def test_fuzzing_buscar_alimento():
    tipoAlimentos = ['perro', 'gato', 'conejo', 'hamster', 'loro']
    nombreProductos = {
        'perro': ['dogchao', 'perritos', 'dusky', 'happyfood', 'dogyomo', 'My dog food'],
        'gato': ['cat food', 'whiskas', 'happy food cat', 'cat yomy', 'happy cat ', 'My cat food'],
        'conejo': ['la comida del conejo', 'Alimento conejo', 'rabbit food', 'rabbit yomi', 'delicias del conejo'],
        'hamster': ['la comida del hamster', 'alimento hamster', 'Hamster yomi', 'las delicias del hamster'],
        'loro': ['alpiste', 'semillas', 'comida Condoritos', 'lo mejor del condorito', 'comida de aves']
    }
    cantidad_alimentos = random.randint(100, 100)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_alimentos):
        cantidadAlimento = random.randint(10, 50)
        cantidadContenido = random.randint(500, 1000)
        precio = random.randint(1000, 10000)
        codigoAlimento = uuid.uuid4()
        tipoAlimento = random.choice(tipoAlimentos)
        nombreProducto = random.choice(nombreProductos[tipoAlimento])
        if i % 10 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('tipoAlimento', tipoAlimento)
            especificacion.agregar_parametro('nombreProducto', nombreProducto)
            especificaciones.append(especificacion)
        alimento = Alimento(codigoAlimento, tipoAlimento, nombreProducto, cantidadAlimento, cantidadContenido, precio)
        inventario.agregar_alimento(alimento)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_alimento(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_alimento(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('tipoAlimento', 'ballena')
    print(inventario.alimentos)
    assert len(list(inventario.buscar_alimento(esp_fake))) == 0
    alimento = Alimento(codigoAlimento, tipoAlimento, nombreProducto, cantidadAlimento, cantidadContenido, precio)
    try:
        inventario.agregar_alimento(alimento)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_buscar_alimento()
    test_fuzzing_buscar_alimento()
