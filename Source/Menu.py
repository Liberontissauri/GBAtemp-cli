
from prompt_toolkit import prompt
from os import get_terminal_size
import Parser

class Menu:
    terminal_height = get_terminal_size().lines
    selected_option = "Help"
    content = "GBAtemp CLI help screen"

    def __init__(self):
        print("\033[H\033[J") # Cleaning the console
        print("\n"*50 + self.content) # Printing page content
        print((self.terminal_height-3-self.content.count("\n"))*"\n") # Making space to place the prompt at the bottom of the command line
        userinput = prompt(" {} >> ".format(self.selected_option)) # Creating and displaying command prompt

        option_dict = {
            "news":self.news,
            "exit":self.close
        }
        
        if userinput not in option_dict:
            self.__init__()
        else:
            option_dict[userinput]()
    
    def news(self):
        self.content = Parser.Page("https://gbatemp.net/","News")
        self.content = self.content.getnews()
        self.selected_option = "News"
        self.__init__()

    def close(self):
        print("\n"*50 + "\033[H\033[J")
    
menu = Menu()
