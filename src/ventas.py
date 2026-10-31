import os
import sys
from estructuras import crearVenta, crearMovimiento
from datetime import datetime
from archivos import cargarProductos, cargarVentas, cargarMovimientos, guardarProductos, guardarVentas, guardarMovimientos

productos = cargarProductos()
ventas = cargarVentas()
movimientos = cargarMovimientos()

def gestionVentas(): 
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            print("""
====================================================================================================================
                                                    REGISTRO DE VENTAS
====================================================================================================================""")
            opcion = int(input(""" 
Elija una opción:
1. Registrar Venta
2. Regresar a Menú Principal
3. Salir
Opción: """))

            os.system("cls" if os.name == "nt" else "clear")
            match opcion:
                case 1:
                    registroVentas()
                case 2:
                    return
                case 3:
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
                            return
                        else:
                            print("Error: Debe ingresar únicamente S o N.")
                case _:
                    print("Opción no válida.")
                    input("\nPresione Enter para continuar...")

        except ValueError:
            print("Error: Debe ingresar únicamente números.")
            input("Presione Enter para continuar...")

def registroVentas():
    print("""
====================================================================================================================
                                                    CREACION DE VENTAS
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

        if len(ventas) == 0:
            correlativo = 1
        else:
            correlativo = ventas[-1]["correlativoVenta"] + 1

        subtotalGeneral = 0
        detalle = []
        fecha = datetime.now().strftime('%d/%m/%Y')
        print(f"Número de Documento: {correlativo}")
        print("Fecha de Venta: ", fecha)

        print("""
====================================================================================================================
                                                    DETALLE DE VENTA
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
                    if len(detalle) == 0:
                        print("""
====================================================================================================================
                                                    OPERACIÓN CANCELADA
====================================================================================================================""")
                        input("\nPresione Enter para continuar...")
                        return
                    else:
                        break  
                continue  

            if productoEncontrado['estado'] != 'Activo':
                print("\033[33mEl producto se encuentra inactivo.\033[0m")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    if len(detalle) == 0:
                        print("""
====================================================================================================================
                                                    OPERACIÓN CANCELADA
====================================================================================================================""")
                        input("\nPresione Enter para continuar...")
                        return
                    else:
                        break
                continue

            cantidadValida = False
            terminarVenta = False
            while True:  
                cantidad = validarTexto("Ingrese cantidad: ")
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor que cero.")
                    continue  

                if productoEncontrado['cantidad'] <= 0:
                    print(f"\033[31mNo hay existencias. Disponible: {productoEncontrado['cantidad']}\033[0m")
                    intento = validarOpcion("¿Desea ingresar otro producto? (Si/No): ")
                    if not intento:
                        if len(detalle) == 0:
                            print("""
====================================================================================================================
                                                    OPERACIÓN CANCELADA
====================================================================================================================""")
                            input("\nPresione Enter para continuar...")
                            return
                        else:
                            terminarVenta = True  
                            break  
                    else:
                        break  

                elif cantidad > productoEncontrado['cantidad']:
                    print("\033[31mInventario insuficiente\033[0m")
                    print(f"\033[31mCantidad Disponible: {productoEncontrado['cantidad']}\033[0m")
                    continue  
                else:
                    cantidadValida = True
                    break  

            if terminarVenta:
                break  

            if not cantidadValida:
                continue 

            productoDuplicado = False
            for value in detalle:
                if codigo == value['codigo']:
                    value['cantidad'] += cantidad
                    value['subtotal'] += cantidad * productoEncontrado['precio']

                    for total in detalle:
                        subtotalGeneral += total['subtotal']
                        
                    productoDuplicado = True 
                    break 

            if not productoDuplicado:
                subtotalProducto = cantidad * productoEncontrado['precio']
                subtotalGeneral += subtotalProducto
                detalle.append({
                    "codigo": productoEncontrado["codigo"],
                    "nombre": productoEncontrado["nombre"],
                    "precio": productoEncontrado["precio"],
                    "cantidad": cantidad,
                    "subtotal": subtotalProducto
                })


            agregarProducto = validarOpcion("¿Desea agregar otro producto? (Si/No): ")
            if not agregarProducto:
                break  

        iva = round(subtotalGeneral * 0.12, 2)
        totalVenta = round(subtotalGeneral + iva, 2)
        guardar = validarOpcion("¿Desea guardar el documento? (Si/No): ")
        if guardar:    
            print("""
====================================================================================================================
                                                RESUMEN DE VENTA
====================================================================================================================""")
            print(
                f"{'Código':<10} "
                f"{'Producto':<75} "
                f"{'Cantiad':<15} "
                f"{'Total':>12}"  
            )
                
            for item in detalle:
                print(f"{item['codigo']:<10} {item['nombre']:<75}{item['cantidad']:^15} {item['subtotal']:>12.2f}")
                print("-" * 115)
            print(f"Subtotal : Q.{subtotalGeneral:.2f}")
            print(f"IVA 12%  : Q.{iva:.2f}")
            print(f"Total    : Q.{totalVenta:.2f}")
            print("====================================================================================================================")

            #ACTUALIZACION Y GUARDA EL DOCUMENTO
            for item in detalle:
                for prod in productos:
                    if prod['codigo'] == item['codigo']:
                        prod['cantidad'] -= item['cantidad']

                              
                        tipoMovimiento = "Salida"
                        descripcion = f"Salida de Venta por pedido No. {correlativo}"
                        movimiento = crearMovimiento(
                            fecha,
                            tipoMovimiento,
                            descripcion,
                            item['codigo'],
                            item['cantidad']
                        )
                        movimientos.append(movimiento)
                        break

            guardarMovimientos(movimientos)
            registroVenta = crearVenta(correlativo, fecha, totalVenta, detalle)
            ventas.append(registroVenta)
            guardarVentas(ventas)
            guardarProductos(productos)
            
            print("""
====================================================================================================================
                                                DOCUMENTO GUARDADO CON ÉXITO
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
        else:
            print("""
====================================================================================================================
OPERACION CANCELADA: EL DOCUMENTO NO SE GUARDO
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
    else:
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
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

