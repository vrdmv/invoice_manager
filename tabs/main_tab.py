from PyQt5 import QtCore, QtWidgets
from tabs.visual import Visual
from tabs.exchange import Exchange

class MainTab(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(0, 0, 1120, 750))
        self.main_tab = QtWidgets.QWidget()
        self.addTab(self.main_tab, "")
        self.visual_tab = Visual()
        self.addTab(self.visual_tab, "")
        self.exch_tab = Exchange()
        self.addTab(self.exch_tab, "")


