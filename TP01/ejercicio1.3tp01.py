#Crea una clase Dispositivo con los siguientes atributos: marca, modelo, anio, precio
# Tareas
# 1. Creá 6 dispositivos con año y precio guardándolo en una lista
# 2. Mostrá la lista de dispositivos.

class Dispositivo:
    def __init__(self, marca: str, modelo: str, anio: int, precio: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

dispositivos = [
    Dispositivo("MarcaA", "M1", 2021, 35000.0),
    Dispositivo("MarcaB", "M2", 2025, 70000.0),
    Dispositivo("MarcaC", "M3", 2013, 10000.0),
    Dispositivo("MarcaD", "M4", 2022, 54000.0),
    Dispositivo("MarcaE", "M5", 2023, 65000.0),
]
print("Dispositivos(modelo - precio):")
for d in dispositivos:
    print(f"-{d.modelo} - {d.precio:.0f}")
