import sklearn.metrics
import numpy as np


def ev_silhouette(individuo, datos, n_clusters):
    # TODO Preguntar si no es trampa
    """Calcula el puntaje de silhouette para el 'individuo' dado en base a
    los 'datos' indicados.
    Si la cantidad de clusters no coincide con la esperada se penaliza la
    solucion asignandole -1.0, el peor valor de silhouette.

    :param individuo: Individuo a ser evaluado
    :param datos: Datos sobre los cuales se evaluara el individuo
    :param n_clusters: Cantidad de clusters deseados
    :returns: Tupla de un puntaje de silhouette"""
    tabla_particiones = sklearn.metrics.pairwise_distances_argmin(datos,
                                                                  individuo)
    if len(np.unique(tabla_particiones)) != n_clusters:
        return -1.0,

    return sklearn.metrics.silhouette_score(datos, tabla_particiones),


def ev_calinski_harabaz(individuo, datos, n_clusters):
    tabla_particiones = sklearn.metrics.pairwise_distances_argmin(datos,
                                                                  individuo)

    if len(np.unique(tabla_particiones)) != n_clusters:
        return -1,

    return sklearn.metrics.calinski_harabaz_score(datos, tabla_particiones),