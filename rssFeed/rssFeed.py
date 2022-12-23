"""
@Stefan Rompen 2022
stefan.rompen7@gmail.com

This code fills up your OLED connected to a ESP32. By default, it looks for the P2000 messages 
given by the RSS-feed (alameringen.nl). This project has been made to test the ESP32 I just got
and I wanted to do a RSS project for the first time. 
"""

# Imports
import feedparser
from threading import Timer



# This function gets the RSS data and stores data into global variables
def getData():
    Feed = feedparser.parse("https://www.alarmeringen.nl/feeds/region/limburg-zuid.rss")
    Entry = Feed.entries[0]

    # Get guid(code)
    global guidNum
    guidNum = Entry.guid

    # Get Title
    try:
        global title
        title = Entry.title
    except:
        title = "N.A.V."

    # Get Description
    try:
       global description
       description = Entry.description
    except:
        description = "N.A.V"

    # Get Date/Time of the event
    global dtEvent
    dtEvent = Entry.published

    # Combine Title and Description, set to lower
    try:
        global titleAndDesc
        LocalTitleAndDesc = title + description
        titleAndDesc = LocalTitleAndDesc.lower()
    except:
        titleAndDesc = "N.A.V"



# Validates the content having important/relevant locations
def locationIsRelevant():
    if "wijlre" in titleAndDesc or "valkenburg" in titleAndDesc: 
        return True
    else:
        return False



# Looks for an updates GUID-value
def checkForUpdate(number):
    global LocalGuidNum

    if len(LocalGuidNum) == 0: 
        LocalGuidNum = number
    if LocalGuidNum == number: 
        return False
    else:  
        LocalGuidNum == number
        return True



# Just here to print the data
def printIt():
    getData()
    print("Loc relevant? ", locationIsRelevant(), '\n', "Titel:   " + title, '\n', "Beschrijving:   " + description, '\n', "Timestamp:   " + dtEvent,'\n','\n')
    Timer(30.0, printIt).start()

# EXECUTE:
printIt()



#def showIt():
#    getData()
#    if checkForUpdate(guidNum):
#        display.clear()
#        display.text('Hellow World')

