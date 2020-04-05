import sys
import shutil
import send2trash
from components import database
from components import workenv
from components.contextmenu import ContextMenu
from components.palette import dark_palette
from components.view import *
from invoice import Invoice
from invoiceman_gui import UiMainWindow


class Logic(QMainWindow, UiMainWindow, Invoice):
    """The Logic class contains all of the program's functions"""
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.listView = ListView(self.tabwidget.main_tab)
        self.treeView = TreeView(self.tabwidget.main_tab)
        self.treeView.setColumnHidden(1, True)
        self.treeView.setColumnWidth(0, 300)
        self.project_button.clicked.connect(self.make_project)
        self.invoice_button.clicked.connect(self.write_custom_pdf)
        self.treeView.doubleClicked.connect(self.open_file)
        self.treeView.clicked.connect(self.check_status)
        self.treeView.customContextMenuRequested.connect(self.open_menu)
        self.listView.clicked.connect(self.show_files)
        self.tabwidget.currentChanged.connect(self.refresh_visual_tab)
        self.tabwidget.currentChanged.connect(self.refresh_exchange_tab)

    # Program Functions
    def show_files(self, index):
        """When a directory is selected in the list view, display all of its
        files in the tree view."""
        cur_path = self.listView.dirModel.fileInfo(index).absoluteFilePath()
        self.treeView.setRootIndex(self.treeView.fileModel.setRootPath(cur_path))

    def open_file(self, index):
        """ Open file upon double-click."""
        cur_path = self.treeView.fileModel.fileInfo(index).absoluteFilePath()
        os.startfile(cur_path)

    def check_status(self, index):
        """Check invoice status based on database entries."""
        file_name = self.treeView.fileModel.fileName(index)
        try:
            if database.status_query(file_name[:-4]) == 'Draft':
                self.progressBar.renew("Draft", 25)
            if database.status_query(file_name[:-4]) == 'Dispatched':
                self.progressBar.renew("Dispatched", 50)
            if database.status_query(file_name[:-4]) == 'Overdue':
                self.progressBar.renew("Overdue", 75)
            if database.status_query(file_name[:-4]) == 'Paid':
                self.progressBar.renew("Paid", 100)
        except TypeError:
            return

    def dlt(self, index):
        """ Send the selected file to the recycle bin/delete database entry."""
        cur_path = self.treeView.fileModel.fileInfo(index).absoluteFilePath()
        send2trash.send2trash(os.path.abspath(cur_path))
        database.delete_entry(cur_path[36:-4])

    def move_to_archive(self, index):
        """Move selected file to archive"""
        try:
            source = self.treeView.fileModel.fileInfo(index).absoluteFilePath()
            destination = workenv.create_archive()
            shutil.move(os.path.abspath(source), os.path.abspath(destination))
        except shutil.Error:
            return

    def copy(self, index):
        """Copy the selected file within the same directory."""
        source = self.treeView.fileModel.fileInfo(index).absoluteFilePath()
        destination = self.listView.dirModel.fileInfo(index).absoluteFilePath()
        if not os.path.exists(destination):
            shutil.copy(os.path.abspath(source), os.path.abspath(destination))
        else:
            new_dest = destination[:-4] + " - Copy" + destination[-4:]
            shutil.copy(os.path.abspath(source), os.path.abspath(new_dest))

    def open_menu(self, position):
        """Setup a context menu, containing various options, to open upon right
        click."""
        index = self.treeView.indexAt(position)
        file_name = self.treeView.fileModel.fileName(index)
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
                database.update_status(file_name[:-4], "Dispatched")
                self.check_status(index)
            if action == menu.paid:
                database.update_status(file_name[:-4], "Paid")
                self.check_status(index)
            if action == menu.overdue:
                database.update_status(file_name[:-4], "Overdue")
                self.check_status(index)
        except PermissionError:
            return

    def refresh_visual_tab(self):
        index = self.tabwidget.currentIndex()
        if index == 1:
            self.tabwidget.visual_tab.update_piechart()

    def refresh_exchange_tab(self):
        index = self.tabwidget.currentIndex()
        if index == 2:
            self.tabwidget.exch_tab.update_cashflow_labels()

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
                    self.show_popup()
            else:
                active = False


workenv.create_workdir()
workenv.create_archive()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    qApp.setPalette(dark_palette)
    qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da;"
                       " border: 1px solid white; }")
    logic = Logic()
    logic.show()
    sys.exit(app.exec_())
