class Barrel:
    """ Attributes:
        name: (string) name of the barrel
        image_path: relative path to image
    """
    BASE_DIR = "../../assets/barrels/"
    def __init__(self, name):
        self.name = name
        self.image_path = Barrel.BASE_DIR + type(self).__name__ + ".png"

class Suppressor(Barrel):
    def __init__(self):
        super().__init__("Suppressor")

class Compensator(Barrel):
    def __init__(self):
        super().__init__("Compensator")

class Flash_Hider(Barrel):
    def __init__(self):
        super().__init__("Flash Hider")

class Extended_Barrel(Barrel):
    def __init__(self):
        super().__init__("Extended Barrel")

class Muzzle_Break(Barrel):
    def __init__(self):
        super().__init__("Muzzle Break")

class No_Barrel(Barrel):
    def __init__(self):
        super().__init__("None")
        self.image_path = "../assets/None.png"


