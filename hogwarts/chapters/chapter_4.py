import sys
import random 
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.character import *
from universe.house import *
from random import randint 

character["First Name"] = "Jack"
character["Last Name"] = "Smith"
character["House"] = "Gryffindor"  # Example assignment, this would be set based on sorting logic

def create_team(house,team_data,is_player):
    team = {
        'name' : house ,
        'score' : 0 ,
        'has_scored' : 0 ,
        'has_blocked' : 0 ,
        'caught_snitch' : False ,
        'players' : team_data ,
        'is_player' : is_player
    }
    return team

def pre_quiditch_match(character):
    print("As you enter the quiditch stadium, the exitement is at its peak !")
    input("press enter to continue...")
    print("As you are preparing yourself in the locker room ron comes at you.")
    input("press enter to continue...")
    print("Hey", character["First Name"] ,"! Ready for the match ?")
    input("too bad i'm injured... but i will support you from the stands !")
    print("This is the final match of the season, and the whole school is watching. Hermione too...")
    input("Hey, see you after the match !")

def quiditch_match(character):
    team_players = load_file('hogwarts/data/teams_quidditch.json')
    player_house = character["House"]
    opponent_house = random.choice([house for house in team_players.keys() if house != character["House"]])
    
    team_players[player_house]["players"][0] = character["First Name"] + " " + character["Last Name"] + " (Seeker)"
    team_players[player_house]["captain"] = character["First Name"] + " " + character["Last Name"]

    team1 = create_team(player_house,team_players[player_house],True)
    team2 = create_team(opponent_house,team_players[opponent_house],False)

    snitch = False

    def display_score(team1,team2):                                
        print("Current Score:")
        print(player_house ,":", team1['score'])
        print(opponent_house ,":", team2['score'])

    def display_team(house,team):
        print(team['name'],"team :")
        player_team_list = team['players']['players']
        for i in range(len(player_team_list)):
            print("-",player_team_list[i])

    def golden_snitch_appears():
        if randint(1,6) == 6:
            return True
        else:
            return False
        
    def catch_golden_snitch():
        if randint(1,2) == 1:
            return True
        else:
            return False
    
    def attempt_goal(attacking_team,defending_team,player_seeker):
        if randint(1,10) >= 6:
            attacking_team['score'] += 10
            attacking_team['has_scored'] += 1
            if player_seeker == True:
                print("You've scored 10 points !")
            else:
                print("10 points scored for", attacking_team['players']['players'][randint(0,3)])
        else:
            defending_team['has_blocked'] += 1
            print(defending_team['players']['players'][randint(4,6)], "has blocked the shot")
            return None
    
    display_team(player_house,team1)
    input("press enter to continue...")
    display_team(opponent_house,team2)
    input("press enter to continue...")
    print("===== The quiditch final can finally start opposing ", character["House"], "to", opponent_house, " =====")
    input("You are the seeker, your goal is to score goals and catch the snitch")
    input("You feel your entire body twitching with adrenaline as you mount your broomstick.") #start of the match with text and all
    for i in range (1,10):
        print("===== Turn",i,"=====")
        attempt_goal(team1,team2,True)
        attempt_goal(team2,team1,False)
        if golden_snitch_appears() == True and snitch == False:
            input("The golden snitch has appeared, will you catch it ?")
            goldenball = [
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀",
    "⠀⢸⡿⠛⠶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀",
    "⠀⠀⢻⣿⣶⣤⣈⠙⠻⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠻⢸⣿⣿⣿⣶⣤⣈⠛⠷⣦⣄⠀⠀⠀⠀⠈⢿⣿⣿⣿⣧⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠋⠹⡇⢿⣿⣿⣷⣦⣀⠙⠷⣦⡀⠀⠀⠀⠻⣿⣿⣿⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣷⣦⡈⠛⢦⠀⠀⠀⠘⠛⠻⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠙⠻⠂⣀⣴⣶⣿⣿⣷⣶⣤⣀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⡄⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⢉⣉⠙⢿⣿⣿⠿⠋⣀⠁⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠁⣿⠛⠷⠀⣤⣤⡄⢸⡿⠁⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣶⣾⣿⣿⡇⠈⠁⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀"
]
            for e in goldenball:
                print(e)
            snitch = True
            if catch_golden_snitch() == True:
                team1['caught_snitch'] = 1
                team1['score'] += 150
                input("WOW you have catched the snitch 150 points for your team")
            else:
                team2['caught_snitch'] = 1
                team2['score'] += 150
                input("Sadly the other team has the snitch 150 points for them")
        display_score(team1,team2)
        input("press enter to continue")
    print("The final score is :")
    display_score(team1,team2)
    input("Press enter to continue...")
    if snitch == True:
        if team1["caught_snitch"] == True:
            "You've catched the snitch in the match, congratulations"
        if team2["caught_snitch"] == True:
            "They've catched the snitch this match"
        
    if team1['score'] >= team2['score']:
        print("You've did it, you are the quiditch champion ! Congrats ! Your house gets 500 points")
        update_house_point(houses,player_house,500)
        input("Press enter to continue...")
    else:
        print("You've failed to win this year's quiditch championship, maybe next year ?")
        update_house_point(houses,opponent_house,500)
        input("press enter to continue...")


def start_chapter_4(character):
    print("============ Chapter 4 : The Quidditch match  ============")
    quiditch_match(character)
    display_character(character)
    print("=======================  End of Chapter 4 ========================")
