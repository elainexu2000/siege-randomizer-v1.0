from weapons.weapon import Weapon

class HandCannon(Weapon):
    def __init__(self, name):
        super().__init__(name, ["None"], ["None"], ["None"], 0)

class Gonne_6(HandCannon):
    def __init__(self):
        super().__init__("Gonne-6")