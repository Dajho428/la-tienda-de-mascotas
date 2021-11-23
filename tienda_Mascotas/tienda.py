from tienda_Mascotas.Dominio.mascota import Mascota
from tienda_Mascotas.Dominio.inventario import Inventario
from tienda_Mascotas.Dominio.alimento import Alimento
from tienda_Mascotas.Dominio.accesorio import Accesorio
from tienda_Mascotas.Dominio.cliente import Cliente
from tienda_Mascotas.Dominio.empleado import Empleado
from tienda_Mascotas.Dominio.venta import Venta

from tienda_Mascotas.Infraestructura.persistenciaAccesorio import PersistenciaAccesorio
from tienda_Mascotas.Infraestructura.persistenciaAlimento import PersistenciaAlimento
from tienda_Mascotas.Infraestructura.persistenciaCliente import PersistenciaCliente
from tienda_Mascotas.Infraestructura.persistenciaEmpleado import PersistenciaEmpleado
from tienda_Mascotas.Infraestructura.persistenciaMascota import PersistenciaMascota
from tienda_Mascotas.Dominio.especificacion import Especificacion
import requests
from tienda_Mascotas.Infraestructura.configuracion import Configuracion
import os

from tienda_Mascotas.Infraestructura.persistenciaVenta import PersistenciaVenta


class Tienda():

    def generarInventario(self):
        saverMascota = PersistenciaMascota()
        saverMascota.connect()
        saverAccesorios = PersistenciaAccesorio()
        saverAccesorios.connect()
        saverAlimentos = PersistenciaAlimento()
        saverAlimentos.connect()
        saverCliente = PersistenciaCliente()
        saverCliente.connect()
        saverEmpleado = PersistenciaEmpleado()
        saverEmpleado.connect()
        saverVenta = PersistenciaVenta()
        saverVenta.connect()
        inventario = Inventario()
        mascotas = saverMascota.consultar_tabla_mascota()
        alimentos = saverAlimentos.consultar_tabla_alimento()
        accesorios = saverAccesorios.consultar_tabla_accesorio()
        clientes = saverCliente.consultar_tabla_cliente()
        empleados = saverEmpleado.consultar_tabla_empleado()
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


if __name__ == '__main__':

    """Primero declaramos la persistencia y luego utilizamos el metodo saver.connect cuando iniciamos la aplicacion
    esto genera la base de datos sqlite y las tablas de la entitades que necesitamos con sus atributos"""

    saverMascota = PersistenciaMascota()
    saverMascota.connect()
    saverAccesorios = PersistenciaAccesorio()
    saverAccesorios.connect()
    saverAlimentos = PersistenciaAlimento()
    saverAlimentos.connect()
    saverCliente = PersistenciaCliente()
    saverCliente.connect()
    saverEmpleado = PersistenciaEmpleado()
    saverEmpleado.connect()
    saverVenta = PersistenciaVenta()
    saverVenta.connect()

    # def actualizarMascota(inventario):
    #     espec = Especificacion()
    #     mascota = Mascota("123", "Gato", "Persa", "Michi", 1, 150000.0, 10)
    #     espec.agregar_parametro("codigoMascota", mascota.codigoMascota)
    #     mascota_aux = list(inventario.buscar_mascota(espec))
    #     mascota._actualizar(mascota_aux, mascota_aux.codigoMascota)

    # Metodo generar configuracion, el cual trae la configuracion que esta guardada en archivo plano json

    """En el metodo generarInventario cargamos los datos que estan guardados tanto en archivos planos json y 
    los que estan guardados en base de datos sqlite para utilizarlos en uno solo, en este caso la clase inventario"""


    def generarInventario():
        inventario = Inventario()
        mascotas = saverMascota.consultar_tabla_mascota()
        alimentos = saverAlimentos.consultar_tabla_alimento()
        accesorios = saverAccesorios.consultar_tabla_accesorio()
        clientes = saverCliente.consultar_tabla_cliente()
        empleados = saverEmpleado.consultar_tabla_empleado()
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
        ventas = saverVenta.consultar_tabla_venta(inventario)
        for venta in ventas:
            inventario.agregar_venta(venta)

        return inventario


    """En el metodo agregar informacion, le damos al usuario una seria de opciones dadas por un while,
    y dependiendo la que elija, lo lleva a llenar los datos de la clase que escogio.Dependiendo de la configuracion
    esta lo guarda como un archivo plano json o base sqlite"""


    def agregar_informacion():
        inventario = generarInventario()
        ans = True
        while ans:
            print("""
        BIENVENIDO A LA TIENDA DE MASCOTAS, ELIGE ENTRE NUESTRAS OPCIONES,
        PARA MANTENER LA TIENDA ORDENADA Y REGISTRAR SUS ELEMENTOS
        
        1.Agregar nueva mascota.
        2.Agregar nuevo alimento de mascotas.
        3.Agregar nuevo accesorio de mascotas.
        4.Agregar nuevo cliente.
        5.Agregar nuevo empleado.
        6.Regresar al menu principal.
        """)
            ans = input("Cual de las opciones quieres?: ")
            if ans == "1":
                codigoMascota = str(input("Ingrse el codigo de la mascota:"))
                tipo_mascota = str(input("Ingrese el de que tipo de animal que es la mascota:"))
                raza = str(input("Ingrese la raza de la mascota:"))
                nombre = str(input("Ingres el nombre provicional de la mascota:"))
                edad = int(input("Ingrese la edad que tiene la mascota:"))
                precioMascota = float(input("Ingrese el precio de la mascota:"))
                cantidadMascota = int(input("Ingrese la cantidad de mascotas que hay con estas caracteristicas:"))
                mascota = Mascota(codigoMascota, tipo_mascota, raza, nombre, edad, precioMascota, cantidadMascota)
                try:
                    inventario.agregar_mascota(mascota)
                    url = "http://localhost:2020/mascota_guardar/"
                    body = {
                        "codigoMascota": codigoMascota,
                        "tipoMascota": tipo_mascota,
                        "raza": raza,
                        "edad": edad,
                        "nombre": nombre,
                        "cantidad": cantidadMascota,
                        "precio": precioMascota,
                    }
                    print("\n Se agrego la mascota con exito en bd")
                    response = requests.request("POST", url, data=body)
                    print(response.status_code)
                except Exception as ex:
                    print(ex)


            elif ans == "2":
                codigoAlimento = str(input("Ingrse el codigo del alimento:"))
                tipo_alimento = str(input("Ingrese el tipo de alimento que quiere registrar:"))
                nombreAlimento = str(input("Ingrese el nombre del producto::"))
                cantidadAlimento = int(input("Ingrese numero de existencias del articulo:"))
                cantidadContenido = int(input("Ingrese la cantidad de contenido del producto(en gramos):"))
                precioAlimento = float(input("Ingrese el precio del producto alimenticio:"))
                alimento = Alimento(codigoAlimento, tipo_alimento, nombreAlimento, cantidadAlimento, cantidadContenido,
                                    precioAlimento)
                try:
                    inventario.agregar_alimento(alimento)
                    url = "http://localhost:2020/alimento_guardar/"
                    body = {
                        "codigoAlimento": codigoAlimento,
                        "tipoAlimento": tipo_alimento,
                        "nombre": nombreAlimento,
                        "cantidadAlimento": cantidadAlimento,
                        "cantidadContenido": cantidadContenido,
                        "precio": precioAlimento,
                    }
                    print("\n Se agrego el alimento con exito en bd")
                    response = requests.request("POST", url, data=body)
                    print(response.status_code)
                except Exception as ex:
                    print(ex)
            elif ans == "3":
                codigoAccesorio = str(input("Ingrese el codigo del accesorio:"))
                nombreAccesorio = str(input("Ingrese el nombre del accesorio:"))
                descripcionAccesorio = str(input("Ingrese una descripcion corta del accesorio:"))
                usoAccesorio = str(input("Ingrese el uso del accesorio:"))
                precioAccesorio = float(input("Ingrese el precio del accesorio:"))
                cantidadAccesorio = int(input("Ingrese la cantidad de existencias del accesorio:"))
                accesorio = Accesorio(codigoAccesorio, nombreAccesorio,precioAccesorio,cantidadAccesorio,
                                      descripcionAccesorio, usoAccesorio )
                try:
                    inventario.agregar_accesorio(accesorio)
                    url = "http://localhost:2020/accesorio_guardar/"
                    body = {
                        "codigoAccesorio": codigoAccesorio,
                        "nombre": nombreAccesorio,
                        "cantidad": cantidadAccesorio,
                        "precio": precioAccesorio,
                        "descripcionAccesorio": descripcionAccesorio,
                        "usoAccesorio": usoAccesorio,
                    }
                    response = requests.request("POST", url, data=body)
                    print(response.status_code)
                    print("\n Se agrego el accesorio de mascotas con exito en bd")
                except Exception as ex:
                    print(ex)

            elif ans == "4":
                registrar_cliente()
                # codigoCliente = str(input("Ingrse el codigo del cliente:"))
                # nombreCliente = str(input("Ingrese el nombre del cliente:"))
                # cedulaCliente = str(input("Ingrese la cedula del cliente:"))
                # apellidoCliente = str(input("Ingrese el apellido del cliente:"))
                # generoCliente = str(input("Ingrese el genero del cliente:"))
                # edadCliente = int(input("Ingrese la edad del cliente"))
                # direccionCliente = str(input("Ingrese la direccion de residencia del cliente:"))
                # correoCliente = str(input("Ingrese el correo de contacto del cliente:"))
                # tiempoCliente = str(input("Ingrese el tiempo que lleva la persona siendo su cliente:"))
                # cliente = Cliente(codigoCliente, nombreCliente, apellidoCliente, cedulaCliente, generoCliente
                #                   , direccionCliente, correoCliente, edadCliente, tiempoCliente)
                # try:
                #     inventario.agregar_cliente(cliente)
                #     url = "http://localhost:2020/cliente_guardar/"
                #     body = {
                #         "codigoCliente": codigoCliente,
                #         "nombre": nombreCliente,
                #         "apellido": apellidoCliente,
                #         "cedula": cedulaCliente,
                #         "genero": generoCliente,
                #         "direccion": direccionCliente,
                #         "correo": correoCliente,
                #         "edad": edadCliente,
                #         "tiempoCliente": tiempoCliente,
                #     }
                #     response = requests.request("POST", url, data=body)
                #     print(response.status_code)
                #     print("\n Se agrego el nuevo cliente con exito en bd")
                # except Exception as ex:
                #     print(ex)

            elif ans == "5":
                codigoEmpleado = str(input("Ingrse el codigo del empleado:"))
                nombreEmpleado = str(input("Ingrese el nombre del empleado:"))
                cedulaEmpleado = str(input("Ingrese la cedula del empleado:"))
                apellidoEmpleado = str(input("Ingrese el apellido del empleado:"))
                generoEmpleado = str(input("Ingrese el genero del empleado:"))
                edadEmpleado = int(input("Ingrese la edad del empleado:"))
                direccionEmpleado = str(input("Ingrese la direccion de residencia del empleado:"))
                correoEmpleado = str(input("Ingrese el correo de contacto del empledo:"))
                cargoEmpleado = str(input("Ingrese el cargo que tiene el empleado en la tienda:"))
                horarioEmpleado = str(input("Ingrese el horario que cumple el empleado:"))
                salarioEmpleado = str(input("Ingrese el salario que tiene el empleado:"))
                empleado = Empleado(codigoEmpleado, nombreEmpleado, cedulaEmpleado, apellidoEmpleado, cargoEmpleado,
                                    salarioEmpleado, generoEmpleado,
                                    edadEmpleado, direccionEmpleado, correoEmpleado, horarioEmpleado)
                try:
                    inventario.agregar_empleado(empleado)
                    url = "http://localhost:2020/empleado_guardar/"
                    body = {
                        "codigo": codigoEmpleado,
                        "nombre": nombreEmpleado,
                        "apellido": apellidoEmpleado,
                        "cedula": cedulaEmpleado,
                        "genero": generoEmpleado,
                        "direccion": direccionEmpleado,
                        "correo": correoEmpleado,
                        "edad": edadEmpleado,
                        "cargo": cargoEmpleado,
                        "salario": salarioEmpleado,
                        "horario": horarioEmpleado,
                    }
                    response = requests.request("POST", url, data=body)
                    print(response.status_code)
                    print("\n Se agrego el nuevo empleado con exito en bd")
                except Exception as ex:
                    print(ex)

            elif ans == "6":
                ans = False
            elif ans != "":
                print("\n Opcion no es valida, verifique el numero ingresado")


    def registrar_cliente():
        inventario = generarInventario()
        codigoCliente = str(input("Ingrse el codigo del cliente:"))
        nombreCliente = str(input("Ingrese el nombre del cliente:"))
        apellidoCliente = str(input("Ingrese el apellido del cliente:"))
        cedulaCliente = str(input("Ingrese la cedula del cliente:"))
        generoCliente = str(input("Ingrese el genero del cliente: "))
        edadCliente = int(input("Ingrese la edad del cliente: "))
        direccionCliente = str(input("Ingrese la direccion de residencia del cliente:"))
        correoCliente = str(input("Ingrese el correo de contacto del cliente:"))
        tiempoCliente = str(input("Ingrese el tiempo que lleva la persona siendo su cliente:"))
        cliente = Cliente(codigoCliente, nombreCliente, apellidoCliente, cedulaCliente, generoCliente
                          , direccionCliente, correoCliente, edadCliente, tiempoCliente)
        try:
            inventario.agregar_cliente(cliente)
            url = "http://localhost:2020/cliente_guardar/"
            body = {
                "codigoCliente": codigoCliente,
                "nombre": nombreCliente,
                "apellido": apellidoCliente,
                "cedula": cedulaCliente,
                "genero": generoCliente,
                "direccion": direccionCliente,
                "correo": correoCliente,
                "edad": edadCliente,
                "tiempoCliente": tiempoCliente,
            }
            response = requests.request("POST", url, data=body)
            print(response.status_code)
            print("\n Se agrego el nuevo cliente con exito en bd")
        except Exception as ex:
            print(ex)
"""En el metodo buscar informacion el usuario se le da un menu de opciones para buscar la clase que quiera,y por 
los atributos que quiera. Dependiendo de la clase que elija, se despliegan una serie de caracteristicas. El usuario
escoje el numero de caracteristicas, el numero de referencia a la caracteristica y por ultimo el valor de esta,
luego de esto se visualiza la representacion del objeto en caso de que exista"""


def actualizarInformacion():
    inventario = generarInventario()
    ansAct = True
    while ansAct:
        print("""
        BIENVENIDO A LA TIENDA DE MASCOTAS, ELIGE ENTRE NUESTRAS OPCIONES,
        PARA MANTENER LA TIENDA ORDENADA Y ACTUALIZAR SUS ELEMENTOS
        
        1.actualizar mascota.
        2.actualizar alimento de mascotas.
        3.actualizar accesorio de mascotas.
        4.actualizar cliente.
        5.actualizar empleado.
        6.Regresar al menu principal.
        """)
        ansAct = input("Cual de las opciones quieres?: ")
        if ansAct == "1":
            codigoMascota = input("Ingrese el codigo de la mascota que quiere editar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoMascota", codigoMascota)
            mascotas = list(inventario.buscar_mascota(espc))
            print(len(mascotas))
            atributos = {}
            atributos["codigoMascota"] = codigoMascota
            atributos["tipoMascota"] = mascotas[0].tipoMascota
            atributos["raza"] = mascotas[0].raza
            atributos["edad"] = mascotas[0].edad
            atributos["nombre"] = mascotas[0].nombre
            atributos["cantidad"] = mascotas[0].cantidad
            atributos["precio"] = mascotas[0].precio
            cantidadAtributos = int(input("Ingrese la cantidad de caracteristicas de la mascota que quiere editar:"))
            for i in range(0, cantidadAtributos):
                caracteristica = input("Ingrese la caracteristica que quiere editar:")
                valor = input("Ingrese el valor por el cual quiere reemplazarla:")
                atributos[caracteristica] = valor
            url = "http://localhost:2020/mascota_actualizar/" + codigoMascota
            body = {

                "tipoMascota": atributos["tipoMascota"],
                "raza": atributos["raza"],
                "edad": atributos["edad"],
                "nombre": atributos["nombre"],
                "cantidad": atributos["cantidad"],
                "precio": atributos["precio"],

            }
            response = requests.request("PUT", url, data=body)
            print(response.status_code)
        elif ansAct == "2":
            codigoAlimento = input("Ingrese el codigo del alimento que quiere editar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoAlimento", codigoAlimento)
            alimento = list(inventario.buscar_alimento(espc))
            print(len(alimento))
            atributos = {}
            atributos["codigoAlimento"] = codigoAlimento
            atributos["tipoAlimento"] = alimento[0].tipoAlimento
            atributos["nombreProducto"] = alimento[0].nombreProducto
            atributos["cantidadAlimento"] = alimento[0].cantidadAlimento
            atributos["cantidadContenido"] = alimento[0].cantidadContenido
            atributos["precio"] = alimento[0].precio
            cantidadAtributos = int(input("Ingrese la cantidad de caracteristicas del alimento que quiere editar:"))
            for i in range(0, cantidadAtributos):
                caracteristica = input("Ingrese la caracteristica que quiere editar:")
                valor = input("Ingrese el valor por el cual quiere reemplazarla:")
                atributos[caracteristica] = valor
            url = "http://localhost:2020/alimento_actualizar/" + codigoAlimento
            body = {
                "tipoAlimento": atributos["tipoAlimento"],
                "nombreProducto": atributos["nombreProducto"],
                "cantidadAlimento": atributos["cantidadAlimento"],
                "cantidadContenido": atributos["cantidadContenido"],
                "precio": atributos["precio"],
            }
            response = requests.request("PUT", url, data=body)
            print(response.status_code)
        elif ansAct == "3":
            codigoAccesorio = input("Ingrese el codigo del accesorio que quiere editar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoAccesorio", codigoAccesorio)
            accesorio = list(inventario.buscar_accesorio(espc))
            print(len(accesorio))
            atributos = {}
            atributos["codigoAccesorio"] = codigoAccesorio
            atributos["nombreAccesorio"] = accesorio[0].nombreAccesorio
            atributos["descripcionAccesorio"] = accesorio[0].descripcionAccesorio
            atributos["cantidadAccesorio"] = accesorio[0].cantidad
            atributos["precioAccesorio"] = accesorio[0].precio
            atributos["usoAccesorio"] = accesorio[0].usoAccesorio
            cantidadAtributos = int(input("Ingrese la cantidad de caracteristicas del accesorio que quiere editar:"))
            for i in range(0, cantidadAtributos):
                caracteristica = input("Ingrese la caracteristica que quiere editar:")
                valor = input("Ingrese el valor por el cual quiere reemplazarla:")
                atributos[caracteristica] = valor
            url = "http://localhost:2020/accesorio_actualizar/" + codigoAccesorio
            body = {
                "nombreAccesorio": atributos["nombreAccesorio"],
                "precioAccesorio": atributos["precioAccesorio"],
                "cantidadAccesorio": atributos["cantidadAccesorio"],
                "descripcionAccesorio": atributos["descripcionAccesorio"],
                "usoAccesorio": atributos["usoAccesorio"],
            }
            response = requests.request("PUT", url, data=body)
            print(response.status_code)
        elif ansAct == "4":
            codigoCliente = input("Ingrese el codigo del cliente que quiere editar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoCliente", codigoCliente)
            cliente = list(inventario.buscar_cliente(espc))
            print(len(cliente))
            atributos = {}
            atributos["codigoCliente"] = codigoCliente
            atributos["nombre"] = cliente[0].nombre
            atributos["apellido"] = cliente[0].apellido
            atributos["cedula"] = cliente[0].cedula
            atributos["genero"] = cliente[0].genero
            atributos["direccion"] = cliente[0].direccion
            atributos["correo"] = cliente[0].correo
            atributos["edad"] = cliente[0].edad
            atributos["tiempoCliente"] = cliente[0].tiempoCliente
            cantidadAtributos = int(input("Ingrese la cantidad de caracteristicas del cliente que quiere editar:"))
            for i in range(0, cantidadAtributos):
                caracteristica = input("Ingrese la caracteristica que quiere editar:")
                valor = input("Ingrese el valor por el cual quiere reemplazarla:")
                atributos[caracteristica] = valor
            url = "http://localhost:2020/cliente_actualizar/" + codigoCliente
            body = {
                "nombre": atributos["nombre"],
                "apellido": atributos["apellido"],
                "cedula": atributos["cedula"],
                "genero": atributos["genero"],
                "direccion": atributos["direccion"],
                "correo": atributos["correo"],
                "edad": atributos["edad"],
                "tiempoCliente": atributos["tiempoCliente"],
            }
            response = requests.request("PUT", url, data=body)
            print(response.status_code)

        elif ansAct == "5":
            codigoEmpleado = input("Ingrese el codigo del empleado que quiere editar:")
            espc = Especificacion()
            espc.agregar_parametro("codigo", codigoEmpleado)
            empleado = list(inventario.buscar_empleado(espc))
            print(len(empleado))
            atributos = {}
            atributos["codigo"] = codigoEmpleado
            atributos["nombre"] = empleado[0].nombre
            atributos["apellido"] = empleado[0].apellido
            atributos["cedula"] = empleado[0].cedula
            atributos["genero"] = empleado[0].genero
            atributos["direccion"] = empleado[0].direccion
            atributos["correo"] = empleado[0].correo
            atributos["edad"] = empleado[0].edad
            atributos["cargo"] = empleado[0].cargo
            atributos["salario"] = empleado[0].salario
            atributos["horario"] = empleado[0].horario
            cantidadAtributos = int(input("Ingrese la cantidad de caracteristicas del cliente que quiere editar:"))
            for i in range(0, cantidadAtributos):
                caracteristica = input("Ingrese la caracteristica que quiere editar:")
                valor = input("Ingrese el valor por el cual quiere reemplazarla:")
                atributos[caracteristica] = valor
            url = "http://localhost:2020/empleado_actualizar/" + codigoEmpleado
            body = {
                "nombre": atributos["nombre"],
                "apellido": atributos["apellido"],
                "cedula": atributos["cedula"],
                "genero": atributos["genero"],
                "direccion": atributos["direccion"],
                "correo": atributos["correo"],
                "edad": atributos["edad"],
                "cargo": atributos["cargo"],
                "salario": atributos["salario"],
                "horario": atributos["horario"],
            }
            response = requests.request("PUT", url, data=body)
            print(response.status_code)
        else:
            ansAct = False


def eliminarInformacion():
    inventario = generarInventario()
    ansDel = True
    while ansDel:
        print("""
        BIENVENIDO A LA TIENDA DE MASCOTAS, ELIGE ENTRE NUESTRAS OPCIONES,
        PARA MANTENER LA TIENDA ORDENADA Y ELIMINAR SUS ELEMENTOS
        
        1.eliminar una mascota.
        2.eliminar alimento de mascotas.
        3.eliminar accesorio de mascotas.
        4.Regresar al menu principal.
        """)
        ansDel = input("Cual de las opciones quieres?: ")
        if ansDel == "1":
            codigoMascota = input("Ingrese el codigo de la mascota que quiere eliminar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoMascota", codigoMascota)
            mascota = list(inventario.buscar_mascota(espc))
            if len(mascota) != 0:
                print(mascota)
                print("""Esta seguro de eliminar esta mascota?
                          1. Si
                          2. No""")
                confirmacion = input("cual de las opciones quieres?:")
                if confirmacion == "1":
                    url = "http://localhost:2020/mascota_eliminar/" + codigoMascota
                    response = requests.request("DELETE", url)
                    print(response.status_code)
                elif confirmacion == "2":
                    pass
                else:
                    print("Ingrese una de las opciones correspondientes!")
            else:
                print("No hay mascotas registradas con este codigo")
        elif ansDel == "2":
            codigoAlimento = input("Ingrese el codigo del alimento que quiere eliminar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoAlimento", codigoAlimento)
            alimento = list(inventario.buscar_alimento(espc))
            if len(alimento) != 0:
                print(alimento)
                print("""Esta seguro de eliminar este alimento?
                          1. Si
                          2. No""")
                confirmacion = input("cual de las opciones quieres?:")
                if confirmacion == "1":
                    url = "http://localhost:2020/alimento_eliminar/" + codigoAlimento
                    response = requests.request("DELETE", url)
                    print(response.status_code)
                elif confirmacion == "2":
                    pass
                else:
                    print("Ingrese una de las opciones correspondientes!")
            else:
                print("No hay alimentos registrados con este codigo")
        elif ansDel == "3":
            codigoAccesorio = input("Ingrese el codigo del accesorio que quiere eliminar:")
            espc = Especificacion()
            espc.agregar_parametro("codigoAccesorio", codigoAccesorio)
            accesorio = list(inventario.buscar_accesorio(espc))
            if len(accesorio) != 0:
                print(accesorio)
                print("""Esta seguro de eliminar este accesorio?
                          1. Si
                          2. No""")
                confirmacion = input("cual de las opciones quieres?:")
                if confirmacion == "1":
                    url = "http://localhost:2020/accesorio_eliminar/" + codigoAccesorio
                    response = requests.request("DELETE", url)
                    print(response.status_code)
                elif confirmacion == "2":
                    pass
                else:
                    print("Ingrese una de las opciones correspondientes!")
            else:
                print("No hay accesorios registrados con este codigo")
        elif ansDel == "4":
            ansDel = False


def buscar_informacion():
    opc = True
    inventario = generarInventario()
    while opc:
        especificacion = Especificacion()
        print("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA BUSCAR TUS ELEMENTOS Y TENER UN CONTROL SOBRE ESTOS
            
            1.Buscar mascota.
            2.Buscar alimento de mascotas.
            3.Buscar accesorio de mascotas.
            4.Buscar cliente.
            5.Buscar empleado.
            6.Regresar al menu principal.
            """)
        opc = input("Ingrese la opcion que desee:")
        if opc == "1":
            print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A LA MASCOTA.
                
                1.Codigo mascota.
                2.tipo de mascota.
                3.raza de la mascota.
                4.nombre de la mascota.
                5.precio de la mascota.
                6.edad mascota.
                7.Regresar.
                """)
            resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
            if resultado > 6:
                print("No puede buscar por mas de 5 atributos para la mascota")
            else:
                for i in range(resultado):
                    llave = input("Ingrese el numero al que corresponde la caracteristica:")
                    valor = input("Ingrese el valor de la caracteristica:")
                    if llave == "1":
                        llave = "codigoMascota"
                    elif llave == "2":
                        llave = "tipoMascota"
                    elif llave == "3":
                        llave = "raza"
                    elif llave == "4":
                        llave = "nombre"
                    elif llave == "5":
                        llave = "precio"
                    elif llave == "6":
                        llave == "edad"
                    elif llave == "7":
                        print("No hubo busqueda")
                    elif llave != "":
                        print("Ingreso opciones invalidas")
                    especificacion.agregar_parametro(llave, valor)
                print(list(inventario.buscar_mascota(especificacion)))
        elif opc == "2":
            print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ALIMENTO PARA MASCOTAS.
                
                1.Codigo alimento de mascotas.
                2.tipo de alimento de mascotas.
                3.cantidad existencias.
                4.nombre del producto.
                5.precio del producto.
                6.cantidad de contenido alimento.
                7.Regresar.
                """)
            resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
            if resultado > 6:
                print("No puede buscar por mas de 5 atributos para el alimento")
            else:
                for i in range(resultado):
                    llave = input("Ingrese el numero al que corresponde la caracteristica:")
                    valor = input("Ingrese el valor de la caracteristica:")
                    if llave == "1":
                        llave = "codigoAlimento"
                    elif llave == "2":
                        llave = "tipoAlimento"
                    elif llave == "3":
                        llave = "cantidadAlimento"
                    elif llave == "4":
                        llave = "nombreProducto"
                    elif llave == "5":
                        llave = "precio"
                    elif llave == "6":
                        llave == "cantidadContenido"
                    elif llave == "7":
                        print("No hubo busqueda")
                    elif llave != "":
                        print("Ingreso opciones invalidas")
                    especificacion.agregar_parametro(llave, valor)
                print(list(inventario.buscar_alimento(especificacion)))
        elif opc == "3":
            print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                EL ACCESORIO DE MASCOTAS.
                
                1.Codigo accesorio.
                2.Nombre del accesorio.
                3.Cantidad existencias del accesorio.
                4.Precio del accesorio.
                5.Descripcion del accesorio.
                6.Uso del accesorio.
                7.Regresar.
                """)
            resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
            if resultado > 6:
                print("No puede buscar por mas de 5 atributos para el accesorio")
            else:
                for i in range(resultado):
                    llave = input("Ingrese el numero al que corresponde la caracteristica:")
                    valor = input("Ingrese el valor de la caracteristica:")
                    if llave == "1":
                        llave = "codigoAccesorio"
                    elif llave == "2":
                        llave = "nombreAccesorio"
                    elif llave == "3":
                        llave = "cantidadAccesorio"
                    elif llave == "4":
                        llave = "precioAccesorio"
                    elif llave == "5":
                        llave = "descripcionAccesorio"
                    elif llave == "6":
                        llave == "usoAccesorio"
                    elif llave == "7":
                        print("No hubo busqueda")
                    elif llave != "":
                        print("Ingreso opciones invalidas")
                    especificacion.agregar_parametro(llave, valor)
                print(list(inventario.buscar_accesorio(especificacion)))
        elif opc == "4":
            print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL CLIENTE.
                
                1.Codigo del cliente.
                2.Cedula del cliente.
                3.Genero del cliente.
                4.Nombre del cliente.
                5.apellido del cliente.
                6.Edad el cliente.
                7.Direccion del cliente.
                8.Correo del cliente.
                9.Tiempo como cliente de la tienda.
                10.Regresar.
                """)
            resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
            if resultado > 8:
                print("No puede buscar por mas de 8 atributos para el cliente")
            else:
                for i in range(resultado):
                    llave = input("Ingrese el numero al que corresponde la caracteristica:")
                    valor = input("Ingrese el valor de la caracteristica:")
                    if llave == "1":
                        llave = "codigoCliente"
                    elif llave == "2":
                        llave = "cedula"
                    elif llave == "3":
                        llave = "genero"
                    elif llave == "4":
                        llave = "nombre"
                    elif llave == "5":
                        llave = "apellido"
                    elif llave == "6":
                        llave == "edad"
                    elif llave == "7":
                        llave = "direccion"
                    elif llave == "8":
                        llave = "correo"
                    elif llave == "9":
                        llave = "tiempoCliente"
                    elif llave == "10":
                        print("No hubo busqueda")
                    elif llave != "":
                        print("Ingreso opciones invalidas")
                    especificacion.agregar_parametro(llave, valor)
                print(list(inventario.buscar_cliente(especificacion)))
        elif opc == "5":
            print("""
                ESTOS SON LAS CARACTERISTICAS POR LAS CUALES USTED PUEDE BUSCAR 
                A EL EMPLEADO.
                
                1.Codigo del empleado.
                2.Cedula del empleado.
                3.Genero del empleado.
                4.Nombre del empleado.
                5.apellido del apellido.
                6.Edad del empleado.
                7.Direccion del empleado.
                8.Correo del empleado.
                9.Cargo del empleado.
                10.Horario del empleado.
                11.Salario del empleado.
                12.Regresar.
                """)
            resultado = int(input("Ingrese el numero de caracteristicas por las que quiere buscar:"))
            if resultado > 8:
                print("No puede buscar por mas de 8 atributos para el cliente")
            else:
                for i in range(resultado):
                    llave = input("Ingrese el numero al que corresponde la caracteristica:")
                    valor = input("Ingrese el valor de la caracteristica:")
                    if llave == "1":
                        llave = "codigo"
                    elif llave == "2":
                        llave = "cedula"
                    elif llave == "3":
                        llave = "genero"
                    elif llave == "4":
                        llave = "nombre"
                    elif llave == "5":
                        llave = "apellido"
                    elif llave == "6":
                        llave = "edad"
                    elif llave == "7":
                        llave = "direccion"
                    elif llave == "8":
                        llave = "correo"
                    elif llave == "9":
                        llave = "cargo"
                    elif llave == "10":
                        llave = "horario"
                    elif llave == "11":
                        llave = "salario"
                    elif llave == "12":
                        print("No hubo busqueda")
                    elif llave != "":
                        print("Ingreso opciones invalidas")
                    especificacion.agregar_parametro(llave, valor)
                print(list(inventario.buscar_empleado(especificacion)))
        elif opc == "6":
            opc = False
        elif opc != "":
            print("\n Opcion invalida porfavor rectifica")


def generarVenta():
    inventario = generarInventario()
    respVenta = True
    while respVenta:
        print("""
                ESCOJA EL ELEMENTO QUE QUIERE COMPRAR:
                
                1.Mascota.
                2.Accesorio.
                3.Alimento.
                4.Terminar y salir.
                """)
        respVenta = input("Cual de las opciones quieres?: ")
        if respVenta == "1":
            venderMascota(inventario)
        elif respVenta == "2":
            venderAccesorio(inventario)
        elif respVenta == "3":
            venderAlimento(inventario)
        elif respVenta == "4":
            respVenta = False
        else:
            print("Ingrese una de las opciones maldito fracasado!")


def venderMascota(inventario):
    for mascota in inventario.mascotas:
        print("codigoMascota: " + str(mascota.codigoMascota) + "\n"
              + "Nombre: " + mascota.nombre + "\n"
              + "Tipo de mascota: " + mascota.tipoMascota + "\n"
              + "Raza: " + mascota.raza + "\n"
              + "Edad: " + str(mascota.edad) + "\n"
              + "Cantidad disponible: " + str(mascota.cantidad) + "\n"
              + "Precio: " + str(mascota.precio) + "\n")
        # Actualizar la base de datos
    codigoMascota = input("Ingrese el codigo de la mascota que se quiere comprar: ")
    codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
    codigoEmpleado = input("Ingrese el codigo del empleado que realiza la venta: ")
    cantidad = int(input("Ingrese la cantidad de mascotas que desea comprar: "))
    espc = Especificacion()
    espc.agregar_parametro("codigoMascota", codigoMascota)
    espcEmpleado = Especificacion()
    espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
    espcCliente = Especificacion()
    espcCliente.agregar_parametro("codigoCliente", codigoCliente)
    mascotas = list(inventario.buscar_mascota(espc))
    while (mascotas[0].cantidad < cantidad):
        cantidad = int(input(
            "La cantidad ingresada supera nuestro stock.\nPor favor ingresa la nueva cantidad de mascotas que desea comprar: "))
    empleados = list(inventario.buscar_empleado(espcEmpleado))
    while len(empleados) == 0:
        codigoEmpleado = input("Codigo de empleado no valido\nIngrese el codigo del empleado que realiza la venta: ")
        espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
        empleados = list(inventario.buscar_empleado(espcEmpleado))

    clientes = list(inventario.buscar_cliente(espcCliente))
    while len(clientes) == 0:
        print("¿Desea registrar un nuevo cliente?")
        resp = int(input("1. Si\n2. No"))
        if resp == 1:
            registrar_cliente()
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        elif resp == 2:
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        else:
            print("Ingrese una opcion valida estupido")
    precioTotal = cantidad * mascotas[0].precio
    venta = Venta(clientes[0], empleados[0], mascotas[0].nombre, cantidad, mascotas[0].precio, precioTotal)
    mascotas[0].cantidad = mascotas[0].cantidad - cantidad
    saverMascota.actualizar_mascota(mascotas[0], mascotas[0].codigoMascota)
    try:
        inventario.agregar_venta(venta)
        url = "http://localhost:2020/venta_guardar/"
        body = {
            "cantidadVenta": cantidad,
            "precioUnidad": mascotas[0].precio,
            "precioTotal": precioTotal,
            "nombreProducto": mascotas[0].nombre,
            "codigoCliente": codigoCliente,
            "codigo": codigoEmpleado
        }
        response = requests.request("POST", url, data=body)
        print(response.status_code)
        print("\n Se agrego la venta con exito en bd")
    except Exception as ex:
        print(ex)


def venderAccesorio(inventario):
    for accesorio in inventario.accesorios:
        print("codigo accesorio: " + str(accesorio.codigoAccesorio) + "\n"
              + "Nombre: " + accesorio.nombreAccesorio + "\n"
              + "Descripcion: " + accesorio.descripcionAccesorio + "\n"
              + "Uso: " + accesorio.usoAccesorio + "\n"
              + "Cantidad diponible: " + str(accesorio.cantidad) + "\n"
              + "Precio: " + str(accesorio.precio)+"\n")
        # Actualizar la base de datos
    codigoAccesorio = input("Ingrese el codigo del accesorio que se quiere comprar: ")
    codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
    codigoEmpleado = input("Ingrese el codigo del empleado que realiza la venta: ")
    cantidad = int(input("Ingrese la cantidad de accesorios que desea comprar: "))
    espc = Especificacion()
    espc.agregar_parametro("codigoAccesorio", codigoAccesorio)
    espcEmpleado = Especificacion()
    espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
    espcCliente = Especificacion()
    espcCliente.agregar_parametro("codigoCliente", codigoCliente)
    accesorios = list(inventario.buscar_accesorio(espc))
    while (accesorios[0].cantidad < cantidad):
        cantidad = int(input(
            "La cantidad ingresada supera nuestro stock.\nPor favor ingresa la nueva cantidad de mascotas que desea comprar: "))
    empleados = list(inventario.buscar_empleado(espcEmpleado))
    while len(empleados) == 0:
        codigoEmpleado = input("Codigo de empleado no valido\nIngrese el codigo del empleado que realiza la venta: ")
        espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
        empleados = list(inventario.buscar_empleado(espcEmpleado))

    clientes = list(inventario.buscar_cliente(espcCliente))
    while len(clientes) == 0:
        print("¿Desea registrar un nuevo cliente?")
        resp = int(input("1. Si\n2. No"))
        if resp == 1:
            registrar_cliente()
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        elif resp == 2:
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        else:
            print("Ingrese una opcion valida estupido")
    precioTotal = cantidad * accesorios[0].precio
    venta = Venta(clientes[0], empleados[0], accesorios[0].nombreAccesorio, cantidad, accesorios[0].precio, precioTotal)
    accesorios[0].cantidad = accesorios[0].cantidad - cantidad
    saverAccesorios.actualizar_accesorio(accesorios[0], accesorios[0].codigoAccesorio)
    try:
        inventario.agregar_venta(venta)
        url = "http://localhost:2020/venta_guardar/"
        body = {
            "cantidadVenta": cantidad,
            "precioUnidad": accesorios[0].precio,
            "precioTotal": precioTotal,
            "nombreProducto": accesorios[0].nombreAccesorio,
            "codigoCliente": codigoCliente,
            "codigo": codigoEmpleado
        }
        response = requests.request("POST", url, data=body)
        print(response.status_code)
        print("\n Se agrego la venta con exito en bd")
    except Exception as ex:
        print(ex)


def venderAlimento(inventario):
    for alimento in inventario.alimentos:
        print("codigo alimento: " + str(alimento.codigoAlimento) + "\n"
              + "Nombre: " + alimento.nombreProducto + "\n"
              + "Tipo de alimento: " + alimento.tipoAlimento + "\n"
              + "Contenido: " + str(alimento.cantidadContenido) + "\n"
              + "Cantidad diponible: " + str(alimento.cantidad) + "\n"
              + "Precio: " + str(alimento.precio)+"\n")
        # Actualizar la base de datos
    codigoAlimento = input("Ingrese el codigo del alimento que se quiere comprar: ")
    codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
    codigoEmpleado = input("Ingrese el codigo del empleado que realiza la venta: ")
    cantidad = int(input("Ingrese la cantidad de alimentos que desea comprar: "))
    espc = Especificacion()
    espc.agregar_parametro("codigoAlimento", codigoAlimento)
    espcEmpleado = Especificacion()
    espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
    espcCliente = Especificacion()
    espcCliente.agregar_parametro("codigoCliente", codigoCliente)
    alimentos = list(inventario.buscar_alimento(espc))
    while (alimentos[0].cantidadAlimento < cantidad):
        cantidad = int(input(
            "La cantidad ingresada supera nuestro stock.\nPor favor ingresa la nueva cantidad de mascotas que desea comprar: "))
    empleados = list(inventario.buscar_empleado(espcEmpleado))
    while len(empleados) == 0:
        codigoEmpleado = input("Codigo de empleado no valido\nIngrese el codigo del empleado que realiza la venta: ")
        espcEmpleado.agregar_parametro("codigo", codigoEmpleado)
        empleados = list(inventario.buscar_empleado(espcEmpleado))

    clientes = list(inventario.buscar_cliente(espcCliente))
    while len(clientes) == 0:
        print("¿Desea registrar un nuevo cliente?")
        resp = int(input("1. Si\n2. No"))
        if resp == 1:
            registrar_cliente()
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        elif resp == 2:
            codigoCliente = input("Ingrese el codigo del cliente que realiza la compra: ")
            espcCliente.agregar_parametro("codigoCliente", codigoCliente)
            clientes = list(inventario.buscar_cliente(espcCliente))
        else:
            print("Ingrese una opcion valida estupido")
    precioTotal = cantidad * alimentos[0].precio
    venta = Venta(clientes[0], empleados[0], alimentos[0].nombreProducto, cantidad, alimentos[0].precio, precioTotal)
    alimentos[0].cantidad = alimentos[0].cantidad - cantidad
    saverAlimentos.actualizar_alimento(alimentos[0], alimentos[0].codigoAlimento)
    try:
        inventario.agregar_venta(venta)
        url = "http://localhost:2020/venta_guardar/"
        body = {
            "cantidadVenta": cantidad,
            "precioUnidad": alimentos[0].precio,
            "precioTotal": precioTotal,
            "nombreProducto": alimentos[0].nombreProducto,
            "codigoCliente": codigoCliente,
            "codigo": codigoEmpleado
        }
        response = requests.request("POST", url, data=body)
        print(response.status_code)
        print("\n Se agrego la venta con exito en bd")
    except Exception as ex:
        print(ex)


"""Este es el while principal donde se ejecutan todos los metodos previamente dichos dependiendo de la 
decision del usuario"""

ansPrin = True
while ansPrin:
    print("""
            BIENVENIDO A LA TIENDA DE MASCOTAS, ELEGI ENTRE NUESTRAS OPCIONES,
            PARA AGREGAR, BUSCAR O VENDER UN ELEMENTO DE TU TIENDA:
            
            1.Agregar elemento.
            2.Actualizar elemento.
            3.Eliminar elemento.
            4.Buscar elemento.
            5.Vender elemento.
            6.Terminar y salir.
            """)
    ansPrin = input("Cual de las opciones quieres?: ")
    if ansPrin == "1":
        agregar_informacion()
    elif ansPrin == "2":
        actualizarInformacion()
    elif ansPrin == "3":
        eliminarInformacion()
    elif ansPrin == "4":
        buscar_informacion()
    elif ansPrin == "5":
        generarVenta()
    elif ansPrin != "":
        print("\n Nos vemos hasta la proxima!")
        ansPrin = False
