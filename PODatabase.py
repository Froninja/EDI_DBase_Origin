from PurchaseOrder import PurchaseOrder
import shelve

class PODatabase(object):
    """Stores a set of PurchaseOrder objects and represents them to the user"""
    def __init__(self):
        self.purchase_orders = shelve.open('PO_Data')
        self.export_paths = dict()
        with open("Config.txt") as config:
            for line in config:
                line = line.split(': ')
                self.export_paths[line[0]] = line[1].rstrip('\n').rstrip('\r')

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
        if len(self.purchase_orders) > 0:
            with open(db_file, 'w') as db:
                write_string = ""
                for PO in self.purchase_orders.itervalues():
                    write_string += "{},{},{},{},{},{},{},{},{}\n".format(
                        PO.po_number, PO.customer, PO.creation_date, PO.start_ship,
                        PO.cancel_ship, PO.total_cost, PO.discount, PO.label,
                        PO.complete)
                db.write(write_string)

    def read_db(self, db_file):
        """Reads POs from supplied CSV file and adds to the database object"""
        with open(db_file, 'r') as db:
            for line in db:
                if len(line) > 1:
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

    def read_export(self, customer):
        """Reads the TLW export based on customer name. If the PO number is not
        already in the program data, adds it"""
        export_file = self.get_export_file(customer)
        with open(export_file, 'r') as export:
            for line in export:
                line = line.rstrip('\n').rstrip('\r').split(',')
                if line[1] != 'PO #':
                    if line[1].lstrip('0') not in self.purchase_orders:
                        PO = PurchaseOrder(line[1].lstrip('0'), customer)
                        PO.cancel_ship = line[4]
                        #PO.total_cost = self.get_cost_from_exp(PO.po_number,
                        #                                       export_file)
                        PO.get_items_from_export(export_file)
                        PO.get_stores_from_export(export_file)
                        for item in PO.items.itervalues():
                            PO.total_cost += (item.cost * item.total_qty)
                        self.purchase_orders[PO.po_number] = PO
                    else:
                        PO = self.purchase_orders[line[1].lstrip('0')]
                        PO.cancel_ship = line[4]
                        #PO.total_cost = self.get_cost_from_exp(PO.po_number,
                                                               #export_file)
                        PO.get_items_from_export(export_file)
                        PO.get_stores_from_export(export_file)
                        PO.total_cost = 0
                        for item in PO.items.itervalues():
                            PO.total_cost += (item.cost * item.total_qty)
                        self.purchase_orders.sync()

    def get_cost_from_exp(self, po_num, export_file):
        """Searches the TLW export for all lines matching the supplied PO
        number and returns total cost based on the sum of each line's cost"""
        total_cost = 0
        with open(export_file, 'r') as export:
            for line in export:
                #if len(line) > 1:
                line = line.rstrip('\n').rstrip('\r').split(',')
                if line[1] == po_num:
                    total_cost += float(line[7]) * int(line[9])
        return total_cost

    def check_export_against_db(self, PO_num):
        """For a given PO Number in the export file, checks against the data
        file loaded at program start. If the PO already exists, returns false
        """
        if PO_num != "PO #":
            if PO_num in self.purchase_orders:
                return True
            else:
                return False
        else:
            return True

    def get_export_file(self, customer):
        return self.export_paths[customer]