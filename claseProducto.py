#Azul
#explicar la clase abstracta, por que
class Producto():
    #explicar constructor, definir por que los atributos son privados
    def __init__(self, nombre, precioVenta, precioCosto):
        self.__nombre = nombre
        self.__precioVenta = precioVenta
        self.__precioCosto = precioCosto
        self.__ganancia = self.__calcularGanancia()
    #explicar metodo publico get
    def get(self, name):
        if(name=="nombre"):
            return self.__nombre
        elif(name=="precioVenta"):
            return self.__precioVenta
        elif(name=="precioCosto"):
            return self.__precioCosto
        elif(name=="ganancia"):
            return self.__ganancia
    #explicar metodo publico set
    def set(self, name, valor):
        if(name=="nombre"):
            self.__nombre = valor
        elif(name=="precioVenta"):
            self.__precioVenta = valor
            self.__ganancia = self.__calcularGanancia()
        elif(name=="precioCosto"):
            self.__precioCosto = valor
            self.__ganancia = self.__calcularGanancia()
    #explicar por que es un metodo privado y que hace
    def __calcularGanancia(self):
        return (self.__precioVenta - self.__precioCosto)
    #explicar porque este metodo es publico 
    def mostrarProducto(self):
        return f'Nombre: {self.__nombre} - Precio de venta: ${self.__precioVenta} - Precio de costo: ${self.__precioCosto} - Ganancia: ${self.__ganancia}'




