# numeros = [10, "20", 30]
# print(numeros)

# ---- Agregar y eliminar ----
# numeros.append(40)        # agrega al final [10, "20", 30, 40]
# print(numeros)
# numeros.insert(1, 15)     # inserta en posición 1 [10, 15, "20", 30, 40]
# print(numeros)
# numeros.extend([50, 60])  # extiende con otra lista [10, 15, "20", 30, 40, 50, 60]
# print(numeros)
# numeros.remove("20")      # elimina la primera aparición de "20"
# print(numeros)
# ultimo = numeros.pop()    # elimina y retorna el último o índice dado
# print(ultimo)
# numeros.clear()           # elimina todos los elementos quedando []
# print(numeros)

# ---- Acceso y consulta ----
numeros = [10, 20, 30, 40, 50, 30]
print(numeros)
# print(numeros[1])         # acceso por índice: 20
# print(numeros[-1])        # último elemento: 30
# print(30 in numeros)      # True si está en la lista
# print(numeros.count(30))  # cuántas veces aparece: 30
# print(numeros.index(40))  # posición de la primera aparición de 40
# print(len(numeros))       # cantidad de elementos: 6

# ---- Ordenamiento y reversa ----
# numeros.reverse()         # invierte el orden actual
# print(numeros)
# numeros.sort()            # ordena de menor a mayor
# print(numeros)
# numeros.sort(reverse=True)# ordena de mayor a menor
# print(numeros)
# copia = sorted(numeros)   # crea una nueva lista ordenada no modifica la original
# print(copia)

# ---- Copia y rebanado ----
# copia = numeros.copy()    # copia superficial de la lista
# print(copia)
# sublista = numeros[1:4]   # rebanado (slice): elementos en posiciones 1 a 3
# print(sublista)
