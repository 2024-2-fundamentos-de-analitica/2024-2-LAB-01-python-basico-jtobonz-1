"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    max_min = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            letra = line.split('\t')[0]
            valor = int(line.split('\t')[1])

            if letra in max_min:
                if valor > max_min[letra][0]:
                    max_min[letra] = (valor, max_min[letra][1])
                if valor < max_min[letra][1]:
                    max_min[letra] = (max_min[letra][0], valor)
            else:
                max_min[letra] = (valor, valor)

    registro = [(letra, maximo, minimo) for letra, (maximo, minimo) in max_min.items()]
    registro.sort()

    return registro
