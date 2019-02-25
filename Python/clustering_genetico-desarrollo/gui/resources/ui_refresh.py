# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refresh.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 522)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget_graph = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_graph.sizePolicy().hasHeightForWidth())
        self.widget_graph.setSizePolicy(sizePolicy)
        self.widget_graph.setBaseSize(QtCore.QSize(0, 0))
        self.widget_graph.setObjectName("widget_graph")
        self.widget_tabla = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_tabla.sizePolicy().hasHeightForWidth())
        self.widget_tabla.setSizePolicy(sizePolicy)
        self.widget_tabla.setObjectName("widget_tabla")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 691, 28))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir_Archivo = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName("actionAbrir_Archivo")
        self.actionConfiguracion = QtWidgets.QAction(MainWindow)
        self.actionConfiguracion.setEnabled(False)
        self.actionConfiguracion.setObjectName("actionConfiguracion")
        self.actionReiniciar = QtWidgets.QAction(MainWindow)
        self.actionReiniciar.setEnabled(False)
        self.actionReiniciar.setObjectName("actionReiniciar")
        self.actionClasificar = QtWidgets.QAction(MainWindow)
        self.actionClasificar.setEnabled(False)
        self.actionClasificar.setObjectName("actionClasificar")
        self.toolBar.addAction(self.actionAbrir_Archivo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReiniciar)
        self.toolBar.addAction(self.actionConfiguracion)
        self.toolBar.addAction(self.actionClasificar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clustering Genetico 2000"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAbrir_Archivo.setText(_translate("MainWindow", "Abrir archivo"))
        self.actionConfiguracion.setText(_translate("MainWindow", "Configuracion"))
        self.actionReiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.actionClasificar.setText(_translate("MainWindow", "Clasificar"))

