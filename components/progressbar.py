from PyQt5 import QtCore, QtWidgets

class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None, total=100):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(270, 670, 815, 23))
        self.setToolTip("Invoice status")
        self.setAutoFillBackground(False)
        self.setStyleSheet("")
        self.setMaximum(total)
        self.setTextVisible(True)
        self.setObjectName("progressBar")
        self._text = None

    def renew(self, text, value):
        self._text = text
        self.setValue(value)

    def text(self):
        return self._text

    # def change_color(self, color):
    #     template_css = """QProgressBar::chunk { background: %s; }"""
    #     css = template_css % color
    #     self.setStyleSheet(css)