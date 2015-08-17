from PODatabase import PODatabase
from PurchaseOrder import PurchaseOrder

print('Hello world')

db = PODatabase()

db.read_db("C:\Users\Jacob\Documents\PO_DB.csv")

db.console_print()