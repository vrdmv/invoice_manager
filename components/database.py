import pymongo.errors
from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox


def show_popup():
    """Show a pop-up message if invoice name already exists"""
    msg = QMessageBox()
    msg.setWindowTitle("No database connection")
    msg.setText("There is currently no connection established with the database")
    msg.setIcon(QMessageBox.Warning)
    x = msg.exec_()


try:
    cluster = MongoClient("mongodb+srv://dimovik:10307060@thecluster-noqgm.gcp.mongodb.net/test?retryWrites=true&w=majority")
    database = cluster["invoiceman"]
    collection = database["invoice_status"]
except pymongo.errors.ConfigurationError:
    print("No access to database!")


def set_initstatus(name):
    """Set the invoice's status"""
    try:
        post = {"invoice_name": f"{name}", "status": "Draft"}
        collection.insert_one(post)
    except NameError:
        show_popup()


def status_query(name):
    """Make a query to the database and check the for the status of a given
    invoice."""
    try:
        stats_query = collection.find_one({"invoice_name": f"{name}"})
        return stats_query["status"]
    except NameError:
        show_popup()


def update_status(name, status):
    """Update the invoice's status"""
    try:
        collection.update_one({"invoice_name": f"{name}"},
                              {"$set": {"status": f"{status}"}})
    except NameError:
        show_popup()


def delete_entry(name):
    """Delete the database entry."""
    try:
        collection.delete_one({"invoice_name": f"{name}"})
    except NameError:
        show_popup()


def get_dispatched():
    """Checks the status of all invoices."""
    dispatched = []
    try:
        results = collection.find({})
        for result in results:
            if result['status'] == "Dispatched":
                dispatched.append(result['status'])
        return len(dispatched)
    except NameError:
        show_popup()


def get_overdue():
    """Checks the status of all invoices."""
    overdue = []
    try:
        results = collection.find({})
        for result in results:
            if result['status'] == "Overdue":
                overdue.append(result['status'])
        return len(overdue)
    except NameError:
        show_popup()


def get_paid():
    """Checks the status of all invoices."""
    paid = []
    try:
        results = collection.find({})
        for result in results:
            if result['status'] == "Paid":
                paid.append(result["status"])
        return len(paid)
    except NameError:
        show_popup()
