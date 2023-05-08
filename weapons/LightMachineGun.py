from weapons.Weapon import Weapon

class LightMachineGun(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = ["None", "Compensator", "Flash Hider", "Muzzle Break"]
    UNDER_BARRELS = Weapon.UNDER_BARRELS

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 2.5):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)

from weapons.LightMachineGun import LightMachineGun as LMG

class LMG_6P41(LMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("6P41", barrels = LMG.BARRELS + ["Suppressor"], max_magnification=updated_mag)

class G8A1(LMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("G8A1", barrels = LMG.BARRELS + ["Suppressor"], max_magnification = updated_mag)

class M249(LMG):
    def __init__(self):
        super().__init__("M249")

class M249_SAW(LMG):
    def __init__(self):
        super().__init__("M249 SAW")

class T_95_LSW(LMG):
    def __init__(self):
        super().__init__("T-95 LSW", barrels = LMG.BARRELS + ["Suppressor"])

class LMG_E(LMG):
    def __init__(self):
        super().__init__("LMG-E", barrels = LMG.BARRELS + ["Suppressor"], max_magnification = 2.0)

class DP27(LMG):
    def __init__(self):
        super().__init__("DP27", grips = ["None"], barrels = ["None"], under_barrels = ["None"], max_magnification = 1.0)

class ALDA_5_56(LMG):
    def __init__(self):
        super().__init__("ALDA 5.56", grips = ["None", "Vertical Grip"], max_magnification = 1.0)

if __name__ == "__main__":
    l1 = T_95_LSW()
    print(l1)
    g8 = G8A1(updated_mag=1.0)
    print(g8.scopes)