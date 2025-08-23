#Estamos desarrollando una plataforma de streaming con un servicio 
#OTT de suscripción (cómo Netflix)  y queremos armar la clase 
#Pelicula (titulo, director, duracion_min, genero)
# Tareas;
# 1. Crear 5 películas.
# 2. Construir una lista con títulos del género "Drama" usando for.
# 3. Corregir la duración de una con set_duracion_min

class Pelicula:
    def __init__(
        self, titulo: str, director: str, duracion_min: int, genero: str
    ) -> None:
        self.titulo = titulo
        self.director = director
        self.durecion_min = duracion_min
        self.genero = genero

def get_titulo(self) -> str:
    return self.titulo

def get_director(self) -> str:
    return self.director

def get_duracion_min(self) -> int:
    return self.duracion_min

def get_genero(self) -> str:
    return self.genero

def set_titulo(self, nuevo_titulo: str) -> None:
    self.titulo = nuevo_titulo

def set_director(self, nuevo_director: str) -> None:
    self.director = nuevo_director

def set_duracion_min(self, nuevo_duracion_min: int) -> None:
    self.duracion_min = nuevo_duracion_min

def set_genero(self, nuevo_genero: str) -> None:
    self.genero = nuevo_genero

peliculas = [
    Pelicula("P1", "DirA", 95, "Drama"),
    Pelicula("P2", "DirB", 120, "Accion"),
    Pelicula("P3", "DirC", 140, "Drama"),
    Pelicula("P4", "DirD", 110, "Comedia"),
    Pelicula("P5", "DirE", 130, "Drama"),
]

titulos_drama = []
for p in peliculas:
    if p.get_genero() == "Drama":
        titulos_drama.append(p.get_titulo())
        print("Dramas:", titulos_drama)

print("Antes:", peliculas[0].get_titulo(), peliculas[0].get_duracion_min())

peliculas[0].set_duracion_min(150)

print("Despues:", peliculas[0].get_titulo(), peliculas[0].get_duracion_min())
