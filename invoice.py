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
                    database.set_initstatus(self.name, self.data_dict['total'])
                    active = False
                else:
                    self.show_popup()
            else:
                active = False

    def open_dialog(self):
        """Populate the pdf template with user input"""
        if self.dialog.exec_():
            self.data_dict['business_name_1'] = self.dialog.input_list[0].text()
            self.data_dict['customer_name'] = self.dialog.input_list[1].text()
            self.data_dict['customer_email'] = self.dialog.input_list[2].text()
            self.data_dict['invoice_number'] = self.dialog.input_list[3].text()
            self.data_dict['send_date'] = self.dialog.input_list[4].text()
            self.data_dict['due_date'] = self.dialog.input_list[5].text()
            self.data_dict['note_contents'] = self.dialog.input_list[6].text()
            self.data_dict['item_1'] = self.dialog.input_list[7].text()
            self.data_dict['item_1_quantity'] = self.dialog.input_list[8].text()
            self.data_dict['item_1_price'] = self.dialog.input_list[9].text()
            self.data_dict['item_1_amount'] = self.dialog.input_list[10].text()
            self.data_dict['subtotal'] = self.dialog.input_list[11].text()
            self.data_dict['tax'] = self.dialog.input_list[12].text()
            self.data_dict['discounts'] = self.dialog.input_list[13].text()
            self.data_dict['total'] = self.dialog.input_list[14].text()
            self.data_dict['business_name_2'] = self.dialog.input_list[15].text()
            self.data_dict['business_email_address'] = self.dialog.input_list[16].text()
            self.data_dict['business_phone_number'] = self.dialog.input_list[17].text()
            new_pdf = self.process_pdf(self.template_path)
            self.produce_invoice(self.output_path, new_pdf)

    def process_pdf(self, template_path):
        """Access the pdf fields."""
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
        """Make a new invoice pdf document, populated with the user's input"""
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