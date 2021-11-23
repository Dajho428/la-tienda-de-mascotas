class ElementoCompra():

    def __init__(self, cantidad, precio):
        self.cantidad = cantidad
        self.precio = precio

    def apreciar(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def controlCantidad(self, nuevaCantidad):
        self.cantidadA = nuevaCantidad
