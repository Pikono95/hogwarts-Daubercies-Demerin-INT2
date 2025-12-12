import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)
import utils.input_utils as u

def update_house_point(houses,houses_name,points):
    if houses_name in houses == True:
        houses[houses_name] += points
    else :
        print("The house name isn't valid")
    
houses = {"Gryffindor": 0,
          "Hufflepuff": 0,
            "Ravenclaw": 0,
            "Slytherin": 0}
    
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

def assign_house(character, questions):
    house = {"Gryffindor": character["Attributes"]["Bravery"]*2,"Slytherin": character["Attributes"]["Ambition"]*2,"Hufflepuff": character["Attributes"]["Loyalty"]*2,"Ravenclaw": character["Attributes"]["Intelligence"]*2}
    for i in range(0,len(questions),3):
        answer = ask_choice(questions[i], questions[i+1])
        house_name = questions[i+2][questions[i+1].index(answer)]
        house[house_name] += 3
    print("sumary of scores :")
    for h in house:
        print(f"{h} : {house[h]} points")
    assigned_house = max(house, key=house.get)
    return assigned_house        