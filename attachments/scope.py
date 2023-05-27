class Scope:
    """ Attributes:
        name: (string) name of the scope
        image_path: relative path to image
    """
    BASE_DIR = "../assets/sights/"
    def __init__(self, name):
        self.name = name
        self.image_path = Scope.BASE_DIR + type(self).__name__ + ".png"
    
class Holo_A(Scope):
    def __init__(self):
        super().__init__("Holographic A")

class Holo_B(Scope):
    def __init__(self):
        super().__init__("Holographic B")

class Holo_C(Scope):
    def __init__(self):
        super().__init__("Holographic C")

class Holo_D(Scope):
    def __init__(self):
        super().__init__("Holographic D")

class Red_Dot_A(Scope):
    def __init__(self):
        super().__init__("Red Dot A")

class Red_Dot_B(Scope):
    def __init__(self):
        super().__init__("Red Dot B")

class Red_Dot_C(Scope):
    def __init__(self):
        super().__init__("Red Dot C")

class Reflex_A(Scope):
    def __init__(self):
        super().__init__("Reflex A")

class Reflex_B(Scope):
    def __init__(self):
        super().__init__("Reflex B")

class Reflex_C(Scope):
    def __init__(self):
        super().__init__("Reflex C")

class Scope_15x(Scope):
    def __init__(self):
        super().__init__("1.5x")

class Scope_20x(Scope):
    def __init__(self):
        super().__init__("2.0x")

class Scope_25x(Scope):
    def __init__(self):
        super().__init__("2.5x")

class Scope_30x(Scope):
    def __init__(self):
        super().__init__("3.0x")

if __name__ == "__main__":
    scopes = [cls() for cls in Scope.__subclasses__()]
    for s in scopes:
        print(s.image_path)