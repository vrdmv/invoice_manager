from PyQt5.QtWidgets import *
from components.form import Form
from components.workenv import create_workdir
from components import database
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
        self.data_dict = {
            'business_name_1': '',
            'customer_name': '',
            'customer_email': '',
            'invoice_number': '',
            'send_date': '',
            'due_date': '',
            'note_contents': '',
            'item_1': '',
            'item_1_quantity': '',
            'item_1_price': '',
            'item_1_amount': '',
            'subtotal': '',
            'tax': '',
            'discounts': '',
            'total': '',
            'business_name_2': '',
            'business_email_address': '',
            'business_phone_number': ''
        }

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
                    database.set_initstatus(self.name)
                    active = False
                else:
                    self.show_popup()
            else:
                active = False

    def open_dialog(self):
        if self.dialog.exec_():
            self.data_dict['business_name_1'] = self.dialog.get_input_1()
            self.data_dict['customer_name'] = self.dialog.get_input_2()
            self.data_dict['customer_email'] = self.dialog.get_input_3()
            self.data_dict['invoice_number'] = self.dialog.get_input_4()
            self.data_dict['send_date'] = self.dialog.get_input_5()
            self.data_dict['due_date'] = self.dialog.get_input_6()
            self.data_dict['note_contents'] = self.dialog.get_input_7()
            self.data_dict['item_1'] = self.dialog.get_input_8()
            self.data_dict['item_1_quantity'] = self.dialog.get_input_9()
            self.data_dict['item_1_price'] = self.dialog.get_input_10()
            self.data_dict['item_1_amount'] = self.dialog.get_input_11()
            self.data_dict['subtotal'] = self.dialog.get_input_12()
            self.data_dict['tax'] = self.dialog.get_input_13()
            self.data_dict['discounts'] = self.dialog.get_input_14()
            self.data_dict['total'] = self.dialog.get_input_15()
            self.data_dict['business_name_2'] = self.dialog.get_input_16()
            self.data_dict['business_email_address'] = self.dialog.get_input_17()
            self.data_dict['business_phone_number'] = self.dialog.get_input_18()
            new_pdf = self.process_pdf(self.template_path)
            self.produce_invoice(self.output_path, new_pdf)


    def process_pdf(self, template_path):
        try:
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
        except pdfrw.PdfParseError:
            self.show_popup_2()



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

    def show_popup_2(self):
        """Show a pop-up message if invoice name already exists"""
        msg = QMessageBox()
        msg.setWindowTitle("Missing template.")
        msg.setText("The invoice template is missing."
                    "Please add the invoice template to the same directory as"
                    "the .exe file.")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()