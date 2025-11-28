import json
def ask_number(rep,maxi = None,mini = None)
    numb = int(input(rep))
    if maxi = None and mini = None:
        while numb < mimi or numb > maxi:
            print("Please enter a number between ",mini," and ",maxi,".")
            numb = int(input(rep))
    return numb
def ask_text(text):
    a = 0
    while a == 0 or a == None or a == '':
        a = input(text)
    return a.strip()
def ask_choice(message, option):
    a = 0
    while a == 0:
        for i in range(len(options):
            a = input(message)
    return options[int(a)-1]
f = ask_choice("Select an option:", ["Option 1", "Option 2", "Option 3"])