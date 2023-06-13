from weapons.weapon import Weapon
from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *

class HandCannon(Weapon):
    BASE_DIR = "../static/assets/weapons/hand_cannons/"

    def __init__(self, name):
        super().__init__(name, [No_Grip,], [No_Barrel,], [No_Under_Barrel,], 0)
        self.image_path = HandCannon.BASE_DIR + type(self).__name__ + ".png"

class Gonne_6(HandCannon):
    def __init__(self):
        super().__init__("Gonne-6")

if __name__ == "__main__":
    hgs = [cls() for cls in HandCannon.__subclasses__()]
    for hg in hgs:
        print(hg.image_path)
        print(hg.scopes)
        print(hg.grips)
        print(hg.barrels)
        print(hg.under_barrels)
