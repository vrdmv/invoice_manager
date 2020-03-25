from PyQt5.QtWidgets import *
from components.form import Form
from workenv import create_workdir
import database
import os
import pdfrw

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


class Invoice(QInputDialog):
    """Create an invoice from a pdf template and populate it based on user
     input."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.work_dir = create_workdir()
        self.template_path = 'invoice_template.pdf'
        self.dialog = Form()
        input_1 = self.dialog.get_input_1()
        self.data_dict = {
            'business_name_1': f"{input_1}",
            'customer_name': 'company.io',
            'customer_email': 'joe@company.io',
            'invoice_number': '102394',
            'send_date': '2018-02-13',
            'due_date': '2018-03-13',
            'note_contents': 'Thank you for your business, Joe',
            'item_1': 'Data consulting services',
            'item_1_quantity': '10 hours',
            'item_1_price': '$200/hr',
            'item_1_amount': '$2000',
            'subtotal': '$2000',
            'tax': '0',
            'discounts': '0',
            'total': '$2000',
            'business_name_2': 'Bostata LLC',
            'business_email_address': 'hi@bostata.com',
            'business_phone_number': '(617) 930-4294'
        }
        new_pdf = self.process_pdf(self.template_path)
        self.dialog.accepted.connect(lambda: self.produce_invoice(self.output_path, new_pdf))

    def write_custom_pdf(self):
        """Create an invoice based on a pdf template."""
        user_input = QInputDialog()
        active = True
        while active:
            text, ok = user_input.getText(self, "Invoice name",
                                          "Please enter a name for the invoice          ")
            if ok and text != '':
                self.name = text
                self.output_path = f"{self.work_dir}" + "\\" + \
                                      f"{self.name}" + ".pdf"
                if not os.path.exists(self.output_path):
                    self.open_dialog()
                    # database.set_initstatus(self.name)
                    active = False
                else:
                    self.show_popup()
            else:
                active = False

    def open_dialog(self):
        self.dialog.exec_()

    def process_pdf(self, template_path):
        template_pdf = pdfrw.PdfReader(template_path)
        template_pdf.Root.AcroForm.update(
            pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        annotations = template_pdf.pages[0][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in self.data_dict.keys():
                        annotation.update(pdfrw.PdfDict(
                            V=f"{self.data_dict[key]}"))
        return template_pdf

    def produce_invoice(self, output_path, new_pdf):
        new_invoice = pdfrw.PdfWriter().write(output_path, new_pdf)
        return new_invoice

    def show_popup(self):
        """Show a pop-up message if invoice name already exists"""
        msg = QMessageBox()
        msg.setWindowTitle("File/folder already exists.")
        msg.setText("The invoice or project you are trying to create "
                    "already exists."
                    " Please specify another name.")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
