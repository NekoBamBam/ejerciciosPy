#Pide al usuario su nombre y apellido por separado. 
#Guarda cada uno en variables con nombres claros (ejemplo: first_name, last_name). 
#Imprime su nombre completo. 

primer_nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = f"{primer_nombre} {apellido}"
print(nombre_completo)