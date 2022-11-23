# # lista = [1, 2, 3, 4, "Cinco", 6.0]
# # lista_2 = list()  # se crea la lista

# # lista_2.append(10)  # con append se usa para agregar elemtos a la lista
# # lista_2.append("Veinte")
# # lista_2.append('a')

# # print(lista)  # se imprime la lista
# # print(lista_2)

# # print(lista_2[1])

# # lista_2.count

# # nombres = ["Juan", "Aaron", "Zacarias"]
# # nombres.sort()
# # print(nombres)

# lista = [1, 2, 3, 4, 5]
# print(len(lista))
# # len es para ver la cantidad de elementos de la lista

# lista.append(6)
# # append es para agregar elementos al final de la lista
# agregado = [7, 8, 9]

# lista.extend(agregado)
# # extend agrega datos a una lista a partir de otra lista, se agrega el 7,8,9

# lista.remove(8)
# # remove es para eliminar un elemento de la lista que se conoce, aqui elimina el 8

# lista.pop()
# # pop remueve el ultimo dato de la lista, para este ejemplo estaria eliminando el 9

# print(lista)

# lista2 = ["hola", "hola", 23, 34, 45, 56, 23, 23, "adios"]
# # count nos permite contabilizar la cantidad de veces que se repite un dato conocido
# print(lista2.count(23))

# lista.reverse()
# print(lista)

# animales = ["vaca", "conejo", "perro", "delfin"]
# animales.sort()
# print(animales)

# lista.sort()
# print(lista)

lista = [1, 2, 3, 4]
print(lista)
# se usa del para eliminar algun elemento de una lista sabiendo su posicion
del lista[2]
print(lista)

# lista[0] = 5
# print(lista)

diccionario = {
    1: "Uno",
    2: "Dos",
    3: "Tres"
}
print(diccionario)
diccionario[4] = "Cuatro"
print(diccionario)
