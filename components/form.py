from PyQt5.QtWidgets import *


# Create input class, pass form and label
# getter property to get self.input.text
# pass key to input class and

class Form(QDialog):
    """Show a pop-up form for the user to input invoice data."""
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, parent=None):
        super().__init__(parent)
        self.input_1 = QLineEdit(self)
        self.input_2 = QLineEdit(self)
        self.input_3 = QLineEdit(self)
        self.input_4 = QLineEdit(self)
        self.input_5 = QLineEdit(self)
        self.input_6 = QLineEdit(self)
        self.input_7 = QLineEdit(self)
        self.input_8 = QLineEdit(self)
        self.input_9 = QLineEdit(self)
        self.input_10 = QLineEdit(self)
        self.input_11 = QLineEdit(self)
        self.input_12 = QLineEdit(self)
        self.input_13 = QLineEdit(self)
        self.input_14 = QLineEdit(self)
        self.input_15 = QLineEdit(self)
        self.input_16 = QLineEdit(self)
        self.input_17 = QLineEdit(self)
        self.input_18 = QLineEdit(self)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok |
                                           QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.formbox = QGroupBox("Please provide invoice data below: ")
        layout = QFormLayout()
        layout.addRow(QLabel("Business name: "), self.input_1)
        layout.addRow(QLabel("Customer name: "), self.input_2)
        layout.addRow(QLabel("Customer email: "), self.input_3)
        layout.addRow(QLabel("Invoice number: "), self.input_4)
        layout.addRow(QLabel("Sent date: "), self.input_5)
        layout.addRow(QLabel("Due date: "), self.input_6)
        layout.addRow(QLabel("Note: "), self.input_7)
        layout.addRow(QLabel("Item 1: "), self.input_8)
        layout.addRow(QLabel("Item 1 Quantity: "), self.input_9)
        layout.addRow(QLabel("Item 1 Price: "), self.input_10)
        layout.addRow(QLabel("Item 1 Amount: "), self.input_11)
        layout.addRow(QLabel("Subtotal: "), self.input_12)
        layout.addRow(QLabel("Tax: "), self.input_13)
        layout.addRow(QLabel("Discounts: "), self.input_14)
        layout.addRow(QLabel("Total: "), self.input_15)
        layout.addRow(QLabel("Business name repeat: "), self.input_16)
        layout.addRow(QLabel("Business email: "), self.input_17)
        layout.addRow(QLabel("Business phone: "), self.input_18)
        self.formbox.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formbox)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)
        self.setMinimumWidth(400)
        self.setWindowTitle("Invoice data input")

    def get_input_1(self):
        return self.input_1.text()

    def get_input_2(self):
        return self.input_2.text()

    def get_input_3(self):
        return self.input_3.text()

    def get_input_4(self):
        return self.input_5.text()

    def get_input_5(self):
        return self.input_5.text()

    def get_input_6(self):
        return self.input_6.text()

    def get_input_7(self):
        return self.input_7.text()

    def get_input_8(self):
        return self.input_8.text()

    def get_input_9(self):
        return self.input_9.text()

    def get_input_10(self):
        return self.input_10.text()

    def get_input_11(self):
        return self.input_11.text()

    def get_input_12(self):
        return self.input_12.text()

    def get_input_13(self):
        return self.input_13.text()

    def get_input_14(self):
        return self.input_14.text()

    def get_input_15(self):
        return self.input_15.text()

    def get_input_16(self):
        return self.input_16.text()

    def get_input_17(self):
        return self.input_17.text()

    def get_input_18(self):
        return self.input_18.text()