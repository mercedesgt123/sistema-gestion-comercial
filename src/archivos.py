import os
import pprint

productos = []
ventas = []
movimientos = []
datosInventario = []

# ==================== RUTAS ====================
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



# ==================== PRODUCTOS ====================
def guardarProductos(productos_actualizados):
    global productos 

    productos = productos_actualizados  
    
    with open(RUTA_PRODUCTOS, "w", encoding="utf-8") as f:
        f.write("productos = ")
        f.write(
            pprint.pformat(
                productos_actualizados,
                indent=4,
                sort_dicts=False
            )
        )
        f.write("\n")

def cargarProductos():
    global productos
    datos = {}
    try:
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
            exec(f.read(), datos)
        productos = datos.get("productos", [])  
        return productos
    except FileNotFoundError:
        productos = []
        return []


    
# ==================== VENTAS ====================
def guardarVentas(ventas_actualizadas):
    global ventas  
    ventas = ventas_actualizadas
    
    with open(RUTA_VENTAS, "w", encoding="utf-8") as f:
        f.write("ventas = ")
        f.write(
            pprint.pformat(
                ventas_actualizadas,
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


# ==================== MOVIMIENTOS ====================
def guardarMovimientos(movimientos_actualizados):
    global movimientosInventario  
    movimientosInventario = movimientos_actualizados
    
    with open(RUTA_MOVIMIENTOS, "w", encoding="utf-8") as f:
        f.write("movimientosInventario = ")
        f.write(
            pprint.pformat(
                movimientos_actualizados,
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

# ==================== ENTRADAS/INVENTARIO ====================
def guardarEntradas(entradas_actualizadas):
    global datosInventario 
    datosInventario = entradas_actualizadas
    
    with open(RUTA_ENTRADAS, "w", encoding="utf-8") as f:
        f.write("datosInventario = ")
        f.write(
            pprint.pformat(
                entradas_actualizadas,
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