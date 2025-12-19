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

def display_main_menu():
    print("1. Start Chapter 1 - Arrival in the magical world.")
    print("2. exit")
def launch_menu_choice():
    houses = {"Gryffindor": 0,"Hufflepuff": 0,"Ravenclaw": 0,"Slytherin": 0}
    for 
