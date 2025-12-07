import * from universe.character.py
import * from utils.input_utils.py

def introduction():
    print("Welcome to the harry poter universe, player!")
    a = input("Continue? (Press enter)")
    print("You find yourself in a small room with your lovely familly composed of your conspirationist oncle and your spoiled brat couzin")
    a = input("Continue? (Press enter)")
    print( "in short, you are livling the dream")

def create_character():
    chara = init_character() 
    chara["First Name"] = ask_text("What is your first name? ")
    chara["Last Name"] = ask_text("What is your last name? ")
    chara["attributes"]["Bravery"] = ask_number("On a scale from 1 to 10, how brave are you? ",1,10)
    chara["attributes"]["Intelligence"] = ask_number("On a scale from 1 to 10, how intelligent are you? ",1,10)
    chara["attributes"]["Loyalty"] = ask_number("On a scale from 1 to 10, how loyal are you? ",1,10)
    character["attributes"]["Ambition"] = ask_number("On a scale from 1 to 10, how ambitious are you? ",1,10)*
    display_character(chara)
    return chara

def recieve_letter(character):
    print("An owl flies through the window and falls down but it quickly come back up, delivering a letter sealed with the Hogwarts crest...")
    a = input("read it ? (Press enter)")
    print(f"Dear {character["First name"]},\nWe are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry !")
    a = 