from PyQt5.QtWidgets import *

# Create input class, pass form and label
# getter property to get self.input.text
# pass key to input class and

class UserInput(QLineEdit):
    """Show a pop-up form for the user to input invoice data."""
    def __init__(self, label, parent=None):
        super().__init__(parent)
        self.label = QLabel(label)
        self.input = QLineEdit(self)







