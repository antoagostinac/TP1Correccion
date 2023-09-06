from claseFunciones import Funciones as f
from claseTienda import Tienda
from claseComestible import Comestible

#El codigo comienza importando clases y funciones de otros modulos.
#Hay tres modulos llamados "claseFunciones", "claseTienda", y "claseProducto" 
#que contienen clases y funciones utilizadas en el programa.

listaProductosSinPrecioVenta = f.obtenerListaProductos()
#Se llama a la funcion obtenerListaProductos() del modulo "claseFunciones" para obtener una lista de productos. 
#Esta lista es una lista de diccionarios con informacion sobre productos.

elecSeccion = -1

# Se crean tres instancias de la clase Tienda llamadas tienda1, tienda2, y tienda3. 
# Estas tiendas se inicializan sin ningun producto inicialmente.
tienda1 = Tienda("Coronel", 2, "Moreno 1400", "Kiosco")
tienda2 = Tienda("Castillo", 3, "Maradona 1600", "Kiosco")
tienda3 = Tienda("Ortega", 1, "Belgrano 700", "Kiosco")

while(elecSeccion!=3):
#El codigo entra en un bucle while donde el usuario puede seleccionar entre tres opciones: "Seccion Tiendas", "Seccion Productos" o "Salir". 
#Dependiendo de la opcion elegida, se ejecutan diferentes acciones.
    #primera opcion seccion tiendas
    elecSeccion = int(input("1-Seccion Tiendas\n2-Seccion Productos\n3-Salir\nSeleccione: "))
    if(elecSeccion==1):
        #seccion tiendas
        #seleccionar tienda
        elecTienda=-1
        #Si el usuario selecciona la "Seccion Tiendas", se muestra un submenu donde el usuario puede seleccionar una tienda entre 
        #"Tienda Coronel," "Tienda Castillo," y "Tienda Ortega." 
        while(elecTienda!=4):
            elecTienda = int(input("1-Tienda Coronel\n2-Tienda Castillo\n3-Tienda Ortega\n4-Atras\nSeleccione: "))
            if(elecTienda==1):
                #Dependiendo de la tienda seleccionada, se muestra otro submenu donde el usuario puede realizar operaciones
                #como agregar un nuevo producto o actualizar el precio de un producto existente en esa tienda.
                elecOpcionT=-1
                while(elecOpcionT!=3):
                    elecOpcionT = int(input("1-Agregar nuevo producto\n2-Actualizar precio\n3-Atras\nSeleccione: "))
                    if(elecOpcionT==1):
                        #Se muestra la lista de productos para que la tienda pueda elegir que producto agregar
                        print(f.listaProductosATexto(listaProductosSinPrecioVenta))
                        nombreProducto = input("Ingrese el nombre del producto que desea agregar: ")
                        precio = float(input("Ingrese el precio que le pondria al producto para la venta: "))
                        producto1=""
                        for producto in listaProductosSinPrecioVenta:
                            if(nombreProducto==(producto.get("nombre"))):
                                #Se crea una instancia de Comestible
                                producto1 = Comestible(nombreProducto, producto.get("precioCosto"), producto.get("fechaVencimiento"), precio)
                                break
                        #Se agrega el producto a la tienda
                        tienda1.agregarProducto(producto1, precio)
                        #Se muestra la lista de productos de la tienda actualizada
                        print(tienda1.mostrarListaProductos())
                    elif(elecOpcionT==2):
                        #Se obtiene la lista de Productos de la tienda
                        listaPro=tienda1.get("listaProductos")
                        #Se muestran los productos actuales en la tienda
                        print(tienda1.mostrarListaProductos())
                        nombreProducto = input("Ingrese el nombre del producto que desea actualizar el precio: ")
                        precio = float(input("Ingrese el precio que le pondria al producto: "))
                        bandera=False
                        for producto in listaPro:
                            if(nombreProducto==producto.get("nombre")):
                                bandera=True
                        #Si encuentra el producto en la lista de productos de la tienda
                        #entonces permite actualizar su precio
                        if(bandera):
                            tienda1.actualizarPrecio(nombreProducto, precio)
            elif(elecTienda==2):
                #Dependiendo de la tienda seleccionada, se muestra otro submenu donde el usuario puede realizar operaciones
                #como agregar un nuevo producto o actualizar el precio de un producto existente en esa tienda.
                elecOpcionT=-1
                while(elecOpcionT!=3):
                    elecOpcionT = int(input("1-Agregar nuevo producto\n2-Actualizar precio\n3-Atras\nSeleccione: "))
                    if(elecOpcionT==1):
                        print(f.listaProductosATexto(listaProductosSinPrecioVenta))
                        nombreProducto = input("Ingrese el nombre del producto que desea agregar: ")
                        precio = float(input("Ingrese el precio que le pondria al producto: "))
                        producto1=""
                        for producto in listaProductosSinPrecioVenta:
                            if(nombreProducto==(producto.get("nombre"))):
                                producto1 = Comestible(nombreProducto, producto.get("precioCosto"), producto.get("fechaVencimiento"), precio)
                                break
                        tienda2.agregarProducto(producto1, precio)
                        print(tienda2.mostrarListaProductos())
                    elif(elecOpcionT==2):
                        listaPro=tienda2.get("listaProductos")
                        print(tienda2.mostrarListaProductos())
                        nombreProducto = input("Ingrese el nombre del producto que desea actualizar el precio: ")
                        precio = float(input("Ingrese el precio que le pondria al producto: "))
                        bandera=False
                        for producto in listaPro:
                            if(nombreProducto==producto.get("nombre")):
                                bandera=True
                        if(bandera):
                            tienda2.actualizarPrecio(nombreProducto, precio)
            elif(elecTienda==3):
                #Dependiendo de la tienda seleccionada, se muestra otro submenu donde el usuario puede realizar operaciones
                #como agregar un nuevo producto o actualizar el precio de un producto existente en esa tienda.
                elecOpcionT=-1
                while(elecOpcionT!=3):
                    elecOpcionT = int(input("1-Agregar nuevo producto\n2-Actualizar precio\n3-Atras\nSeleccione: "))
                    if(elecOpcionT==1):
                        print(f.listaProductosATexto(listaProductosSinPrecioVenta))
                        nombreProducto = input("Ingrese el nombre del producto que desea agregar: ")
                        precio = float(input("Ingrese el precio que le pondria al producto: "))
                        producto1=""
                        for producto in listaProductosSinPrecioVenta:
                            if(nombreProducto==(producto.get("nombre"))):
                                producto1 = Comestible(nombreProducto, producto.get("precioCosto"), producto.get("fechaVencimiento"), precio)
                                break
                        tienda3.agregarProducto(producto1, precio)
                        print(tienda3.mostrarListaProductos())
                    elif(elecOpcionT==2):
                        listaPro=tienda3.get("listaProductos")
                        print(tienda3.mostrarListaProductos())
                        nombreProducto = input("Ingrese el nombre del producto que desea actualizar el precio: ")
                        precio = float(input("Ingrese el precio que le pondria al producto: "))
                        bandera=False
                        for producto in listaPro:
                            if(nombreProducto==producto.get("nombre")):
                                bandera=True
                        if(bandera):
                            tienda3.actualizarPrecio(nombreProducto, precio)
    elif(elecSeccion==2):
        #Si el usuario selecciona la "Seccion Productos" el programa muestra una lista de productos disponibles 
        #en cada tienda y luego calcula la media de precios de un producto especifico seleccionado por el usuario en todas las tiendas.
        print(tienda1.mostrarListaProductos())
        print(tienda2.mostrarListaProductos())
        print(tienda3.mostrarListaProductos())
        listaTiendas = [tienda1, tienda2, tienda3]
        nombreProducto = input("Seleccione el nombre del producto que desea calcular la media entre la lista de Tiendas: ")
        #Se llama al metodo estatico calcularMedia para obtener el promedio del producto
        mediaProducto = f.calcularMedia(listaTiendas, nombreProducto)
        print(f"La media del producto {nombreProducto} es {mediaProducto:.2f}")
        
    #El programa permite al usuario salir del bucle principal seleccionando la opcion numero 3 "Salir" en el menu principal.
