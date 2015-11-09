from PODatabase import PODatabase
from PurchaseOrder import PurchaseOrder

db = PODatabase()

for customer in db.export_paths.iterkeys():
    db.read_export(customer)
#for po in db.purchase_orders.itervalues():
    #print po.po_number
    #po.total_cost = 0
    #po.total_qty = 0
    #for item in po.items.itervalues():
    #    po.total_cost += (item.cost * item.total_qty)
    #    po.total_qty += item.total_qty
    #print po.total_cost
    #db.purchase_orders.sync()
#db.console_print()
print db.purchase_orders['6119622'].total_cost
db.purchase_orders.close()
input = raw_input("")