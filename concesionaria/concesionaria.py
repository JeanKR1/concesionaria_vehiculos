"""
Módulo: concesionaria.py
- Clase Concesionaria que gestiona una colección de Vehiculos.
"""
from __future__ import annotations
from typing import List
from .vehiculo import Vehiculo

class Concesionaria:
    """
    Clase principal que administra el catálogo de vehículos de la concesionaria.

    Responsabilidades:
        - Almacenar una lista de vehículos.
        - Agregar vehículos al catálogo.
        - Mostrar el catálogo y calcular el total.
    """
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._vehiculos: List[Vehiculo] = []

    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """
        Agrega un vehículo al catálogo. 
        Acepta cualquier instancia que derive de Vehiculo (Polimorfismo de tipos).
        """
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("Solo se pueden agregar instancias de Vehiculo o sus subclases.")
        self._vehiculos.append(vehiculo)

    def calcular_total(self) -> float:
        """Retorna el valor total de todos los vehículos en el catálogo."""
        return sum(v.get_precio() for v in self._vehiculos)

    def mostrar_catalogo(self) -> str:
        """
        Devuelve un reporte en texto del catálogo actual con descripción y precio.
        También incluye el total acumulado de la concesionaria.
        """
        if not self._vehiculos:
            return f"Concesionaria {self.nombre} - Catálogo vacío."

        lineas = [f"Concesionaria {self.nombre} - Catálogo de Vehículos", "-" * 60]
        for idx, veh in enumerate(self._vehiculos, start=1):
            # Nota: descripcion() es polimórfico: cada subclase imprime lo suyo.
            lineas.append(f"{idx}. {veh.descripcion()} -> Precio: ${veh.get_precio():,.2f}")
        lineas.append("-" * 60)
        lineas.append(f"TOTAL: ${self.calcular_total():,.2f}")
        return "\n".join(lineas)
