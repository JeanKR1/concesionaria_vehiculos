"""
Programa principal (main.py)
- Menú de ventas interactivo para agregar vehículos a la concesionaria.
- Se precargan 12 vehículos (4 autos, 4 motos, 4 camiones).
- Se aplican los conceptos de POO: Herencia, Polimorfismo y Encapsulamiento.
"""

from concesionaria.auto import Auto
from concesionaria.moto import Moto
from concesionaria.camion import Camion
from concesionaria.concesionaria import Concesionaria


def precargar_vehiculos(dealer: Concesionaria):
    """Agrega 12 vehículos iniciales a la concesionaria."""

    # 🚗 AUTOS
    dealer.agregar_vehiculo(Auto("Honda", "Civic", 15500000, 4))
    dealer.agregar_vehiculo(Auto("Ford", "Focus", 13800000, 5))
    dealer.agregar_vehiculo(Auto("Toyota", "Yaris", 11200000, 4))
    dealer.agregar_vehiculo(Auto("Chevrolet", "Onix", 10500000, 4))

    # 🏍️ MOTOS
    dealer.agregar_vehiculo(Moto("Kawasaki", "Ninja 400", 6200000, 399))
    dealer.agregar_vehiculo(Moto("Yamaha", "MT-07", 7800000, 689))
    dealer.agregar_vehiculo(Moto("Suzuki", "GSX-R600", 9100000, 599))
    dealer.agregar_vehiculo(Moto("Honda", "CB500F", 5900000, 471))

    # 🚛 CAMIONES
    dealer.agregar_vehiculo(Camion("Mercedes-Benz", "Actros", 92000000, 25.0))
    dealer.agregar_vehiculo(Camion("Volvo", "FH16", 105000000, 30.0))
    dealer.agregar_vehiculo(Camion("Scania", "R450", 98500000, 28.0))
    dealer.agregar_vehiculo(Camion("Iveco", "Stralis", 88000000, 24.0))


def menu():
    """Menú de ventas para interactuar con la concesionaria."""

    dealer = Concesionaria("Motores del Sur")

    # Precargamos los 12 vehículos iniciales
    precargar_vehiculos(dealer)
    print("✅ Vehículos en venta de la concesionaria.")

    # Bucle del menú
    while True:
        print("\n=== MENÚ DE VENTAS ===")
        print("1. Agregar Auto")
        print("2. Agregar Moto")
        print("3. Agregar Camión")
        print("4. Mostrar Catálogo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # -------------------- AGREGAR AUTO --------------------
        if opcion == "1":
            try:
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                precio = float(input("Precio: "))
                puertas = int(input("Número de puertas: "))
                auto = Auto(marca, modelo, precio, puertas)
                dealer.agregar_vehiculo(auto)
                print("✅ Auto agregado con éxito.")
            except Exception as e:
                print(f"❌ Error: {e}")

        # -------------------- AGREGAR MOTO --------------------
        elif opcion == "2":
            try:
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                precio = float(input("Precio: "))
                cilindrada = int(input("Cilindrada (cc): "))
                moto = Moto(marca, modelo, precio, cilindrada)
                dealer.agregar_vehiculo(moto)
                print("✅ Moto agregada con éxito.")
            except Exception as e:
                print(f"❌ Error: {e}")

        # -------------------- AGREGAR CAMIÓN --------------------
        elif opcion == "3":
            try:
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                precio = float(input("Precio: "))
                capacidad = float(input("Capacidad de carga (toneladas): "))
                camion = Camion(marca, modelo, precio, capacidad)
                dealer.agregar_vehiculo(camion)
                print("✅ Camión agregado con éxito.")
            except Exception as e:
                print(f"❌ Error: {e}")

        # -------------------- MOSTRAR CATÁLOGO --------------------
        elif opcion == "4":
            print("\n" + dealer.mostrar_catalogo())

        # -------------------- SALIR --------------------
        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Gracias por usar la concesionaria!")
            break

        else:
            print("⚠️ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()


