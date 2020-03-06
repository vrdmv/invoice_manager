from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setSortingEnabled(True)
        self.setGeometry(QtCore.QRect(270, 90, 801, 571))
        self.setObjectName("treeView")
        self.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setContextMenuPolicy(Qt.CustomContextMenu)



class ListView(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(10, 190, 221, 471))
        self.setAlternatingRowColors(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragEnabled(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setMovement(QListView.Snap)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setObjectName("listView")
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)