class Grip:
    """ Attributes:
        name: (string) name of the grip
        image_path: relative path to image
    """
    BASE_DIR = "../assets/grips/"
    def __init__(self, name):
        self.name = name
        self.image_path = Grip.BASE_DIR + type(self).__name__ + ".png"