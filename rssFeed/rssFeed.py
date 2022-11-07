"""
Stefan Rompen
"""
import feedparser
import pyfirmata
from threading import Timer
import time


# Set variables
title = ""
description = ""
dtEvent = ""
titleAndDesc = ""
guidNum = ""
LocalGuidNum = ""


# This function gets the RSS data and stores data into global variables
def getData():
    Feed = feedparser.parse("https://www.alarmeringen.nl/feeds/region/limburg-zuid.rss")
    Entry = Feed.entries[0]

    # Get guid(code)
    global guidNum
    guidNum = Entry.guid

    # Get Title
    if not Entry.title:
        global title
        title = "N.A.V"
    else:
        title = Entry.title

    # Get Description
    if not Entry.description:
        global description
        description = "N.A.V"
    else:
        description = Entry.description

    # Get Date/Time of the event
    global dtEvent
    dtEvent = Entry.published

    # Combine Title and Description, set to lower
    global titleAndDesc
    LocalTitleAndDesc = title + description
    titleAndDesc = LocalTitleAndDesc.lower()


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
    print("Loc relevant? ", locationIsRelevant(), '\n', title, '\n', description, '\n', dtEvent,'\n', "UPDATE :", checkForUpdate(guidNum),'\n','\n')
    # Delay
    Timer(30.0, printIt).start()



# EXECUTE:
printIt()

