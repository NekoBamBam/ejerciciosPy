# ej1
print("Hola mundo")

# ej2
edad = 10

if edad > 18 and edad < 60:
    print("mayor de edad")

elif edad < 18:
    print("menor de edad")

else:
    print("no cumplis requisitos")

#ej3
print("numeros del 1 al 5 multiplicados por 2 con bucle for:")
for numero in range(1,6):
    print(numero * 2)

print("\nNumeros del 1 al 5 multiplicados por 2 con bucle while:")
contador = 1
while contador <= 5:
    print(contador * 2)
    contador += 1