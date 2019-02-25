from PyQt5 import QtWidgets, QtCore, QtGui
from .resources import ui_refresh
from . import graph
from . import tabla
from . import helpers
from clustering_genetico import clustering_genetico
from clustering_genetico.clustering_genetico import OperadorEvaluacion, \
    OperadorMutacion, OperadorCruza, OperadorSeleccion
import numpy as np


class MainWindow(QtWidgets.QMainWindow, ui_refresh.Ui_MainWindow):
    # Definimos una nueva señal
    evento_archivo_abierto = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, *args, **kwargs):
        # Inicializamos la superclase
        super(MainWindow, self).__init__(*args, **kwargs)

        # Creamos el backend del programa
        self.clustering_genetico = clustering_genetico.ClusteringGenetico()

        # Cargamos la configuracion definida en la clase Ui_MainWindow
        self.setupUi(self)

        # Creamos el lienzo y lo agregamos
        self.frame_graph_vl = QtWidgets.QVBoxLayout(self.widget_graph)
        self.soporte_lienzo = graph.SoporteLienzo(self.widget_graph)
        self.frame_graph_vl.insertWidget(0, self.soporte_lienzo)

        # Creamos la tala y la agregamos
        self.frame_tabla_vl = QtWidgets.QVBoxLayout(self.widget_tabla)
        self.tabla = QtWidgets.QTableView()
        self.frame_tabla_vl.insertWidget(0, self.tabla)
        self.tabla_model = tabla.TablaModel()
        self.tabla.setModel(self.tabla_model)

        self.tabla.setBaseSize(0, 200)
        self.soporte_lienzo.setBaseSize(0, 400)
        self.splitter.setSizes([80, 20])

        # Conectamos las señales a sus respectivos slots
        self.actionAbrir_Archivo.triggered.connect(self.abrir_archivo)
        self.evento_archivo_abierto.connect(self.archivo_abierto)
        self.actionClasificar.triggered.connect(self.clasificar)

    def abrir_archivo(self):
        # Obtenemos la direccion del archivo, limitando las posibilidades de
        # seleccion a archivos con extension .tsv o en su defecto .txt
        archivo = QtWidgets.QFileDialog.getOpenFileName(
            filter="Archivo de texto TSV (*.tsv, *.txt)")

        # Si se cancelo la ventana entonces salimos de la funcion
        if not all(archivo):
            return

        # Si se puede abrir el archivo emitimos una señal adjuntando los datos.
        if self.clustering_genetico.datos_desde_archivo(archivo[0]):
            self.evento_archivo_abierto.emit(
                self.clustering_genetico.datos)

        # Si hubo un problema al abrir el archivo emitimos una alerta
        # anunciandolo.
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Hubo un problema "
                                                          "al cargar el "
                                                          "archivo",
                                           QtWidgets.QMessageBox.Ok)

    def archivo_abierto(self, datos):
        self.soporte_lienzo.grafico.graficar_datos(datos)

        self.tabla_model = tabla.TablaModel()
        self.tabla_model.cargar_datos(datos)
        self.tabla.setModel(self.tabla_model)

        self.actionClasificar.setEnabled(True)
        self.actionConfiguracion.setEnabled(True)
        self.actionReiniciar.setEnabled(False)

    def clasificar(self):
        k = 6
        npob = 100
        ngen = 50


        # Generamos los colores necesarios para el grafico
        colores = helpers.generar_colores_unicos(k)

        # Configuramos el motor de clustering genetico
        self.clustering_genetico.registrar(OperadorSeleccion.SeleccionRandom,
                                           k=npob)
        self.clustering_genetico.registrar(OperadorCruza.OnePoint)
        self.clustering_genetico.registrar(OperadorMutacion.DatosRandom,
                                           datos=self.clustering_genetico.datos,
                                           indpb=0.5)
        self.clustering_genetico.registrar(OperadorEvaluacion.Silhouette,
                                           datos=self.clustering_genetico.datos,
                                           n_clusters=k)

        # Obtenemos el resultado de la clasificacion
        clasificacion = self.clustering_genetico.clasificar(k, ngen, npob, 0.5,
                                                            0.2)

        # Enviamos solo la tabla de asignacion al grafico
        self.soporte_lienzo.grafico.graficar_clasificacion(clasificacion[0],
                                                           colores)
        self.tabla.model().cargar_clasificacion(clasificacion[0], colores)
