from PurchaseOrder import PurchaseOrder

class PODatabase(object):
    """description of class"""
    def __init__(self, purchase_orders):
        self.purchase_orders = dict()
        for purchase_order in purchase_orders:
            self.purchase_orders[purchase_order.po_number] = purchase_order

    def console_print(self):
        #print """{0:15d} {1:9d} {2:13d} {3:10d} {4:11d} {5:10d} {6:8d} {7:15d}
            #{8:5d}""".format("Customer", "PO Number", "Creation Date",
            #"Start Ship", "Cancel Date", "Total Cost", "Discount", "Label",
            #"Status")
        print repr("Customer").rjust(15), repr("PO Number").rjust(9),
        print repr("Creation Date").rjust(13), repr("Start Ship").rjust(10),
        print repr("Cancel Date").rjust(11), repr("Total Cost").rjust(10),
        print repr("Discount").rjust(8), repr("Label").rjust(15),
        print repr("Status").rjust(5)
        for PO in self.purchase_orders.itervalues():
            print repr(PO.customer).rjust(15), repr(PO.po_number).rjust(9),
            print repr(PO.creation_date).rjust(13),
            print repr(PO.start_ship).rjust(10), repr(PO.cancel_ship).rjust(11),
            print repr(PO.total_cost).rjust(10), repr(PO.discount).rjust(8),
            print repr(PO.label).rjust(15), repr(PO.complete).rjust(5)