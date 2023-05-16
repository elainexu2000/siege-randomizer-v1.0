from weapons.Weapon import Weapon

class SubmachineGun(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = Weapon.BARRELS
    UNDER_BARRELS = Weapon.UNDER_BARRELS

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)

from weapons.SubmachineGun import SubmachineGun as SMG

class PDW9(SMG):
    def __init__(self, updated_mag = 2.5):
        super().__init__("PDW9", max_magnification = updated_mag)

class FMG_9(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("FMG-9", grips = ["None"], max_magnification = updated_mag)

class MP7(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("MP7", grips = ["None"], max_magnification = updated_mag)

class MP5K(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("MP5K", grips = ["None"], max_magnification = updated_mag)

class UMP45(SMG):
    def __init__(self):
        super().__init__("UMP45", max_magnification = 1.5)

class MP5(SMG):
    def __init__(self, updated_mag = 2.0):
        super().__init__("MP5", max_magnification = updated_mag)

class P90(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("P90", grips = ["None"], max_magnification = updated_mag)

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
        super().__init__("MP5SD", grips = ["None"], max_magnification = 1.5)

class VECTOR_45_ACP(SMG):
    def __init__(self, updated_mag = 1.5):
        super().__init__("Vector.45 ACP", max_magnification = updated_mag)

class T_5_SMG(SMG):
    def __init__(self):
        super().__init__("T-5 SMG")

class SCORPION_EVO_3_A1(SMG):
    def __init__(self):
        super().__init__("Sorpion EVO 3 A1", barrels = ["None", "Suppressor", "Compensator", "Flash Hider", "Muzzle Break"])

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
