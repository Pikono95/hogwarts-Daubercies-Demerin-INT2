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
    a = 0
    while a == 0:
        print(message, end='\n')
        for i in range(len(option)):
            print(str(i+1)+". "+str(option[i]))
        a = int(input()) 
    return option[a-1]

def ask_number(rep,maxi = None,mini = None):
    numb = int(input(rep))
    if maxi is not None and mini is not None:
        while numb < mini or numb > maxi:
            print(f"Please enter a number between {mini} and {maxi}.")
            numb = int(input(rep))
    return numb

def load_file(file_path):
    with open(file_path, 'r') as file:
        rep = json.load(file)
    return rep