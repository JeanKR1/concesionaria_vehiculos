"""
Módulo: moto.py
- Clase Moto hereda de Vehiculo (Herencia) y sobrescribe descripcion (Polimorfismo).
"""
from __future__ import annotations
from .vehiculo import Vehiculo

class Moto(Vehiculo):
    """
    Clase hija que representa una Moto.
    Atributo adicional:
        - cilindrada (int): cilindrada en centímetros cúbicos (cc).
    """
    def __init__(self, marca: str, modelo: str, precio: float, cilindrada: int) -> None:
        super().__init__(marca, modelo, precio)
        if not isinstance(cilindrada, int) or cilindrada <= 0:
            raise ValueError("La cilindrada debe ser un entero positivo (en cc).")
        self.cilindrada = cilindrada

    # Polimorfismo: sobreescritura del método de la clase base
    def descripcion(self) -> str:
        return f"Moto marca {self.marca}, modelo {self.modelo}, {self.cilindrada} cc"
