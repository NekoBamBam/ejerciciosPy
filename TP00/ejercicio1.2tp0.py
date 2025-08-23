#Pide al usuario cuántos artículos quiere comprar (entero). 
#Pide luego el nombre del artículo (cadena). 
#Imprime: Vas a comprar <cantidad> unidades de <artículo>.

articulo = input("Ingrese el articulo a comprar: ")
cantidad = int(input("Su cantidad: "))
print(f"Vas a comprar {cantidad} unidades de {articulo}")