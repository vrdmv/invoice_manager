from PyQt5 import QtCore, QtGui, QtWidgets

class Label(QtWidgets.QLabel):
    def __init__(self, coordinates, parent=None):
        super().__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.setFont(font)
        self.setGeometry(QtCore.QRect(*coordinates))