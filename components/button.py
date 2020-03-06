from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton


class Button(QPushButton):
    def __init__(self, name, coordinates, parent=None):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.setFont(font)
        self.setObjectName(name)
        self.setGeometry(QtCore.QRect(*coordinates))


class RadioButton(QRadioButton):
    def __init__(self, name, coordinates, parent=None):
        super().__init__(parent)
        self.setObjectName(name)
        self.setGeometry(QtCore.QRect(*coordinates))
