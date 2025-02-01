"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    cantidad_letra = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            letra = line.split('\t')[0]
            valores = (line.split('\t')[4]).split(',')

            for ele in valores:
                valor = int(ele.split(':')[1])

                if letra in cantidad_letra:
                    cantidad_letra[letra] += valor
                else:
                    cantidad_letra[letra] = valor

    sorted_items = sorted(cantidad_letra.items(), key=lambda x: x[0])
    result = dict(sorted_items)

    return result