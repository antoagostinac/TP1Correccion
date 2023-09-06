#Azul
#explicar clase abstracta por que
class Edificio():
    #explicar constructor, definir por que los atributos son privados
    def __init__(self, nombre, cantidadPisos, direccion):
        self.__nombre = nombre
        self.__cantidadPisos = cantidadPisos
        self.__direccion = direccion
    #explicar get
    def get(self, name):
        if(name=="nombre"):
            return self.__nombre
        elif(name=="cantidadPisos"):
            return self.__cantidadPisos
        elif(name=="direccion"):
            return self.__direccion
    #explicar set
    def set(self, name, valor):
        if(name=="nombre"):
            self.__nombre = valor
        elif(name=="cantidadPisos"):
            self.__cantidadPisos = valor
        elif(name=="direccion"):
            self.__direccion = valor
    #explicar por que metodo publico
    def mostrarInformacion(self):
        return f'Nombre: {self.__nombre}\nCantidad de pisos: {self.__cantidadPisos}\nDireccion: {self.__direccion}'





