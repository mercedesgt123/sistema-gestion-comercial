import os
import pprint
from archivos import productos 
import main
 
RUTA_ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archivos.py")
def guardar_productos(lista):
    """Reescribe archivo.py con la lista de productos."""
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        f.write("productos = " + pprint.pformat(lista, sort_dicts=False))

def gestionProductos():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            opcion = int(input(""" 
==================================================
            MÓDULO GESTION DE PRODUCTOS
==================================================

Elija una opción:
1. Registrar Producto
2. Consultar Producto por Código
3. Listado de Productos
4. Modificar Producto
5. Desactivar Producto
6. Regresar a Menú Principal
7. Salir

Escriba una Opción: """))

            os.system("cls" if os.name == "nt" else "clear")
            match opcion:
                case 1:
                    registroProducto()
                case 2:
                    buscarProducto()
                case 3: 
                    listaProductos()
                case 4: 
                    modificarProducto()
                case 5:
                    desactivarProducto()
                case 6:
                    main.menuPrincipal()
                case 7:
                    print("""
==================================================
                    SALIR
==================================================""")
                    while True:
                        cerrar = input(
                        "¿Desea continuar?\n"
                        "[N] Continuar\n"
                        "[S] Salir\n"
                        "Seleccione una opción: ").strip().upper()

                        if cerrar == "N":
                            break
                        elif cerrar == "S":
                            print("Saliendo...")
                            return 
                        else:
                            print("Error: Debe ingresar únicamente S o N.")
                case _:
                    print("Opción no válida.")
                    input("\nPresione Enter para continuar...")
        except ValueError:
            print("Error: Debe ingresar únicamente números.")
            input("Presione Enter para continuar...")
                
def registroProducto():
    print("""
==================================================
                REGISTRAR PRODUCTO
==================================================""")

    if len(productos) == 0:
        codigo = 1
    else:
        codigo = productos[-1]["codigo"] + 1
    print("Código Producto: ", codigo)

    while True:
        nombre = input("Ingrese el nombre del Producto: ").strip().capitalize()
        if nombre != "":
            break
        print("Error: Debe ingresar el nombre del producto.")

    while True:
        categoria = input("Ingrese la categoría del Producto: ").strip()
        if categoria != "":
            break
        print("Error: Debe ingresar la categoría del producto.")

    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio > 0:
                break
            print("Error: El precio no puede ser negativo")
        except ValueError:
            print("Debe ingresar un valor válido.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible: "))
            if cantidad > 0:
                break
            print("Error: La cantidad disponible no puede ser negativa")
        except ValueError:
            print("Debe ingresar un valor válido.")

    while True:
        try:
            stock = int(input("Ingrese el stock mínimo: "))
            if stock > 0:
                break
            print("Error: La cantidad de stock no puede ser negativa.")
        except ValueError:
            print("Debe ingresar un valor válido.")
    
    while True:
        estado = input("Ingrese el estado del producto (Activo/Inactivo): ").strip().capitalize()
        if estado in ["Activo", "Inactivo"]:
            break
        print("Error: Debe ingresar 'Activo' o 'Inactivo'.")
        

    for value in productos:
        if nombre.lower() == value['nombre'].lower():
            print("No puede ingresar porductos duplicados.")
            input("Presione Enter para continuar...")
            return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad,
        "stock": stock,
        "estado": estado
    }

    productos.append(producto)
    guardar_productos(productos)
    print("""
==================================================")
            PRODUCTO REGISTRADO CON EXITO
==================================================""")
    input("Presione Enter para continuar...")

def buscarProducto():
    print("""
==================================================
                 CONSULTAR PRODUCTO
==================================================""")
    if productos:
        while True:
            try:
                buscar = int(input("Ingrese código del producto:  "))

                encontrado = 0
                for val in productos:
                    if val['codigo'] == buscar:
                        encontrado += 1
                        print("""
==================================================
            INFORMACION DEL PRODUCTO
==================================================""")
                        print("Código             : ", val['codigo'])
                        print("Nombre             : ", val['nombre'])
                        print("Categoría          : ", val['categoria'])
                        print("Precio             :  Q.", val['precio'])
                        print("Cantidad Disponible: ", val['cantidad'])
                        print("Stock Mínimo       : ", val['stock'])
                        print("Estado             : ", val['estado'])
                        print("==================================================")
                        input("Presione Enter para continuar...")
                        return

                if encontrado == 0:
                    print("""
==================================================
            INFORMACION DEL PRODUCTO
==================================================""")
                    print("Producto no encontrado.")
                    print("==================================================")
                    input("Presione Enter para continuar...")
                    return
                
            except ValueError:
                print("Debe ingresar un valor válido.")

def listaProductos():
    print("""
==========================================================================================
                                    LISTADO DE PRODUCTOS 
==========================================================================================""")
    if productos:
        print(f"\n\n{'Código':<8} {'Nombre':<20} {'Categoría':<15} {'Precio':<10} {'Cantidad':<10} {'Stock':<8} {'Estado':<10}")
        print("-" * 90)

        for val in productos:
            print(
                f"{val['codigo']:<8} "
                f"{val['nombre']:<20} "
                f"{val['categoria']:<15} "
                f"Q{val['precio']:<9.2f} "
                f"{val['cantidad']:^10} "
                f"{val['stock']:^8} "
                f"{val['estado']:<10}"
            )
        print("-" * 90)
        input("\n\nPresione Enter para continuar...")

    else:
        print("No hay productos registrados.")
    

def modificarProducto():
    print("""
==================================================
            MODIFICACION DE PRODUCTO 
==================================================""")
    if productos: 
        while True:
            try:
                buscar = int(input("Ingrese código del producto:  "))
                break
            except ValueError:
                print("Debe ingresar un valor válido.")   
                
        encontrado = 0    
        for val in productos:
            if val['codigo'] == buscar:
                encontrado += 1
                os.system("cls" if os.name == "nt" else "clear")
                print("""
==================================================
            INGRESO LOS NUEVOS DATOS 
==================================================""")
                while True:
                    try:
                        precio = float(input("\nIngrese el precio: "))
                        if precio > 0:
                            break
                        print("Error: El precio no puede ser negativo")
                    except ValueError:
                        print("Debe ingresar un valor válido.")

                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad disponible: "))
                        if cantidad > 0:
                            break
                        print("Error: La cantidad disponible no puede ser negativa")
                    except ValueError:
                        print("Debe ingresar un valor válido.")

                while True:
                    try:
                        stock = int(input("Ingrese el stock mínimo: "))
                        if stock > 0:
                            break
                        print("Error: La cantidad de stock no puede ser negativa.")
                    except ValueError:
                        print("Debe ingresar un valor válido.")    
    
                val['precio'] = precio
                val['cantidad'] = cantidad
                val['stock'] = stock
                guardar_productos(productos)
        
                print("""
==================================================
            DATOS ACTUALIZADOS CON EXITO
==================================================""")
                input("\nPresione Enter para continuar...")
                return

        if encontrado == 0:
            print("""
==================================================
            PRODUCTO NO ENCOTRADO
==================================================""")
            input("Presione Enter para continuar...")
            return
    else: 
        print("No hay Productos Registrados.")
                    
def desactivarProducto():
    print("""
==================================================
                DESACTIVAR PRODUCTO 
==================================================""")
    if productos: 
        while True:
            try:
                codigo = int(input("Ingrese código del producto:  "))
                break
            except ValueError:
                print("Debe ingresar un valor válido.")  

        encontrado = 0
        for val in productos:
            if codigo == val['codigo']:
                if val['estado'] == "Inactivo":
                    print("""
==================================================                
El producto se encuentra inactivo.
==================================================""")                 
                    input("Presione Enter para continuar...")
                    return
                encontrado += 1

                while True:
                    opcion = input("¿Desea desactivar el producto? (Si/No): ").strip().capitalize()

                    if opcion == "No":
                        print("""
==================================================                
                Operación cancelada
==================================================""")
                        input("Presione Enter para continuar...")
                        return                    
                    
                    if opcion == "Si":
                        break
                
                    print("Error: Debe ingresar 'Si' o 'No'.")

                val['estado'] = 'Inactivo'
                guardar_productos(productos)
                print("""
==================================================                
El producto fue desactivado correctamente.
==================================================""")
                input("Presione Enter para continuar...")
                return

        if encontrado == 0:
            print("""
==================================================                
Producto no encontrado.
==================================================""")
            input("Presione Enter para continuar...")
            return
        
    else:
        print("No hay productos registrados.")
