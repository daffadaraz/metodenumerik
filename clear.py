import os

def clear():
    if os.name == "nt":
        os.system('cls')
        pass
    else:
        os.system('clear')
