import numpy as np
import deap.base, deap.tools
from . import base
from . import operadores
import enum
import sklearn.metrics
import functools


class ClusteringGenetico(object):

    def __init__(self):
        self.datos = None
        self.nucleo = deap.base.Toolbox()

    def datos_desde_archivo(self, direccion_archivo, delimiter="\t"):
        """Carga los datos desde una direccion dada. Si la carga se realiza
        correctamente devuelve True. Si hubo un problema al cargar los
        datos devuelve Falso."""
        try:
            self.datos = np.loadtxt(direccion_archivo, delimiter=delimiter)
        except ValueError:
            # TODO ¿Seteamos los datos a None?
            return False
        return True

    def registrar(self, operador, **kwargs):
        """Registra operadores geneticos"""
        self.nucleo.register(str(operador), operador.value, **kwargs)

    def clasificar(self, k, ngen, npob, cxpb, mtpb):
        """Ejecuta el algoritmo de clustering genetico con los operadores
        registrados anteriormente."""
        ldim = self.__obtener_limites(self.datos)
        poblacion = base.generar_poblacion_centroides(k, npob, ldim)

        salondelafama = deap.tools.HallOfFame(1, similar=np.array_equal)
        base.clustering_genetico_simple(poblacion, self.nucleo, cxpb, mtpb,
                                        ngen, halloffame=salondelafama)

        mejor_individuo = salondelafama[0]

        return sklearn.metrics.pairwise_distances_argmin_min(self.datos,
                                                             mejor_individuo)

    @staticmethod
    def __obtener_limites(ndarray):
        limites_inferiores = np.min(ndarray, axis=0)
        limites_superiores = np.max(ndarray, axis=0)
        return limites_inferiores, limites_superiores


class OperadorSeleccion(enum.Enum):
    SeleccionRandom = functools.partial(deap.tools.selRandom)

    def __str__(self):
        return "select"


class OperadorCruza(enum.Enum):
    OnePoint = functools.partial(deap.tools.cxOnePoint)

    def __str__(self):
        return "mate"


class OperadorMutacion(enum.Enum):
    DatosRandom = functools.partial(operadores.mut_centroide_random)

    def __str__(self):
        return "mutate"


class OperadorEvaluacion(enum.Enum):
    Silhouette = functools.partial(operadores.ev_silhouette)
    Calinski_Harabaz = functools.partial(operadores.ev_calinski_harabaz)

    def __str__(self):
        return "evaluate"


if __name__ == "__main__":
    import os

    current_path = os.path.abspath(os.path.dirname(__file__))
    direccion_archivo = os.path.join(current_path, "dataset01.txt")

    clustering_genetico_2000 = ClusteringGenetico()

    clustering_genetico_2000.datos_desde_archivo(direccion_archivo)
    clustering_genetico_2000.registrar(
        OperadorSeleccion.SeleccionRandom, k=100)
    clustering_genetico_2000.registrar(OperadorCruza.OnePoint)
    clustering_genetico_2000.registrar(OperadorMutacion.DatosRandom,
                                       datos=clustering_genetico_2000.datos,
                                       indpb=0.5)
    clustering_genetico_2000.registrar(
        OperadorEvaluacion.Silhouette, datos=clustering_genetico_2000.datos,
        n_clusters=2)

    res = clustering_genetico_2000.clasificar(2, 20, 100, 0.5, 0.2)

    print(res)
