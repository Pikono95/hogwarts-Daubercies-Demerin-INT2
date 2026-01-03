import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)


def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }
    return character

def display_character(character):
    print("Character Information:")
    print("First Name: {} ".format(character["First Name"]))
    print("Last Name: {} ".format(character["Last Name"]))
    print("Money: {}".format(character["Money"]))
    print("Inventory: {}".format(", ".join(character["Inventory"]) if character["Inventory"] else "Empty"))
    print("Spells: {}".format(", ".join(spell["name"] for spell in character.get("Spells", [])) or "None"))
    print("Attributes:")
    for attr, value in character["Attributes"].items():
        print("  {}: {}".format(attr, value))

def modify_money(character,amount):
    character["Money"] += amount
    return character["Money"]

def add_item(character,item):
    character["Inventory"].append(item)
    return character["Inventory"]