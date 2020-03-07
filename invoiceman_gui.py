from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from components.progressbar import ProgressBar
from components.label import Label
from components.button import Button, RadioButton
from components.view import *


class UiMainWindow(object):
    """The UIMainWindow class sets up the program's graphical user interface
    and its underlying functions"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Invoice Manager")
        MainWindow.resize(1120, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ListView model characteristics & functionality
        self.listView = ListView(self.centralwidget)
        path = r"C:\Invoice Manager"
        self.dirModel = QtWidgets.QFileSystemModel()
        self.dirModel.setRootPath(QtCore.QDir.rootPath())
        self.dirModel.setReadOnly(False)
        self.listView.setModel(self.dirModel)
        self.listView.setRootIndex(self.dirModel.index(path))

        # TreeView model characteristics & functionality
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setReadOnly(False)
        self.treeView = TreeView(self.centralwidget)
        self.treeView.setModel(self.fileModel)
        self.treeView.setRootIndex(self.fileModel.index(path))
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnWidth(0, 300)

        # Graphical components
        self.project_button = Button("project_button", (10, 80, 121, 41), self.centralwidget)
        self.invoice_button = Button("invoice_button", (10, 20, 121, 41), self.centralwidget)
        self.radioButton = RadioButton("Draft", (460, 60, 95, 20), (self.centralwidget))
        self.radioButton_2 = RadioButton("Approved", (570, 60, 95, 20), (self.centralwidget))
        self.radioButton_3 = RadioButton("Dispatched", (700, 60, 95, 20), (self.centralwidget))
        self.radioButton_4 = RadioButton("Paid", (830, 60, 95, 20), (self.centralwidget))
        self.radioButton_5 = RadioButton("Overdue", (920, 60, 95, 20), (self.centralwidget))
        self.progressBar = ProgressBar(self.centralwidget)
        self.project_label = Label("project_label", (90, 160, 61, 21), self.centralwidget)
        self.invoice_label = Label("invoice_label", (270, 60, 81, 21), self.centralwidget)

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