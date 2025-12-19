import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)

from chapters.chapter_1 import *
from chapters.chapter_2 import *
from chapters.chapter_3 import *
from chapters.chapter_4 import *
from universe.character import *
from universe.house import *
from utils.input_utils import *

def display_main_menu():
    choice = ["Start Chapter 1 - Arrival in the magical world.", "Exit"]
    rep = ask_choice("Choose :",choice)
    return choice.index(rep) + 1

def launch_menu_choice():
    houses = {"Gryffindor": 0,"Hufflepuff": 0,"Ravenclaw": 0,"Slytherin": 0}
    choice = display_main_menu()
    if choice == 1:
        character = start_chapter_1()
        start_chapter_2(character)
        start_chapter_3(character,houses)
    elif choice == 2:
        print("Exiting the game. Goodbye!")
        exit()


    
    
    
