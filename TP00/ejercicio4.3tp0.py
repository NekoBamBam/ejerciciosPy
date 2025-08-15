contador = 0
while True:
     n = int(input("Número (0 para terminar): "))
     if n == 0:
          break
     contador += 1
print("Has introducido", contador,"numeros.")