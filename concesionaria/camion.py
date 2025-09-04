"""
Módulo: camion.py
- Clase Camion hereda de Vehiculo (Herencia) y sobrescribe descripcion (Polimorfismo).
"""
from __future__ import annotations
from .vehiculo import Vehiculo

class Camion(Vehiculo):
    """
    Clase hija que representa un Camión.
    Atributo adicional:
        - capacidad_carga (float): capacidad de carga en toneladas.
    """
    def __init__(self, marca: str, modelo: str, precio: float, capacidad_carga: float) -> None:
        super().__init__(marca, modelo, precio)
        if not isinstance(capacidad_carga, (int, float)) or capacidad_carga <= 0:
            raise ValueError("La capacidad de carga debe ser un número positivo (en toneladas).")
        self.capacidad_carga = float(capacidad_carga)

    # Polimorfismo: sobreescritura del método de la clase base
    def descripcion(self) -> str:
        return f"Camión marca {self.marca}, modelo {self.modelo}, {self.capacidad_carga:.1f} toneladas de carga"
