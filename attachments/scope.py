class Scope:
    """ Attributes:
        name: (string) name of the scope
        image_path: relative path to image
        magnification: in [0, 1, 1.5, 2, 2.5, 3]
    """
    BASE_DIR = "../../assets/sights/"
    def __init__(self, name):
        self.name = name
        self.image_path = Scope.BASE_DIR + type(self).__name__ + ".png"
        self.magnification = 0
    
    def __str__(self):
        return self.name
    
class Holo_A(Scope):
    def __init__(self):
        super().__init__("Holographic A")
        self.magnification = 1

class Holo_B(Scope):
    def __init__(self):
        super().__init__("Holographic B")
        self.magnification = 1

class Holo_C(Scope):
    def __init__(self):
        super().__init__("Holographic C")
        self.magnification = 1

class Holo_D(Scope):
    def __init__(self):
        super().__init__("Holographic D")
        self.magnification = 1

class Red_Dot_A(Scope):
    def __init__(self):
        super().__init__("Red Dot A")
        self.magnification = 1

class Red_Dot_B(Scope):
    def __init__(self):
        super().__init__("Red Dot B")
        self.magnification = 1

class Red_Dot_C(Scope):
    def __init__(self):
        super().__init__("Red Dot C")
        self.magnification = 1

class Reflex_A(Scope):
    def __init__(self):
        super().__init__("Reflex A")
        self.magnification = 1

class Reflex_B(Scope):
    def __init__(self):
        super().__init__("Reflex B")
        self.magnification = 1

class Reflex_C(Scope):
    def __init__(self):
        super().__init__("Reflex C")
        self.magnification = 1

class Scope_15x(Scope):
    def __init__(self):
        super().__init__("1.5x")
        self.magnification = 1.5

class Scope_20x(Scope):
    def __init__(self):
        super().__init__("2.0x")
        self.magnification = 2

class Scope_25x_A(Scope):
    def __init__(self):
        super().__init__("2.5x A")
        self.magnification = 2.5

class Scope_25x_B(Scope):
    def __init__(self):
        super().__init__("2.5x B")
        self.magnification = 2.5

class Scope_30x(Scope):
    def __init__(self):
        super().__init__("3.0x")
        self.magnification = 3

class No_Scope(Scope):
    def __init__(self):
        super().__init__("None")
        self.image_path = "../assets/None.png"
        self.magnification = 0

if __name__ == "__main__":
    scopes = [cls() for cls in Scope.__subclasses__()]
    for s in scopes:
        print(s.image_path)
        print(s.magnification)