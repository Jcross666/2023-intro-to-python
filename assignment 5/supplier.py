#jacob cross
#1/13/24
#this code imports the part class, and then initiallizes the name adds the part to the list, and gets the price of the part
import part

class Supplier:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, name, price):
        added_part = part.Part(name, price)
        self.parts.append(added_part)
    def get_price(self, part):
        for supplied_parts in self.parts:
            if supplied_parts.name == part:
                return supplied_parts.cost
        return None
    def part_exists(self, part):
        for supplied_parts in self.parts:
            if supplied_parts.name == part:
                return True
        return False
