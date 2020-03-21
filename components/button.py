from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, coordinates, parent=None):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.setFont(font)
        self.setGeometry(QtCore.QRect(*coordinates))
