class Cancion:
    def __init__(
        self, titulo: str, artista: str, duracion_seg: int, genero: str
    ) -> None:
        self.titulo = titulo
        self.artista = artista
        self.duracion_seg = duracion_seg
        self.genero = genero

canciones = [
    Cancion("Tema A", "Banda X", 210, "Rock"),
    Cancion("Tema B", "Banda Y", 145, "Pop"),
    Cancion("Tema C", "Banda Z", 110, "Cumbia"),
    Cancion("Tema D", "Banda W", 215, "Jazz"),
    Cancion("Tema E", "Banda P", 200, "Rap"),
]
rock = []
for c in canciones:
    if c.titulo == "Rock":
        rock.append(c.titulo)
        print("Rock:", rock)
