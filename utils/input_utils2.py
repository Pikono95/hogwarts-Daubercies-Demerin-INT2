import json
def ask_number(rep,maxi = None,mini = None):
    numb = int(input(rep))
    if maxi = None and mini = None:
        while numb < mimi or numb > maxi:
            print("Please enter a number between ",mini," and ",maxi,".")
            numb = int(input(rep))
    return numb
def load_file(file_path):
    with open(file_path, 'r') as file:
        rep = json.load(file)
    return rep
