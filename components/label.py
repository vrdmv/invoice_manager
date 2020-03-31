from PyQt5 import QtCore, QtGui, QtWidgets

class Label(QtWidgets.QLabel):
    def __init__(self, coordinates, text, font_size, parent=None):
        super().__init__(parent)
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(font_size)
        self.font.setWeight(50)
        self.font.setBold(False)
        self.setFont(self.font)
        self.setGeometry(QtCore.QRect(*coordinates))
        self.setText(text)
