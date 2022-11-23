# el slicing en python es para recorrer una lista y extraer subelementos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista)
# recorrer lista de incio a fin
print(lista[:])

# recorrer lista tomando un subelemento
print(lista[3:6])

# recorre r los primeros 3 elementos
print(lista[:3])

# recorrer los ultimos 3 elementos
print(lista[-3:])

# recorrer tomando el ultimo elemento de la lista
print(lista[-1:])

# tomar todos los elementos cada 3 posiciones (de 3 en 3)
print(lista[::3])

# invertir una lista
print(lista[::-1])

# recorrer una lista de cadenas a la inversa
texto = "Hola buenas tardes"
print(texto[::-1])
