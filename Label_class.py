from PyQt5 import QtCore, QtGui, QtWidgets

class Label(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.setFont(font)