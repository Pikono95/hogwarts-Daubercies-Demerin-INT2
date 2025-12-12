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
        a = input("Continue ? (Press enter)")
        print(f"You : Yes, I can't wait to learn magic and meet new friends.")
        print("Ron : Me too ! My family is full of wizards, I hope I'll be in Gryffindor like them.")
        character["Attributes"]["Loyalty"] += 1
        print("You and Ron chat for the rest of the journey, becoming fast friends. You've gained 1 Loyalty point.")
    #ron
    #hermione
    print("As you settle into your compartment, another stranger goes to sit with you")
    b = input("Continue ? (Press enter)")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of magic ?'")
    a = ask_choice("How do you respond ?",["Yes, I love learning new things","Uh.... no, I prefer adventure books"])
    #hermione

def start_chapter_2(character):
    meet_friends(character)
    assign_house(character,questions)
    

start_chapter_2(character)