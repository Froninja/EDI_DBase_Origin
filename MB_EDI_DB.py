from PODatabase import PODatabase
from PurchaseOrder import PurchaseOrder

db = PODatabase()

db.read_db("C:\Users\Jacob\Documents\PO_DB.csv")
for customer in db.export_paths.iterkeys():
    db.read_export(customer)
db.console_print()
db.write_db("C:\Users\Jacob\Documents\PO_DB.csv")
input = raw_input("")