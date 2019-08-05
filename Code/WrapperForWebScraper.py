'''
Created on 4 ago. 2019

@author: ingov
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Code.WebScraperForAllMusic import parserForInformation

def getDiscography(artist):
    """
    @param artist: This parameter is a string that contains the name of the band/artist we
    want to search for.
    @return: Nothing
    
    This method is the method we should run to make all this funcionality work. Notice that
    we can't just parse allmusic's pages using a URL where we add somehow the name of the artist as
    allmusic adds IDs to identify different artists or entities with the same name. So we have
    to be creative.
    In this case, we get the name of the artist and use selenium's webdriver to get a browser
    open allmusic.com, search for our artist, get the artist that appears first in our search,
    go its page, go to tab discography and then get the HTML of the page and then call the method
    parserForInformation where we will parse the HTML to get the information we will print in
    console.
    """
    try:
        #We get a Chrome browser and open it
        browser = webdriver.Chrome()
        #We go to allmusic.com
        browser.get("https://www.allmusic.com")
        #We maximize the window
        browser.maximize_window()
        time.sleep(5)
        #We get the button I do not accept that belongs to the initial pop-up we get and click
        #on it
        acceptButton = browser.find_element_by_class_name("qc-cmp-button")
        acceptButton.click()
        time.sleep(5)
        #We get the input that belongs to the search feature in the upper bar
        searchInput = browser.find_element_by_class_name("site-search-input")
        #We write there the name of our artist/band
        searchInput.send_keys(artist)
        #We press Enter to send the form that will control the search
        searchInput.send_keys(u'\ue007')
        time.sleep(5)
        #In the results page, we get the link that changes the view to filter only by artists
        #and click on it
        artistsLink = browser.find_element_by_partial_link_text("Artists")
        artistsLink.click()
        #We get the element that contains all the results with artists with that name
        results = browser.find_element_by_class_name("results")
        #We get the first element in that list and click on it
        firstResult = results.find_element_by_xpath("//li[1]/div[2]/div[1]/a")
        firstResult.click()
        time.sleep(5)
        #We close the element that blocks our vision
        x = browser.find_element_by_link_text("X")
        x.click()
        time.sleep(3)
        #We get the link to change to tab discrography and click on it
        tabDisc = browser.find_element_by_css_selector("li.tab.discography")
        action = ActionChains(browser)
        action.move_to_element(tabDisc)
        action.perform()
        time.sleep(3)
        action.click(tabDisc)
        action.perform()
        #print(browser.page_source)
        print(browser.title)
        print("")
        parserForInformation(browser.page_source)
    except Exception as e:
        print(e)
    finally:
        #When we finish this function, correctly or throwing an exception, we close the browser
        #We should always close the browser at the end of this function so we use the feature
        #finally
        browser.quit()
