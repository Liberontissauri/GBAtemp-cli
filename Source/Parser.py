import requests
from bs4 import BeautifulSoup

class Page:
    def __init__(self, current_page, page_type):
        self.current_page = current_page
        self.page_type = page_type

    def getnews(self):

        parsed = "\nGBAtemp - Site & Scene News\n\n\n"

        toparse = requests.get("https://gbatemp.net/").content
        toparse = BeautifulSoup(toparse, "html.parser")

        news_list_unparsed = toparse.findAll("li",{"class":"news_item full"})

        news_list = []
        comment_number_list = []
        dates_list = []
        authors_list = []

        for news in news_list_unparsed:
            counter = 0
            for tag in news.findAll("a"):
                if tag.get_text() != "":
                    counter += 1
                    if counter == 1:
                        news_list.append(tag.get_text())
                    elif counter == 2:
                        comment_number_list.append(tag.get_text().replace("	",""))
                    elif counter == 3:
                        dates_list.append(tag.get_text())
                    elif counter == 4:
                        authors_list.append(tag.get_text())
                    
        for i in range(0,len(news_list)):
            parsed += "  " + news_list[i] + "\n"
            parsed += "  " + dates_list[i] + "\n"
            parsed += "  " + "by " + authors_list[i] + " - " + comment_number_list[i].replace("\n","") + " Comments\n\n\n"
        
        return parsed
    
