#Pide el radio y calcula área (π.r²) y perímetro (2.π.r).

import math 
radio = float(input("Radio del ciruclo: "))
if radio > 0:
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    print(f"Area: {area:.2f},Perimetro {perimetro:.2f}")
else:
    print("Radio no valido")