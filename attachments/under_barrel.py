class Under_Barrel:
    """ Attributes:
        name: (string) name of the under barrel
        image_path: relative path to image
    """
    BASE_DIR = "../static/assets/under_barrels/"
    def __init__(self, name) :
        self.name = name
        self.image_path = Under_Barrel.BASE_DIR + type(self).__name__ + ".png"
    
class Laser(Under_Barrel):
    def __init__(self):
        super().__init__("Laser")

class No_Under_Barrel(Under_Barrel):
    def __init__(self):
        super().__init__("None")
        self.image_path = "../static/assets/None.png"
