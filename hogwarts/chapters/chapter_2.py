import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.house import *
from universe.character import *
from chapters.chapter_1 import *

def meet_friends(character):
    #ron
    print("You find a seat on the train, a young ginger boy approaches you.")
    print("Ron : Hi, I'm Ron Weasley, mind if I sit here ?")
    a = ask_choice("Do you let him sit with you ?",["Yes","No"])
    if a == "Yes":
        print("Ron : Thanks ! So, are you excited about starting at Hogwarts ?")
        print(f"You : Yes, I can't wait to learn magic and meet new friends.")
        input("Continue ? (Press enter)")
        print("Ron : Me too ! My family is full of wizards, I hope I'll be in Gryffindor like them.")
        character["Attributes"]["Loyalty"] += 1
        print("You and Ron chat for the rest of the journey, becoming fast friends. You've gained 1 Loyalty point.")
    
    #ron
    #hermione
    input("The train passes by dragons and as you look someone enters your compartment. (Press enter)")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of magic ?'")
    a = ask_choice("How do you respond ?",["Yes, I love learning new things","Uh.... no, I prefer adventure books"])
    if a == "Yes, I love learning new things":
        print("Hermione : That's great ! We should study together sometime.")
        character["Attributes"]["Intelligence"] += 2
        input("You and Hermione discuss your favorite books and subjects. You've gained 1 Intelligence point. (Press enter)")
    else:
        print("Hermione : Oh, well, I suppose adventure books can be fun too.")
        character["Attributes"]["Intelligence"] += -2
        input("You and Hermione have a brief conversation before she returns to her seat. You've lost 2 Intelligence points. (Press enter)")
    #hermione
    #drago
    b = ask_choice("I'm Draco Malfoy, It's best to choose your friends carefully from the start, don't you think ?",(["Shake his hand politely"],["Ignore him completely"],["Respond with arrogance"]))
    if b == "Shake his hand politely":
        print("Draco : Hmph, we'll see about that.")
        character["Attributes"]["Ambition"] += 1
        input(" A polite and respectful reaction reflects strategy and social cunning. You've gained 1 Ambition point. (Press enter)")
    elif b == "Ignore him completely":
        print("Draco : How rude !")
        character["Attributes"]["Loyalty"] += 1
        input("Ignoring Draco shows loyalty to your own choices and friends. (Press enter)")
    else:
        print("Draco : Interesting response.")
        character["Attributes"]["Bravery"] += 1
        input("Responding arrogantly demonstrates courage in the face of a conflictual situation. You've gained 1 Bravery point. (Press enter)")
    #drago
def start_chapter_2(character):
    meet_friends(character)
    assign_house(character,questions)
    

