
from prompt_toolkit import prompt
from os import get_terminal_size
import Parser

class Menu:
    terminal_height = get_terminal_size().lines
    selected_option = "Help"
    content = "\nGBAtemp CLI help screen"
    links = []

    def __init__(self):
        print("\033[H\033[J") # Cleaning the console
        print("\n"*50 + self.content) # Printing page content
        print((self.terminal_height-4-self.content.count("\n"))*"\n") # Making space to place the prompt at the bottom of the command line

        userinput = prompt("\n" + " {} >> ".format(self.selected_option)) # Creating and displaying command prompt
        
        if " " in userinput:
            arguments = userinput[userinput.find(" "):]
            userinput = userinput[:userinput.find(" ")]

        option_dict = {
            "news":self.news,
            "exit":self.close,
            "go":None
            
        }
        go_options_dict = {
            "News":self.newsarticle

        }
        
        if userinput not in option_dict:
            self.__init__()
        elif userinput == "go":
            
            go_options_dict[self.selected_option](arguments)
        else:
            option_dict[userinput]()
    
    def news(self):
        self.content = Parser.Page()
        self.content, self.links = self.content.get_news(1)
        self.selected_option = "News"
        self.__init__()

    def newsarticle(self,arguments):
        self.content = Parser.Page()
        self.content = self.content.get_news_article(self.links[int(arguments)])
        self.__init__()

    def close(self):
        print("\n"*50 + "\033[H\033[J")
    
menu = Menu()
