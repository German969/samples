from PyQt5 import QtWidgets, QtGui, QtCore


class TablaModel(QtGui.QStandardItemModel):

    def __init__(self):
        super(TablaModel, self).__init__()

    def cargar_datos(self, datos):
        self.datos = datos

        self.setRowCount(datos.shape[0])
        self.setColumnCount(datos.shape[1])

        for fila in range(self.rowCount()):
            for columna in range(self.columnCount()):
                self.setItem(fila, columna, QtGui.QStandardItem(str(datos[
                                                                        fila][columna])))

    def cargar_clasificacion(self, clasificacion, colores):
        columna_clasificacion = self.datos.shape[1]
        self.insertColumn(columna_clasificacion)
        self.setHorizontalHeaderItem(columna_clasificacion,
                                     QtGui.QStandardItem("Clasificacion"))

        for fila in range(self.rowCount()):
            self.setItem(fila, columna_clasificacion, QtGui.QStandardItem(
                str(clasificacion[fila])))

            for columna in range(self.columnCount()):
                self.setData(self.index(fila, columna), QtGui.QBrush(colores[
                                                                         clasificacion[fila]]), 8)