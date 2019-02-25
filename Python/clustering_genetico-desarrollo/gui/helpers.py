from PyQt5 import QtGui
import random


def generar_colores_unicos(n):
    """Implementacion de generacion en base al golden ratio

    Mas informacion en:
    * http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally
     -algorithms/
    * https://martin.ankerl.com/2009/12/09/how-to-create-random-colors
    -programmatically/

    Sobre HSV: https://www.lifewire.com/what-is-hsv-in-design-1078068
    """
    golden_ratio = 0.618033988749895

    lista_colores = []

    # Definimos un numero aleatorio que nos indica el color inicial
    color_inicial = random.random()

    for i in range(n):
        # Generamos el color aleatorio a partir del numero aleatorio generado
        #  inicialmente y el golden ratio, multiplicado por i que asegura la
        # no repeticion de colores. El modulo devuelve la parte real del
        # resultado.
        h = (color_inicial + golden_ratio * i) % 1

        # H es la porcion del modelo de color. S es la saturacion (cantidad
        # de gris) en 0 es gris, 1 es el color principal. V es el brillo (
        # value), funciona junto con la saturacion, 0 es negro y 1 es el
        # brillo maximo.
        qcolor = QtGui.QColor.fromHsvF(h, 0.65, 0.95)
        lista_colores.append(qcolor)

    return lista_colores
