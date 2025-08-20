class Vuelo:
    def __init__(self, codigo: str, origen: str, destino: str, fecha: str, precio: float) -> None:
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio

    # Getters
    def get_codigo(self) -> str: 
        return self.codigo
    def get_origen(self) -> str: 
        return self.origen
    def get_destino(self) -> str: 
        return self.destino
    def get_fecha(self) -> str: 
        return self.fecha
    def get_precio(self) -> float: 
        return self.precio

    # Setters
    def set_codigo(self, nuevo_codigo: str) -> None: 
        self.codigo = nuevo_codigo
    def set_origen(self, nuevo_origen: str) -> None: 
        self.origen = nuevo_origen
    def set_destino(self, nuevo_destino: str) -> None: 
        self.destino = nuevo_destino
    def set_fecha(self, nueva_fecha: str) -> None: 
        self.fecha = nueva_fecha
    def set_precio(self, nuevo_precio: float) -> None: 
        self.precio = nuevo_precio


# Cargar 6 vuelos
vuelos_data = [
    ("AR1001", "AEP", "CBA", "2025-09-10", 180000),
    ("AR2002", "EZE", "MDZ", "2025-09-12", 220000),
    ("AR3003", "AEP", "COR", "2025-10-01", 195000),
    ("AR4004", "EPA", "USH", "2025-11-05", 350000),
    ("AR5005", "AEP", "BRC", "2025-08-25", 199999),
    ("AR6006", "EZE", "COR", "2025-09-20", 175000),
]

vuelos = [Vuelo(*datos) for datos in vuelos_data]

# Vuelos desde EZE con precio < 200000
codigos_eze_baratos = []
for vuelo in vuelos:
    if vuelo.get_origen() == "EZE" and vuelo.get_precio() < 200000:
        codigos_eze_baratos.append(vuelo.get_codigo())

print("Desde EZE y < 200000:", codigos_eze_baratos)


# Más barato hacia un destino dado (sin min)
destino_obj = "COR"
mas_barato = None
for vuelo in vuelos:
    if vuelo.get_destino() == destino_obj:
        if mas_barato is None or vuelo.get_precio() < mas_barato.get_precio():
            mas_barato = vuelo

if mas_barato is not None:
    print("Más barato a", destino_obj + ":", mas_barato.get_codigo(), mas_barato.get_precio())
else:
    print("No hay vuelos a", destino_obj)


# Ajustar precio y recalcular
if mas_barato is not None:
    print("\nAjustando precio de:", mas_barato.get_codigo(), "— antes:", mas_barato.get_precio())
    mas_barato.set_precio(150000.0)
    print("Después:", mas_barato.get_precio())

    # Recalcular
    mas_barato_recalculo = None
    for vuelo in vuelos:
        if vuelo.get_destino() == destino_obj:
            if mas_barato_recalculo is None or vuelo.get_precio() < mas_barato_recalculo.get_precio():
                mas_barato_recalculo = vuelo

    print("\nTras ajuste — más barato a", destino_obj + ":", 
          mas_barato_recalculo.get_codigo(), mas_barato_recalculo.get_precio())
