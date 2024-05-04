class Grip:
    """ Attributes:
        name: (string) name of the grip
        image_path: relative path to image
    """
    BASE_DIR = "../static/assets/grips/"
    def __init__(self, name):
        self.name = name
        self.image_path = Grip.BASE_DIR + type(self).__name__ + ".png"
    
class Vertical_Grip(Grip):
    def __init__(self):
        super().__init__("Vertical Grip")

class Angled_Grip(Grip):
    def __init__(self):
        super().__init__("Angled Grip")

class No_Grip(Grip):
    def __init__(self):
        super().__init__("None")
        self.image_path = "../static/assets/None.png"

# add horizontal grip
        
if __name__ == "__main__":
    grips = [cls() for cls in Grip.__subclasses__()]
    for g in grips:
        print(g.image_path)
