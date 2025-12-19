import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)

import utils.input_utils as u
from universe.character import *

character = init_character()
character["Attributes"]["Bravery"]= 7
character["Attributes"]["Intelligence"]= 5
character["Attributes"]["Loyalty"]= 6
character["Attributes"]["Ambition"]= 4

houses = {"Gryffindor": 0,"Hufflepuff": 0,"Ravenclaw": 0,"Slytherin": 0}

def update_house_point(houses,houses_name,points):
    if houses_name in houses.keys():
        houses[houses_name] += points
    else :
        print("The house name isn't valid")
    
def display_winning_house(houses):
    winning_house = max(houses, key=houses.get)
    print("The house that is winning is", winning_house, "with", houses[winning_house], "points")
    return winning_house

questions = [
 ( "You see a friend in danger. What do you do?",
 ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

 ("Which trait describes you best?",
 ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

 ("When faced with a difficult challenge, you...",
 ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends",
 "Analyze the problem"],
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])]

def assign_house(character,questions):
    print("Entering the hall you see the sorting hat on a chair on the pedestal.")
    a = input("Continue ? (Press enter)")
    print("The hat is placed on your head, you feel it analyzing your mind...")
    b = input("Continue ? (Press enter)")
    score_house = {"Gryffindor": character["Attributes"]["Bravery"]*2, "Hufflepuff": character["Attributes"]["Loyalty"]*2,"Ravenclaw": character["Attributes"]["Intelligence"]*2, "Slytherin": character["Attributes"]["Ambition"]*2}
    for i in range(len(questions)):
        print(questions[i][0])
        choice = u.ask_choice("Choose an option:", questions[i][1])
        score_house[questions[i][2][questions[i][1].index(choice)]] += 2
    max_score = max(score_house.values())
    for house, score in score_house.items():
        if score == max_score:
            house_name = house
            break
    character["House"] = house_name
    print(f"You have been assigned to {house_name}!")
    return character

