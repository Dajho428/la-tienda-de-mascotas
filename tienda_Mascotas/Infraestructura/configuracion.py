class Configuracion():
    def __init__(self, codigoUnico=1):
        self.codigoUnico = codigoUnico
        self.estado = "archivo plano json"

    def cambiarEstadoConfiguracion(self, nuevaConfiguracion):
        self.estado = nuevaConfiguracion

    def __repr__(self):
        return self.estado
