from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Invoice Manager")
        MainWindow.resize(1120, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # New Project button characteristics
        self.project_button = QtWidgets.QPushButton(self.centralwidget)
        self.project_button.setGeometry(QtCore.QRect(10, 80, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.project_button.setFont(font)
        self.project_button.setObjectName("project_button")

        # New Invoice button characteristics
        self.invoice_button = QtWidgets.QPushButton(self.centralwidget)
        self.invoice_button.setGeometry(QtCore.QRect(10, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.invoice_button.setFont(font)
        self.invoice_button.setObjectName("invoice_button")

        # ListView model characteristics & functionality
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 190, 221, 471))
        self.listView.setAlternatingRowColors(True)
        self.listView.setAcceptDrops(True)
        self.listView.setDropIndicatorShown(True)
        self.listView.setDragEnabled(True)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setMovement(QListView.Snap)
        self.listView.setDefaultDropAction(Qt.MoveAction)
        self.listView.setObjectName("listView")
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        path = r"C:\Invoice Manager"

        self.dirModel = QtWidgets.QFileSystemModel()
        self.dirModel.setRootPath(QtCore.QDir.rootPath())
        self.dirModel.setReadOnly(False)
        self.listView.setModel(self.dirModel)
        self.listView.setRootIndex(self.dirModel.index(path))

        # TreeView model characteristics & functionality
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setReadOnly(False)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setModel(self.fileModel)
        self.treeView.setRootIndex(self.fileModel.index(path))
        self.treeView.setDragEnabled(True)
        self.treeView.setAcceptDrops(True)
        self.treeView.setDropIndicatorShown(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setColumnWidth(0, 400)
        self.treeView.setColumnHidden(1, True)
        self.treeView.setGeometry(QtCore.QRect(270, 90, 801, 571))
        self.treeView.setObjectName("treeView")
        self.treeView.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.treeView.setDefaultDropAction(Qt.MoveAction)
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)

        # Radio button characterisics
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(460, 60, 95, 20))
        self.radioButton.setObjectName("Draft")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(570, 60, 95, 20))
        self.radioButton_2.setObjectName("Approved")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(690, 60, 95, 20))
        self.radioButton_3.setObjectName("Dispatched")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(810, 60, 95, 20))
        self.radioButton_4.setObjectName("Paid")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(930, 60, 95, 20))
        self.radioButton_5.setObjectName("Overdue")

        # Progress bar characteristics
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 670, 801, 23))
        self.progressBar.setToolTip("Invoice status")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("")
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        # Labels
        self.project_label = QtWidgets.QLabel(self.centralwidget)
        self.project_label.setGeometry(QtCore.QRect(90, 160, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.project_label.setFont(font)
        self.project_label.setObjectName("project_label")
        self.invoice_label = QtWidgets.QLabel(self.centralwidget)
        self.invoice_label.setGeometry(QtCore.QRect(270, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.invoice_label.setFont(font)
        self.invoice_label.setObjectName("invoice_label")

        # MainWindow characteristics
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("Invoice Manager", "Invoice Manager"))
        self.project_button.setText(_translate("MainWindow", "+ New Project"))
        self.project_button.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.project_button.setToolTip("Shortcut: Ctrl+P")
        self.invoice_button.setText(_translate("MainWindow", "+ New Invoice"))
        self.invoice_button.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.invoice_button.setToolTip("Shortcut: Ctrl+N")
        self.project_label.setText(_translate("MainWindow", "Projects"))
        self.invoice_label.setText(_translate("MainWindow", "Invoices"))
        self.radioButton.setText(_translate("MainWindow", "Draft"))
        self.radioButton_2.setText(_translate("MainWindow", "Approved"))
        self.radioButton_3.setText(_translate("MainWindow", "Dispatched"))
        self.radioButton_4.setText(_translate("MainWindow", "Paid"))
        self.radioButton_5.setText(_translate("MainWindow", "Overdue"))

