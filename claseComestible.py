from claseProducto import Producto
#explicar clase 
class Comestible(Producto):
    #explicar constructor, definir por que los atributos son privados
    def __init__(self, nombre, precioCosto, fechaVencimiento, precioVenta=0):
        super().__init__(nombre, precioVenta, precioCosto)
        self.__fechaVencimiento = fechaVencimiento
    #explicar get
    def get(self, name):
        if(name=="nombre"):
            return super().get("nombre")
        elif(name=="precioVenta"):
            return super().get("precioVenta")
        elif(name=="precioCosto"):
            return super().get("precioCosto")
        elif(name=="ganancia"):
            return super().get("ganancia")
        elif(name=="fechaVencimiento"):
            return self.__fechaVencimiento
    #explicar set
    def set(self, name, valor):
        if(name=="nombre"):
            super().set("nombre", valor)
        elif(name=="precioVenta"):
            super().set("precioVenta", valor)
        elif(name=="precioCosto"):
            super().set("precioCosto", valor)
        elif(name=="fechaVencimiento"):
            self.__fechaVencimiento = valor
    #explicar por que ocurre polimorfismo
    def mostrarProducto(self):
        return super().mostrarProducto()+f' - Fecha vencimiento: {self.__fechaVencimiento}'

