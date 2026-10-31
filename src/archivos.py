import os
import pprint

RUTA_PRODUCTOS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "datos",
    "datosProductos.py"   
)

RUTA_VENTAS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "datos",
    "datosVentas.py"
)

RUTA_MOVIMIENTOS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "datos",
    "movimientosInventario.py"
)

RUTA_ENTRADAS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "datos",
    "datosInventario.py"
)

def guardarProductos(productos):
    with open(RUTA_PRODUCTOS, "w", encoding="utf-8") as f:
        f.write("productos = ")
        f.write(
            pprint.pformat(
                productos,
                indent=4,
                sort_dicts=False
            )
        )
        f.write("\n")

def cargarProductos():
    datos = {}
    try:
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
            exec(f.read(), datos)

        return datos.get("productos", [])

    except FileNotFoundError:
        return []

def guardarVentas(ventas):
    with open(RUTA_VENTAS, "w", encoding="utf-8") as f:
        f.write("ventas = ")
        f.write(
            pprint.pformat(
                ventas,
                indent=4,
                sort_dicts=False
            )
        )
        f.write("\n")

def cargarVentas():
    datos = {}
    try:
        with open(RUTA_VENTAS, "r", encoding="utf-8") as f:
            exec(f.read(), datos)

        return datos.get("ventas", [])

    except FileNotFoundError:
        return []

def guardarMovimientos(movimientosInventario):
    with open(RUTA_MOVIMIENTOS, "w", encoding="utf-8") as f:
        f.write("movimientosInventario = ")
        f.write(
            pprint.pformat(
                movimientosInventario,
                indent=4,
                sort_dicts=False
            )
        )
        f.write("\n")


def cargarMovimientos():
    datos = {}
    try:
        with open(RUTA_MOVIMIENTOS, "r", encoding="utf-8") as f:
            exec(f.read(), datos)

        return datos.get("movimientosInventario", [])

    except FileNotFoundError:
        return []


def guardarEntradas(datosInventario):
    with open(RUTA_ENTRADAS, "w", encoding="utf-8") as f:
        f.write("datosInventario = ")
        f.write(
            pprint.pformat(
                datosInventario,
                indent=4,
                sort_dicts=False
            )
        )
        f.write("\n")

def cargarEntradas():
    datos = {}
    try:
        with open(RUTA_ENTRADAS, "r", encoding="utf-8") as f:
            exec(f.read(), datos)

        return datos.get("datosInventario", [])

    except FileNotFoundError:
        return []