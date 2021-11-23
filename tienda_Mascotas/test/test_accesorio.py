from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.accesorio import Accesorio
import uuid
import random


def test_buscar_accesorio():
    nombresAccesorios = ['collar', 'juguete de morder', 'abrigo', 'rascador', 'jaula']
    usos = {'collar': ['pasiar', 'identificar'],
            'juguete de morder': ['morder', 'Controlar ansiedad', 'entretenimiento'],
            'abrigo': ['lucir', 'calentar'],
            'rascador': ['rascar'],
            'jaula': ['pasear', 'controlar', 'aislar']}
    inventario = Inventario()
    for nombreAccesorio in nombresAccesorios:
        for uso in usos:
            codigoAccesorio = uuid.uuid4()
            precioAccesorio = random.randint(1000, 10000)
            descripcionAccesorio = "Bonito"
            cantidadAccesorio = random.randint(10, 100)
            inventario.agregar_accesorio(
                Accesorio(codigoAccesorio, nombreAccesorio, cantidadAccesorio, precioAccesorio, descripcionAccesorio,
                          uso))
    especificacion = Especificacion()
    especificacion.agregar_parametro('nombreAccesorio', 'collar')
    for accesorio in inventario.buscar_accesorio(especificacion):
        assert accesorio is not None
    assert len(list(inventario.buscar_accesorio(especificacion))) > 0
    print(list(inventario.buscar_accesorio(especificacion)))
    print(inventario.accesorios)


def test_fuzzing_buscar_accesorio():
    nombresAccesorios = ['collar', 'juguete de morder', 'arbrigo', 'rascador', 'jaula']
    usos = ['rascar', 'morder', 'jugar', 'vestir', 'pasiar']
    cantidad_accesorios = random.randint(100, 100)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_accesorios):
        codigoAccesorio = uuid.uuid4()
        precioAccesorio = random.randint(1000, 10000)
        descripcionAccesorio = "Bonito"
        cantidadAccesorio = random.randint(10, 100)
        nombreAccesorio = random.choice(nombresAccesorios)
        uso = random.choice(usos)
        if i % 10 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('nombreAccesorio', nombreAccesorio)
            especificacion.agregar_parametro('usoAccesorio', uso)
            especificaciones.append(especificacion)
        accesorio = Accesorio(codigoAccesorio, nombreAccesorio, cantidadAccesorio, precioAccesorio,
                              descripcionAccesorio, uso)
        inventario.agregar_accesorio(accesorio)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_accesorio(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_accesorio(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('usoAccesorio', 'volar')
    print(inventario.accesorios)
    assert len(list(inventario.buscar_accesorio(esp_fake))) == 0
    accesorio = Accesorio(codigoAccesorio, nombreAccesorio, cantidadAccesorio, precioAccesorio, descripcionAccesorio,
                          uso)
    try:
        inventario.agregar_accesorio(accesorio)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_buscar_accesorio()
    test_fuzzing_buscar_accesorio()
