import os
import sys
from estructuras import crearRegistroEntrada, crearMovimiento
from datetime import datetime
from archivos import cargarProductos, cargarMovimientos, cargarEntradas, guardarProductos, guardarMovimientos, guardarEntradas

productos = cargarProductos()
entradas = cargarEntradas()
movimientos = cargarMovimientos()

def controlInventario(): 
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            print(""" 
====================================================================================================================
                                            CONTROL DE INVENTARIO     
====================================================================================================================
""")
            opcion = int(input(""" 
            Elija una opción:
            1. Consultar existencias de productos
            2. Registrar Entradas de Inventario
            3. Actualizar Cantidades disponibles
            4. Productos Sctock Mínimo
            5. Historial de Movimientos de Inventario
            6. Regresar a Menú Principal
            7. Salir
            Opción: """))

            os.system("cls" if os.name == "nt" else "clear")
            match opcion:
                case 1:
                    consultarExistencias()
                case 2:
                    registroEntradas()
                case 3: 
                    actualizar()
                case 4:
                    stockProductos()
                case 5:
                    historialMovimientos()
                case 6:
                    return
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

def consultarExistencias():
    print(""" 
====================================================================================================================
                                                    EXISTENCIAS DE PRODUCTOS    
====================================================================================================================""")

    if productos:
        print(
            f"{'Código':<10} "
            f"{'Producto':<75} "
            f"{'':<15} "
            f"{'Existencia':>12}"  
        )
        print("-" * 115)
    
        for val in productos:
            if val['cantidad'] > 0 and val['estado'] == "Activo":
                print(
                    f"{val['codigo']:<10} "
                    f"{val['nombre']:<75} "
                    f"{'':<15} "
                    f"{val['cantidad']:^12} "
                )

        print("-" * 115)
        input("\n\nPresione Enter para continuar...")
    
    else:
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return

def registroEntradas():
    print(""" 
====================================================================================================================
                                                REGISTRO DE ENTRADAS   
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

        if len(entradas) == 0:
            correlativo = 1
        else:
            correlativo = entradas[-1]["documento"] + 1

        detalle = []
        fecha = datetime.now().strftime('%d/%m/%Y')
        print(f"Número de Documento: {correlativo}")
        print("Fecha de Venta: ", fecha)
        observacion = input("Ingrese una observacion (Opcional): ")
  
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
OPERACIÓN CANCELADA: EL DOCUMENTO NO SE GUARDÓ
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
OPERACIÓN CANCELADA: EL DOCUMENTO NO SE GUARDÓ
====================================================================================================================""")
                        input("\nPresione Enter para continuar...")
                        return
                    else:
                        break
                continue

            productoDuplicado = False
            for value in detalle:
                if codigo == value['codigo']:
                    productoDuplicado = True
                    break  

            if productoDuplicado:
                print("\033[32mNo puede ingresar el mismo producto dos veces.\033[0m")
                print("Por favor ingrese un producto diferente.")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    if len(detalle) == 0:
                        print("""
====================================================================================================================
OPERACIÓN CANCELADA: EL DOCUMENTO NO SE GUARDÓ
====================================================================================================================""")
                        input("\nPresione Enter para continuar...")
                        return
                    else:
                        break  
                continue  


            while True:  
                cantidad = validarTexto("Ingrese cantidad: ")
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor que cero.")
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
                    print(f"Error:El precio debe ser mayor que cero.")
                    continue
                break

            
            detalle.append({
                    "codigo": productoEncontrado["codigo"],
                    "nombre": productoEncontrado["nombre"],
                    "cantidad": cantidad,
                    "precio": precio
            })

            agregarProducto = validarOpcion("¿Desea agregar otro producto? (Si/No): ")
            if not agregarProducto:
                break

        guardar = validarOpcion("¿Desea guardar el documento? (Si/No): ")
        if guardar:    
            print("""
====================================================================================================================
                                            RESUMEN DE REGISTRO DE ENTRADA
====================================================================================================================""")
            print("Número de documento: ", correlativo)
            print("Fecha: ", fecha)
            print("Observación: ", observacion)
            print("""
====================================================================================================================
                                                        DETALLE 
====================================================================================================================""")
            print(
                f"{'Código':<10} "
                f"{'Producto':<75} "
                f"{'Cantidad':<15} "
                f"{'Precio':>12}"  
            )
            print("-" * 115)
            for item in detalle:
                print(
                    f"{item['codigo']:<10} "
                    f"{item['nombre']:<75} "
                    f"{item['cantidad']:^15} "
                    f"{item['precio']:>12.2f} "
                )

                #ACTUALIZACION Y GUARDA EL DOCUMENTO
            for item in detalle:
                for prod in productos:
                    if prod['codigo'] == item['codigo']:
                        prod['cantidad'] += item['cantidad']
                        prod['precio'] = item['precio']

                              
                        tipoMovimiento = "Entrada"
                        descripcion = f"Ingreso de producto por documento No. {correlativo}"
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
            entrada = crearRegistroEntrada(correlativo, fecha, observacion, detalle)
            entradas.append(entrada)
            guardarEntradas(entradas)
            guardarProductos(productos)

            print("""
====================================================================================================================
                                        DOCUMENTO GUARDADO CON ÉXITO
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
        else:
            print("""
====================================================================================================================
                                                OPERACION CANCELADA
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
    else:
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return

def actualizar():
    print(""" 
====================================================================================================================
                                                    ACTUALIZAR EXISTENCIAS   
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

        detalle = []
        fecha = datetime.now().strftime('%d/%m/%Y')
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

            if productoEncontrado['estado'] != 'Activo':
                print("\033[33mEl producto se encuentra inactivo.\033[0m")
                intento = validarOpcion("¿Desea intentar con otro producto? (Si/No): ")
                if not intento:
                    print("""
====================================================================================================================
                                                    OPERACIÓN CANCELADA
====================================================================================================================""")
                    input("\nPresione Enter para continuar...")
                    return
                continue
            
            print(f"\033[32mExistencia Actual: \033[0m", int(productoEncontrado['cantidad']))
            while True:  
                cantidad = validarTexto("Ingrese cantidad: ")
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor que cero.")
                    continue          
                break
            

            detalle.append({
                'codigo': productoEncontrado['codigo'],
                'nombre': productoEncontrado['nombre'],
                'cantidad': cantidad  
            })

            agregarProducto = validarOpcion("¿Desea agregar otro producto? (Si/No): ")
            if not agregarProducto:
                break

        guardar = validarOpcion("¿Desea guardar el documento? (Si/No): ")
        if guardar:    
            print("""
====================================================================================================================
                                                    DATOS ACTUALIZADOS
====================================================================================================================""")
            print(
                f"{'Código':<10} "
                f"{'Producto':<75} "
                f"{'':<15} "
                f"{'Existencia':>12}"  
            )
            print("-" * 115)
                
            for item in detalle:
                print(
                    f"{item['codigo']:<10} "
                    f"{item['nombre']:<75} "
                    f"{'':<15} "
                    f"{item['cantidad']:^12} "
                )

            print("-" * 115)
                #ACTUALIZACION 
            for item in detalle:
                for prod in productos:
                    if prod['codigo'] == item['codigo']:
                        prod['cantidad'] = item['cantidad']
                              
                        tipoMovimiento = "Ajuste"
                        descripcion = f"Ajuste por descuadre"
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
            guardarProductos(productos)

            print("""
====================================================================================================================
                                            ACTUALIZADO CON ÉXITO
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
        else:
            print("""
====================================================================================================================
                                                    OPERACION CANCELADA 
====================================================================================================================""")
            input("\nPresione Enter para continuar...")
            return
    else:        
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return

def stockProductos():
    print(""" 
====================================================================================================================
                                                    STOCK MINIMO   
====================================================================================================================""")
    if productos:
        print(
            f"{'Código':<10} "
            f"{'Producto':<75} "
            f"{'Disponible':<15} "
            f"{'Stock Minímo':>12}"  
        )
        print("-" * 115)
        for val in productos:
            if val['cantidad'] <= val['stock'] and val['estado'] == "Activo":
                print(
                    f"{val['codigo']:<10} "
                    f"{val['nombre']:<75} "
                    f"{val['cantidad']:^15} "
                    f"{val['stock']:^12}"
                )

        print("-" * 115)
        input("\n\nPresione Enter para continuar...")
        return
    else:
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return


def historialMovimientos():
    print("""
=====================================================================================================
                                        HISTORIAL DE MOVIMIENTOS
=====================================================================================================""")
    if movimientos:
        print(f"\n{'Fecha':<12} {'Tipo':<15}  {'Descripción':<45} {'Código':<12} {'Cantidad':^12}")
        print("-" * 100)

        for val in movimientos:

            if val['tipo'] == "Entrada":
                color = "\033[32m"
            elif val['tipo'] == "Salida":
                color = "\033[31m"
            else:
                color = "\033[33m"

            print(
                f"{color}"
                f"{val['fecha']:<12} "
                f"{val['tipo']:<15} "
                f"{val['descripcion']:<45} "
                f"{val['codigoProducto']:^12} "
                f"{val['cantidad']:^12}"
                "\033[0m"
            )

        print("-" * 100)        
        input("\nPresione Enter para continuar...")
    else:
        print("No hay movimientos registrados.")
        input("\nPresione Enter para continuar...")
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