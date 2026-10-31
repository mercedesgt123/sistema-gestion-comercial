import os
from archivos import guardarProductos, cargarProductos
from estructuras import crearProducto
import sys

productos =  cargarProductos()
def gestionProductos():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            opcion = int(input(""" 
====================================================================================================================
                                                    MÓDULO GESTION DE PRODUCTOS
====================================================================================================================
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
                    return
                    #import main
                    #main.menuPrincipal()
                case 7:
                    print("""
====================================================================================================================
                                                                 SALIR
====================================================================================================================""")
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
                            sys.exit()
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
====================================================================================================================
                                                    REGISTRAR PRODUCTO
====================================================================================================================""")
    print("Presione 0 si desea salir")
    opcion = input("Ingrese opción: ").strip().upper()
    if opcion == "0":
        print("""
====================================================================================================================
                                                    OPERACIÓN CANCELADA
====================================================================================================================""")
        input("\nPresione Enter para continuar...")
        return

    print("""
====================================================================================================================
                                                    INGRESO DE DATOS 
====================================================================================================================""")
    if len(productos) == 0:
        codigo = 1
    else:
        codigo = productos[-1]["codigo"] + 1
    print("Código Producto: ", codigo)

    producto = []  
    while True:
        nombre = ingresarTexto("Ingrese nombre del producto: ")

        productoDuplicado = False
        for val in productos:
            if val['nombre'].lower() == nombre.lower():
                productoDuplicado = val
                break  

        if productoDuplicado:
            print("\033[31mProducto Duplicado.\033[0m")
            intento = validarOpcion("¿Desea intentar con otro nombre? (Si/No): ")
            if not intento:
                if len(producto) == 0:
                    print("""
====================================================================================================================
OPERACIÓN CANCELADA: PRODUCTO NO GUARDADO
====================================================================================================================""")
                    input("\nPresione Enter para continuar...")
                    return
                else:
                    break  
            continue 

        categoria = ingresarTexto("Ingrese categoría del producto: ")
          
        while True:  
            cantidad = validarTexto("Ingrese cantidad: ")
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor que cero.")
                continue          
            break

        while True:  
            stock = validarTexto("Ingrese stock mínimo: ")
            if stock <= 0:
                print("Error: El stock debe ser mayor que cero.")
                continue          
            break

        while True:
            entrada = input("Ingrese precio: ").strip()
            if not entrada:
                print("Error: Precio no puede estar vacío.")
                continue

            try:
                precio = float(entrada)
            except ValueError:
                print("Error: Debe ingresar un valor válido.")
                continue

            if precio <= 0:
                print("Error: El precio debe ser mayor que cero.")
                continue
            break
        
        while True:
            estado = input("Ingrese el estado del producto (Activo/Inactivo): ").strip().capitalize()
            if estado in ["Activo", "Inactivo"]:
                break
            print("Error: Debe ingresar 'Activo' o 'Inactivo'.")

        prod = crearProducto(codigo, nombre, categoria, cantidad, precio, stock, estado)
        producto.append(prod)
        
        agregarProducto = validarOpcion("¿Desea agregar otro producto? (Si/No): ")
        if not agregarProducto:
            break

        codigo += 1
        print("Código Producto: ", codigo)

    guardar = validarOpcion("¿Desea guardar los datos? (Si/No): ")
    if guardar:    
        print("""
====================================================================================================================
                                                RESUMEN DE PRODUCTO
====================================================================================================================""")
        print(
            f"{'Código':<10} "
            f"{'Nombre':<25} "
            f"{'Categoría':<25} "
            f"{'Cantidad':^10} "
            f"{'Stock Mínimo':<15} "
            f"{'Precio':>12} "
            f"{'Estado':<12}"
        )

        print("-" * 115)
        
        for item in producto:
            print(
                f"{item['codigo']:<10} "
                f"{item['nombre']:<25} "
                f"{item['categoria']:<25} "
                f"{item['cantidad']:^10} "
                f"{item['stock']:<15} "
                f"Q{item['precio']:>12.2f} "  
                f"{item['estado']:<12}"
            )
        
        for p in producto:
            productos.append(p)
        
        guardarProductos(productos)

        print("""
====================================================================================================================
                                            ***DATOS GUARDADOS CON ÉXITO***
====================================================================================================================""")
        input("\nPresione Enter para continuar...")
    else:
        print("""
====================================================================================================================
OPERACION CANCELADA
====================================================================================================================""")
        input("\nPresione Enter para continuar...") 
        return               

def buscarProducto():
    print("""
====================================================================================================================
                                                        CONSULTAR PRODUCTO
====================================================================================================================""")
    if productos:
        print("Presione 0 si desea salir")
        opcion = input("Ingrese opción: ").strip().upper()
        if opcion == "0":
            print("""
====================================================================================================================
                                                        OPERACIÓN CANCELADA
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
            return
        print("""
====================================================================================================================
                                                    INGRESE DATO A BUSCAR
====================================================================================================================""")

        while True:
            codigo = validarTexto("Ingrese código del producto: ")

            productoEncontrado = False
            for val in productos:
                if val['codigo'] == codigo:
                    productoEncontrado = val
                    break  

            print("""
====================================================================================================================
                                            INFORMACION DE PRODUCTO
====================================================================================================================""")
            print(
                    f"{'Código':<10} "
                    f"{'Nombre':<25} "
                    f"{'Categoría':<25} "
                    f"{'Cantidad':^10} "
                    f"{'Stock Mínimo':<15} "
                    f"{'Precio':>12} "
                    f"{'Estado':>12}"
                )
            print("-" * 115)

            if productoEncontrado:
                print(
                    f"{productoEncontrado['codigo']:<10} "
                    f"{productoEncontrado['nombre']:<25} "
                    f"{productoEncontrado['categoria']:<25} "
                    f"{productoEncontrado['cantidad']:^10} "
                    f"{productoEncontrado['stock']:^15} "
                    f"{productoEncontrado['precio']:>12} "
                    f"{productoEncontrado['estado']:>12}"
                )
                print("-" * 115)
            else: 
                print("Producto no encontrado")
                print("-" * 115)

            buscaOtro = validarOpcion("¿Desea buscar otro producto? (Si/No): ")
            if not buscaOtro:
                break  
    else:
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return


def listaProductos():
    print("""
====================================================================================================================
                                                    LISTADO DE PRODUCTOS 
====================================================================================================================""")
    if productos:
        print(
            f"{'Código':<10} "
            f"{'Nombre':<25} "
            f"{'Categoría':<25} "
            f"{'Cantidad':^10} "
            f"{'Stock Mínimo':<15} "
            f"{'Precio':>12} "
            f"{'Estado':>12}"
            )
        print("-" * 115)
            
        for val in productos:
            print(
                f"{val['codigo']:<10} "
                f"{val['nombre']:<25} "
                f"{val['categoria']:<25} "
                f"{val['cantidad']:^10} "
                f"{val['stock']:^15} "
                f"{val['precio']:>12} "
                f"{val['estado']:>12}"
            )

        print("-" * 115)
        input("\n\nPresione Enter para continuar...")
    else:
        print("No hay Productos Registrados.")
        print("==========================================================================================")
        input("Presione Enter para continuar...")
        return

def modificarProducto():
    print("""
====================================================================================================================
                                        MODIFICACION DE PRODUCTO 
====================================================================================================================""")
    if productos:
        print("Presione 0 si desea salir")
        opcion = input("Ingrese opción: ").strip().upper()
        if opcion == "0":
            print("""
====================================================================================================================
                                            OPERACIÓN CANCELADA
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
            return

        print("""
====================================================================================================================
                                            INGRESO DE DATOS 
====================================================================================================================""")

        while True:
            codigo = validarTexto("Ingrese código del producto: ")

            productoEncontrado = False
            for val in productos:
                if val['codigo'] == codigo:
                    productoEncontrado = val
                    break  

            if not productoEncontrado:
                print("\033[31mProducto no encontrado.\033[0m")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    print("""
====================================================================================================================
OPERACIÓN CANCELADA
====================================================================================================================""")
                    input("\nPresione Enter para continuar...")
                    return  
                continue 

            categoria = ingresarTexto("Ingrese categoría del producto: ")
              
            while True:  
                stock = validarTexto("Ingrese stock mínimo: ")
                if stock > 0:
                    break
                print("Error: El stock debe ser mayor que cero.")
              
            while True:
                entrada = input("Ingrese precio: ").strip()
                if not entrada:
                    print("Error: Precio no puede estar vacío.")
                    continue
                try:
                    precio = float(entrada)
                    if precio > 0:
                        break
                    print("Error: El precio debe ser mayor que cero.")
                except ValueError:
                    print("Error: Debe ingresar un valor válido.")

            guardar = validarOpcion("¿Desea guardar los cambios de este producto? (Si/No): ")
            if guardar:  
                productoEncontrado['categoria'] = categoria
                productoEncontrado['stock'] = stock
                productoEncontrado['precio'] = precio
                
                print("""
====================================================================================================================
                                   SE ACTUALIZARON LOS DATOS
====================================================================================================================""")
                print(
                    f"{'Código':<10} "
                    f"{'Categoría':<75} "
                    f"{'Stock Mínimo':<15} "
                    f"{'Precio':>12}"  
                )
                print("-" * 115)
                print(
                    f"{productoEncontrado['codigo']:<10} "
                    f"{productoEncontrado['categoria']:<75} "
                    f"{productoEncontrado['stock']:^15} "
                    f"{productoEncontrado['precio']:>12.2f}"  
                )
                print("-" * 115)

                guardarProductos(productos)
                print("Cambios guardados exitosamente.")
            else: 
                print("""
====================================================================================================================
OPERACIÓN CANCELADA: LOS CAMBIOS NO SE GUARDARON
====================================================================================================================""")

            otro = validarOpcion("¿Desea modificar otro producto? (Si/No): ")
            if not otro:
                break 

        input("\nPresione Enter para continuar...")
        return  
    else:              
        print("No hay Productos Registrados.")
        print("==========================================================================================")
        input("Presione Enter para continuar...")
        return

        
def desactivarProducto():
    print("""
====================================================================================================================
                                             DESACTIVAR DE PRODUCTO 
====================================================================================================================""")
    if productos:
        print("Presione 0 si desea salir")
        opcion = input("Ingrese opción: ").strip().upper()
        if opcion == "0":
            print("""
====================================================================================================================
                                                OPERACIÓN CANCELADA
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
            return

        print("""
====================================================================================================================
                                            INGRESO DE DATOS 
====================================================================================================================""")

        while True:
            codigo = validarTexto("Ingrese código del producto: ")

            productoEncontrado = False
            for val in productos:
                if val['codigo'] == codigo:
                    productoEncontrado = val
                    break  

            if not productoEncontrado:
                print("\033[31mProducto no encontrado.\033[0m")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    print("""
====================================================================================================================
OPERACIÓN CANCELADA
====================================================================================================================""")
                    input("\nPresione Enter para continuar...")
                    return  
                continue 

            if productoEncontrado['estado'] == "Inactivo":
                print("\033[31mEl producto ya se encuentra inactivo\033[0m")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    print("""
====================================================================================================================
OPERACIÓN CANCELADA
====================================================================================================================""")
                    input("\nPresione Enter para continuar...")
                    return  
                continue 


            while True:
                estado = input("Ingrese el estado del producto (Inactivo): ").strip().capitalize()
                if estado == "Inactivo":
                    break
                print("Error: Debe ingresar 'Inactivo'.")


              
           

            guardar = validarOpcion("¿Desea guardar los cambios de este producto? (Si/No): ")
            if guardar:  
                productoEncontrado['estado'] = estado
                
                print("""
====================================================================================================================
                                   SE ACTUALIZARON LOS DATOS
====================================================================================================================""")
                print(
                    f"{'Código':<10} "
                    f"{'':<75} "
                    f"{'':<15} "
                    f"{'Estado':>12}"  
                )
                print("-" * 115)
                print(
                    f"{productoEncontrado['codigo']:<10} "
                    f"{'':<75} "
                    f"{'':^15} "
                    f"{productoEncontrado['estado']:>12}"  
                )
                print("-" * 115)

                guardarProductos(productos)
                print("Cambios guardados exitosamente.")
            else: 
                print("""
====================================================================================================================
OPERACIÓN CANCELADA: LOS CAMBIOS NO SE GUARDARON
====================================================================================================================""")

            otro = validarOpcion("¿Desea modificar otro producto? (Si/No): ")
            if not otro:
                break 

        input("\nPresione Enter para continuar...")
        return  
    else:              
        print("No hay Productos Registrados.")
        print("==========================================================================================")
        input("Presione Enter para continuar...")
        return



def validarTexto(datos):
    while True:
        entrada = input(datos).strip()  
   
        if entrada == "":
            print("Error: El campo no puede estar vacío.")
            continue
        
        if not entrada.isdigit():
            print("Error: Debe ingresar únicamente números.")
            continue
        
        valor = int(entrada)
        return valor
       

def validarOpcion(mensaje):
    while True:
        valor = input(mensaje).strip().capitalize()
        if valor in ("Si", "No"):
            return valor == "Si"
        print("Error: Escriba 'Si' o 'No'.")

def ingresarTexto(mensaje):
    while True:
        valor = input(mensaje).strip().capitalize()
        if valor != "":
            return valor
        print("Error: Debe ingresar un valor. No puede quedar vacío.")