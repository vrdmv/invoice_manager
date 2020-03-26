from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

path = os.path.join("C:\\", "Invoice Manager")


class TreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setSortingEnabled(True)
        self.setGeometry(QtCore.QRect(270, 90, 815, 571))
        self.setObjectName("treeView")
        self.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fileModel = QFileSystemModel()
        self.fileModel.setReadOnly(False)
        self.setModel(self.fileModel)
        self.setRootIndex(self.fileModel.index(path))


class ListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(30, 190, 221, 471))
        self.setAlternatingRowColors(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragEnabled(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setMovement(QListView.Snap)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setObjectName("listView")
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setReadOnly(False)
        self.setModel(self.dirModel)
        self.setRootIndex(self.dirModel.index(path))

