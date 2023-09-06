#Azul
class Edificio():
#Se crea una clase edificio que es una clase abstracta que va ser plantilla para otra clase
    def __init__(self, nombre, cantidadPisos, direccion):
#El constructor toma tres argumentos nombre, cantidadPisos y direccion.
#Los atributo se definden como privado ya que solo pueden acceder desde dentro de la clase. 
#Estos argumentos se utiliza para inicializar los atributod del objeto __nombre,__cantidadPisos y __direccion. 
        self.__nombre = nombre
        self.__cantidadPisos = cantidadPisos
        self.__direccion = direccion
#Esto es un metodo get para la clase edificio se va utilizar para recuperar el valor de un atributo que seria name.
    def get(self, name):
        if(name=="nombre"):
            return self.__nombre
        elif(name=="cantidadPisos"):
            return self.__cantidadPisos
        elif(name=="direccion"):
            return self.__direccion
    def set(self, name, valor):
#Esto es metodo set para la clase edificio se utiliza para estabalecer el valor de un atributo.
#El metodo toma dos argumento name que especifica el nombre del atributo a establacer y valor que especifica el nuevo valor para el atributo.
        if(name=="nombre"):
            self.__nombre = valor
        elif(name=="cantidadPisos"):
            self.__cantidadPisos = valor
        elif(name=="direccion"):
            self.__direccion = valor
#Esto es un metodo publico llamado mostrarInformacio para la clase edificio .
#Un metodo publico puede ser accedido desde fuera de la clase y el metodo lo devuelve una cadena que contine infromacion sobre los atributos.
    def mostrarInformacion(self):
        return f'Nombre: {self.__nombre}\nCantidad de pisos: {self.__cantidadPisos}\nDireccion: {self.__direccion}'





