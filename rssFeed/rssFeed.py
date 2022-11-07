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


# Set variables
"""
title = ""
description = ""
dtEvent = ""
titleAndDesc = ""
guidNum = ""
LocalGuidNum = ""
"""

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
    global titleAndDesc
    LocalTitleAndDesc = title + description
    titleAndDesc = LocalTitleAndDesc.lower()
    print('PING')


# Validates the content having important/relevant locations
def locationIsRelevant():
    if "wijlre" in titleAndDesc or "valkenburg" in titleAndDesc: # It just looks or these cities are called in the feed
        return True
    else:
        return False


# Looks for an updates GUID-value
def checkForUpdate(number):
    global LocalGuidNum

    if len(LocalGuidNum) == 0: # When there is no value, fill it up with the current GUID
        LocalGuidNum = number
    if LocalGuidNum == number: # In case the current GUID is the same as the local: no new message
        return False
    else: # In case the GUID and local number are different: new message! 
        LocalGuidNum == number
        return True


# Just here to print the data
def printIt():
    getData()
    print("Loc relevant? ", locationIsRelevant(), '\n', title, '\n', description, '\n', dtEvent,'\n','\n')
    # Delay
    Timer(30.0, printIt).start()



# EXECUTE:
printIt()

