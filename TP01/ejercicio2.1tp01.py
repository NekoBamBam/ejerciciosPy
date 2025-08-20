class Articulo:
    def __init__(self, nombre: str, precio: float, stock: int, categoria: str) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

def get_nombre(self) -> str:
    return self.nombre

def get_precio(self) -> float:
    return self.precio

def get_stock(self) -> int:
    return self.stock

def get_categoria(self) -> str:
    return self.categoria

def set_nombre(self,nuevo_nombre: str) -> None:
    self.nombre = nuevo_nombre

def set_precio(self,nuevo_precio: float) -> None:
    self.precio = nuevo_precio

def set_stock(self,nuevo_stock: int) -> None:
    self.stock = nuevo_stock

def set_categoria(self,nuevo_categoria: str) -> None:
    self.categoria = nuevo_categoria

articulos = [
    Articulo("Leche", 1200.00, 50, "Alimentos"),
    Articulo("Aceite", 4500.00, 20, "Alimentos"),
    Articulo("Yerba", 3800.00, 30, "Alimentos"),
    Articulo("Detergente", 5200.00, 15, "Limpieza"),
    Articulo("Papel Hig.", 4300.00, 40, "Higiene"),
]
nombres_caros = []
for a in articulos:
    if a.get_precio() > 4000:
        nombres_caros.append(a.get_nombre())
print("Caros (>4000):", nombres_caros)

#cambiar el precio de uno y mostrar el cambio
print("Antes:",articulos[0].get_nombre(),
articulos[0].get_precio())
articulos[0].set_precio(6000.0)
print("Despues:", articulos[0].get_nombre(),
articulos[0].get_precio())