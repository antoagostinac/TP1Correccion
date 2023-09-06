#Azul
from claseEdificio import Edificio
from claseFunciones import Funciones as f
#comentar de que trata la clase, explicar que hereda de Edificio
class Tienda(Edificio):
    #explicar constructor, definir por que los atributos son privados
    def __init__(self, nombre, cantidadPisos, direccion, tipo):
        super().__init__(nombre, cantidadPisos, direccion)
        self.__listaProductos = []
        self.__tipo = tipo
    #explicar metodo publico get
    def get(self, name):
        if(name=="nombre"):
            return super().get("nombre")
        elif(name=="cantidadPisos"):
            return super().get("cantidadPisos")
        elif(name=="direccion"):
            return super().get("direccion")
        elif(name=="listaProductos"):
            return self.__listaProductos
        elif(name=="tipo"):
            return self.__tipo
    #explicar metodo publico set
    def set(self, name, valor):
        if(name=="nombre"):
            super().set("nombre", valor)
        elif(name=="cantidadPisos"):
            super().set("cantidadPisos", valor)
        elif(name=="direccion"):
            super().set("direccion", valor)
        elif(name=="listaProductos"):
            self.__listaProductos = valor
        elif(name=="tipo"):
            self.__tipo = valor
    #texto para mostrar la lista de productos, metodo privado, explicar por que
    def __textoListaProductos(self): 
        return f.listaProductosATexto(self.__listaProductos)
        #textoProductos = ""
        #for producto in self.__listaProductos:
        #    textoProductos += (producto.mostrarProducto()+"\n")
        #return textoProductos
    #metodo publico, explicar que hace por que
    def agregarProducto(self, producto, precio):
        producto.set("precioVenta", precio)
        self.__listaProductos.append(producto)
    #metodo publico, explicar que hace por que es publico
    def actualizarPrecio(self, name, precio):
        for producto in self.__listaProductos:
            if(producto.get("nombre")==name):
                producto.set("precioVenta", precio)
                break
    #metodo publico, explicar por que, que hace
    def mostrarListaProductos(self):
        return f'\nLista de productos:\n{self.__textoListaProductos()}'
    #ocurre polimorfismo aqui con este metodo, explicar por que
    def mostrarInformacion(self):
        return super().mostrarInformacion()+f'\nLista de productos:\n{self.mostrarListaProductos()}'



