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

#####TODO: rewrite this 
def print_loadout_cmd(loadout):
    """
        Formats and prints a loadout dictionary suitable for displaying in command prompt
    """
    print("Operator:", loadout["Operator"]["Name"], ":", loadout["Operator"]["Image"])
    print("Gadget:", loadout["Gadget"]["Name"], ":", loadout["Gadget"]["Image"])

    print("Primary:", loadout["Primary"]["Name"], ":", loadout["Primary"]["Image"])
    print("Primary Scope:", loadout["Primary"]["Scope"]["Name"], ":", loadout["Primary"]["Scope"]["Image"])
    print("Primary Barrel: ", loadout["Primary"]["Barrel"]["Name"], ":", loadout["Primary"]["Barrel"]["Image"])
    print("Primary Under Barrel: ", loadout["Primary"]["Under Barrel"]["Name"], ":", loadout["Primary"]["Under Barrel"]["Image"])

    print("Secondary: ", loadout["Secondary"]["Name"], ":", loadout["Secondary"]["Image"])
    print("Secondary Scope:", loadout["Secondary"]["Scope"]["Name"], ":", loadout["Secondary"]["Scope"]["Image"])
    print("Secondary Barrel: ", loadout["Secondary"]["Barrel"]["Name"], ":", loadout["Secondary"]["Barrel"]["Image"])
    print("Secondary Under Barrel: ", loadout["Secondary"]["Under Barrel"]["Name"], ":",loadout["Secondary"]["Under Barrel"]["Image"])

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
            operator = choice(ATTACKERS)
        elif option == 2:
            operator = choice(DEFENDERS)
        else:
            operator = choice(ALL_OPERATORS)
        
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
    

