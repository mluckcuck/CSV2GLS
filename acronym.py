#!/usr/bin/env python
"""
CV2GLS

Matt Luckcuck <m.luckcuck@tutanota.com>

Glossary Package Acronym Object
"""

class Acronym(object):
    """Stores an acronym, ensuring that the key is unique """

    indexMap = {}

    def __init__(self, acronym, description):
        self.setKey(acronym.lower().strip("\n").replace("&","and"))
        self.acronym=acronym.upper().strip("\n").replace("&","\&")
        self.description = description.strip("\n").strip('\"')

    def getKey(self):
        return self.key

    def getAcronym(self):
        return self.acronym

    def getDescription(self):
        return self.description

    def setKey(self, key):
        """ Sets the key, appending an ordinal number if it already exists """
        #if the key already exists...
        if key in Acronym.indexMap.keys():
            #get the current number of times that key exists...
            curKeyindex = Acronym.indexMap[key]

            #append that number and append to the key...
            self.key = key + str(curKeyindex)
            #increment the currnet number of key instances
            Acronym.indexMap[key]= curKeyindex+1
            #works because the first key is 0, but that isn't printed
        else:
            Acronym.indexMap[key] = 1
            self.key = key

    def getGLSLine(self):
        glsLine = "\\newacronym{" + self.getKey() + "}{" + self.getAcronym() + "}{" + self.getDescription() + "}\n"
        return glsLine
        

