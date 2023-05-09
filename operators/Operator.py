from random import choice

class Operator:
    """ Attributes:
        name: operator name
        side: "Attack" or "Defend"
        gadgets: set of all available gadgets
        primaries: set of all available primary weapons
        secondaries: set of all available secondary weapons
    """
    def __init__(self, name, side):
        """
        Precondition: side in ["Attack", "Defend"]
        """
        self.name = name
        self.side = side
        self.gadgets = []
        self.primaries = []
        self.secondaries = []
    
    def __str__(self):
        return self.name
    
    def add_gadget(self, gadget):
        """
        Precondition: gadget is a valid Gadget object
        """
        if self.side != gadget.side:
                print("Side mismatch: ", str(gadget), "is not", self.side, "specific")
                # raise ValueError <-- how to handle this?
        self.gadgets.append(gadget)

    def add_weapon(self, weapon, is_primary = True):
        """
        Precondition: weapon is a valid Weapon object, is_primary = True if this weapon is a primary weapon
        """
        if is_primary:
            self.primaries.append(weapon)
        else:
            self.secondaries.append(weapon)
    
    def get_random_loadout(self):
        """
        Returns a random loadout in the form of a dictionary with keys = element type and values = element identity
        """
        loadout = {}
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
        loadout["Gadget"] = str(choice(self.gadgets))
        return loadout


        

