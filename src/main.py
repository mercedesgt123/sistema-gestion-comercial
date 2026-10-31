#Funciones para importar mòdulos
import os
import productos
import ventas
import inventario
import reportes

def menuPrincipal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        try:
            opcion = int(input(""" 
====================================================================================================================

                                            SISTEMA DE GESTIÓN COMERCIAL

====================================================================================================================

    
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
                    ventas.gestionVentas()
                case 3:
                    inventario.controlInventario()
                case 4: 
                    reportes.estadisticasReportes()
                case 5:
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
                            return
                        else:
                            print("Error: Debe ingresar únicamente S o N.")
                case _:
                    print("Opción no válida.")
                    input("\nPresione Enter para continuar...")

        except ValueError:
            print("Error: Debe ingresar únicamente números.")
            input("Presione Enter para continuar...")

menuPrincipal()