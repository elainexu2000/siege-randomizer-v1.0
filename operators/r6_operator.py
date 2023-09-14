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
    #BASE_DIR = "../../assets/operators/icons/"
    BASE_DIR = "../static/assets/operator_icons/"
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.gadgets = []
        self.primaries = []
        self.secondaries = []
        self.image_path = Operator.BASE_DIR + type(self).__name__.lower() + '.png'
    
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
        """Creates a new entry in the loadout dictionary: key = entity_name, 
            value = {"Name":obj.name, "Image": obj.image_path}
        Precondition: loadout is a dictionary, obj is a non-null Object with attributes 'name' and 'image_path' 
            (Operator, Gadget, Weapon, Scope, Barrel, Under_Barrel), entity_name is a string which serves as a key in loadout
        Example: create_subdictionary(loadout = {}, Ash(), "Operator")
            loadout = {
                "Operator": {
                    "Name": "Ash",
                    "Image": "../asset/operators/Ash.png"
                    }
                }
        """
        loadout[entity_name] = {}
        loadout[entity_name]["Name"] = obj.name
        loadout[entity_name]["Image"] = obj.image_path

    def add_randomized_weapon(loadout, weapon, is_primary):
        """Adds a weapon to loadout
        Precondition: loadout is a dictionary; weapon is a non-null Weapon object; is_primary is true if weapon is a primary weapon
        """
        name = "Primary" if is_primary else "Secondary"
        Operator.create_subdictionary(loadout, weapon, name)
        scope_class = choice(weapon.scopes)
        Operator.create_subdictionary(loadout[name], scope_class(), "Scope")
        barrel_class = choice(weapon.barrels)
        Operator.create_subdictionary(loadout[name], barrel_class(), "Barrel")
        under_barrel_class = choice(weapon.under_barrels)
        Operator.create_subdictionary(loadout[name], under_barrel_class(), "Under Barrel")

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