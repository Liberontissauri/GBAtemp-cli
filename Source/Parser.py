import requests
from bs4 import BeautifulSoup
from time import sleep
from os import get_terminal_size

class Page:
    def getnews(self,pagenum):

        parsed = "-"*get_terminal_size().columns+"\nGBAtemp - Site & Scene News - Page 1\n\n\n\n"

        toparse = requests.get("https://gbatemp.net/forums/gbatemp-scene-news.101/page-{}".format(pagenum)).content
        toparse = BeautifulSoup(toparse, "html.parser")

        news_list_unparsed = toparse.findAll("div",{"class":"titleText"})

        news_names_list = []
        comment_number_list = []
        dates_list = []
        authors_list = []
        links_list = []

        for new in news_list_unparsed:
            if new.find("a",{"class":"PreviewTooltip"}) is not None:
                news_names_list.append(new.find("a",{"class":"PreviewTooltip"}).get_text())
                links_list.append("https://gbatemp.net/"+new.find("a",{"class":"PreviewTooltip"}).get("href"))
            if new.find("a",{"class":"username"}) is not None:
                authors_list.append(new.find("a",{"class":"username"}).get_text())
            if new.find("span",{"class":"DateTime"}) is not None:
                dates_list.append(new.find("span",{"class":"DateTime"}).get_text())
            elif new.find("abbr",{"class":"DateTime"}) is not None:
                dates_list.append(new.find("abbr",{"class":"DateTime"}).get("data-datestring"))

        for block in toparse.findAll("dl",{"class":"major"}):
            if block.find("dd") is not None:
                comment_number_list.append(block.find("dd").get_text())
        
        for i in range(0,len(news_names_list)):
            parsed += "      " + news_names_list[i] + "\n"
            parsed += " {} - ".format(str(i)) + dates_list[i] + "\n"
            parsed += "      " + "by " + authors_list[i] + " - " + comment_number_list[i].replace("\n","") + " Comments\n\n\n"
            

        return parsed, links_list
