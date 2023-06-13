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
        self.image_path = Operator.BASE_DIR + type(self).__name__ + '.png'
    
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

    def create_subdictionary(loadout, obj, entity_name):
        loadout[entity_name] = {}
        loadout[entity_name]["Name"] = obj.name
        loadout[entity_name]["Image"] = obj.image_path

    def add_randomized_weapon(loadout, weapon, is_primary):
        name = "Primary" if is_primary else "Secondary"
        Operator.create_subdictionary(loadout, weapon, name)
        scope_class = choice(weapon.scopes)
        scope = scope_class()
        Operator.create_subdictionary(loadout[name], scope, "Scope")
        barrel_class = choice(weapon.barrels)
        barrel = barrel_class()
        Operator.create_subdictionary(loadout[name], barrel, "Barrel")
        under_barrel_class = choice(weapon.under_barrels)
        under_barrel = under_barrel_class()
        Operator.create_subdictionary(loadout[name], under_barrel, "Under Barrel")

    def get_random_loadout(self):
        """
        Returns a random loadout in the form of a nested dictionary
        """
        loadout = {}
        Operator.create_subdictionary(loadout, self, "Operator")
        gadget = choice(self.gadgets)
        Operator.create_subdictionary(loadout, gadget, "Gadget")

        primary = choice(self.primaries)
        Operator.add_randomized_weapon(loadout, primary, is_primary=True)
        secondary = choice(self.secondaries)
        Operator.add_randomized_weapon(loadout, secondary, is_primary=False)
        return loadout

if __name__ == '__main__':
    r = Operator("Recruit", "Attack")
    
    loadout = {}
    Operator.create_subdictionary(loadout, r, "Primary")
    Operator.create_subdictionary(loadout["Primary"], r, "Scope")
    print(loadout)
