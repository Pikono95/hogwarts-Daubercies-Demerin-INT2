import sys
import random 
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.character import *

def learn_spells(character):
    print("You begin your magic lessons at Hogwarts !")
    spells = load_file('hogwarts/data/spells.json')
    learn = [0,0,0]
    while learn[0] < 3 or learn[1] < 1 or learn[2] < 1:
        spell = random.randint(0,len(spells)-1)
        if spells[spell]['type'] == 'Utility' and learn[0] < 3 and spells[spell] not in character['Spells']:
            print(f"You have learned the spell {spells[spell]['name']} ({spells[spell]['type']}) !")
            character['Spells'].append(spells[spell])
            learn[0] += 1
            a = input("Press Enter to continue...")
        if spells[spell]['type'] == 'Offensive' and learn[1] < 1 and spells[spell] not in character['Spells']:
            print(f"You have learned the spell {spells[spell]['name']} ({spells[spell]['type']}) !")
            character['Spells'].append(spells[spell])
            learn[1] += 1
            a = input("Press Enter to continue...")
        if spells[spell]['type'] == 'Defensive' and learn[2] < 1 and spells[spell] not in character['Spells']:
            print(f"You have learned the spell {spells[spell]['name']} ({spells[spell]['type']})!")
            character['Spells'].append(spells[spell])
            learn[2] += 1
            a = input("Press Enter to continue...")
    print("You have completed your basic spell training at Hogwarts")
    print("Here are the spells you have learned:")
    for i in range(len(character['Spells'])):
        print(f"- {character['Spells'][i]['name']} ({character['Spells'][i]['type']}) : {character['Spells'][i]['description']}")

def magic_quiz(character):
    

learn_spells(init_character())
