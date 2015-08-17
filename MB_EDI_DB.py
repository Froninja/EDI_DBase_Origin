from PODatabase import PODatabase
from PurchaseOrder import PurchaseOrder

print('Hello world')

purchase_orders = []

for num in range(10):
    purchase_orders.append(PurchaseOrder(num, "Saks"))

db = PODatabase(purchase_orders)

db.console_print()