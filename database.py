from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://dimovik:10307060@thecluster-noqgm.gcp.mongodb.net/test?retryWrites=true&w=majority")
database = cluster["invoiceman"]
collection = database["invoice_status"]


def set_initstatus(name):
    """Set the invoice's status"""
    post = {"invoice_name": f"{name}", "status": "Draft"}
    collection.insert_one(post)

def status_query(name):
    """Make a query to the database and check the for the status of a given
    invoice."""
    status_query = collection.find_one({"invoice_name": f"{name}"})
    return status_query["status"]

def update2dispatched(name):
    """Update the invoice's status"""
    collection.update_one({"invoice_name": f"{name}"},
                          {"$set": {"status": "Dispatched"}})

def update2paid(name):
    """Update the invoice's status"""
    collection.update_one({"invoice_name": f"{name}"},
                          {"$set": {"status": "Paid"}})

def update2overdue(name):
    """Update the invoice's status"""
    collection.update_one({"invoice_name": f"{name}"},
                          {"$set": {"status": "Overdue"}})

def delete_entry(name):
    """Delete the database entry."""
    collection.delete_one({"invoice_name": f"{name}"})

def get_dispatched():
    """Checks the status of all invoices."""
    dispatched = []
    results = collection.find({})
    for result in results:
        if result['status'] == "Dispatched":
            dispatched.append(result['status'])
    return(len(dispatched))

def get_overdue():
    """Checks the status of all invoices."""
    paid = []
    results = collection.find({})
    for result in results:
        if result['status'] == "Overdue":
            paid.append(result['status'])
    return(len(paid))

def get_paid():
    """Checks the status of all invoices."""
    overdue = []
    results = collection.find({})
    for result in results:
        if result['status'] == "Paid":
            overdue.append(result["status"])
    return(len(overdue))