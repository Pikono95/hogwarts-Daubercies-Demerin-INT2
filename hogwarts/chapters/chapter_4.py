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

team_players = load_file('hogwarts/data/teams_quidditch.json')



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
    player_house = character["House"]
    opponent_house = random.choice([house for house in team_players.keys() if house != character["House"]])
    player_team = team_players[character["House"]]
    opponent_team = team_players[opponent_house]

    team_players[player_house]["players"][0] = character["First Name"] + " " + character["Last Name"] + " (Seeker)"
    print(team_players[character["House"]])
    team_players[player_house]["captain"] = character["First Name"] + " " + character["Last Name"]

    print("===== The quiditch final can finally start opposing ", character["House"], "to", opponent_house, " =====")
    
    score = {                                                             #All the functions necessary for the match
        player_house: 0,
        opponent_house: 0
    }

    def display_score():                                
        print("Current Score:")
        print(player_house ,":", score[player_house])
        print(opponent_house ,":", score[opponent_house])

    def golden_snith_appears():
        if randint(1,6) == 6:
            return True
        else:
            return False
        
    def catch_golden_snitch(player_team,opponent_team):
        if randint(1,2) == 1:
            score[player_house] += 150
        else:
            score[opponent_house] += 150
       
   
    input("You feel your entire body twitching with adrenaline as you mount your broomstick.") #start of the match with text and all

def start_chapter_4(character):
    print("============ Chapter 4 : conclusion ============")
    quiditch_match(character)

quiditch_match(character)
