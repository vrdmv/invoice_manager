from PyQt5 import QtCore, QtGui, QtWidgets

class Frame(QtWidgets.QFrame):
    def __init__(self, coordinates, shape, shadow, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(*coordinates))
        self.setFrameShape(shape)
        self.setFrameShadow(shadow)

class ComboBox(QtWidgets.QComboBox):
    def __init__(self, coordinates, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(*coordinates))

class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, coordinates, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(*coordinates))

class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, coordinates, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(*coordinates))