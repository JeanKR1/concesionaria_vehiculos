"""
Módulo: auto.py
- Clase Auto hereda de Vehiculo (Herencia) y sobrescribe descripcion (Polimorfismo).
"""
from __future__ import annotations
from .vehiculo import Vehiculo

class Auto(Vehiculo):
    """
    Clase hija que representa un Auto.
    Atributo adicional:
        - puertas (int): número de puertas del auto.
    """
    def __init__(self, marca: str, modelo: str, precio: float, puertas: int) -> None:
        super().__init__(marca, modelo, precio)  # Llamada al constructor de la clase base (Herencia)
        if not isinstance(puertas, int) or puertas <= 0:
            raise ValueError("El número de puertas debe ser un entero positivo.")
        self.puertas = puertas

    # Polimorfismo: sobreescritura del método de la clase base
    def descripcion(self) -> str:
        return f"Auto marca {self.marca}, modelo {self.modelo}, {self.puertas} puertas"
