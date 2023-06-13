from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class AssaultRifle(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = [No_Barrel, Suppressor, Compensator, Flash_Hider, Muzzle_Brake]
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../static/assets/weapons/assault_rifles/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = AssaultRifle.BASE_DIR + type(self).__name__ + ".png"

from weapons.assault_rifle import AssaultRifle as AR

class R4C(AR):
    def __init__(self):
        super().__init__("R4-C", barrels = AR.BARRELS + [Extended_Barrel,])

class G36C(AR):
    def __init__(self, updated_mag = 1.5):
        super().__init__("G36C", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = updated_mag)

class L85A2(AR):
    def __init__(self, updated_mag = 2.0):
        super().__init__("L85A2", max_magnification = updated_mag)

class AR33(AR):
    def __init__(self, updated_mag = 2.5):
        super().__init__("AR33", max_magnification = updated_mag)
        
class AR_556XI(AR):
    def __init__(self, updated_mag = 2.5):
        super().__init__("556XI", max_magnification = updated_mag)

class F2(AR):
    def __init__(self):
        super().__init__("F2", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 1.5)
        
class AK_12(AR):
    def __init__(self, updated_mag = 2.5):
        super().__init__("AK-12", max_magnification = updated_mag)

class AUG_A2(AR):
    def __init__(self, updated_mag = 2.5):
        super().__init__("AUG A2", grips = [No_Grip,], max_magnification = updated_mag)

class AR_552_Commando(AR):
    def __init__(self, updated_mag = 2.0):
        super().__init__("552 Commando", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = updated_mag)

class C8_SFW(AR):
    def __init__(self):
        super().__init__("C8-SFW", grips = [No_Grip,], barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 1.5)

class MK17_CQB(AR):
    def __init__(self):
        super().__init__("MK17 CQB", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification= 2.0)

class Para_308(AR):
    def __init__(self, updated_mag = 2.0):
        super().__init__("Para-308", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification= updated_mag)

class Type_89(AR):
    def __init__(self):
        super().__init__("Type-89", max_magnification = 2.5)

class C7E(AR):
    def __init__(self):
        super().__init__("C7E", max_magnification = 2.0)

class M762(AR):
    def __init__(self):
        super().__init__("M762", max_magnification = 2.0)

class V308(AR):
    def __init__(self):
        super().__init__("V308", max_magnification = 2.5)

class SPEAR_308(AR):
    def __init__(self, updated_mag = 2.0):
        super().__init__("SPEAR.308", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = updated_mag)

class M4(AR):
    def __init__(self):
        super().__init__("M4", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification= 2.0)

class AK_74M(AR):
    def __init__(self):
        super().__init__("AK-74M", grips = [No_Grip,], max_magnification = 2.5)

class ARX200(AR):
    def __init__(self, updated_mag = 2.0):
        super().__init__("ARX200", max_magnification = updated_mag)

class F90(AR):
    def __init__(self):
        super().__init__("F90", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 2.5)

class SC3000K(AR):
    def __init__(self):
        super().__init__("SC3000K", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification= 2.0)

class POF_9(AR):
    def __init__(self):
        super().__init__("POF-9", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 2.5)

class AR_416_C_CARBINE(AR):
    def __init__(self):
        super().__init__("416-C CARBINE", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 1.0)

class COMMANDO_9(AR):
    def __init__(self):
        super().__init__("Commando 9", barrels = AR.BARRELS + [Extended_Barrel,], max_magnification = 1.0)
    
if __name__ == "__main__":
    print(AssaultRifle.BARRELS)
    ars = [cls() for cls in AR.__subclasses__()]
    for ar in ars:
        print(ar.image_path)
        print(ar.scopes)
        print(ar.grips)
        print(ar.barrels)
        print(ar.under_barrels)