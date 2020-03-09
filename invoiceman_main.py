from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from invoiceman_gui import UiMainWindow
from components.palette import dark_palette
from components.invoice import Invoice, collection
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

        # "New Project" button function call
        self.project_button.clicked.connect(self.make_project)

        # "New Invoice" button function call
        self.invoice_button.clicked.connect(self.make_invoice)

        # When folder in listView is clicked, the items stored in it are
        # displayed in the treeview.
        self.listView.clicked.connect(self.on_click)

        # Returns the name of the file which was clicked last
        self.treeView.clicked.connect(self.check_status)

        # Open item in treeview when double-clicked
        self.treeView.doubleClicked.connect(self.on_dblclick)

        # Open context menu when item clicked in treeView.
        self.treeView.customContextMenuRequested.connect(self.openmenu)

        # Update progress bar based on radio button toggled
        self.radioButton.toggled['bool'].connect(lambda: self.progressBar.setValue(25))
        self.radioButton_2.toggled['bool'].connect(lambda: self.progressBar.setValue(50))
        self.radioButton_3.toggled['bool'].connect(lambda: self.progressBar.setValue(75))
        self.radioButton_4.toggled['bool'].connect(lambda: self.progressBar.setValue(100))


    # Program Functions
    def on_click(self, index):
        """When a directory is selected in the list view, show all of its files
        in the tree view."""
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.treeView.setRootIndex(self.fileModel.setRootPath(path))

    def on_dblclick(self, index):
        """ Open file upon double-click."""
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        path_str = str(path)
        os.startfile(path_str)

    def check_status(self, index):
        """Check invoice status based on database etries"""
        raw_filename = self.fileModel.fileName(index)
        file_name = raw_filename[:-5]
        status_query = collection.find_one({"invoice_name": f"{file_name}"})
        if status_query["status"] == 'Draft':
            self.radioButton.setChecked(True)
        if status_query["status"] == 'Dispatched':
            self.radioButton_2.setChecked(True)
        if status_query["status"] == 'Paid':
            self.radioButton_3.setChecked(True)
        if status_query["status"] == 'Overdue':
            self.radioButton_4.setChecked(True)

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
            copy = " - Copy"
            new_dest = dest_1half + f"{copy}" + dest_2half
            shutil.copy(os.path.abspath(source), os.path.abspath(new_dest))

    def openmenu(self, position):
        """Setup a context menu, containing various options, to open upon right
        click."""
        index = self.treeView.indexAt(position)
        if not index.isValid():
            return
        menu = QMenu(self)
        rename_action = menu.addAction("Rename")
        copy_action = menu.addAction("Copy")
        delete_action = menu.addAction("Send to trashbin")
        archive_action = menu.addAction("Move to archive")
        action = menu.exec_(self.treeView.viewport().mapToGlobal(position))
        try:
            if action == delete_action:
                self.dlt(index)
            if action == rename_action:
                self.treeView.edit(index)
            if action == copy_action:
                self.copy(index)
            if action == archive_action:
                self.move_to_archive(index)
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
