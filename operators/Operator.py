from random import choice

class Operator:
    """ Attributes:
        name: operator name
        side: in ["Attack", "Defend"]
        gadgets: set of two available gadgets
        primary: set of all available primary weapons
        secondary: set of all available secondary weapons
    """
    def __init__(self, name, side):
        """
        Precondition: side in ["Attack", "Defend"]
        """
        self.name = name
        self.side = side
        self.gadgets = []
        self.primary = []
        self.secondary = []
    
    def __str__(self):
        return self.name
    
    def add_gadget(self, gadget):
        self.gadgets.append(gadget)

    def add_weapon(self, weapon, is_primary = True):
        """
        Precondition: weapon is a valid Weapon object, is_primary = True if this weapon is a primary weapon
        """
        if is_primary:
            self.primary.append(weapon)
        else:
            self.secondary.append(weapon)
    
    def get_random_loadout(self):
        loadout = {}
        primary = choice(self.primary)
        loadout["Primary"] = str(primary)
        loadout["Primary Grip"] = choice(primary.grips)
        loadout["Primary Barrel"] = choice(primary.barrels)
        loadout["Primary Scope"] = choice(primary.scopes)
        loadout["Primary Under Barrel"] = choice(primary.under_barrels)
        
        secondary = choice(self.secondary)
        loadout["Secondary"] = str(secondary)
        loadout["Secondary Grip"] = choice(secondary.grips)
        loadout["Secondary Barrel"] = choice(secondary.barrels)
        loadout["Secondary Scope"] = choice(secondary.scopes)
        loadout["Secondary Under Barrel"] = choice(secondary.under_barrels)
        loadout["Gadget"] = str(choice(self.gadgets))
        return loadout
    
    def get_random_primary(self):
        primary = choice(self.primary)
        primary_grip = choice(primary.grips)
        primary_barrel = choice(primary.barrels)
        primary_scope = choice(primary.scopes)
        primary_under_barrel = choice(primary.under_barrels)
        return primary, primary_grip, primary_barrel, primary_scope, primary_under_barrel

        

