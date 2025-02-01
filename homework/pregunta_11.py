"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    cantidad_letra = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            filter = line.split('\t')[3]
            letra = filter.split(',')
            valor = int(line.split('\t')[1])

            for ele in letra:
                if ele in cantidad_letra:
                    cantidad_letra[ele] += valor
                else:
                    cantidad_letra[ele] = valor
    sorted_items = sorted(cantidad_letra.items(), key=lambda x: x[0])
    result = dict(sorted_items)

    return result