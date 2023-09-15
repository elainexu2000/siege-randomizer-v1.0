from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class MachinePistol(Weapon):
    GRIPS = [No_Grip,]
    BARRELS = Weapon.BARRELS
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../static/assets/weapons/machine_pistols/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = MachinePistol.BASE_DIR + type(self).__name__ + ".png"

class Bearing_9(MachinePistol):
    def __init__(self):
        super().__init__("Bearing 9")

class SMG_12(MachinePistol):
    def __init__(self):
        super().__init__("SMG-12", grips = Weapon.GRIPS, barrels = [Suppressor,])

class SMG_11(MachinePistol):
    def __init__(self):
        super().__init__("SMG-11", grips = Weapon.GRIPS)

class C75_Auto(MachinePistol):
    def __init__(self):
        super().__init__("C75 Auto", barrels = [No_Barrel, Suppressor,])

class SPSMG9(MachinePistol):
    def __init__(self):
        super().__init__("SPSMG9")

if __name__ == "__main__":
    hgs = [cls() for cls in MachinePistol.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)
