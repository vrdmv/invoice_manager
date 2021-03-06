from currency_converter import CurrencyConverter
from components.tablewidget import TableWidget
from components.label import Label
from components.button import Button
from components import database
from components.misc import *



c = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')


class Exchange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Initialize the ui elements of the exchange rate tab"""
        currencies = ("EUR", "USD", "GBP")
        self.frame_1 = Frame((20, 10, 1077, 690), QtWidgets.QFrame.StyledPanel,
                             QtWidgets.QFrame.Raised, self)
        self.lay_1 = QtWidgets.QHBoxLayout(self.frame_1)
        self.frame_2 = Frame((105, 90, 881, 48), QtWidgets.QFrame.StyledPanel,
                             QtWidgets.QFrame.Raised, self.frame_1)
        self.lay_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.label = Label((30, 30, 71, 21), "Convert", 11, self.frame_2)
        self.lay_2.addWidget(self.label)
        self.line = LineEdit((120, 30, 121, 21), self.frame_2)
        self.lay_2.addWidget(self.line)
        self.label_2 = Label((270, 30, 21, 21), "of", 11, self.frame_2)
        self.lay_2.addWidget(self.label_2)
        self.combo = ComboBox((420, 30, 21, 21), self.frame_2)
        self.combo.addItems(currencies)
        self.lay_2.addWidget(self.combo)
        self.label_3 = Label((270, 30, 21, 21), "to", 11, self.frame_2)
        self.lay_2.addWidget(self.label_3)
        self.combo_2 = ComboBox((460, 30, 81, 21), self.frame_2)
        self.combo_2.addItems(currencies)
        self.lay_2.addWidget(self.combo_2)
        self.label_4 = Label((570, 30, 171, 21), "with exchange rate of", 11,
                             self.frame_2)
        self.lay_2.addWidget(self.label_4)
        self.date_edit = DateEdit((300, 30, 121, 21), self.frame_2)
        self.lay_2.addWidget(self.date_edit)
        self.label_5 = Label((300, 30, 121, 21), "(dd-mm-yyyy)", 11,
                             self.frame_2)
        self.lay_2.addWidget(self.label_5)
        self.convert_button = Button((105, 185, 151, 41), "Convert amounts",
                                     "Enter", "Shortcut: 'Enter'", self.frame_1)
        self.frame_3 = Frame((295, 170, 691, 76), QtWidgets.QFrame.StyledPanel,
                             QtWidgets.QFrame.Raised, self.frame_1)
        self.lay_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.tablewidget = TableWidget(self.frame_3)
        self.tablewidget.setSortingEnabled(False)
        item_1 = self.tablewidget.verticalHeaderItem(0)
        item_1.setText("")
        item_2 = self.tablewidget.horizontalHeaderItem(0)
        item_2.setText("Date")
        item_3 = self.tablewidget.horizontalHeaderItem(1)
        item_3.setText("Original amount")
        item_4 = self.tablewidget.horizontalHeaderItem(2)
        item_4.setText("Converted amount")
        item_5 = self.tablewidget.horizontalHeaderItem(3)
        item_5.setText("Exchange rate")

        self.lay_3.addWidget(self.tablewidget)
        self.label_6 = Label((450, 25, 221, 41), "- Currency converter -", 11,
                             self.frame_1)
        self.combo.setCurrentIndex(currencies.index('EUR'))
        self.combo_2.setCurrentIndex(currencies.index('USD'))
        self.convert_button.clicked.connect(self.process_input)

        self.label_7 = Label((450, 290, 221, 41), "- Cashflow summary -", 11,
                             self.frame_1)

        self.label_8 = Label((515, 550, 41, 41), "Paid", 9, self.frame_1)
        self.label_9 = Label((150, 550, 61, 41), "Pending", 9, self.frame_1)
        self.label_10 = Label((880, 550, 61, 41), "Overdue", 9, self.frame_1)

        self.label_11 = Label((40, 430, 271, 71), "€0", 40, self.frame_1)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_12 = Label((390, 430, 271, 71), "€0", 40, self.frame_1)
        self.label_12.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_13 = Label((770, 430, 271, 71), "€0", 40, self.frame_1)
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter)

    def process_input(self):
        self.text = self.line.text()
        self.item_1 = self.combo.currentText()
        self.item_2 = self.combo_2.currentText()
        self.date = self.date_edit.date().toPyDate()
        self.result_raw = c.convert(float(self.text), self.item_1, self.item_2,
                           date=self.date)
        self.result = round(self.result_raw, 2)
        self.exchange_rate = round(self.result/int(self.text), 4)
        self.display_output()

    def display_output(self):
        self.tablewidget.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.date}"))
        self.tablewidget.setItem(0, 1, QtWidgets.QTableWidgetItem(self.text +
                                                                  " " +
                                                                  f"{self.item_1}"))
        self.tablewidget.setItem(0, 2, QtWidgets.QTableWidgetItem(f"{self.result}" +
                                                                  " " +
                                                                  f"{self.item_2}"))
        self.tablewidget.setItem(0, 3,
                                 QtWidgets.QTableWidgetItem("1 " + f"{self.item_1}" +
                                                            " = " +
                                                            f"{self.exchange_rate}" +
                                                            " " +
                                                            f"{self.item_2}"))


    def update_cashflow_labels(self):
        self.label_11.clear()
        self.label_12.clear()
        self.label_13.clear()
        try:
            pending, overdue, paid = database.get_total()
            pending_str = "€" + f"{pending}"
            self.label_11.setText(pending_str)
            overdue_str = "€" + f"{overdue}"
            self.label_13.setText(overdue_str)
            paid_str = "€" + f"{paid}"
            self.label_12.setText(paid_str)
        except TypeError:
            self.label_11.setText("€0")
            self.label_12.setText("€0")
            self.label_13.setText("€0")
            return self.label_11, self.label_12, self.label_13
