from random import choice

class Operator:
    """ Attributes:
        name: operator name
        side: "Attack" or "Defend"
        gadgets: set of all available gadgets
        primaries: set of all available primary weapons
        secondaries: set of all available secondary weapons
        image_path: path to operator icon
    """
    BASE_DIR = "../assets/operators/icons/"

    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.gadgets = []
        self.primaries = []
        self.secondaries = []
        self.image_path = Operator.BASE_DIR
    
    def __str__(self):
        return self.name
    
    def add_gadget(self, gadget):
        if self.side != gadget.side:
            print("Side mismatch: ", str(gadget), "is not", self.side, "specific")
        else:
            self.gadgets.append(gadget)

    def add_weapon(self, weapon, is_primary = True):
        """
        Precondition: weapon is a valid Weapon object, is_primary = True if this weapon is a primary weapon
        """
        if is_primary:
            self.primaries.append(weapon)
        else:
            self.secondaries.append(weapon)
    
    def add_path_to_icon(self):
        self.image_path += self.name + '.png'

    ###TODO: change this implementation
    def get_random_loadout(self):
        """
        Returns a random loadout in the form of a dictionary with key = element type and value = element identity
        """

        """
        loadout = {}
        loadout["Primary Weapon"] = {}
        loadout["Secondary Weapon"] = {}
        return loadout
        """
        loadout = {}
        loadout["Operator Name"] = self.name
        primary = choice(self.primaries)
        loadout["Primary"] = str(primary)
        loadout["Primary Grip"] = choice(primary.grips)
        loadout["Primary Barrel"] = choice(primary.barrels)
        loadout["Primary Scope"] = choice(primary.scopes)
        loadout["Primary Under Barrel"] = choice(primary.under_barrels)
        secondary = choice(self.secondaries)
        loadout["Secondary"] = str(secondary)
        loadout["Secondary Grip"] = choice(secondary.grips)
        loadout["Secondary Barrel"] = choice(secondary.barrels)
        loadout["Secondary Scope"] = choice(secondary.scopes)
        loadout["Secondary Under Barrel"] = choice(secondary.under_barrels)
        loadout["Gadget Name"] = str(choice(self.gadgets))
        return loadout
        
if __name__ == '__main__':
    o1 = Operator('Ash', 'Attack')
    o1.add_path_to_icon()
    print(o1.image_path)

        

