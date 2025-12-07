from hogwarts.utils import input_utils
def update_house_point(houses,houses_name,points):
    if houses_name in houses == True:
        houses[houses_name] += points
    else :
        print("The house name isn't valid")
    
houses = {"Gryffindor": 5,
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

def assign_house(character, house_name):
    for i in range(len(questions)):
        print(questions[i][0])
        choic


