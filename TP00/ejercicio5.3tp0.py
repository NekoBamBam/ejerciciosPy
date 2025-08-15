base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
if base > 0 and altura > 0:
    print("Area:", base * altura)
    print("Perimetro", 2 * (base + altura))
else:
    print("Dimensiones invalidas")
