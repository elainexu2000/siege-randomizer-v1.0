from weapons.Weapon import Weapon

class Shield(Weapon):
    def __init__(self, name, grips = ["None"], barrels = ["None"], under_barrels = ["None"], max_magnification = 0):
        super().__init__(name, grips, barrels, under_barrels, max_magnification)
    
class LE_ROC_Shield(Shield):
    def __init__(self):
        super().__init__("LE_ROC_Shield")

class Ballistic_Shield(Shield):
    def __init__(self):
        super().__init__("Ballistic Shield")

class G52_Tactical_Shield(Shield):
    def __init__(self):
        super().__init__("G52-Tactical-Shield")

class CCE_Shield(Shield):
    def __init__(self):
        super().__init__("CCE Shield")