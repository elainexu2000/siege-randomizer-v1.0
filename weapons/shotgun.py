from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class Shotgun(Weapon):
    GRIPS = [No_Grip,]
    BARRELS = [No_Barrel,]
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../static/assets/weapons/shotguns/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = Shotgun.BASE_DIR + type(self).__name__ + ".png"

class M590A1(Shotgun):
    def __init__(self):
        super().__init__("M590A1")

class M1014(Shotgun):
    def __init__(self):
        super().__init__("M1014")

class SG_CQB(Shotgun):
    def __init__(self):
        super().__init__("SG-CQB", grips = Shotgun.GRIPS + [Vertical_Grip,])

class SUPERNOVA(Shotgun):
    def __init__(self):
        super().__init__("SUPERNOVA", barrels = Shotgun.BARRELS + [Suppressor,])

class ITA12L(Shotgun):
    def __init__(self):
        super().__init__("ITA12L")

class ITA12S(Shotgun):
    def __init__(self):
        super().__init__("ITA12S")

class SIX12_SD(Shotgun):
    def __init__(self):
        super().__init__("SIX12 SD", barrels = [Suppressor,])

class BOSG_12_2(Shotgun):
    def __init__(self):
        super().__init__("BOSG.12.2", grips = Weapon.GRIPS, max_magnification = 2.5)

class SASG_12(Shotgun):
    def __init__(self):
        super().__init__("SASG-12", grips = Weapon.GRIPS, barrels = Shotgun.BARRELS + [Suppressor,])

class SUPER_SHORTY(Shotgun):
    def __init__(self):
        super().__init__("SUPER SHORTY")

class Bailiff_410(Shotgun):
    def __init__(self):
        super().__init__("Bailiff 410")

class M870(Shotgun):
    def __init__(self):
        super().__init__("M870")

class SUPER90(Shotgun):
    def __init__(self):
        super().__init__("SUPER 90")

class SPAS_12(Shotgun):
    def __init__(self):
        super().__init__("SPAS-12")

class SPAS_15(Shotgun):
    def __init__(self):
        super().__init__("SPAS-15")

class FO_12(Shotgun):
    def __init__(self):
        super().__init__("FO-12", grips = Weapon.GRIPS, barrels = Shotgun.BARRELS + [Suppressor, Extended_Barrel,])

class ACS12(Shotgun):
    def __init__(self, updated_mag = 2.0):
        super().__init__("ACS12", grips = Weapon.GRIPS, max_magnification = updated_mag)

class TCSG12(Shotgun):
    def __init__(self):
        super().__init__("TCSG12", grips = Weapon.GRIPS, barrels = Shotgun.BARRELS + [Suppressor,], max_magnification = 2.0)

if __name__ == "__main__":
    hgs = [cls() for cls in Shotgun.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)