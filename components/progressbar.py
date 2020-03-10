from PyQt5 import QtCore, QtGui, QtWidgets

class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None, total=100):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(270, 670, 801, 23))
        self.setToolTip("Invoice status")
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.setMaximum(total)
        self.setTextVisible(True)
        self.setObjectName("progressBar")
        self._text = None

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text

    def change_color(self, color):
        template_css = """QProgressBar::chunk { background: %s; }"""
        css = template_css % color
        self.setStyleSheet(css)