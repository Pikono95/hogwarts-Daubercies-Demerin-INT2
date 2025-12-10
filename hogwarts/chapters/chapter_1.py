import * from hogwarts.universe.character.py
import * from hogwarts.utils.input_utils.py

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
    a = ask_choice("Do you accept the invatation to hogwarts ?",["Yes","No"])
    if a == "Yes":
        print("*Your uncle comes up to you*")
        print("Uncle : What are you doing reading that rubbish ? they are juste going to do experiments on you like they did with your parents ! \n" \
        "they work with the CIA to make humanaty theirs slaves")
        a = input("Continue ? (Press enter)")
        print(f"You : *ignoring him* I am going to Hogwarts Uncle, I have to go !")
        print("Uncle : i don't care anyway, go where you want, you are not getting a single galleon from me anymore !")
    if a == "No":
        print("You decide to ignore the letter, your uncle seems pleased by your decision.")
        print("Uncle : good choice, they are evil trying to subdue humanity !")
        print("The end.")
        exit()
    
def meet_hagrid(character):

def buy_supplies(character):
    print("Catalog of available items:")
    catalog={
    "1": ["Magic Wand", 35, "Galleons (required)"],
    "2": ["Wizard Robe", 20, "Galleons (required)"],
    "3": ["Tin Cauldron", 15, "Galleons"],
    "4": ["Potions Book", 25, "Galleons (required)"],
    "5": ["Magic Quill", 5, "Galleons"],
    "6": ["Enchanted Book", 30, "Galleons"],
    "7": ["Copper Scale", 10, "Galleons"],
    "8": ["Invisibility Cloak", 100, "Galleons"]
    }
    for i in catalog:
        print(f"- {catalog[i][0]} : {catalog[i][1]} {catalog[i][2]}")
    while "1" not in character["Inventory"] or "2" not in character["Inventory"] or "4" not in character["Inventory"]:
        print(f"You have {character["Money"]} Galleons.\nRemaining required items :")
        for i in catalog:
            if catalog[i][2] == "Galleons (required)" and i not in character["Inventory"]:
                print(f"- {catalog[i][0]}", end='')
        a=input("\nEnter the number of the item to buy:")
        if character["Money"]-catalog[a][1] > 0:
            character["Inventory"].append(a)
            character["Money"] -= catalog[a][1]
            print(f"You bought: {catalog[a][0]} (- {catalog[a][1]} Galleons).\n")
        else:
            print(f"You have {character["Money"]} Galleons. You can't buy it\n")

    