class Gadget:
    """ Attributes:
        name: (string) name of the gadget
        side: in ["Attack", "Defend"]
    """
    def __init__(self, name, is_attacker_specific):
        self.name = name
        self.side = "Attack" if is_attacker_specific else "Defend"
    
    def __str__(self):
        return self.name

class Frag_Grenade(Gadget):
    def __init__(self):
        super().__init__("Frag Grenade", True)

class Stun_Grenade(Gadget):
    def __init__(self):
        super().__init__("Stun Grenade", True)

class Breach_Charge(Gadget):
    def __init__(self):
        super().__init__("Breach Charge", True)

class Claymore(Gadget):
    def __init__(self):
        super().__init__("Claymore", True)

class Smoke_Grenade(Gadget):
    def __init__(self):
        super().__init__("Smoke Grenade", True)

class Hard_Breach_Charge(Gadget):
    def __init__(self):
        super().__init__("Hard Breach Charge", True)

class Impact_EMP_Grenade(Gadget):
    def __init__(self):
        super().__init__("Impact EMP Grenade", True)

class Barbed_Wire(Gadget):
    def __init__(self):
        super().__init__("Barbed Wire", False)

class Deployable_Shield(Gadget):
    def __init__(self):
        super().__init__("Deployable Shield", False)

class Nitro_Cell(Gadget):
    def __init__(self):
        super().__init__("Nitro Cell", False)

class Bulletproof_Camera(Gadget):
    def __init__(self):
        super().__init__("Bulletproof Camera", False)

class Proximity_Alarm(Gadget):
    def __init__(self):
        super().__init__("Proximity Alarm", False)

class Impact_Grenade(Gadget):
    def __init__(self):
        super().__init__("Impact Grenade", False)