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