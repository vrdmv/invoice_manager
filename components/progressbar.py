from PyQt5 import QtCore, QtGui, QtWidgets

class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(270, 670, 801, 23))
        self.setToolTip("Invoice status")
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.setMaximum(100)
        self.setTextVisible(False)
        self.setObjectName("progressBar")
