from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class SubmachineGun(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = Weapon.BARRELS
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../assets/weapons/submachine_guns/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = SubmachineGun.BASE_DIR + type(self).__name__ + ".png"

from weapons.submachine_gun import SubmachineGun as SMG

class PDW9(SMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("PDW9", max_magnification = updated_mag)

class FMG_9(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("FMG-9", grips = [No_Grip,], max_magnification = updated_mag)

class MP7(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("MP7", grips = [No_Grip,], max_magnification = updated_mag)

class MP5K(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("MP5K", grips = [No_Grip,], max_magnification = updated_mag)

class UMP45(SMG):
    def __init__(self):
        super().__init__("UMP45", max_magnification = 1.5)

class MP5(SMG):
    def __init__(self, updated_mag = 2.0):
        super().__init__("MP5", max_magnification = updated_mag)

class P90(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("P90", grips = [No_Grip,], max_magnification = updated_mag)

class SMG_9x19VSN(SMG):
    def __init__(self, updated_mag = 2.0):
        super().__init__("9x19VSN", max_magnification = updated_mag)

class SMG_9mm_C1(SMG):
    def __init__(self):
        super().__init__("9mm C1", max_magnification = 1.5)

class MPX(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("MPX", max_magnification = updated_mag)

class M12(SMG):
    def __init__(self):
        super().__init__("M12")

class MP5SD(SMG):
    def __init__(self):
        super().__init__("MP5SD", grips = [No_Grip,], max_magnification = 1.5)

class VECTOR_45_ACP(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("Vector.45 ACP", max_magnification = updated_mag)

class T_5_SMG(SMG):
    def __init__(self):
        super().__init__("T-5 SMG")

class SCORPION_EVO_3_A1(SMG):
    def __init__(self):
        super().__init__("Sorpion EVO 3 A1", barrels = [No_Barrel, Suppressor, Compensator, Flash_Hider, Muzzle_Break,])

class K1A(SMG):
    def __init__(self):
        super().__init__("K1A")

class Mx4_Storm(SMG):
    def __init__(self):
        super().__init__("Mx4 Storm")

class AUG_A3(SMG):
    def __init__(self):
        super().__init__("AUG A3")

class P10_RONI(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("P10 Roni", max_magnification = updated_mag)

class UZK50GI(SMG):
    def __init__(self):
        super().__init__("UZK50GI")

if __name__ == "__main__":
    hgs = [cls() for cls in SMG.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)
