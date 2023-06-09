from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class LightMachineGun(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = [No_Barrel, Compensator, Flash_Hider, Muzzle_Break,]
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../assets/weapons/light_machine_guns/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 2.5):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = LightMachineGun.BASE_DIR + type(self).__name__ + ".png"

from weapons.light_machine_gun import LightMachineGun as LMG

class LMG_6P41(LMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("6P41", barrels = LMG.BARRELS + [Suppressor,], max_magnification=updated_mag)

class G8A1(LMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("G8A1", barrels = LMG.BARRELS + [Suppressor,], max_magnification = updated_mag)

class M249(LMG):
    def __init__(self):
        super().__init__("M249")

class M249_SAW(LMG):
    def __init__(self):
        super().__init__("M249 SAW")

class T_95_LSW(LMG):
    def __init__(self):
        super().__init__("T-95 LSW", barrels = LMG.BARRELS + [Suppressor,])

class LMG_E(LMG):
    def __init__(self):
        super().__init__("LMG-E", barrels = LMG.BARRELS + [Suppressor,], max_magnification = 2.0)

class DP27(LMG):
    def __init__(self):
        super().__init__("DP27", grips = [No_Grip,], barrels = [No_Barrel,], under_barrels = [No_Under_Barrel,], max_magnification = 1.0)

class ALDA_5_56(LMG):
    def __init__(self):
        super().__init__("ALDA 5.56", grips = [No_Grip, Vertical_Grip,], max_magnification = 1.0)

if __name__ == "__main__":
    hgs = [cls() for cls in LMG.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)