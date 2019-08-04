'''
Created on 4 ago. 2019

@author: ingov
'''
def userStarsDecode(stars):
    """
    @param stars: This parameter is a string that contains the property class of the div
    that contains the stars users have given to an album in allmusic.com's discography tab in
    a group's page. We get this parameter from the function that parses the discography page
    @return: Nothing, but we print a string that contains the equivalent in number of stars 
    given to an album so we can use it when printing the information of an album in the console
    
    Basically this function gets the class of the div that contains the picture with the stars
    given to an album by users and translate this to a string "s" where we tell users the number
    of stars.
    """
    s = "User Reviews: "
    if stars == "rating-average-10":
        s+="5 stars"
    elif stars == "rating-average-9":
        s+="4.5 stars"
    elif stars == "rating-average-8":
        s+="4 stars"
    elif stars == "rating-average-7":
        s+="3.5 stars"
    elif stars == "rating-average-6":
        s+="3 stars"
    elif stars == "rating-average-5":
        s+="2.5 stars"
    elif stars == "rating-average-4":
        s+="2 stars"
    elif stars == "rating-average-3":
        s+="1.5 stars"
    elif stars == "rating-average-2":
        s+="1 stars"
    elif stars == "rating-average-1":
        s+="0.5 stars"
    else:
        s+= "Not Rated"
    print(s)        

def starsDecode(stars):
    """
    @param stars: This parameter is a string that contains the property class of the div
    that contains the stars allmusic's critics have given to an album in allmusic.com's 
    discography tab in a group's page. We get this parameter from the function that parses 
    the discography page
    @return: Nothing, but we print a string that contains the equivalent in number of stars 
    given to an album so we can use it when printing the information of an album in the console
    
    Basically this function gets the class of the div that contains the picture with the stars
    given to an album by users and translate this to a string "s" where we tell users the number
    of stars.
    """
    s = "AllMusic Review: "
    if stars == "rating-allmusic-9":
        s+="5 stars"
    elif stars == "rating-allmusic-8":
        s+="4.5 stars"
    elif stars == "rating-allmusic-7":
        s+="4 stars"
    elif stars == "rating-allmusic-6":
        s+="3.5 stars"
    elif stars == "rating-allmusic-5":
        s+="3 stars"
    elif stars == "rating-allmusic-4":
        s+="2.5 stars"
    elif stars == "rating-allmusic-3":
        s+="2 stars"
    elif stars == "rating-allmusic-2":
        s+="1.5 stars"
    elif stars == "rating-allmusic-1":
        s+="1 stars"
    elif stars == "rating-allmusic-0":
        s+="0.5 stars"
    else:
        s+= "Not Rated"
    print(s)                    

def deleteIntroTabs(s):
    """
    @param s: String where we want to delete tabs ("\t") and enters ("\r")
    @return: The same string "s" without those special characters
    """
    s = s.replace("\n","")
    #s = s.replace(" ","")
    s = s.replace("\t","")
    return s

def deleteSpaces(s):
    """
    @param s: String where we want to delete tabs ("\t"), enters ("\r") and spaces (" ")
    @return: The same string "s" without those special characters
    """
    s = s.replace(" ","")
    s = s.replace("\n","")
    s = s.replace("\t","")
    return s