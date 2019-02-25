from deap import algorithms, base, creator, tools
from . import operadores
import functools
import numpy as np
import time


def generar_poblacion_centroides(k, npop, ldim):
    """Genera una poblacion donde los individuos representan soluciones de
    clustering.

    :param k: El numero de clusters deseados.
    :param npop: Tamaño de la poblacion.
    :param ldim: Array de forma [2, ndim] donde se definen los limites de
    cada dimension.
    :returns: Lista de individuos

    Ejemplo de ldim: [[2, 3], [4, 5]]. El primer array contiene los minimos
    segundo contiene los maximos. Para la primera dimension, el limite
    inferior es 2 y el superior 4.
    """
    # Crea las clases necesarias para la utilizacion del framework. El peso
    # positivo indica que se desea maximizar la aptitud.
    # TODO Analizar si Individuo es subclase de np.ndarray o list
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individuo", np.ndarray, fitness=creator.FitnessMax)

    # Crea un toolbox para la generacion de la poblacion inicial en base a
    # los datos ingresados como parametros. No se utiliza la misma que se
    # ingresa como parametro porque sino se estarian registrando metodos en
    # ella.
    toolbox_local = base.Toolbox()

    # Registra los metodos necesarios para la generacion de la poblacion
    # inicial. Su funcionamiento se basa en functools.partial(funcion,
    # parametros). El resultado de functools.partial() es un puntero a la
    # funcion definida con los parametros establecidos.
    generador_centroides = functools.partial(np.random.uniform, ldim[0],
                                             ldim[1])
    toolbox_local.register("individuo", tools.initRepeat, creator.Individuo,
                           generador_centroides, k)
    toolbox_local.register("poblacion", tools.initRepeat, list,
                           toolbox_local.individuo, npop)

    # Se genera la poblacion inicial utilizando las funciones registradas
    # anteriormente.
    return toolbox_local.poblacion()


def clustering_genetico_simple(poblacion, toolbox, cxpb, mutpb, ngen,
                               stats=None, halloffame=None, verbose=__debug__):
    """Aplicacion del algoritmo genetico simple.

    :param poblacion: El numero de clusters deseados
    :param toolbox: Una clase deap.base.Toolbox que contiene los operadores
    geneticos.
    :param cxpb: Probabilidad de cruzar dos individuos
    :param mutpb: Probabilidad de mutar un individuo
    :param ngen: Numero de generaciones
    :param stats: Completar
    :param halloffame: Completar
    :param verbose: Completar
    :returns: La poblacion final
    """

    # Se calculan las aptitudes para la poblacion generada, para ello se
    # utiliza la funcion evaluar proveida a traves del parametro 'toolbox'.
    ind_no_validos = [ind for ind in poblacion if not ind.fitness.valid]
    aptitudes = toolbox.map(toolbox.evaluate, ind_no_validos)
    for ind, apt in zip(ind_no_validos, aptitudes):
        ind.fitness.values = apt

    if halloffame is not None:
        halloffame.update(poblacion)

    for gen in range(1, ngen + 1):
        # Se seleccionan los individuos y posteriormente se aplica la
        # mutacion y cruza segun las funciones indicadas en el parametro
        # toolbox.
        # TODO Analizar el metodo de generacion de la nueva poblacion
        offspring = toolbox.select(poblacion)
        offspring = algorithms.varAnd(offspring, toolbox, cxpb, mutpb)

        # Se debe recalcular la aptitud de los individuos afectados por la
        # cruza y mutacion.
        ind_no_validos = [ind for ind in offspring if not ind.fitness.valid]
        aptitudes = toolbox.map(toolbox.evaluate, ind_no_validos)
        for ind, apt in zip(ind_no_validos, aptitudes):
            ind.fitness.values = apt

        if halloffame is not None:
            halloffame.update(offspring)

        # Se asigna el offspring (nueva generacion) como poblacion.
        poblacion[:] = offspring

    return poblacion


if __name__ == "__main__":
    # Esta seccion se ejecuta solo cuando se especifica este archivo como
    # punto de entrada, no es parte del modulo de clustering geneticos.
    import os
    import sklearn.preprocessing

    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, "dataset01.txt")
    data = np.loadtxt(file_path, dtype=float, delimiter="\t")

    #datos = sklearn.preprocessing.scale(data)
    #scaler = sklearn.preprocessing.StandardScaler()
    #scaler.fit(data)
    #datos = scaler.transform(data)
    datos = data

    k = 2

    toolbox = base.Toolbox()

    toolbox.register("evaluate", operadores.ev_silhouette, datos=datos,
                     n_clusters=k)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", operadores.mut_centroide_random, datos=datos,
                     indpb=0.2)
    toolbox.register("select", tools.selRandom, k=100)

    halloffame = tools.HallOfFame(5, similar=np.array_equal)

    inicio = time.time()
    pob_inicial = generar_poblacion_centroides(k, 100, [np.min(datos, axis=0),
                                                       np.max(datos, axis=0)])
    fin = time.time()

    print("\nTiempo generacion poblacion {0}".format(fin - inicio))

    inicio = time.time()
    poblacion = clustering_genetico_simple(pob_inicial, toolbox, 0.5, 0.2, 20,
                                           halloffame=halloffame)

    fin = time.time()
    print('\nBest individual:\n', halloffame[0])
    print("\n Puntaje: {0}".format(halloffame[0].fitness.values))

    print("\n Tiempo: {0}".format(fin - inicio))
