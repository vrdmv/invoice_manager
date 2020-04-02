from PyQt5.QtWidgets import *


class Form(QDialog):
    """Show a pop-up form for the user to input invoice data."""
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, parent=None):
        super().__init__(parent)

        self.input_list = [QLineEdit(self), QLineEdit(self), QLineEdit(self),
                           QLineEdit(self), QLineEdit(self), QLineEdit(self),
                           QLineEdit(self), QLineEdit(self), QLineEdit(self),
                           QLineEdit(self), QLineEdit(self), QLineEdit(self),
                           QLineEdit(self), QLineEdit(self), QLineEdit(self),
                           QLineEdit(self), QLineEdit(self), QLineEdit(self)]

        self.input = self.input_list[0]
        self.input_1 = self.input_list[1]
        self.input_2 = self.input_list[2]
        self.input_3 = self.input_list[3]
        self.input_4 = self.input_list[4]
        self.input_5 = self.input_list[5]
        self.input_6 = self.input_list[6]
        self.input_7 = self.input_list[7]
        self.input_8 = self.input_list[8]
        self.input_9 = self.input_list[9]
        self.input_10 = self.input_list[10]
        self.input_11 = self.input_list[11]
        self.input_12 = self.input_list[12]
        self.input_13 = self.input_list[13]
        self.input_14 = self.input_list[14]
        self.input_15 = self.input_list[15]
        self.input_16 = self.input_list[16]
        self.input_17 = self.input_list[17]

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok |
                                           QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.formbox = QGroupBox("Please provide invoice data below: ")
        layout = QFormLayout()
        layout.addRow(QLabel("Business name: "), self.input)
        layout.addRow(QLabel("Customer name: "), self.input_1)
        layout.addRow(QLabel("Customer email: "), self.input_2)
        layout.addRow(QLabel("Invoice number: "), self.input_3)
        layout.addRow(QLabel("Sent date: "), self.input_4)
        layout.addRow(QLabel("Due date: "), self.input_5)
        layout.addRow(QLabel("Note: "), self.input_6)
        layout.addRow(QLabel("Item 1: "), self.input_7)
        layout.addRow(QLabel("Item 1 Quantity: "), self.input_8)
        layout.addRow(QLabel("Item 1 Price: "), self.input_9)
        layout.addRow(QLabel("Item 1 Amount: "), self.input_10)
        layout.addRow(QLabel("Subtotal: "), self.input_11)
        layout.addRow(QLabel("Tax: "), self.input_12)
        layout.addRow(QLabel("Discounts: "), self.input_13)
        layout.addRow(QLabel("Total: "), self.input_14)
        layout.addRow(QLabel("Business name repeat: "), self.input_15)
        layout.addRow(QLabel("Business email: "), self.input_16)
        layout.addRow(QLabel("Business phone: "), self.input_17)
        self.formbox.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formbox)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)
        self.setMinimumWidth(400)
        self.setWindowTitle("Invoice data input")
