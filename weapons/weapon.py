from attachments.scope import *
from attachments.barrel import *
from attachments.grip import *
from attachments.under_barrel import *
class Weapon:
    """ Attributes:
        name: weapon name (as displayed in game)
        grips: available grips (including None)
        barrels: available barrels (including None)
        scopes: available scopes (including None)
        under_barrel: available under barrels (including None)
        image_path: relative path to weapon's image representation
    """
    """
        Ubisoft's balancing strategies for Rainbow Six Siege involve controlling access to 
        high-level magnifying scopes. The scopes available for a given weapon may vary depending 
        on the operator using it and their allowed maximum magnification. 
        By default, each weapon's "scopes" field lists out all scopes available to this particular 
        weapon among all users, ranging from non-magnifying to the highest degree of magnification.
        E.g. AUG A2's default 'scope' field consists of all scopes with 0x (no scope), 1.0x, 1.5x, 2.0x, and 
        2.5x, as the maximum magnification for this weapon is 2.5x. However, not all users have access to
        all of these magnifications. 
    """
    GRIPS = (No_Grip, Vertical_Grip, Angled_Grip)
    BARRELS = (No_Barrel, Suppressor, Compensator, Flash_Hider, Extended_Barrel, Muzzle_Brake)
    UNDER_BARRELS = (No_Under_Barrel, Laser)

    """
    GRIPS = ("None", "Vertical Grip", "Angled Grip")
    BARRELS = ("None", "Suppressor", "Compensator", "Flash Hider", "Extended Barrel", "Muzzle Brake")
    UNDER_BARRELS = ("None", "Laser")
    ONE_TIME = ("None", "Holo A", "Holo B", "Holo C", "Holo D", "Red Dot A", "Red Dot B", "Red Dot C", "Reflex A", "Reflex B", "Reflex C",)
    ONE_PT_FIVE = ("1.5x",)
    TWO_TIMES = ("2.0x",)
    TWO_PT_FIVE = ('2.5x A', '2.5x B',)
    THREE_TIMES = ('3.0x',)
    """
    ALL_SCOPES = tuple([cls for cls in Scope.__subclasses__()])
    ONE_TIME = tuple([cls for cls in Scope.__subclasses__() if cls().magnification <= 1])
    ONE_PT_FIVE = (Scope_15x,)
    TWO_TIMES = (Scope_20x,)
    TWO_PT_FIVE = (Scope_25x_A, Scope_25x_B,)
    THREE_TIMES = (Scope_30x,)

    def __init__(self, name, grips, barrels, under_barrels, max_magnification):
        self.name = name
        self.grips = grips
        self.barrels = barrels
        self.under_barrels = under_barrels
        
        if max_magnification == 0:
            self.scopes = (No_Scope,)
        elif max_magnification == 1:
            self.scopes = Weapon.ONE_TIME
        elif max_magnification == 1.5:
            self.scopes = Weapon.ONE_TIME + Weapon.ONE_PT_FIVE
        elif max_magnification == 2.0:
            self.scopes = Weapon.ONE_TIME + Weapon.ONE_PT_FIVE + Weapon.TWO_TIMES
        elif max_magnification == 2.5: 
            self.scopes = Weapon.ONE_TIME + Weapon.ONE_PT_FIVE + Weapon.TWO_TIMES + Weapon.TWO_PT_FIVE
        else:
            self.scopes = Weapon.ONE_TIME + Weapon.ONE_PT_FIVE + Weapon.TWO_TIMES + Weapon.TWO_PT_FIVE + Weapon.THREE_TIMES
    
    def __str__(self):
        """ Overrides the string representation of Weapon objects
        Postcondition: returns the weapon name as displayed in game (not necessarily  identical to class name)
        """
        return self.name
    
    def print_tuple(t):
        for item in t:
            print(item, sep = " ")

    if __name__ == "__main__":
        print_tuple(ONE_TIME)
        print()
        print_tuple(ONE_PT_FIVE)
        print()
        print_tuple(TWO_TIMES)
        print()
        print_tuple(TWO_PT_FIVE)
        print()
        print_tuple(THREE_TIMES)

        
