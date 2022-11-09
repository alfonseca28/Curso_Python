diccionario = {}
print(type(diccionario))

diccionario2 = {
    'dato1': "numero1",
    'dato2': "numero2",
    'booleano': "True",
    'flotante': "3.1416",
    'lista': [12, 24, 48],
    'diccionario': {
        'dicchijo1': 1,
        'dicchijo2': 2
    }
    # lo que va entre comillas simples es el nombre del dato, seguido los 2 puntos para asignar el valos del dato
}
# print(diccionario2['booleano'])
# bul = diccionario2['booleano']
print(diccionario2.keys())
print(diccionario2.values())
# se llaman llaves lo que va entre comillas simples ('')
