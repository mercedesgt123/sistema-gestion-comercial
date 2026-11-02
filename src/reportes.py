import os
import sys
from datetime import datetime
from archivos import cargarProductos, cargarMovimientos, cargarEntradas, cargarVentas

productos = cargarProductos()
entradas = cargarEntradas()
movimientos = cargarMovimientos()
ventas =  cargarVentas()

def estadisticasReportes(): 
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            print(""" 
====================================================================================================================
                                            CONTROL DE INVENTARIO     
====================================================================================================================""")
            opcion = int(input(""" 
Elija una opción:
1. Reporte general de productos
2. Reporte de productos con existencias iguales o inferiores al stock mínimo
3. Reporte historial de venta
4. Reporte total de ingresos por ventas
5. Reporte de producto con mayor cantidad de unidades vendidas
6. Reporte de Valor total del inventario disponible
7. Reporte Promedio de ventas por período
8. Regresar a Menú Principal
9. Salir

Opción: """))

            os.system("cls" if os.name == "nt" else "clear")
            match opcion:
                case 1:
                    reporteProductos()
                case 2:
                    reporteExistenciaStock()
                case 3: 
                    reporteHistorialVenta()
                case 4:
                    reporteIngresosVentas()
                case 5:
                    reporteProductoVenta()
                case 6: 
                    reporteTotalInventario()
                case 7: 
                    reportePromedioVentas()
                case 8:
                    return
                case 9:
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

def reporteProductos():
    print(""" 
====================================================================================================================
                                                    REPORTE DE PRODUCTOS  
====================================================================================================================""")
    if productos:
        print(
            f"{'Código':<10} "
            f"{'Producto':<28} "
            f"{'Categoría':<27} "
            f"{'Precio':<10} "
            f"{'Existencia':<10}"  
            f"{'Stock':>10} "
            f"{'Estado':>15} "
        )
        print("-" * 116)

        for item in productos:
            print(
                f"{item['codigo']:<10} "
                f"{item['nombre']:<28} "
                f"{item['categoria']:<27} "
                f"Q.{item['precio']:<10.2f} "
                f"{item['cantidad']:>8}"  
                f"{item['stock']:>10} "
                f"{item['estado']:>15} "
            )
        print("-" * 116)
        input("\nPresione Enter para continuar...")
    else: 
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return

def reporteExistenciaStock():
    print(""" 
====================================================================================================================
                        REPORTE DE PRODUCTOS CON EXISTENCIA IGUAL O INFERIOR AL STOCK MÍNIMO   
====================================================================================================================""")
    if productos:
        print(
            f"{'Código':<10} "
            f"{'Producto':<28} "
            f"{'Categoría':<27} "
            f"{'':<10} "
            f"{'Existencia':>10} "
            f"{'Stock':>10} "
            f"{'Estado':>15} "
        )
        print("-" * 116)

        contador = 0

        for item in productos:
            if item['cantidad'] <= item['stock']:
                contador += 1
                print(
                    f"{item['codigo']:<10} "
                    f"{item['nombre']:<28} "
                    f"{item['categoria']:<27} "
                    f"{'':<9} "  
                    f"{item['cantidad']:>10} "
                    f"{item['stock']:>10} "
                    f"{item['estado']:>15} "
                )
        print("-" * 116)
        input("\nPresione Enter para continuar...")
    else: 
        print("No hay Productos Registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return



def reporteHistorialVenta():
    print("""
====================================================================================================================
                                        REPORTE DE HISTORIAL DE VENTAS                                              
====================================================================================================================""")
    if ventas:
        print(
            f"{'Documento':<28} "
            f"{'Fecha':<68} "
            f"{'Total':>18}"
        )
        print("-" * 116)

        for item in ventas:
            print(
                f"{item['correlativoVenta']:<28} "
                f"{item['fecha']:<68} "
                f"Q.{item['total']:>15.2f}"
            )
        print("-" * 116)
        input("\nPresione Enter para continuar...")
    else:
        print("No hay Ventas Registradas en el Historial.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")

def reporteIngresosVentas():
    print("""
====================================================================================================================
                                            REPORTE TOTAL DE INGRESOS POR VENTA
====================================================================================================================""")

    if ventas:
        print(
            f"{'Documento':<10} "
            f"{'':<28} "
            f"{'Fecha':<27} "
            f"{'':<10} "
            f"{'':>10} "
            f"{'':>10} "
            f"{'Total':>15}"
        )

        print("-" * 116)

        for item in ventas:
            print(
                f"{item['correlativoVenta']:<10} "
                f"{'':<28} "
                f"{item['fecha']:<27} "
                f"{'':<10} "
                f"{'':>10} "
                f"{'':>10} "
                f"Q.{item['total']:>12.2f}"
            )

        print("-" * 116)

        totalVentas = 0
        for item in ventas:
            totalVentas += item["total"] 


        print(
            f"{'':<90}"
            f"Total Ingresos Q.{totalVentas:>8.2f}"
        )

        print("====================================================================================================================")
        input("\nPresione Enter para continuar...")
    else:
        print("No hay datos registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")

def reporteProductoVenta():
    print("""
====================================================================================================================
                                REPORTE DE PRODUCTO CON MAYOR CANTIDAD DE UNIDADES VENDIDAS
====================================================================================================================""")

    if ventas:
        codigoMayor = ""
        nombreMayor = ""
        cantidadMayor = 0

        productosVendidos = {}

        for venta in ventas:
            for item in venta["detalle"]:

                codigo = item["codigo"]

                if codigo not in productosVendidos:
                    productosVendidos[codigo] = {
                        "nombre": item["nombre"],
                        "cantidad": item["cantidad"]
                    }
                else:
                    productosVendidos[codigo]["cantidad"] += item["cantidad"]

        for codigo, datos in productosVendidos.items():

            if datos["cantidad"] > cantidadMayor:
                cantidadMayor = datos["cantidad"]
                codigoMayor = codigo
                nombreMayor = datos["nombre"]

        print(
            f"{'Código':<20}"
            f"{'Producto':<60}"
            f"{'Cantidad':>20}"
        )

        print("-" * 116)

        print(
            f"{codigoMayor:<20}"
            f"{nombreMayor:<60}"
            f"{cantidadMayor:>20}"
        )

        print("====================================================================================================================" )
        input("\nPresione Enter para continuar...")
    else:
        print("No hay datos registrados.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")

def reporteTotalInventario():
    print("""
====================================================================================================================
                                    REPORTE VALOR TOTAL DEL INVENTARIO DISPONIBLE
====================================================================================================================""")

    if productos:
        valorTotalGeneral = 0

        print(
            f"{'Código':<20}"
            f"{'Producto':<45}"
            f"{'Cantidad':>12}"
            f"{'Precio Unit. (Q)':>18}"
            f"{'Subtotal (Q)':>18}"
        )
        print("-" * 116)

        for prod in productos:
            if prod['estado'] == "Activo":
                cantidad = prod["cantidad"]
                precioUnitario = prod["precio"]
                subtotal = cantidad * precioUnitario
                valorTotalGeneral += subtotal

                print(
                    f"{prod['codigo']:<20}"
                    f"{prod['nombre']:<45}"
                    f"{cantidad:>12}"
                    f"{precioUnitario:>18,.2f}"
                    f"{subtotal:>18,.2f}"
                )

        print("-" * 116) 
        if valorTotalGeneral > 0:
            print(
                f"{'TOTAL GENERAL':<77}"
                f"{valorTotalGeneral:>39,.2f}"
            )
        else:
            print("No hay productos activos en el inventario.")
        
        print("====================================================================================================================")
        input("\nPresione Enter para continuar...")
        print("====================================================================================================================")
    else:
        print("No hay productos registrados en el inventario.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return

def reportePromedioVentas():
    print("""
====================================================================================================================
                            REPORTE PROMEDIO DE VENTAS POR PERÍODO — DATOS REGISTRADOS
====================================================================================================================""")

    if ventas:
        totalVentas = 0
        montoTotalGeneral = 0

        print(
            f"{'No':<8}"
            f"{'Fecha / Período':<30}"
            f"{'Monto Total Venta (Q)':>38}"
            f"{'Cantidad de Artículos':>30}"
        )
        print("-" * 116)

        indice = 1
        for venta in ventas:
            totalVentas = totalVentas + 1
            montoVenta = venta["total"]
            fecha = venta["fecha"]
            
            cantidadArticulos = 0
            for item in venta["detalle"]:
                cantidadArticulos = cantidadArticulos + item["cantidad"]
            
            montoTotalGeneral = montoTotalGeneral + montoVenta

            print(
                f"{indice:<8}"
                f"{fecha:<30}"
                f"{montoVenta:>38,.2f}"
                f"{cantidadArticulos:>30}"
            )
            indice = indice + 1

        promedioPorVenta = montoTotalGeneral / totalVentas

        print("-" * 116)
        print(
            f"{'TOTALES':<38}"
            f"{montoTotalGeneral:>38,.2f}"
        )
        print(
            f"{'PROMEDIO POR VENTA (Q)':<38}"
            f"{promedioPorVenta:>76,.2f}"
        )
        print("====================================================================================================================")
        input("\nPresione Enter para continuar...")
    else:
        print("No hay ventas registradas para calcular el promedio.")
        print("====================================================================================================================")
        input("Presione Enter para continuar...")
        return
