def ask_text(text):
    a = 0
    while a == 0 or a == None:
        a = input(text)
    return a.strip()
