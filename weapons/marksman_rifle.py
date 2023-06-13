from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class MarksmanRifle(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = [No_Barrel, Suppressor, Muzzle_Brake,]
    UNDER_BARRELS = Weapon.UNDER_BARRELS
    BASE_DIR = "../static/assets/weapons/marksman_rifles/"

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, 
                 under_barrels = UNDER_BARRELS, max_magnification = 3.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = MarksmanRifle.BASE_DIR + type(self).__name__ + ".png"

from weapons.marksman_rifle import MarksmanRifle as DMR

class M417(DMR):
    def __init__(self):
        super().__init__("417")

class OTs_03(DMR):
    def __init__(self):
        super().__init__("OTs-03", max_magnification = 1)
        self.scopes = [x for x in self.scopes if x != Reflex_C]

class CAMRS(DMR):
    def __init__(self):
        super().__init__("CAMRS", grips = [No_Grip,])

class SR_25(DMR):
    def __init__(self):
        super().__init__("SR-25")

class Mk_14_EBR(DMR):
    def __init__(self, updated_mag = 3.0):
        super().__init__("Mk 14 EBR", max_magnification = updated_mag)

class AR_15_50(DMR):
    def __init__(self):
        super().__init__("AR-15.50")

class CSRX300(DMR):
    def __init__(self):
        super().__init__("CSRX 300", grips = [No_Grip,], barrels = [No_Barrel,], under_barrels = [No_Under_Barrel,], max_magnification = 0)

if __name__ == "__main__":
    ars = [cls() for cls in DMR.__subclasses__()]
    for ar in ars:
        print(ar)
        print(ar.image_path)
        print(ar.scopes)
        print(ar.grips)
        print(ar.barrels)
        print(ar.under_barrels)