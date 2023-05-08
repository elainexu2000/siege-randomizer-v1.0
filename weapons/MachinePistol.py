from weapons.Weapon import Weapon

class MachinePistol(Weapon):
    GRIPS = ["None"]
    BARRELS = Weapon.BARRELS
    UNDER_BARRELS = Weapon.UNDER_BARRELS

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, under_barrels = UNDER_BARRELS, max_magnification = 1.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)

class Bearing_9(MachinePistol):
    def __init__(self):
        super().__init__("Bearing 9")

class SMG_12(MachinePistol):
    def __init__(self):
        super().__init__("SMG-12", grips = Weapon.GRIPS)

class SMG_11(MachinePistol):
    def __init__(self):
        super().__init__("SMG-11", grips = Weapon.GRIPS)

class C75_Auto(MachinePistol):
    def __init__(self):
        super().__init__("C75 Auto", barrels = ["None", "Suppressor"])

class SPSMG9(MachinePistol):
    def __init__(self):
        super().__init__("SPSMG9")

if __name__ == "__main__":
    print(Bearing_9())