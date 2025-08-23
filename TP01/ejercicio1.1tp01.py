#Definí la clase Ciudad con los siguientes atributos: nombre, provincia, población. 
#Tareas:
# 1. Instanciá 2 ciudades (La Plata, Mar del Plata) con provincia y población aproximada.
# 2. Mostrá con print() sus atributos.
# 3. Usá vars(ciudad) para ver el diccionario interno de una instancia

class Ciudad:
    def __init__(self, nombre: str, provincia: str, poblacion: int) -> None:
        self.nombre = nombre
        self.provincia = provincia
        self.poblacion = poblacion


Ciudad_1 = Ciudad("La plata", "Buenos Aires", 70000)
Ciudad_2 = Ciudad("Mar Del Plata", "Buenos Aires", 62000)
print(
    f"Nombre: {Ciudad_1.nombre},ubicada en la provincia de {Ciudad_1.provincia},con una poblacion de {Ciudad_1.poblacion} habitantes"
)
