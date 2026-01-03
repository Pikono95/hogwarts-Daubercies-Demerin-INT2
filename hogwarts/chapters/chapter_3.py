import sys
import random 
import os

hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.character import *
from universe.house import *
from random import randint 

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
    print("Welcome to the magic quiz!")
    print("Answer the 4 questions correctly to earn point for your house.")
    total_points = 0
    for i in range(4):
        j = random.randint(0, len(load_file('hogwarts/data/magic_quiz.json')) - 1)
        question = load_file('hogwarts/data/magic_quiz.json')[j]
        print(f"{i+1}. {question['question']}")
        choice = input("> ")
        if choice == question['answer']:
            print("Correct answer ! +25 points for your house.")
            total_points += 25
        else:
            print(f"Wrong! The correct answer was: {question['answer']}")
    print("score obtained in the quiz:", total_points, " points")
    return total_points

def start_chapter_3(character,houses):
    print("============ Chapter 3: Learning Magic and Magic Quiz ============")
    learn_spells(character)
    score = magic_quiz(character)
    update_house_point(houses, character['House'], score)
    display_winning_house(houses)
    display_character(character)
    print("=======================  End of Chapter 3 ========================",'\n')
    return character