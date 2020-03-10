from PyQt5.QtWidgets import *
from invoiceman_gui import UiMainWindow
from components.palette import dark_palette
from components.invoice import Invoice
from components.contextmenu import ContextMenu
from database import *
from workenv import *
import sys
import shutil
import send2trash
import os


class Logic(QMainWindow, UiMainWindow, Invoice):
    """The Logic class contains all of the program's functions"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.project_button.clicked.connect(self.make_project)
        self.invoice_button.clicked.connect(self.make_invoice)
        self.listView.clicked.connect(self.show_files)
        self.treeView.clicked.connect(self.check_status)
        self.treeView.doubleClicked.connect(self.open_file)
        self.treeView.customContextMenuRequested.connect(self.open_menu)

    # Program Functions
    def show_files(self, index):
        """When a directory is selected in the list view, display all of its files
        in the tree view."""
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.treeView.setRootIndex(self.fileModel.setRootPath(path))

    def open_file(self, index):
        """ Open file upon double-click."""
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        path_str = str(path)
        os.startfile(path_str)

    def check_status(self, index):
        """Check invoice status based on database entries."""
        raw_filename = self.fileModel.fileName(index)
        file_name = raw_filename[:-5]
        try:
            if status_query(file_name) == 'Draft':
                self.progressBar.renew("Draft", 25)
            if status_query(file_name) == 'Dispatched':
                self.progressBar.renew("Dispatched", 50)
            if status_query(file_name) == 'Overdue':
                self.progressBar.renew("Overdue", 75)
            if status_query(file_name) == 'Paid':
                self.progressBar.renew("Paid", 100)
        except TypeError:
            return

    def dlt(self, index):
        """ Send the selected file to the recycle bin"""
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        send2trash.send2trash(os.path.abspath(path))

    def move_to_archive(self, index):
        """Move selected file to archive"""
        source = self.fileModel.fileInfo(index).absoluteFilePath()
        destination = create_archive()
        shutil.move(os.path.abspath(source), os.path.abspath(destination))

    def copy(self, index):
        """Copy the selected file within the same directory."""
        source = self.fileModel.fileInfo(index).absoluteFilePath()
        destination = self.dirModel.fileInfo(index).absoluteFilePath()
        dest_str = str(destination)
        dest_1half = dest_str[:-5]
        dest_2half = dest_str[-5:]
        if not os.path.exists(dest_str):
            shutil.copy(os.path.abspath(source), os.path.abspath(dest_str))
        else:
            new_dest = dest_1half + " - Copy" + dest_2half
            shutil.copy(os.path.abspath(source), os.path.abspath(new_dest))

    def open_menu(self, position):
        """Setup a context menu, containing various options, to open upon right
        click."""
        index = self.treeView.indexAt(position)
        raw_filename = self.fileModel.fileName(index)
        file_name = raw_filename[:-5]
        if not index.isValid():
            return
        menu = ContextMenu(self)
        action = menu.exec_(self.treeView.viewport().mapToGlobal(position))
        try:
            if action == menu.delete:
                self.dlt(index)
            if action == menu.rename:
                self.treeView.edit(index)
            if action == menu.copy:
                self.copy(index)
            if action == menu.archive:
                self.move_to_archive(index)
            if action == menu.dispatched:
                update2dispatched(file_name)
            if action == menu.paid:
                update2paid(file_name)
            if action == menu.overdue:
                update2overdue(file_name)
        except PermissionError:
            print("Nope, can't do that!")

    def make_project(self):
        """Create a new project folder."""
        active = True
        while active:
            text, ok = QInputDialog.getText(self, "Project name",
                                            "Please enter project name:                    ",
                                            QLineEdit.Normal)
            if ok and text != '':
                project_name = text
                project_dir = os.path.join("C:\\", "Invoice Manager",
                                           f"{project_name}")
                if not os.path.exists(project_dir):
                    os.makedirs(project_dir)
                    active = False
            else:
                active = False


create_workdir()
create_archive()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    qApp.setPalette(dark_palette)
    qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da;"
                       " border: 1px solid white; }")
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())
