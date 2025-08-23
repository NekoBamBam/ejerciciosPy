#Estamos desarrollando un sistema para la UTN y tenemos que definir la clase Estudiante (nombre, legajo, anio_ingreso, carrera) 
# Tareas:
# 1. Crear 6 estudiantes.
# 2. Construir una lista con los legajos de carrera "TUP" usando for.
# 3. Cambiar la carrera de este con set_carrera

class Estudiante:
    def __init__(
        self, nombre: str, legajo: int, anio_ingreso: int, carrera: str
    ) -> None:
        self.nombre = nombre
        self.legajo = legajo
        self.anio_ingreso = anio_ingreso
        self.carrera = carrera

def get_nombre(self) -> str:
    return self.nombre

def get_legajo(self) -> int:
    return self.legajo

def get_anio_ingreso(self) -> int:
    return self.anio_ingreso

def get_carrera(self) -> str:
    return self.carrera

def set_nombre(self, nuevo_nombre: str) -> None:
    self.nombre = nuevo_nombre

def set_legajo(self, nuevo_legajo: str) -> None:
    self.legajo = nuevo_legajo

def set_ingreso(self, nuevo_ingreso: str) -> None:
    self.ingreso = nuevo_ingreso

def set_carrera(self, nuevo_carrera: str) -> None:
    self.carrera = nuevo_carrera

estudiantes = [
    Estudiante("Ana", 101, 2021, "TUP"),
    Estudiante("Luis", 102, 2022, "ITI"),
    Estudiante("Mia", 103, 2024, "TUP"),
    Estudiante("Juan", 104, 2023, "ITI"),
    Estudiante("Sofía", 105, 2020, "TUP"),
    Estudiante("Tom", 106, 2022, "DS"),
]

print("=== Lista de estudiantes (inicial) ===")
orden = 1
for est in estudiantes:
    print(
        f"{orden:>2}. {est.get_nombre()} | Legajo: {est.get_legajo()} |"
        f"Año ingreso: {est.get_anio_ingreso()} | Carrera: {est.get_carrera()}"
    )
    orden += 1

# cambiar la carrera estudiante
estudiantes[1].set_carrera("TUP")
print("=== Lista de estudiantes (inicial) ===")
orden = 1
for est in estudiantes:
    print(
        f"{orden:>2}. {est.get_nombre()} | Legajo: {est.get_legajo()} |"
        f"Año ingreso: {est.get_anio_ingreso()} | Carrera: {est.get_carrera()}"
    )
    orden += 1
