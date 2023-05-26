from random import choice
from operators.attacker import *
from operators.defender import *

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
    for op in ALL_OPERATORS:
        print(op.image_path)