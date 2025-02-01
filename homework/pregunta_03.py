"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    cantidad_letra = {}

    with open('data.csv', 'r') as file:
        for line in file:
            letra = line.split('\t')[0]
            valor = int(line.split('\t')[1])

            if letra in cantidad_letra:
                cantidad_letra[letra] += valor
            else:
                cantidad_letra[letra] = valor

    registro = [(letra, suma) for letra, suma in cantidad_letra.items()]
    registro.sort()

    return registro