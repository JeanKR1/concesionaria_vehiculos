# Laboratorio N.º 1 — Sistema de Vehículos (POO en Python)

Este proyecto implementa un sistema de **Concesionaria** aplicando **POO** (Herencia, Polimorfismo y Encapsulamiento) en Python.

## Estructura
```text
concesionaria_vehiculos/
├── concesionaria/
│   ├── __init__.py
│   ├── vehiculo.py
│   ├── auto.py
│   ├── moto.py
│   └── camion.py
├── main.py
└── README.md
```

## Requisitos
- Python 3.10+ recomendado (funciona desde 3.8).

## Cómo ejecutar
1. Abrir una terminal en la carpeta `concesionaria_vehiculos`.
2. Ejecutar:
   ```bash
   python main.py
   ```
3. Verás el catálogo en la salida de la consola.

## Notas de la rúbrica
- **Encapsulamiento:** el atributo `__precio` es privado, con `get_precio` y `set_precio` con validación (> 0).
- **Herencia y Polimorfismo:** `Auto`, `Moto` y `Camion` heredan de `Vehiculo` y sobreescriben `descripcion()`.
- **Concesionaria:** administra una lista de vehículos, calcula total y muestra catálogo.
- **Main:** instancia los vehículos, usa el setter y muestra el catálogo.

## Compresión para entrega
Puedes comprimir el directorio completo `concesionaria_vehiculos` en `.zip` y subirlo.
