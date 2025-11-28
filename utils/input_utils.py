import json
def ask_number(rep,maxi = None,mini = None):
    numb = int(input(rep))
    if maxi == None and mini == None:
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
        print(message, end='\n')
        for i in range(len(option)):
            print(str(i+1)+". "+option[i])
        a = int(input())
    return option[a-1]
