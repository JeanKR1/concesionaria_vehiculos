"""
Módulo: vehiculo.py
- Clase base Vehiculo con encapsulamiento en __precio.
- Ilustra principios de POO: Encapsulamiento, Abstracción y Polimorfismo (vía método descripcion).
"""
from __future__ import annotations

class Vehiculo:
    """
    Clase base (Padre) para representar un vehículo genérico.

    Atributos públicos:
        - marca (str)
        - modelo (str)
    Atributo encapsulado (privado):
        - __precio (float): usa name-mangling para prevenir acceso directo.

    Métodos:
        - get_precio(): retorna el precio actual (lectura controlada).
        - set_precio(nuevo_precio): valida y actualiza el precio (escritura controlada).
        - descripcion(): provee una descripción genérica del vehículo (polimórfica).
    """
    def __init__(self, marca: str, modelo: str, precio: float) -> None:
        self.marca = marca
        self.modelo = modelo
        # Usamos el setter para aplicar validaciones desde el inicio.
        self.__precio: float | None = None
        self.set_precio(precio)

    # ---------------- Encapsulamiento del atributo __precio -----------------
    def get_precio(self) -> float:
        """Retorna el precio actual del vehículo (acceso controlado)."""
        return float(self.__precio)  # type: ignore

    def set_precio(self, nuevo_precio: float) -> None:
        """
        Establece el precio si es válido (> 0). 
        Aplica validaciones para mantener la integridad del estado.
        """
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número (int o float).")
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = float(nuevo_precio)

    # -------------------- Polimorfismo mediante descripcion ------------------
    def descripcion(self) -> str:
        """
        Descripción genérica. Las clases hijas sobreescriben este método 
        (polimorfismo) para agregar sus propios detalles.
        """
        return f"Vehículo marca {self.marca}, modelo {self.modelo}"

    # Métodos útiles para depuración/impresión
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(marca={self.marca!r}, modelo={self.modelo!r}, precio={self.get_precio():.2f})"
