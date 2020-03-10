from PyQt5 import QtCore, QtGui, QtWidgets

class ContextMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        submenu = QtWidgets.QMenu(self)
        submenu.setTitle("Update status: ")
        self.addMenu(submenu)
        self.rename_action = self.addAction("Rename")
        self.copy_action = self.addAction("Copy")
        self.delete_action = self.addAction("Send to trashbin")
        self.archive_action = self.addAction("Move to archive")
        self.update_1 = submenu.addAction("Set as dispatched")
        self.update_2 = submenu.addAction("Set as paid")
        self.update_3 = submenu.addAction("Set as overdue")