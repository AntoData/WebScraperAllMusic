'''
Created on 4 ago. 2019

@author: ingov
'''
from bs4 import BeautifulSoup
from Code import Utils

def parserForInformation(page_source):
    """
    @param page_source: This is a string that contains the HTML we are going to scrap to print
    the information about the discography of an artist/band
    
    This function is called in method getDiscography after we got to the discography page of
    a band/artist using selenium's webdriver. We use BeautifulSoup to get the information through
    the HTML
    """
    #First we create the object soup that will parse our HTML. We give it as first parameter
    #the string we want to parse, in this case the source code (hTML code) of our page
    #and then we set that it has to be and html parser
    soup = BeautifulSoup(page_source,"html.parser")
    #We get all the elements in the page that are of type table
    tables = BeautifulSoup.find_all(soup, "table")
    #We find all elements inside the second table in the HTML that are of type tr (rows)
    trs = BeautifulSoup.find_all(tables[1], "tr")
    #We go through the different rows (each row is and album) of the table and for each row
    #(each album) we get the columns that contain the information we want to print
    #and we add the columns with the right information to our string "s" where we will
    #keep the information and print it
    for i in range(1,len(trs)):
        tds = BeautifulSoup.find_all(trs[i], "td")
        for j in range(2,len(tds)-1):
            if (j == 2):
                s = Utils.deleteSpaces(tds[j].text)
                print("Year: "+s)
            elif(j !=5 and j!=6):
                s = Utils.deleteIntroTabs(tds[j].text)
                if(j == 4):
                    s = "Label: "+s
                print(s)
            elif(j==5):
                stars = tds[j].div.attrs['class'][1]
                Utils.starsDecode(stars)
            elif(j==6):
                stars = tds[j].div.span.attrs['class'][1]
                Utils.userStarsDecode(stars)
        print("")
