import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)

import utils.input_utils as u
from universe.character import *



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

def assign_house(character, house_name):
    score_house =  {"Gryffindor": character["Attribute"]["Bravery"]*2,"Hufflepuff": 0,"Ravenclaw": 0,"Slytherin": 0}
    print(score_house)
