"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    max_min = {}

    with open('files/input/data.csv', 'r') as file:
        for line in file:
            for pair in line.split('\t')[4].split(','):
                key = pair.split(':')[0]
                value = int(pair.split(':')[1])

                if key in max_min:
                    if value > max_min[key][0]:
                        max_min[key] = (value, max_min[key][1])
                    if value < max_min[key][1]:
                        max_min[key] = (max_min[key][0], value)
                else:
                    max_min[key] = (value, value)

    registro = [(key, maximo, minimo) for key, (maximo, minimo) in max_min.items()]
    registro.sort()

    return registro

print(pregunta_06())