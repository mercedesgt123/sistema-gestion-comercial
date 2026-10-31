def crearProducto(codigo, nombre, categoria, cantidad, precio, stock, estado):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
        "stock": stock,
        "estado": estado
    }


def crearVenta(correlativo, fecha, total, detalle):
    return {
        "correlativoVenta": correlativo,
        "fecha": fecha,
        "total": total,
        "detalle": detalle
    }

def crearMovimiento(fecha, tipoMovimiento, descripcion, codigo,  cantidad):
    return{
        "fecha": fecha,
        "tipo" : tipoMovimiento,
        "descripcion": descripcion,
        "codigoProducto": codigo,
        "cantidad": cantidad
    }

def crearRegistroEntrada(documento, fecha, observacion, detalle):
    return{
        "documento": documento, 
        "fecha": fecha,
        "observacion": observacion,
        "detalle": detalle
    }