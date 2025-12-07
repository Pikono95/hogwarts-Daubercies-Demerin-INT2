def init_character():
    character = {
        "Last Name": None,
        "First Name": None,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": {}
    }
    return character

def display_character(character):
    print("Character Information:")
    print("Name: {} {}".format(character["First Name"], character["Last Name"]))
    print("Money: {}".format(character["Money"]))
    print("Inventory: {}".format(", ".join(character["Inventory"]) if character["Inventory"] else "Empty"))
    print("Spells: {}".format(", ".join(character["Spells"]) if character["Spells"] else "None"))
    print("Attributes:")
    for attr, value in character["Attributes"].items():
        print("  {}: {}".format(attr, value))
