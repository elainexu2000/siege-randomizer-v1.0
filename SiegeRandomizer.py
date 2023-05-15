from random import choice
from operators.Attacker import *
from operators.Defender import *

# Global variables: 
attackers = [cls() for cls in Attacker.__subclasses__()]
defenders = [cls() for cls in Defender.__subclasses__()]
all_operators = attackers + defenders

def print_loadout_cmd(loadout):
    """
        Formats and prints a loadout dictionary suitable for displaying in command prompt
    """
    print("Gadget:", loadout["Gadget"])
    print("Primary:", loadout["Primary"])
    print("         Grip:        ", loadout["Primary Grip"])
    print("         Barrel:      ", loadout["Primary Barrel"])
    print("         Scope:       ", loadout["Primary Scope"])
    print("         Under Barrel:", loadout["Primary Under Barrel"])
    print("Secondary:", loadout["Secondary"])
    print("         Grip:        ", loadout["Secondary Grip"])
    print("         Barrel:      ", loadout["Secondary Barrel"])
    print("         Scope:       ", loadout["Secondary Scope"])
    print("         Under Barrel:", loadout["Secondary Under Barrel"])

def display_available_gadgets_and_weapons(option):
    """
        Helper function that prints all available secondary gadgets and weapons (alongside with the scope of max magnification) for all operators in the designated category:
        option = 1: attackers
        option = 2: defenders
        option = 0 (or any other value): all operators
    """
    candidates = []
    if option == 1:
        candidates = attackers
    elif option == 2:
        candidates = defenders
    else:
        candidates = all_operators
    
    for operator in candidates:
        print(operator, ":", operator.gadgets)
        for weapon in operator.primary:
            print("      ", weapon, ":", weapon.scopes[-1])
        print()
        for weapon in operator.secondary:
            print("      ", weapon, ":", weapon.scopes[-1])

def main():
    while(True):
        print("\nSiege Randomizer: Pick a random operator from...:\
              \n[1] All attackers\
              \n[2] All defenders\
              \n[3] All operators\
              \n[0] Exit program")
        try:
            option = int(input("Enter a number from 0 to 3 (do not include brackets):"))
            if option not in range(4):
                raise ValueError
        except:
            print("Invalid choice. Redirecting to home...")
            continue
        
        if option == 0:
            print("Program terminated. ")
            break
        elif option == 1:
            operator = choice(attackers)
        elif option == 2:
            operator = choice(defenders)
        else:
            operator = choice(all_operators)
        
        print(operator)
        print_loadout_cmd(operator.get_random_loadout())
        
        keep_going = input("Would you like to continue? (Y/N): ")
        if keep_going in ['y', 'Y']:
            continue
        elif keep_going in ['n','N']:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Redirecting to home...")

if __name__ == "__main__":
    main()

