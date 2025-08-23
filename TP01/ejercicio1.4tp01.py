#Creamos la clase Vuelo (codigo, origen, destino, fecha, precio)
# Tareas:
# 1. Creá 6 vuelos con orígenes/destinos, fechas y precios distintos en una lista con un for
# 2. Mostrá los códigos de los vuelos con origen EZE y precio < 200.000 pesos

class Vuelo:
    def __init__(
        self, codigo: str, origen: str, destino: str, fecha: str, precio: float
    ) -> None:
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

vuelos = [
    Vuelo("AR1001", "AEP", "CBA", "2025-09-10", 180000),
    Vuelo("AR2002", "EZE", "MDZ", "2025-09-12", 220000),
    Vuelo("AR3003", "AEP", "COR", "2025-10-01", 195000),
    Vuelo("AR4004", "EPA", "USH", "2025-11-05", 350000),
    Vuelo("AR5005", "AEP", "BRC", "2025-08-25", 199999),
    Vuelo("AR6006", "EZE", "NQN", "2025-09-20", 175000),
]
vuelos = []
for i in range(1, 6):
    codigo = input("Codigo (ej. AR1234): ").strip()
    origen = input("Origen (ej.EZE): ").strip().upper()
    destino = input("Destino (ej.COR/MDZ): ").strip().upper()
    fecha = input("Fecha (AAAA-MM-DD): ").strip()
    precio = float(input("Precio en pesos: ").strip().replace(",", "."))
    vuelos.append(Vuelo(codigo, origen, destino, fecha, precio))

ORIGEN_OBJETIVO = "EZE"
LIMITE_PRECIO = 200000.0
codigos = []
for v in vuelos:
    if v.origen == ORIGEN_OBJETIVO and v.precio < LIMITE_PRECIO:
        codigos.append(v.codigo)
        print(codigos)