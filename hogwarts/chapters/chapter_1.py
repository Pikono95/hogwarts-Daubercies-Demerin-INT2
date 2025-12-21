import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, hogwarts_root)
    
from utils.input_utils import *
from universe.character import *


hogwarts_draw = [
"                                           :                                                                                 ",
"                                         .@@=                                                                                ",
"                                        :@@%@=                                      .=                                       ",
"                                       =@%  %@-                        +=          *@   *@@:                                 ",
"                                      *@%    *@=                        =@#+     +@@.  .=@*:                 *@%+.           ",
"                                     #@+      %@-                      =::*%=#:=@@@*     .                   -@@:            ",
"                                   .@@=        *@=                      #@@@++%@@@@.                                          ",
"             #=                   :@@:          %@-                    :@@@+-#@@@@@@@@@*:                                    ",
"            +@@-  =.             =@@.            #@=                      *+@@@@@@@@@@@%=:          :%+       -              ",
"           :@@@%..%@:           *@#               #@-                     *-@@@@@@@-                .@+:+=*%@#-              ",
"           #@.-@#*@%@.         %@*                 #@-                  .%@@@#*@@@%                 .@@= *@% =    -@@+       ",
"          =@-  -@@: #@:       @@+                   %@-                -@#:    +@@*   .             *-#@=%- .-   :#@@%.      ",
"         :@#    ::   *@.    .*@@@@+                #@@@:                        #@+   .@=*=      .+: :=+#*@@@@:    -.        ",
"         *@:          +@:       -@#    *@#   *@#   #@+                           *-  :%@@@:      -*%@@%::@: -#@=              ",
"        -@=   ##.      +@       -@#    *@#   *@#   *@+                            .    :@.            = =@@@%#*+-            ",
"       .@#   .%%.    .#@@@:     :@@%-              +@+                                  .             ::*@=@@.                ",
"       *@-    #%.    =@@:       :@@++=             +@*                                                 +*. =@%.               ",
"      :@+          .%@@@: +@@. #@@@=-:           %@@@# .%@. =@#                                    +-       +@@.              ",
"     .@@@%%#+.       .@@@%@@@%%@@@#                -@@@@@@@@@@@@%                               -%@@@=       *@%              ",
"      :-=*#@@.        ............                 .+++++++++++==                                =@@@#.       #@%.           ",
"           %@@%      :====  +@@@+                                           .*+ -   +@:          ##+%-         #@#           ",
"           @@.       :@@@@  =@@@=             %=.*                  -@@+    *@@@@#=@@@#=                       .%:-:         ",
"           @#:       .@@@@  =@@@=           .%@=@@@#  *##      =*+.=@%=%@+  +@@=@%-=@@*.    .:                  :@@@.        ",
"          :@+        .%@@@  =@@@=  :+@#@#. -@@%  @@#  #@@. .*  *@@: .  #@#  +@@    -@@=   .#@@+                  +@@@:       ",
"          =@=         %@@@  =@@@@@@@@+ #@% =@@#  @@#  #@@. @@  *@@: .% #@%  =@%    -@@=  %@# +@:                  #@@@.      ",
"          +@-      *-.@@@@. =@@@+ *@@+ +@% -@@*  %@#  #@@. @@. *@@-%@@.#@@  =@@    -@@=  .%@@-.                    #@@@:     ",
"          #@:      :#@@@@@%%%@@@+ +@@+ +@@ :@@= :@@#  #@@.:@@. #@= =@@:#@@. +@@:   -@@-    #@@#                    .%@@-     ",
"          %@.         %@@@. =@@@+ =@@+ +@@  %@@@=%@#  +@@#@@@#@@.   #@@@@*  ==-.   -@@- .%@.+@@*                              ",
"          @@.         %@@@. =@@@*  =@@ *@@.   .  %@#   .%@:  %*        ..          -@@:  :@@@@+                               ",
"         .@@.         %@@@. =@@@*    =#-         %@#                               :@@+   :@=                                 ",
"         :@%         .%@@@: =@@@*           :#.  @@*                                  .                                       ",
"         :@%                +@@@#          =@@+-@*                                                                           ",
"         -@%                                =@@=                                                                              ",
"         =@#                                 .                                                                                ",
"         #@#                                                                                                                  ",
"       :-.                                                                                                                    "
]


def introduction():
    for line in hogwarts_draw:
        print(line)
    print("Welcome to the Harry Potter universe, player!")
    a = input("Continue? (Press enter)")
    print("You find yourself in a small room with your lovely family composed of your conspiracy theorist uncle and your spoiled brat cousin")
    a = input("Continue? (Press enter)")
    print("In short, you are living the dream")

def create_character():
    chara = init_character() 
    chara["First Name"] = ask_text("What is your first name? ")
    chara["Last Name"] = ask_text("What is your last name? ")
    chara["Attributes"]["Bravery"] = ask_number("On a scale from 1 to 10, how brave are you? ",10,1)
    chara["Attributes"]["Intelligence"] = ask_number("On a scale from 1 to 10, how intelligent are you? ",10,1)
    chara["Attributes"]["Loyalty"] = ask_number("On a scale from 1 to 10, how loyal are you? ",10,1)
    chara["Attributes"]["Ambition"] = ask_number("On a scale from 1 to 10, how ambitious are you? ",10,1)
    display_character(chara)
    return chara

def receive_letter(character):
    print("An owl flies through the window and falls down but it quickly comes back up, delivering a letter sealed with the Hogwarts crest...")
    a = input("Read it? (Press enter)")
    print(f"Dear {str(character['First Name'])},\nWe are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry!")
    a = ask_choice("Do you accept the invitation to Hogwarts?", ["Yes", "No"])
    if a == "Yes":
        print("*Your uncle comes up to you*")
        print("Uncle: What are you doing reading that rubbish? They're just going to do experiments on you like they did with your parents!\n"
              "They work with the CIA to make humanity their slaves.")
        a = input("Continue? (Press enter)")
        print(f"You: *ignoring him* I am going to Hogwarts, Uncle, I have to go!")
        print("Uncle: I don't care anyway, go where you want, you are not getting a single galleon from me anymore!")
    if a == "No":
        print("You decide to ignore the letter; your uncle seems pleased by your decision.")
        print("Uncle: Good choice, they are evil trying to subdue humanity!")
        print("The end.")
        exit()
    
def meet_hagrid(character):
    print("On the day of your birthday a giant of a man bursts through the door!")
    a = input("Continue? (Press enter)")
    print(f"Hello {character['First Name']}! I'm here to help you with your shopping on Diagon Alley.")
    a = ask_choice("Do you want to follow Hagrid?", ["Yes", "No"])
    if a == "Yes":
        print("Hagrid: Follow me, we have a lot to do today!")
        print("*You follow Hagrid out of the house and into the streets*")
    if a == "No":
        print("*Hagrid has some very convincing arguments so you follow him anyway*")


def buy_supplies(character):
    print("Catalog of available items:")
    catalog = load_file("hogwarts/data/inventory.json")
    for i in catalog:
        print(f"{i}. {catalog[i][0]} : {catalog[i][1]} Galleons")
    while catalog["1"][0] not in character["Inventory"] or catalog["2"][0] not in character["Inventory"] or catalog["4"][0] not in character["Inventory"]:
        print(f"You have {character["Money"]} Galleons.\nRemaining required items :")
        for i in catalog:
            if f"{i}" in "124" and catalog[i][0] not in character["Inventory"]:
                print(f"- {catalog[i][0]}")
        a=input("Enter the number of the item to buy:")
        if character["Money"]-catalog[f"{a}"][1] > 0:
            character["Inventory"].append(catalog[str(a)][0])
            character["Money"] -= catalog[a][1]
            print(f"You bought: {catalog[a][0]} (- {catalog[a][1]} Galleons).\n")
        else:
            print(f"You have {character["Money"]} Galleons. You can't buy it\n")
    print("All required items have been purchased!")
    print("It's time to choose your Hogwarts pet!")
    print(f"You have {character["Money"]} Galleons")
    print("Available pets:")
    catalog = {"1": ["Owl", 20], "2": ["Cat", 15],"3":["Rat", 10], "4": ["Toad", 5]}
    for i in catalog:
        print(f"- {catalog[i][0]} : {catalog[i][1]} Galleons")
    a = ask_choice("Which pet do you want to buy ?",["Owl","Cat","Rat","Toad"])
    character["Inventory"].append(a)
    character["Money"] -= catalog[[k for k,v in catalog.items() if v[0]==a][0]][1]
    print(f"You bought a {a}! (- {catalog[[k for k,v in catalog.items() if v[0]==a][0]][1]} Galleons)")
    print("All required items have been successfully purchased! Here is your final inventory:")
    display_character(character)

def start_chapter_1():
    print("============ Chapter 1: Arrival in the Magical World ============")
    introduction()
    chara = create_character()
    receive_letter(chara)
    meet_hagrid(chara)
    buy_supplies(chara)
    print("======================== END of Chapter 1 ========================","\n")
    return chara