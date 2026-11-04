# Sistema de Gestión Comercial

Sistema de consola desarrollado en Python para administrar una pequeña empresa: productos, ventas, inventario y reportes estadísticos. Los datos se guardan en archivos, por lo que se conservan entre una ejecución y otra.

## Funcionalidades

- **Gestión de productos:** registrar, consultar por código, listar, modificar y desactivar productos. No permite nombres repetidos ni valores negativos.
- **Registro de ventas:** valida existencias, calcula subtotal, IVA del 12 % y total, genera un número de documento, actualiza el inventario y guarda la venta.
- **Control de inventarios:** consultar existencias, registrar entradas, actualizar cantidades, ver productos en stock mínimo y consultar el historial de movimientos.
- **Reportes y estadísticas:** listado general, productos en stock mínimo, historial de ventas, total de ingresos, producto más vendido, valor total del inventario y promedio de ventas.

## Requisitos

- Python **3.10 o superior** (el menú usa `match-case`).
- No requiere instalar librerías externas: usa solo `os`, `sys`, `datetime` y `pprint`, que vienen con Python.
- Sistema operativo: Windows, Linux o macOS.

## Cómo ejecutar

```bash
git clone https://github.com/mercedesgt123/sistema-gestion-comercial.git
cd sistema-gestion-comercial/src
python main.py
```

Se abre el menú principal. Para salir, elija la opción **5 (Salir)** y confirme con `S`.

> La carpeta `src/datos/` debe existir, porque ahí se guardan los datos. El repositorio incluye archivos de ejemplo para poder probar el sistema de inmediato.

## Menú del sistema

| Opción | Módulo | Qué permite |
|---|---|---|
| 1 | Gestión de Productos | Registrar, consultar, listar, modificar y desactivar productos |
| 2 | Registro de Ventas | Registrar una venta con subtotal, IVA y total |
| 3 | Control de Inventarios | Existencias, entradas, ajustes, stock mínimo e historial |
| 4 | Reportes y Estadísticas | Siete reportes del negocio |
| 5 | Salir | Cierra el programa (pide confirmación) |

## Reglas principales

- El código del producto se asigna automáticamente (consecutivo).
- No se permiten productos con el mismo nombre (sin distinguir mayúsculas).
- Precio, cantidad y stock mínimo deben ser números mayores que cero.
- Un producto **inactivo** no se puede vender ni recibir entradas; desactivar no lo elimina.
- No se puede vender más de la existencia disponible. El inventario se descuenta solo al guardar la venta.
- IVA del 12 % sobre el subtotal, redondeado a dos decimales. Ejemplo: subtotal Q8.90, IVA Q1.07, total Q9.97.

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
├── docs/
│   ├── analisis/          # análisis de procesos
│   ├── diagramas/         # diagramas de flujo
│   ├── manual-tecnico.pdf
│   └── manual-usuario.pdf
└── evidencias/            # capturas de las pruebas
```

## Documentación

| Documento | Ubicación |
|---|---|
| Manual técnico | [docs/manual-tecnico.pdf](docs/manual-tecnico.pdf) |
| Manual de usuario | [docs/manual-usuario.pdf](docs/manual-usuario.pdf) |
| Análisis de procesos | [docs/analisis/](docs/analisis/) |
| Diagramas de flujo | [docs/diagramas/](docs/diagramas/) |
| Pruebas y evidencias | [evidencias/](evidencias/) |

## Pruebas

Se ejecutaron pruebas normales y de situaciones excepcionales, con capturas de pantalla en [`evidencias/`](evidencias/):

- Registrar un producto con datos válidos.
- Intentar registrar un producto duplicado.
- Ingresar cantidades negativas o datos de tipo incorrecto.
- Intentar vender más unidades de las disponibles.
- Consultar un producto inexistente.
- Verificar los resultados de los cálculos y de los reportes.
- Entre otros

## Trabajo en GitHub

- **Commits:** mensajes descriptivos del trabajo realizado.
- **Rama y pull request:** el módulo de ventas se desarrolló en la rama `feature/modulo-ventas` y se integró a `main` mediante un pull request: [COMPLETAR: enlace al pull request].
- **Issues:** [COMPLETAR: enlace a un problema detectado y a una mejora pendiente].
- **Versión final:** [COMPLETAR: enlace al release o etiqueta, por ejemplo v1.0].

## Limitaciones conocidas

- Los reportes muestran los datos cargados al iniciar el programa; para ver una venta reciente hay que reiniciarlo.
- La carpeta `src/datos/` no se crea sola; si falta, el programa falla al guardar.
- Los datos se guardan como archivos de Python y se leen con `exec()`, por lo que no deben editarse a mano ni provenir de fuentes no confiables.
- Está pensado para un solo usuario a la vez.
