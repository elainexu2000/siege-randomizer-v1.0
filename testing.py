from random import choice
from operators.attacker import *
from operators.defender import *
from operators.r6_operator import Operator
from gadgets.gadget import *
from weapons.assault_rifle import *
from weapons.handgun import *
from weapons.light_machine_gun import *
from weapons.machine_pistol import *
from weapons.marksman_rifle import *
from weapons.shield import *
from weapons.shotgun import *
from weapons.submachine_gun import *
from weapons.hand_cannon import *

# Global:
ATTACKERS = tuple([cls() for cls in Attacker.__subclasses__()])
DEFENDERS = tuple([cls() for cls in Defender.__subclasses__()])
ALL_OPERATORS = ATTACKERS + DEFENDERS

def get_random_attacker():
    return choice(ATTACKERS)

def get_random_defender():
    return choice(DEFENDERS)

def get_random_operator():
    return choice(ALL_OPERATORS)

def print_paths():
    for op in ALL_OPERATORS:
        print(op.image_path)

def display_available_gadgets_and_weapons(option):
    """
        Helper function that prints all available secondary gadgets and weapons (alongside with the scope of max magnification) for all operators in the designated category:
        option = 1: attackers
        option = 2: defenders
        option = 0 (or any other value): all operators
    """
    candidates = []
    if option == 1:
        candidates = ATTACKERS
    elif option == 2:
        candidates = DEFENDERS
    else:
        candidates = ALL_OPERATORS
    
    for operator in candidates:
        print(operator, ": ", sep = '' ,end = '')
        for gadget in operator.gadgets:
            print(gadget, ";", sep = '' ,end = ' ')
        print()
        for weapon in operator.primaries:
            print("      ", weapon, ": ", weapon.scopes[-1], sep = '')
        for weapon in operator.secondaries:
            print("      ", weapon, ": ", weapon.scopes[-1], sep = '')


if __name__ == "__main__":
    pass
    """
    glaz = Glaz()
    attacker = Attacker("name")
    print(type(glaz).__name__)
    print(type(attacker).__name__)
    
    for op in ALL_OPERATORS:
        print(op.image_path)
    
    a = Ash()
    print(a.get_random_loadout())
    {
        'Operator': {
            'Name': 'Ash', 
            'Image': '../assets/operators/icons/Ash.png'
        }, 
        'Gadget': {
            'Name': 'Breach Charge', 
            'Image': '../assets/gadgets/attacker_gadgets/Breach_Charge.png'
        }, 
        'Primary': {
            'Name': 'G36C', 
            'Image': '../assets/weapons/assault_rifles/G36C.png', 
            'Scope': {
                'Name': 'Holographic A', 
                'Image': '../assets/sights/Holo_A.png'
            }, 
            'Barrel': {
                'Name': 'Holographic A', 
                'Image': '../assets/sights/Holo_A.png'
            }, 
            'Under Barrel': {
                'Name': 'Laser', 
                'Image': '../assets/under_barrels/Laser.png'
            }
        }, 
        'Secondary': {
            'Name': 'M45 MEUSOC', 
            'Image': '../assets/weapons/handguns/M45_MEUSOC.png', 
            'Scope': {
                'Name': 'None', 
                'Image': '../assets/None.png'
            }, 
            'Barrel': {
                'Name': 'None', 
                'Image': '../assets/None.png'
            }, 
            'Under Barrel': {
                'Name': 'Laser', 
                'Image': '../assets/under_barrels/Laser.png'
            }
        }
    }
    """
    