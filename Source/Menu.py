
from prompt_toolkit import prompt
from os import get_terminal_size

class Menu:
    terminal_height = get_terminal_size().lines
    selected_option = "Help"
    content = "oi\ncomoestás?"

    def __init__(self):
        print("\033[H\033[J") # Cleaning the console
        print(self.content) # Printing page content
        print((self.terminal_height-3-self.content.count("\n"))*"\n") # Making space to place the prompt at the bottom of the command line
        userinput = prompt(" {} >> ".format(self.selected_option)) # Creating and displaying command prompt
    
menu = Menu()
