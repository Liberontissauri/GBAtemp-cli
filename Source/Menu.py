
from prompt_toolkit import prompt
from os import get_terminal_size
import Parser

class Menu:
    terminal_height = get_terminal_size().lines
    selected_option = "Help"
    content = "\nGBAtemp CLI help screen"
    arguments = ""
    links = []

    def __init__(self):
        print("\033[H\033[J") # Cleaning the console
        print("\n"*50 + self.content) # Printing page content
        print((self.terminal_height-4-self.content.count("\n"))*"\n") # Making space to place the prompt at the bottom of the command line

        userinput = prompt("\n" + " {} >> ".format(self.selected_option)) # Creating and displaying command prompt
        
        if " " in userinput: # Verifying the presence of arguments in user input
            self.arguments = userinput[userinput.find(" "):]
            userinput = userinput[:userinput.find(" ")]

        option_dict = { # Possible options for user input (takes userinput to find the correct option)
            "news":self.news,
            "exit":self.close,
            "go":None # The go option will be executed later since it behaves differently depending on the page.
            
        }
        go_options_dict = { # Dictionary to hold the possible usages of the go function (uses the selected option to find the correct option)
            "News":self.newsarticle

        }
        
        if userinput not in option_dict: # Verifying if the user input is valid
            self.__init__()
        elif userinput == "go":
            go_options_dict[self.selected_option]()

        else: # The user input is a normal command (unlike go)
            option_dict[userinput]()
    
    def news(self):
        self.content = Parser.Page()
        try: # Verifying if there is an valid argument for news
            self.content, self.links = self.content.get_news(int(self.arguments))
        except ValueError: # Using default value 1 for argument if no valid argument is given
            self.content, self.links = self.content.get_news(1)
        self.selected_option = "News"
        self.__init__()

    def newsarticle(self):
        self.content = Parser.Page()
        self.content = self.content.get_news_article(self.links[int(self.arguments)])
        self.__init__()

    def close(self):
        print("\n"*50 + "\033[H\033[J")
    
menu = Menu()
