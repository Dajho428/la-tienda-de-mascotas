class Persona():
    def __init__(self, nombre, apellido, cedula, genero, direccion, correo, edad):
        self.cedula = cedula
        self.genero = genero
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.correo = correo

    def cambioNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def cumpleaños(self, nuevaEdad):
        self.edad = nuevaEdad

    def cambioResidencia(self, nuevaResidencia):
        self.direccion = nuevaResidencia

    def cambioCorreo(self, nuevoCorreo):
        self.correo = nuevoCorreo
