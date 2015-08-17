from PurchaseOrder import PurchaseOrder

class PODatabase(object):
    """Stores a set of PurchaseOrder objects and represents them to the user"""
    def __init__(self):
        self.purchase_orders = dict()
        #for purchase_order in purchase_orders:
            #self.purchase_orders[purchase_order.po_number] = purchase_order

    def console_print(self):
        """Prints the information on all POs in the database to the console"""
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

    def write_db(self, db_file):
        """Writes all PO information to the supplied file"""
        with open(db_file, 'w') as db:
            write_string = ""
            for PO in self.purchase_orders.itervalues():
                write_string += "{},{},{},{},{},{},{},{},{}".format(
                    PO.po_number, PO.customer, PO.creation_date, PO.start_ship,
                    PO.cancel_ship, PO.total_cost, PO.discount, PO.label,
                    PO.complete)
            db.write(write_string)

    def read_db(self, db_file):
        """Reads POs from supplied CSV file and adds to the database object"""
        with open(db_file, 'r') as db:
            for line in db:
                line = line.replace('\n','').replace('\r','').split(',')
                PO = PurchaseOrder(line[0], line[1])
                PO.creation_date = line[2]
                PO.start_ship = line[3]
                PO.cancel_ship = line[4]
                PO.total_cost = line[5]
                PO.discount = line[6]
                PO.label = line[7]
                PO.complete = line[8]
                self.purchase_orders[PO.po_number] = PO