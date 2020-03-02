from PyQt5 import QtCore, QtGui, QtWidgets

class Button(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(Button, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.setFont(font)