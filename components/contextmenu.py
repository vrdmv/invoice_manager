from PyQt5 import QtCore, QtGui, QtWidgets

class ContextMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        submenu = QtWidgets.QMenu(self)
        submenu.setTitle("Update status: ")
        self.addMenu(submenu)
        self.rename = self.addAction("Rename")
        self.copy = self.addAction("Copy")
        self.delete = self.addAction("Send to trashbin")
        self.archive = self.addAction("Move to archive")
        self.dispatched = submenu.addAction("Set as dispatched")
        self.paid = submenu.addAction("Set as paid")
        self.overdue = submenu.addAction("Set as overdue")