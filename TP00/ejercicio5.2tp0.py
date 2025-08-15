base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
if base > 0 and altura > 0:
    area = (base * altura) / 2
    print("Area del triangulo: ",area)
else:
    print("No valido")