#jacob cross
#1/13/24
#this code first initiallizes a list and once given adds the name of the supplier to the list, then finds the supplier that has the lowest price of a part that was inputted
class Database:
    def __init__(self):
        self.suppliers = []
    
    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
    
    def find_part(self, part):
        least_cost = float('inf')
        least_cost_supplier = None
        for supplier in self.suppliers:
            price = supplier.get_price(part)
            if price and price < least_cost:
                least_cost = price
                least_cost_supplier = supplier
        if least_cost_supplier:
            return least_cost_supplier.name, least_cost
        else:
            return False, False