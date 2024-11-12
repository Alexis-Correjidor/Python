import itertools
import os
Idproducto:int
Nombre:str
Marca:str
Precio:float
Proveedor:str
Stock:int
Categoria:str
opcion:int
encontrado:bool
# Lista para almacenar los productos
productos = []
### Listar todos los Productos ###
def ver_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\nLista de productos:")
        for producto in productos:
            print(f"ID: {producto['Idproducto']}, Nombre: {producto['Nombre']}, Marca: {producto['Marca']}, Precio: {producto['Precio']}, Proveedor: {producto['Proveedor']},\nCategoría: {producto['Categoria']}, Stock: {producto['Stock']}\n") 
### Registrar nuevo producto ###
def agregar_producto():   
    while True:
        try:
            Idproducto = int(input("Ingrese el ID del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para el ID.")

    Nombre = input("Ingrese el nombre del producto: ")
    Marca = input("Ingrese la marca del producto: ")
    
    while True:
        try:
            Precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    Proveedor = input("Ingrese el proveedor del producto: ")

    while True:
        try:
            Stock = int(input("Ingrese el stock del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para el stock.")

    Categoria = input("Ingrese la categoría del producto: ")
    
    # Crear el producto como un diccionario y agregarlo a la lista
    producto = {
        "Idproducto": Idproducto,
        "Nombre": Nombre,
        "Marca": Marca,
        "Precio": Precio,
        "Proveedor": Proveedor,
        "Stock": Stock,
        "Categoria": Categoria
    }
    productos.append(producto)
    print("Producto agregado con éxito.\n")
### Eliminar un producto ###
def eliminar_producto():
    while True:
        try:
            Idproducto = int(input("Ingrese el ID del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para el ID.")
    for producto in productos:
        if producto["Idproducto"] == Idproducto:
            productos.remove(producto)
            print(f"Producto con ID {Idproducto} eliminado con éxito.\n")
            return
    print(f"No se encontró ningún producto con ID {Idproducto}.\n")
### Listar datos de un producto especifico ###
def producto_especifico():
    while True:
        try:
            Idproducto = int(input("Ingrese el ID del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para el ID.")
    for producto in productos:
        if producto["Idproducto"] == Idproducto:
            print(f"\nProducto con ID {Idproducto}.\n")
            print(f"Nombre: {producto['Nombre']} ,\nMarca: {producto['Marca']} ,\nPrecio: {producto['Precio']} ,\nProveedor: {producto['Proveedor']} ,\nCategoría: {producto['Categoria']} ,\nStock: {producto['Stock']}\n")
            return
    print(f"No se encontró ningún producto con ID {Idproducto}.\n")
### Modificar un producto ###
def modificar_producto():
    while True:
        try:
            Idproducto = int(input("Ingrese el ID del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para el ID.")
    for producto in productos:
        if producto["Idproducto"] == Idproducto:
            print(f"\nProducto con ID {Idproducto}\n")
            for _ in itertools.repeat(None):
                print("\nMenu Modificar:\n")
                print(f"1 - Modificar Nombre : {producto['Nombre']}")
                print(f"2 - Modificar Marca : {producto['Marca']}")
                print(f"3 - Modificar Precio : {producto['Precio']}")
                print(f"4 - Modificar Proveedor : {producto['Proveedor']}")
                print(f"5 - Modificar Categoria : {producto['Categoria']}")
                print(f"6 - Modificar Stock : {producto['Stock']}")
                print(f"7 - Salir de Modificar")
                while True:
                    try:
                        opcion = int(input("Ingresa el número de la opción que deseas: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")
                match opcion:
                    case 1:
                        producto["Nombre"]=input("Ingrese el nombre del producto: ")
                    case 2:
                        producto["Marca"] = input("Ingrese la marca del producto: ")
                    case 3:
                        try:
                            producto["Precio"] = float(input("Ingrese el precio del producto: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un número válido para el precio.")
                    case 4:
                        producto["Proveedor"]=input("Ingrese el proveedor del producto: ")
                    case 5:
                        producto["Categoria"]=input("Ingrese la categoría del producto: ")
                    case 6:
                        try:
                            producto["Stock"]=int(input("Ingrese el stock del producto: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un número entero válido para stock.")
                    case 7:
                        print("Opción seleccionada: Salir de Modificar")
                        os.system('cls')
                        break  
                    case _:
                        print("Opción no válida, intenta nuevamente.")
            return
    print(f"No se encontró ningún producto con ID {Idproducto}.\n")
### Listar producto con menor de 5 en stock ###
def lista_menorStock():
    encontrado = False
    for producto in productos:
        if producto["Stock"] < 5:
            print(f"ID: {producto['Idproducto']}, Nombre: {producto['Nombre']}, Marca: {producto['Marca']}, Precio: {producto['Precio']}, Proveedor: {producto['Proveedor']},\nCategoría: {producto['Categoria']}, Stock: {producto['Stock']}\n") 
            encontrado = True
    if not encontrado:
        print("No se encontró ningún Stock menor a 5.\n")
### Menu Principal ###
def menu():
    print("Menu de Gestion de Productos:\n")
    print("1 - Alta de nuevo producto")
    print("2 - Consulta de datos de producto")
    print("3 - Modificar producto")
    print("4 - Eliminar producto")
    print("5 - Listado completo de los productos")
    print("6 - Listado de productos con menor stock")
    print("7 - Salir")

for _ in itertools.repeat(None):
    menu()
    while True:
        try:
            opcion = int(input("Ingresa el número de la opción que deseas: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    os.system('cls') 
    match opcion:
        case 1:
            print("Opción seleccionada: Alta de nuevo producto")
            agregar_producto()
        case 2:
            print("Opción seleccionada: Consulta de datos de producto")
            producto_especifico()
        case 3:
            print("Opción seleccionada: Modificar producto")
            modificar_producto()
        case 4:
            print("Opción seleccionada: Eliminar producto")
            eliminar_producto()
        case 5:
            print("Opción seleccionada: Listado completo de los productos")
            ver_productos()
        case 6:
            print("Opción seleccionada: Listado de productos con menor stock")
            lista_menorStock()
        case 7:
            print("Opción seleccionada: Salir")
            break  
        case _:
            print("Opción no válida, intenta nuevamente.")
