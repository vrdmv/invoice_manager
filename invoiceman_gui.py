from components.progressbar import ProgressBar
from components.label import Label
from components.button import Button
from components.view import *
from components.main_tab import MainTab


class UiMainWindow(object):
    """The UiMainWindow class sets up the program's graphical user interface."""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Invoice Manager")
        MainWindow.resize(1120, 750)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.tabwidget = MainTab(self.centralwidget)
        self.project_button = Button("project_button", (10, 80, 121, 41),
                                     self.tabwidget.main_tab)
        self.invoice_button = Button("invoice_button", (10, 20, 121, 41),
                                     self.tabwidget.main_tab)
        self.project_label = Label("project_label", (80, 155, 81, 21),
                                   self.tabwidget.main_tab)
        self.invoice_label = Label("invoice_label", (600, 50, 81, 21),
                                   self.tabwidget.main_tab)
        self.status_label = Label("status_label", (210, 550, 800, 263),
                                  self.tabwidget.main_tab)
        self.progressBar = ProgressBar(self.tabwidget.main_tab)

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
        self.project_label.setText(_translate("MainWindow", "- Projects -"))
        self.invoice_label.setText(_translate("MainWindow", "- Invoices -"))
        self.status_label.setText(_translate("MainWindow", "Status: "))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tabwidget.main_tab),
                                  _translate("MainWindow", "Main"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tabwidget.visual_tab),
                                  _translate("MainWindow", "Visual"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tabwidget.exch_tab),
                                  _translate("MainWindow", "Exchange rates"))
        self.tabwidget.exch_tab.label_2.setText(_translate("MainWindow", "Convert"))
        self.tabwidget.exch_tab.label_3.setText(_translate("MainWindow", "of"))
        self.tabwidget.exch_tab.label_4.setText(_translate("MainWindow", "to"))
        self.tabwidget.exch_tab.label_8.setText(_translate("MainWindow", "with exchange rate of"))
        self.tabwidget.exch_tab.label_9.setText(_translate("MainWindow", "(dd-mm-yyyy)"))
        self.tabwidget.exch_tab.pushButton_3.setText(_translate("MainWindow", "Convert amounts"))
        self.tabwidget.exch_tab.tableWidget.setSortingEnabled(False)
        item = self.tabwidget.exch_tab.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tabwidget.exch_tab.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tabwidget.exch_tab.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Original amount"))
        item = self.tabwidget.exch_tab.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Converted amount"))
        item = self.tabwidget.exch_tab.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Exchange rate"))
        __sortingEnabled = self.tabwidget.exch_tab.tableWidget.isSortingEnabled()
        self.tabwidget.exch_tab.tableWidget.setSortingEnabled(False)
        item = self.tabwidget.exch_tab.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "(dd-mm-yyyy)"))
        item = self.tabwidget.exch_tab.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1.00 USD"))
        item = self.tabwidget.exch_tab.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "0.81 EUR "))
        item = self.tabwidget.exch_tab.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "1 EUR = 1.2378 USD"))
        self.tabwidget.exch_tab.label.setText(_translate("MainWindow", "Currency converter"))
        self.tabwidget.exch_tab.tableWidget.setSortingEnabled(__sortingEnabled)