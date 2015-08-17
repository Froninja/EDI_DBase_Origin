class PurchaseOrder(object):
    """Holds all the relevant information for one purchase order.
        Information includes:
        - Purchase Order Number
        - Customer (who submitted the purchase order)
        - Creation Date (determined on customer end)
        - Start Ship Date
        - Cancel Date
        - Total Cost (sum of unit cost * qty for each item in the order)
        - Discount Requested (as a %)
        - Label (created on receiver end)
        - Completion Status (whether it has shipped or not)
        - Items"""
    def __init__(self, po_number, customer):
        self.po_number = po_number
        self.customer = customer
        self.creation_date = ''
        self.start_ship = ''
        self.cancel_ship = ''
        self.total_cost = 0
        self.discount = 0
        self.label = ''
        self.complete = False
        self.items = dict()