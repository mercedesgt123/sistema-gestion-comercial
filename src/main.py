#Funciones para importar mòdulos
import os
import productos

def menuPrincipal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        opcion = int(input(""" 
========================================================================
                        SISTEMA DE GESTIÓN COMERCIAL
========================================================================
    
                                MÓDULOS


1. Gestión de Productos
2. Registro de Ventas
3. Control de Inventarios
4. Reportes y Estadísticas
5. Salir

Escriba una Opción: """))

        os.system("cls" if os.name == "nt" else "clear")
        match opcion:
            case 1:
                productos.gestionProductos()
            case 2:
                print("Selecciono la opción: Registro de Ventas")
                gestionProductos()
            case 3:
                print("Selecciono la opción: Control de Inventarios")
                gestionVenta()
            case 4: 
                print("Selecciono la opción: Reportes y Estadísticas")
                reportes()
            case 5:
                print("""
==================================================
                    SALIR
==================================================""")
                cerrar = input(
                "¿Desea continuar?\n"
                "[N] Continuar\n"
                "[S] Salir\n"
                "Seleccione una opción: ").strip().upper()
                if cerrar == "N":
                    opcion
                else:
                    print("Saliendo.....")
                    break 
            case _:
                print("Opción no válida.")
                input("\nPresione Enter para continuar...")

menuPrincipal()