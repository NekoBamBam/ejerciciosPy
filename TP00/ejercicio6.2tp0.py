import math

def menu():
    while True:
        print("""
        1) Círculo
        2) Triángulo
        3) Rectángulo
        0) Salir
        """)
        opcion = input("Opción: ")

        match opcion:
            case "1":
                radio = float(input("Radio del círculo: "))
                if radio > 0:
                    area = math.pi * radio ** 2
                    perimetro = 2 * math.pi * radio
                    print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")
                else:
                    print("Radio inválido.")
            
            case "2":  
                base = float(input("Base del triángulo: "))
                altura = float(input("Altura del triángulo: "))
                if base > 0 and altura > 0:
                    area = (base * altura) / 2
                    print(f"Área: {area:.2f}")
                    print("Perímetro: No se puede calcular con base y altura solamente.")
                else:
                    print("Dimensiones inválidas.")
            
            case "3":
                base = float(input("Base del rectángulo: "))
                altura = float(input("Altura del rectángulo: "))
                if base > 0 and altura > 0:
                    area = base * altura
                    perimetro = 2 * (base + altura)
                    print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")
                else:
                    print("Dimensiones inválidas.")
            
            case "0":
                break
            case _:
                print("Opción inválida.")

menu()
