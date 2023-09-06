from claseComestible import Comestible

from datetime import datetime
#clase estatica, porque todos los metodos son estaticos
class Funciones(): 
    #explicar constructor, definir por que los atributos son privados
    def __init__(self, listaTiendas, nombreProducto, listaProductos):
        self.__listaTiendas = listaTiendas
        self.__nombreProducto = nombreProducto
        self.__listaProductos = listaProductos
    #explicar metodo publico get
    def get(self, name):
        if(name=="listaTiendas"):
            return self.__listaTiendas
        elif(name=="nombreProducto"):
            return self.__nombreProducto
        else:
            return self.__listaP
    #explicar metodo publico set
    def set(self, name, valor):
        if(name=="listaTiendas"):
            self.__listaTiendas = valor
        elif(name=="nombreProducto"):
            self.__nombreProducto = valor
        else:
            self.__listaP = valor
    # para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    @staticmethod 
    def calcularMedia(listaTiendas, nombreProducto):
        acumulador = 0
        for tienda in listaTiendas:
            listaProductos = tienda.get("listaProductos")
            for producto in listaProductos:
                if(nombreProducto==(producto.get("nombre"))):
                    acumulador += producto.get("precioVenta")
                    break
        nTiendas = len(listaTiendas)
        return (acumulador/nTiendas)
    # para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    #creamos esta lista de productos para ser utilizados luego en el programa principal
    # explicar lo del datetime
    @staticmethod 
    def obtenerListaProductos():
        producto1 = Comestible("harina", 1000, datetime.strptime('5:9:2023', '%d:%m:%Y'))
        producto2 = Comestible("azucar", 1600,datetime.strptime('5:9:2023', '%d:%m:%Y'))
        producto3 = Comestible("leche", 2000, datetime.strptime('5:9:2023', '%d:%m:%Y'))
        listaProductos = [producto1, producto2, producto3]
        return listaProductos
     # para convertir la funcion a un metodo estatico para poder utilizarlo en el principal
    #creamos esta lista de productos para ser utilizados luego en el programa principal
    @staticmethod
    def listaProductosATexto(listaProductos):
        textoProductos = ""
        for producto in listaProductos:
            textoProductos += (producto.mostrarProducto()+"\n")
        return textoProductos





