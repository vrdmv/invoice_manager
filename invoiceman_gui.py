from components.button import Button
from components.label import Label
from components.progressbar import ProgressBar
from components.view import *
from tabs.main_tab import MainTab


class UiMainWindow(object):
    """The UiMainWindow class sets up the program's graphical user interface."""
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("Invoice Manager")
        MainWindow.resize(1120, 750)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setWindowTitle("Invoice Manager")
        self.centralwidget = QWidget(MainWindow)
        self.tabwidget = MainTab(self.centralwidget)
        self.tabwidget.setTabText(0, "Main")
        self.tabwidget.setTabText(1, "Visual")
        self.tabwidget.setTabText(2, "Finance")
        self.project_button = Button((30, 80, 121, 41), "+ New Project",
                                     "Ctrl+P", "Shortcut: Ctrl+P",
                                     self.tabwidget.main_tab)
        self.invoice_button = Button((30, 20, 121, 41), "+ New Invoice",
                                     "Ctrl+N", "Shortcut: Ctrl+N",
                                     self.tabwidget.main_tab)
        self.project_label = Label((90, 155, 95, 21), "- Projects -", 11,
                                   self.tabwidget.main_tab)
        self.invoice_label = Label((600, 50, 95, 21), "- Invoices -", 11,
                                   self.tabwidget.main_tab)
        self.status_label = Label((205, 550, 800, 263), "Status: ", 11,
                                  self.tabwidget.main_tab)
        self.progressBar = ProgressBar(self.tabwidget.main_tab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
