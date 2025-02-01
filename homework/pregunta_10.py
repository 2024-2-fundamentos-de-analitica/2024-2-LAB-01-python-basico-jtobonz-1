"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    cantidad_letra = []

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            campos = line.split('\t')
            letra = campos[0]
            # Contamos elementos separados por coma en columnas 4 y 5
            cantidad_4 = len(campos[3].strip().split(','))
            cantidad_5 = len(campos[4].strip().split(','))

            # Agregamos la tupla directamente a la lista
            cantidad_letra.append((letra, cantidad_4, cantidad_5))

    return cantidad_letra

print(pregunta_10())