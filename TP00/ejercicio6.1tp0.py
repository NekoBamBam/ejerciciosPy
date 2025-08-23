#Usa match para ofrecer un menú: 
# 1) Edad 
# 2) Nombre 
# 3) Carrera 
# 0) Salir 
# Si elige: 
# Edad: pide edad y valida que esté entre 1 y 119. 
# Nombre: pide nombre y valida que no esté vacío ni solo espacios. 
# Carrera: pide carrera y valida que no esté vacía. 
# 0: Muestra el dato o mensaje de error y vuelve al menú. 

def menu(): 
    while True: 
        print(""" 
        1) Edad 
        2) Nombre 
        3) Carrera 
        0) Salir 
        """) 
        opcion = input("Opción: ") 
        match opcion: 
            case "1": 
                try: 
                    edad = int(input("Edad: ")) 
                    if 1 <= edad < 120: 
                        print("Edad válida:", edad) 
                    else: 
                        print("Edad fuera de rango.") 
                except ValueError: 
                    print("Entrada inválida.") 
            case "2": 
                nombre = input("Nombre: ").strip() 
                if nombre: 
                    print("Nombre válido:", nombre) 
                else: 
                    print("Nombre no puede estar vacío.") 
            case "3": 
                carrera = input("Carrera: ").strip() 
                if carrera: 
                    print("Carrera válida:", carrera) 
                else: 
                    print("Carrera no puede estar vacía.") 
            case "0": 
                break 
            case _: 
                print("Opción inválida.") 
 
menu()