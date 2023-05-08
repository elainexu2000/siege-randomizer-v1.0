from random import choice
from operators.Attacker import *
from operators.Defender import *

def get_random_defender():
    return choice([cls() for cls in Defender.__subclasses__()])

def get_random_attacker():
    return choice([cls() for cls in Attacker.__subclasses__()])

def get_random_operator():
    all_ops = [cls() for cls in Attacker.__subclasses__()] + [cls() for cls in Defender.__subclasses__()]
    return choice(all_ops)

def pretty_print_loadout(loadout):
    primary = loadout["Primary"]
    primary_grip = loadout["Primary Grip"]
    primary_barrel = loadout["Primary Barrel"]
    primary_scope = loadout["Primary Scope"]
    primary_under_barrel = loadout["Primary Under Barrel"]

    secondary = loadout["Secondary"]
    secondary_grip = loadout["Secondary Grip"]
    secondary_barrel = loadout["Secondary Barrel"]
    secondary_scope = loadout["Secondary Scope"]
    secondary_under_barrel = loadout["Secondary Under Barrel"]
    gadget = loadout["Gadget"]

    print("Gadget:",gadget)
    print("Primary:", primary)
    print("         Grip:        ", primary_grip)
    print("         Barrel:      ", primary_barrel)
    print("         Scope:       ", primary_scope)
    print("         Under Barrel:", primary_under_barrel)
    print("Secondary:", secondary)
    print("         Grip:        ", secondary_grip)
    print("         Barrel:      ", secondary_barrel)
    print("         Scope:       ", secondary_scope)
    print("         Under Barrel:", secondary_under_barrel)

def display_available_gadgets_and_weapons(option):
    """
        Prints all available secondary gadgets and weapons (alongside with the scope of max magnification) for all operators in the designated category:
        option = 1: attackers
        option = 2: defenders
        option = 0 (or any other value): all operators
        Precondition: option is an integer
    """
    candidates = []
    if option == 1:
        candidates = [cls() for cls in Attacker.__subclasses__()]
    elif option == 2:
        candidates = [cls() for cls in Defender.__subclasses__()]
    else:
        candidates = [cls() for cls in Attacker.__subclasses__()] + [cls() for cls in Defender.__subclasses__()]
    
    for cls in candidates:
        op = cls()
        print(op, ":", op.gadgets)
        for p in op.primary:
            print("      ", p, ":", p.scopes[-1])
        print()
        for p in op.secondary:
            print("      ", p, ":", p.scopes[-1])

def main():
    while(True):
        print("\nSiege Randomizer: Pick a random operator from...:\
              \n[1] All attackers\
              \n[2] All defenders\
              \n[3] All operators\
              \n[0] Terminate the program")
        try:
            option = int(input("Enter a number from 0 to 3 (do not include brackets):"))
            if option not in range(4):
                raise ValueError
        except:
            print("Invalid choice. Please try again.")
            continue
        
        if option == 0:
            print("Program terminated. ")
            break
        elif option == 1:
            op = get_random_attacker()
        elif option == 2:
            op = get_random_defender()
        else:
            op = get_random_operator()
        
        d = op.get_random_loadout()
        print(op)
        pretty_print_loadout(d)
        
        keep_going = input("Would you like to continue? Y/N: ")
        if keep_going in ['y', 'Y']:
            continue
        elif keep_going in ['n','N']:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Redirecting to home...")

if __name__ == "__main__":
    main()

