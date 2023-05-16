from weapons.Weapon import Weapon

class MarksmanRifle(Weapon):
    GRIPS = Weapon.GRIPS
    BARRELS = ["None", "Suppressor", "Muzzle Break"]
    UNDER_BARRELS = Weapon.UNDER_BARRELS

    def __init__(self, name, grips = GRIPS, barrels = BARRELS, 
                 under_barrels = UNDER_BARRELS, max_magnification = 3.0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)

from weapons.MarksmanRifle import MarksmanRifle as DMR

class M417(DMR):
    def __init__(self):
        super().__init__("417")

class OTs_03(DMR):
    def __init__(self):
        super().__init__("OTs-03", max_magnification = 1)
        if 'Reflex C' in self.scopes:
            self.scopes.remove('Reflex C')

class CAMRS(DMR):
    def __init__(self):
        super().__init__("CAMRS", grips = ["None"])

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
        super().__init__("CSRX 300", grips=["None"], barrels=["None"], under_barrels=["None"], max_magnification=0)

if __name__ == "__main__":
    dmr1 = M417()
    print(dmr1)

    dmr2 = CAMRS()
    print(dmr2.grips)