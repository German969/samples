from PyQt5 import QtGui, QtCore, QtChart
import numpy as np
import copy


class SoporteLienzo(QtChart.QChartView):

    def __init__(self, *args, **kwargs):
        super(SoporteLienzo, self).__init__(*args, **kwargs)

        # Creamos un nuevo lienzo y lo asociamos al soporte
        self.grafico = Lienzo()
        self.setChart(self.grafico)

        # Configuramos antialising
        self.setRenderHint(QtGui.QPainter.Antialiasing)

        # Permitimos realizar zoom haciendo clic en un punto y arrastrando el
        #  mouse definiendo el area que se quiere cubrir
        # TODO Reimplementar el zoom para mantener el aspect ratio
        # self.setRubberBand(QtChart.QChartView.RectangleRubberBand)


class Lienzo(QtChart.QChart):

    def __init__(self, *args, **kwargs):
        super(Lienzo, self).__init__(*args, **kwargs)

        self.dim_uno = 0
        self.dim_dos = 1

        self.datos = []
        self.clasificacion = []
        self.colores = []

        self.layout().setContentsMargins(0, 0, 0, 0)
        self._inicializar()

    def _inicializar(self):
        # Definimos los rangos de la absisa y ordenada
        default_x, default_y = QtChart.QValueAxis(), QtChart.QValueAxis()
        default_x.setRange(0, 100)
        default_y.setRange(0, 100)

        # Configuramos el rango de absisa y ordenada del grafico para que
        # inicialmente no sea un cuadro vacio
        # TODO Ver si se puede lograr hacer zoom sin valores
        self.setAxisX(default_x)
        self.setAxisY(default_y)

        # Recuperamos y escondemos las leyendas
        self.legend().hide()

        # Colocamaos el tema oscuro
        self.setTheme(QtChart.QChart.ChartThemeDark)

        self.pen = QtGui.QPen()
        self.pen.setWidth(2)

    def limpiar(self):
        self.removeAllSeries()

    def graficar_clasificacion(self, clasificacion, colores):
        self.limpiar()

        self.clasificacion = clasificacion
        self.colores = colores

        numero_clasificaciones = len(np.unique(clasificacion))

        for i in range(numero_clasificaciones):
            puntos = self.datos[clasificacion == i]
            serie = self._armar_serie(puntos, colores[i])
            self.addSeries(serie)

        self.createDefaultAxes()

    def graficar_datos(self, datos):
        self.limpiar()
        self.datos = datos

        self.addSeries(self._armar_serie(self.datos, QtGui.QColor("lightGrey")))
        self.createDefaultAxes()

    def _armar_serie(self, puntos, color):
        serie_puntos = QtChart.QScatterSeries()

        [serie_puntos.append(x, y) for x, y in puntos[:, [self.dim_uno,
                                                          self.dim_dos]]]

        pen_color = copy.deepcopy(color)
        background_color = copy.deepcopy(color)

        self.pen.setColor(pen_color)
        serie_puntos.setPen(self.pen)

        background_color.setAlpha(120)
        serie_puntos.setColor(background_color)

        return serie_puntos
