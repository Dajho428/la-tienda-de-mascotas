from tienda_Mascotas.Dominio.especificacion import Especificacion
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.mascota import Mascota
import uuid
import random


def test_buscar_mascota():
    tipoMascotas = ['perro', 'gato', 'conejo', 'hamster', 'loro']
    razas = {
        'perro': ['pastor aleman', 'labrador retriver', 'husky siberano', 'bulldog', 'chihuahua', 'pitbull'],
        'gato': ['gato persa', 'bengala', 'siames', 'gato esfinge', 'siberiano', 'angora'],
        'conejo': ['holandes enano', 'mini lop', 'californiano', 'mini rex', 'azul de viena'],
        'hamster': ['ruso', 'roborowski', 'sirio', 'chino', 'enano de campbell'],
        'loro': ['cacatuoidea', 'periquitos', 'cotorras', 'papagayos', 'Amazonas']
    }
    nombresMascotas = ['Zeus', 'Cati', 'Negrito', 'Bigotes', 'Bolita de algodon', 'Pericles', 'Capitan', 'Plumas']
    inventario = Inventario()
    for tipoMascota in tipoMascotas:
        for raza in razas[tipoMascota]:
            nombreMascota = random.choice(nombresMascotas)
            precio = random.randint(10000, 100000)
            cantidadMascota = random.randint(10, 50)
            edad = random.randint(1, 20)
            codigoMascota = uuid.uuid4()
            inventario.agregar_mascota(
                Mascota(codigoMascota, tipoMascota, raza, nombreMascota, edad, precio, cantidadMascota)
            )
    especificacion = Especificacion()
    especificacion.agregar_parametro('tipoMascota', 'perro')
    for mascota in inventario.buscar_mascota(especificacion):
        assert mascota is not None
    assert len(list(inventario.buscar_mascota(especificacion))) > 0
    print(list(inventario.buscar_mascota(especificacion)))
    print(inventario.mascotas)


def test_fuzzing_buscar_mascota():
    tipoMascotas = ['perro', 'gato', 'conejo', 'hamster', 'loro']
    razas = {
        'perro': ['pastor aleman', 'labrador retriver', 'husky siberano', 'bulldog', 'chihuahua', 'pitbull'],
        'gato': ['gato persa', 'bengala', 'siames', 'gato esfinge', 'siberiano', 'angora'],
        'conejo': ['holandes enano', 'mini lop', 'californiano', 'mini rex', 'azul de viena'],
        'hamster': ['ruso', 'roborowski', 'sirio', 'chino', 'enano de campbell'],
        'loro': ['cacatuoidea', 'periquitos', 'cotorras', 'papagayos', 'Amazonas']
    }
    nombresMascotas = ['Zeus', 'Cati', 'Negrito', 'Bigotes', 'Bolita de algodon', 'Pericles', 'Capitan', 'Plumas']
    cantidad_mascotas = random.randint(100, 100)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_mascotas):
        tipoMascota = random.choice(tipoMascotas)
        raza = random.choice(razas[tipoMascota])
        nombreMascota = random.choice(nombresMascotas)
        precio = random.randint(10000, 100000)
        cantidadMascota = random.randint(10, 50)
        edad = random.randint(1, 20)
        codigoMascota = uuid.uuid4()
        if i % 10 == 0:
            especificacion = Especificacion()
            especificacion.agregar_parametro('tipoMascota', tipoMascota)
            especificacion.agregar_parametro('nombre', nombreMascota)
            especificaciones.append(especificacion)
        mascota = Mascota(codigoMascota, tipoMascota, raza, nombreMascota, edad, precio, cantidadMascota)
        inventario.agregar_mascota(mascota)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_mascota(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_mascota(esp)))
    esp_fake = Especificacion()
    esp_fake.agregar_parametro('tipoMascota', 'ballena')
    print(inventario.mascotas)
    assert len(list(inventario.buscar_mascota(esp_fake))) == 0
    mascota = Mascota(codigoMascota, tipoMascota, raza, nombreMascota, edad, precio, cantidadMascota)
    try:
        inventario.agregar_mascota(mascota)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_buscar_mascota()
    test_fuzzing_buscar_mascota()
