# concatenacion

palabra = "dias"
numero = 10
print("---CONCATENACION CON SIGNO MAS (+)---")
print("tengo "+str(numero)+" años")
# cuando tengamos datos de tipo numerico se debe de castear, convirtiendolo a string para poder concatenarlo

# otra forma de concatenar es con una coma (,)
print("\n---IMPRESION CON COMA----")
print("hola", "¿como estas?")

con_coma = "hola", "mundo"
print(con_coma)
# las comas dejan unespaciado automatico al momento de concatenar
# si concatenamos dentro de una variables obtendremos una tupla
# con_coma = "hola", "mundo"

# impresion con .format()

print("\n---IMPRESION CON FORMAT----")
palabra_1 = "Aldo"
print("me tiene hasta los huevo el {0}".format(palabra_1))
# en esta forma de concatenacion no importa el tipo de dato
# la sintaxis consiste en un {0} entre llaves en el sitio en el que se concatenara el dato

print("\n---IMPRESION CON F (f)----")
palabra_2 = "hamburguesa"
print(f"quiero una {palabra_2} por favor")
# este tipo de concatenaicon es la forma mas practica debido a que es facil de entender
# y no hay necesidad de convertir los datos
