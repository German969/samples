import random


def mut_centroide_random(individuo, datos, indpb):
    """Esta funcion muta un individuo reemplazando, en base a una
    probabilidad dada 'indpb', centroides del individuo por puntos aleatorios
    tomados de los datos

    :param individuo: Individuo que se debe mutar
    :param datos: Array del cual se deben obtener los puntos reemplazantes
    :param indpb: Probabilidad de reemplazar cada centroide
    :returns: Tupla de un individuo
    """
    n_datos = datos.shape[0]
    for i in range(len(individuo)):
        if random.random() < indpb:
            indice_punto = random.randint(0, n_datos - 1)
            individuo[i] = datos[indice_punto]

    return individuo,
