from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class Shield(Weapon):
    BASE_DIR = "../static/assets/weapons/shields/"
    def __init__(self, name, grips = [No_Grip,], barrels = [No_Barrel,], under_barrels = [No_Under_Barrel,], max_magnification = 0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
        self.image_path = Shield.BASE_DIR + type(self).__name__ + ".png"

class LE_ROC_Shield(Shield):
    def __init__(self):
        super().__init__("LE ROC Shield")

class Ballistic_Shield(Shield):
    def __init__(self):
        super().__init__("Ballistic Shield")

class G52_Tactical_Shield(Shield):
    def __init__(self):
        super().__init__("G52 Tactical Shield")

class CCE_Shield(Shield):
    def __init__(self):
        super().__init__("CCE Shield")

if __name__ == "__main__":
    hgs = [cls() for cls in Shield.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)