#Pide una nota (0–100) y clasifícala: 
# ≥ 70 → "Aprobado" 
# ≥ 90 → "Con honores" 
# < 70 → "Reprobado" 

nota = int(input("ingrese una nota(del 0 al 100): "))
if nota >= 90:
    print("Aprobado con honores!")
elif nota >= 70:
    print("Aprobado")
else:
    print("Desaprobado")