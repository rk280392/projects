#!/usr/bin/python3

"""Generate funny names by randomly combining names from 2 separate lists."""

import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to silly name generator.\n")
    first_name_list = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'","Bob 'Stinkbug'",
         'Bowel Noises','Boxelder', "Bud 'Lite' ",'Butterbean', 'Buttermilk', 'Buttocks', 
         'Chad', 'Chesterfield','Chewy','Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 
         'Crab Meat','Crapps', 'Dark Skies', 'Dennis Clawhammer','Dicman', 'Elphonso')
    last_name_list = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom','Breedslovetrout',
        'Butterbaugh', 'Clovenhoof', 'Clutterbuck','Cocktoasten', 'Endicott', 'Fewhairs',
        'Gooberdapple', 'Goodensmith','Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
        'Hoosenater','Hootkins', 'Jefferson', 'Jenkins',  'Winterkorn','Woolysocks')
    while True:
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        print(f"{first_name} {last_name}\n", file=sys.stderr)
        try_again = input("Didn't like the name? Try again (Press Enter else n to quit): ")
        if try_again.lower() == "n":
            break
    input("Press Enter to exit \n")

if __name__ == "__main__":
    main()
