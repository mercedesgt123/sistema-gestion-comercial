# Sistema de Gestión Comercial

Sistema de consola desarrollado en Python para administrar una pequeña empresa: productos, ventas, inventario y reportes estadísticos. Los datos se guardan en archivos, por lo que se conservan entre una ejecución y otra.


**Gestión de productos:** registrar, consultar por código, listar, modificar y desactivar productos. No permite nombres repetidos ni valores negativos.
**Registro de ventas:** valida existencias, calcula subtotal, IVA del 12 % y total, genera un número de venta, actualiza el inventario y guarda la venta.
**Control de inventarios:** consultar existencias, registrar entradas, actualizar cantidades, ver productos en stock mínimo y consultar el historial de movimientos.
**Reportes y estadísticas:** listado general, productos en stock mínimo, historial de ventas, total de ingresos, producto más vendido, valor total del inventario y promedio de ventas.

## Requisitos

    Python **3.10 o superior** (el menú usa `match-case`).
    No requiere instalar librerías externas: usa solo `os`, `sys`, `datetime` y `pprint`, que vienen con Python.
    Sistema operativo: Windows, Linux o macOS.

## Cómo ejecutar
```bash
git clone [COMPLETAR: URL del repositorio]
cd [COMPLETAR: nombre-del-repositorio]/src
python main.py
```

Se abre el menú principal. Para salir, elija la opción **5 (Salir)** y confirme con `S`.

> La carpeta `src/datos/` debe existir, porque ahí se guardan los datos. El repositorio incluye archivos de ejemplo para poder probar el sistema de inmediato.

## Estructura del repositorio
```text
sistema-gestion-comercial/
├── README.md
├── .gitignore
├── src/
│   ├── main.py            # menú principal
│   ├── productos.py       # módulo 1: gestión de productos
│   ├── ventas.py          # módulo 2: registro de ventas
│   ├── inventario.py      # módulo 3: control de inventarios
│   ├── reportes.py        # módulo 4: reportes y estadísticas
│   ├── estructuras.py     # creación de registros
│   ├── archivos.py        # carga y guardado de datos
│   └── datos/             # archivos de datos
└── docs/
    ├── analisis/          # análisis de procesos
    ├── diagramas/         # diagramas de flujo
    ├── manual-tecnico.md
    ├── manual-usuario.md
    └── evidencias/        # capturas de las pruebas
```

## Documentación
| Documento | Ubicación |
|---|---|
| Manual técnico | [docs/manual-tecnico.pdf](docs/manual-tecnico.pdf) |
| Manual de usuario | [docs/manual-usuario.pdf](docs/manual-usuario.pdf) |
| Análisis de procesos | [docs/analisis/](docs/analisis/) |
| Diagramas de flujo | [docs/diagramas/](docs/diagramas/) |
| Pruebas y evidencias | [docs/evidencias/](docs/evidencias/) |

## Pruebas

Se ejecutaron pruebas normales y de situaciones excepcionales, con capturas de pantalla en `docs/evidencias/`:

- Registrar un producto con datos válidos.
- Intentar registrar un producto duplicado.
- Ingresar cantidades negativas o datos de tipo incorrecto.
- Intentar vender más unidades de las disponibles.
- Consultar un producto inexistente.
- Verificar los resultados de los cálculos y de los reportes.

## Trabajo en GitHub

- **Commits:** mensajes descriptivos del trabajo realizado.
- **Rama y pull request:** la funcionalidad feature/modulo-ventas y se integró a main mediante un pull request. y se integró mediante un pull request.
- **Issues:** por ejemplo #2: no se permite modificar los datos de una venta ya registrada.
- **Versión final:** v1.0..

## Limitaciones conocidas
Los datos se guardan como archivos de Python y se leen con exec(), por lo que no deben editarse a mano ni provenir de fuentes no confiables.
Está pensado para un solo usuario a la vez.
