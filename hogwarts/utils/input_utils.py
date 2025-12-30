import json
import sys
import os
hogwarts_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hogwarts_root)

def ask_text(text):
    a = 0
    while a == 0 or a == None or a == '':
        a = input(text)
    return a.strip()

def ask_choice(message, option):
    print(message, end='\n')
    for i in range(len(option)):
        print(str(i+1)+". "+str(option[i]))
    a = ask_number("Your choice: ", len(option), 1)
    return option[int(a)-1]

def ask_number(message, max_val=None, min_val=None):
    user_input = 0
    while user_input == 0:
        user_input = input(message)
        valid_numbers = ''
        for number in range(10 ** len(user_input)):
            valid_numbers += str(number)
        if (user_input.isascii() and user_input not in valid_numbers) or user_input == '':
            print("Please enter a valid integer.")
            user_input = 0
        else:
            user_input = int(user_input)
            if min_val is not None and user_input < min_val:
                print(f"Please enter a number >= {min_val}.")
                user_input = 0

            elif max_val is not None and user_input > max_val:
                print(f"Please enter a number <= {max_val}.")
                user_input = 0
    return user_input

def load_file(file_path):
    with open(file_path, 'r') as file:
        rep = json.load(file)
    return rep