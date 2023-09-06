from claseProducto import Producto
#se define una nueva clase llamada Comestible, que es una subclase de la clase Producto
#esta relación de herencia significa que la clase Comestible adquiere todas las propiedades (atributos y métodos) de la clase base Producto. 
#la clase Comestible es una versión más específica o especializada de la clase Producto.
class Comestible(Producto):
    #El constructor toma cuatro argumentos: nombre, precioCosto, fechaVencimiento, y precioVenta (con un valor predeterminado de 0).
    #se utiliza super() para llamar al constructor de la clase base Producto. 
    #Esto asegura que se inicialicen correctamente los atributos heredados de la clase base Producto, como nombre, precioVenta, y precioCosto. 
    #Los valores de estos atributos se pasan desde los argumentos del constructor de Comestible.
    #se define un nuevo atributo privado fechaVencimiento que almacena la fecha de vencimiento específica de un producto comestible. 
    #Este atributo es específico de la clase Comestible y no se encuentra en la clase base Producto.
    def __init__(self, nombre, precioCosto, fechaVencimiento, precioVenta=0):
        super().__init__(nombre, precioVenta, precioCosto)
        self.__fechaVencimiento = fechaVencimiento
    #Este metodo se utiliza para obtener valores de atributos de un objeto Comestible, tanto aquellos que son heredados de la clase base Producto como el atributo específico de la clase Comestible, que es fechaVencimiento.
    #El método get acepta un argumento name y se utiliza una serie de declaraciones if y elif para determinar qué atributo se está solicitando.
    #Si name es igual a "nombre", "precioVenta", "precioCosto", o "ganancia", el método llama al método get de la clase base Producto utilizando super(). esto permite obtener los valores de estos atributos heredados de la clase base.
    #Si name es igual a "fechaVencimiento", el método devuelve el valor del atributo privado fechaVencimiento específico de la clase Comestible. 
    #Esto se hace sin utilizar el método get de la clase base, ya que este atributo es específico de la subclase Comestible.
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
    #se utiliza para modificar valores de atributos de un objeto Comestible, tanto aquellos heredados de la clase base Producto como el atributo específico de la clase Comestible.
    #acepta dos argumentos: name y valor. name se utiliza para especificar qué atributo se desea modificar, y valor es el nuevo valor que se asignará al atributo.
    #Si name es igual a "nombre", "precioVenta", o "precioCosto", el método llama al método set de la clase base Producto utilizando super(). Esto permite modificar los valores de estos atributos heredados de la clase base Producto.
    #Si name es igual a "fechaVencimiento", el método asigna el nuevo valor valor directamente al atributo privado fechaVencimiento específico de la clase Comestible.
    #No se utiliza el método set de la clase base en este caso, ya que este atributo es específico de la subclase Comestible.
    def set(self, name, valor):
        if(name=="nombre"):
            super().set("nombre", valor)
        elif(name=="precioVenta"):
            super().set("precioVenta", valor)
        elif(name=="precioCosto"):
            super().set("precioCosto", valor)
        elif(name=="fechaVencimiento"):
            self.__fechaVencimiento = valor
    #En este metodo mostrarProducto ocurre polimorfismo
    #La clase base Producto tiene un método llamado mostrarProducto que muestra una representación legible de los atributos del producto, incluyendo su nombre, precio de venta, precio de costo y ganancia.
    #En la subclase Comestible, se redefine el método mostrarProducto. Cuando se llama a mostrarProducto en una instancia de Comestible, se ejecutará la versión específica de este método definida en la clase Comestible, en lugar de la versión en la clase base Producto.
    #se utiliza super().mostrarProducto() para llamar al método mostrarProducto de la clase base Producto. Esto permite reutilizar la funcionalidad existente en la clase base y luego agregar información específica de la subclase Comestible.
    #Después de llamar al método mostrarProducto de la clase base, se agrega información específica de Comestible. 
    #En este caso, se añade la fecha de vencimiento del producto comestible a la cadena que se devuelve.
    def mostrarProducto(self):
        return super().mostrarProducto()+f' - Fecha vencimiento: {self.__fechaVencimiento}'

