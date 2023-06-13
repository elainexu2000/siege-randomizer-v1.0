from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class Handgun(Weapon):
    GRIPS = [No_Grip,]
    BARRELS = [No_Barrel, Suppressor, Muzzle_Brake,]
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../static/assets/weapons/handguns/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = Handgun.BASE_DIR + type(self).__name__ + ".png"

class M45_MEUSOC(Handgun):
    def __init__(self):
        super().__init__("M45 MEUSOC")

class USG57(Handgun):
    def __init__(self):
        super().__init__("5.7 USG")

class P226MK25(Handgun):
    def __init__(self):
        super().__init__("P226 MK 25")

class P9(Handgun):
    def __init__(self):
        super().__init__("P9")

class LFP586(Handgun):
    def __init__(self):
        super().__init__("LFP586", barrels = [No_Barrel,])

class PMM(Handgun):
    def __init__(self):
        super().__init__("PMM")

class GSH_18(Handgun):
    def __init__(self):
        super().__init__("GSH-18")

class P12(Handgun):
    def __init__(self):
        super().__init__("P12")

class MK1_9mm(Handgun):
    def __init__(self):
        super().__init__("MK1 9mm")

class D_50(Handgun):
    def __init__(self):
        super().__init__("D-50")

class PRB92(Handgun):
    def __init__(self):
        super().__init__("PRB92")

class LUISON(Handgun):
    def __init__(self):
        super().__init__("LUISON", barrels = [Suppressor,])
        
class P229(Handgun):
    def __init__(self):
        super().__init__("P229")

class USP40(Handgun):
    def __init__(self):
        super().__init__("USP40")

class Q_929(Handgun):
    def __init__(self):
        super().__init__("Q-929")

class RG15(Handgun):
    def __init__(self):
        super().__init__("RG15")

class H_1911_TACOPS(Handgun):
    def __init__(self):
        super().__init__("1911 TACOPS")

class H_44_Mag_Semi_Auto(Handgun):
    def __init__(self):
        super().__init__(".44 Mag Semi-Auto", barrels = [No_Barrel,])

class SDP_9mm(Handgun):
    def __init__(self):
        super().__init__("SDP 9mm")

class KERATOS_357(Handgun):
    def __init__(self):
        super().__init__("KERATOS.357")

class P_10C(Handgun):
    def __init__(self):
        super().__init__("P-10C")

if __name__ == "__main__":
    hgs = [cls() for cls in Handgun.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)
