#Se crea una clase Producto que es una clase abstracta la cual sera plantilla para otra clase "Comestible"
class Producto():
    #El constructor __init__ se utiliza para inicializar los atributos de la instancia de la clase Producto. 
    #Los atributos nombre, precioVenta y precioCosto se inicializan en este método.
    #Los atributos se definen como privados (con nombres que comienzan con __) para evitar que se accedan o modifiquen desde fuera de la clase. 
    #se llama al método privado calcularGanancia() para calcular la ganancia del producto.
    #Este cálculo se realiza restando el precio de costo (precioCosto) al precio de venta (precioVenta). La ganancia resultante se almacena en el atributo ganancia.
    def __init__(self, nombre, precioVenta, precioCosto):
        self.__nombre = nombre
        self.__precioVenta = precioVenta
        self.__precioCosto = precioCosto
        self.__ganancia = self.__calcularGanancia()
        
#Este método se utiliza para obtener valores de atributos privados de la instancia de la clase Producto en función del nombre del atributo que se pasa como argumento. 
#se utiliza una serie de declaraciones if y elif para determinar qué atributo se está solicitando. 
#Si name es igual a "nombre", "precioVenta", "precioCosto", o "ganancia", el método devuelve el valor correspondiente del atributo privado asociado. 
    def get(self, name):
        if(name=="nombre"):
            return self.__nombre
        elif(name=="precioVenta"):
            return self.__precioVenta
        elif(name=="precioCosto"):
            return self.__precioCosto
        elif(name=="ganancia"):
            return self.__ganancia
            
    #este método se utiliza para cambiar los valores de los atributos privados de la instancia de la clase Producto en función del nombre del atributo y el nuevo valor que se pasan como argumentos. 
    #acepta dos argumentos: name y valor. name se utiliza para especificar qué atributo se desea modificar, y valor es el nuevo valor que se asignará al atributo.
    #se utiliza una serie de declaraciones if y elif para determinar qué atributo se está modificando.
    #Si name es igual a "nombre", "precioVenta", o "precioCosto", el método actualiza el valor del atributo privado correspondientecon el nuevo valor proporcionado como argumento.
    #el método también llama al método privado calcularGanancia() para recalcular la ganancia en función de los nuevos valores de precio de venta y precio de costo.
    def set(self, name, valor):
        if(name=="nombre"):
            self.__nombre = valor
        elif(name=="precioVenta"):
            self.__precioVenta = valor
            self.__ganancia = self.__calcularGanancia()
        elif(name=="precioCosto"):
            self.__precioCosto = valor
            self.__ganancia = self.__calcularGanancia()
            
#el método calcularGanancia es privado, lo que significa que solo se puede acceder a él desde dentro de la propia clase Producto. 
#no es accesible desde fuera de la clase, lo que ayuda a ocultar su implementación y protege los datos de la instancia de Producto.
#toma los valores de precioVenta y precioCosto de la instancia actual de Producto. 
#se resta el precioCosto del precioVenta, lo que da como resultado el valor de la ganancia.
    def __calcularGanancia(self):
        return (self.__precioVenta - self.__precioCosto)

#El método mostrarProducto se define como público para que otros partes del código puedan acceder a él.
#se utiliza para mostrar una representación legible de un producto y sus atributos, como el nombre, el precio de venta, el precio de costo y la ganancia.
#no toma ningún argumento aparte de self, que hace referencia a la instancia actual de la clase Producto. Esto significa que el método se aplica a una instancia específica de Producto para mostrar sus atributos.
#se utiliza una cadena de formato para crear una cadena que incluye información sobre el producto. 
#Los valores de los atributos privados nombre, precioVenta, precioCosto y ganancia se insertan en la cadena de formato utilizando las llaves {}. 
    def mostrarProducto(self):
        return f'Nombre: {self.__nombre} - Precio de venta: ${self.__precioVenta} - Precio de costo: ${self.__precioCosto} - Ganancia: ${self.__ganancia}'




