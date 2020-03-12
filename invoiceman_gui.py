from components.progressbar import ProgressBar
from components.label import Label
from components.button import Button
from components.view import *


class UiMainWindow(object):
    """The UiMainWindow class sets up the program's graphical user interface."""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Invoice Manager")
        MainWindow.resize(1120, 750)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.tabwidget = QTabWidget(self.centralwidget)
        self.tabwidget.setGeometry(QRect(0, 0, 1120, 750))
        self.tab = QWidget()
        self.tabwidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tabwidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tabwidget.addTab(self.tab_3, "")

        self.project_button = Button("project_button", (10, 80, 121, 41), self.tab)
        self.invoice_button = Button("invoice_button", (10, 20, 121, 41), self.tab)
        self.project_label = Label("project_label", (90, 160, 61, 21), self.tab)
        self.invoice_label = Label("invoice_label", (600, 60, 81, 21), self.tab)
        self.status_label = Label("status_label", (210, 550, 800, 263), self.tab)
        self.progressBar = ProgressBar(self.tab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("Invoice Manager", "Invoice Manager"))
        self.project_button.setText(_translate("MainWindow", "+ New Project"))
        self.project_button.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.project_button.setToolTip("Shortcut: Ctrl+P")
        self.invoice_button.setText(_translate("MainWindow", "+ New Invoice"))
        self.invoice_button.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.invoice_button.setToolTip("Shortcut: Ctrl+N")
        self.project_label.setText(_translate("MainWindow", "Projects"))
        self.invoice_label.setText(_translate("MainWindow", "Invoices"))
        self.status_label.setText(_translate("MainWindow", "Status: "))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab),
                                  _translate("MainWindow", "Main"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "Visual"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_3),
                                  _translate("MainWindow", "Exchange rates"))
