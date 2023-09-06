#Azul
#Estas son las importaciones de las clases Edificio y Funciones. La clase Edificio se importa directamente,
#mientras que la clase Funciones se importa con el alias f
from claseEdificio import Edificio
from claseFunciones import Funciones as f
#Esta es la definición de una clase llamada Tienda, que hereda de la clase Edificio. 
#Esto significa que la clase Tienda tiene acceso a todos los métodos y atributos de la clase Edificio.
class Tienda(Edificio):
#El constructor de la clase tienda toma 4 argumentos nombre, cantidadPisos, direccion y tipo. Los primeros tres argumentos se pasan al constructor de la clase base (Edificio) utilizando la función super().
#Los atributos __listaProductos y __tipo se inicializan con una lista vacía y el valor del argumento tipo, respectivamente.
#Los atributos son privados ya que solo se pueden acceder desde dentro de la clase y no desde fuera.
    def __init__(self, nombre, cantidadPisos, direccion, tipo):
        super().__init__(nombre, cantidadPisos, direccion)
        self.__listaProductos = []
        self.__tipo = tipo
#Esto es un metodo get para la clase Tienda el método toma un argumento, name, que especifica el nombre del atributo a recuperar.
#Si el nombre del atributo es "nombre", "cantidadPisos" o "direccion", el método llama al método getter de la clase base (Edificio) utilizando la función super(). 
#Si el nombre del atributo es "listaProductos" o "tipo", el método devuelve el valor del atributo correspondiente. 
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
    #Esto es metodo set de clase tienda l método toma dos argumentos: name, que especifica el nombre del atributo a establecer, y valor, que especifica el nuevo valor para el atributo. 
    #Si el nombre del atributo es "nombre", "cantidadPisos" o "direccion", el método llama al método setter de la clase base (Edificio) utilizando la función super(). 
    #Si el nombre del atributo es "listaProductos" o "tipo", el método establece el valor del atributo correspondiente en valor.
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
    #Esto es metodo privado llamado __textoListaProductos para la clase Tienda ,método privado solo puede ser accedido desde dentro de la clase.
    #Este método devuelve una cadena que contiene información sobre los productos en la lista de productos del objeto. 
    #La cadena se genera llamando al método estático listaProductosATexto de la clase importada Funciones (con el alias f) y pasando como argumento la lista de productos del objeto.
    def __textoListaProductos(self): 
        return f.listaProductosATexto(self.__listaProductos)
        #textoProductos = ""
        #for producto in self.__listaProductos:
        #    textoProductos += (producto.mostrarProducto()+"\n")
        #return textoProductos
    #Este es un método público llamado agregarProducto para la clase Tienda. Un método público puede ser accedido desde fuera de la clase.
    #Este método toma dos argumentos: producto y precio.
    #El método establece el valor del atributo "precioVenta" del objeto producto en precio utilizando el método setter del objeto producto. 
    #Luego, el método agrega el objeto producto a la lista de productos del objeto.
    def agregarProducto(self, producto, precio):
        producto.set("precioVenta", precio)
        self.__listaProductos.append(producto)
    #Este es un método público llamado actualizarPrecio para la clase Tienda. 
    #Un método público puede ser accedido desde fuera de la clase.
    #Este método toma dos argumentos: name y precio. 
    #El método busca en la lista de productos del objeto un producto cuyo atributo "nombre" sea igual al valor del argumento name. 
    #Si encuentra un producto que cumpla con esta condición, establece el valor del atributo "precioVenta" del producto en precio utilizando el método setter del objeto producto.
    def actualizarPrecio(self, name, precio):
        for producto in self.__listaProductos:
            if(producto.get("nombre")==name):
                producto.set("precioVenta", precio)
                break
    #Este es un método público llamado mostrarListaProductos para la clase Tienda. 
    #Un método público puede ser accedido desde fuera de la clase.
    #Este método devuelve una cadena que contiene información sobre los productos en la lista de productos del objeto. 
    #La cadena se genera llamando al método privado __textoListaProductos del objeto.
    def mostrarListaProductos(self):
        return f'\nLista de productos:\n{self.__textoListaProductos()}'
    #Este método es un ejemplo de polimorfismo, ya que sobrescribe el comportamiento del método mostrarInformacion de la clase base (Edificio).
    #Esto significa que cuando se llama al método mostrarInformacion en un objeto de la clase Tienda, se ejecutará el código definido en este método en lugar del código definido en el método mostrarInformacion de la clase base (Edificio).
    def mostrarInformacion(self):
        return super().mostrarInformacion()+f'\nLista de productos:\n{self.mostrarListaProductos()}'



