import requests
from bs4 import BeautifulSoup, NavigableString

from os import get_terminal_size

class Page:
    def get_news(self,pagenum):

        parsed = "-"*get_terminal_size().columns+"\nGBAtemp - Site & Scene News - Page {}\n\n".format(pagenum)

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

    def get_news_article(self,url):
        toparse = requests.get(url).content
        toparse = BeautifulSoup(toparse, "html.parser")
        title = ""
        for tag in toparse.findAll("a",{"id":"threadTitle"}):
            if tag != None:
                title = tag.get_text()
                break

        parsed = "-"*get_terminal_size().columns+"\nGBAtemp - {} - Page 1\n\n".format(title)

        header_len = len("GBAtemp - {} - Page 1".format(title))

        current_paragraph = ""

        paragraphs = []

        for element in toparse.find("blockquote",{"class":"messageText SelectQuoteContainer ugc baseHtml"}):
            current_paragraph = str(element).replace("\n", "")
            current_paragraph = current_paragraph.replace("\t","")
            if type(element) is NavigableString and len(current_paragraph)!=0:
                paragraphs.append(current_paragraph)
        
        for paragraph in paragraphs:
            parsed+="\n "
            letter_counter = 0
            for letter in paragraph:
                if letter_counter >= header_len and letter == " ":
                    parsed += "\n"
                    letter_counter = 0
                parsed += letter
                letter_counter += 1
                
                


        return parsed

    def gopage(self,type,path):
        pagefunctions = {

            "News":self.get_news_article
        }
        pagefunctions[type](path)
        