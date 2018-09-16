#!/usr/bin/python
"""
CSV2GLS

Matt Luckcuck <m.luckcuck@tutanota.com>

Reads in a csv file and produces a tex file of acronyms compatible with the LaTeX glossary package
"""

import argparse
from acronym import Acronym
import datetime
import os.path




parser = argparse.ArgumentParser()
parser.add_argument("input", help="The input csv file")
parser.add_argument("-o",  help="The output file location; if no location is given, a file is generated in the same directory as the input file")

args = parser.parse_args()

print("+++ CSV2GPL +++" )
print("+++ Matt Luckcuck 2018 +++")

inputFile = args.input
outputFile = args.o

if not outputFile:
    inputFileName = os.path.splitext(inputFile)[0]
    outputFile = inputFileName + ".tex"

print("+++ Converting " + inputFile + " to " + outputFile)


def openInputFile(inputFile):
    
    try:
        csvFile = open(inputFile, "r")
        return csvFile
    except:
        print("exception opening file " + inputFile)
    

def openOutputFile(outputFile):
    
    try:
        file = open(outputFile, "w")
        return file
    except:
        print("exception opening file " + f)

def processFile(csvFile):
    print("+++ Processing CSV File +++")
    
    firstLine = True
    glsList = []
    with csvFile:
        for line in csvFile:
            if firstLine:
                firstLine = False
            elif len(line)>2: 
                glsList.append(processRow(line))

    return glsList

    
    

def processRow(pair):
    
    pair = pair.split(",", maxsplit=1)
    acronymString = pair[0] 
    description = pair[1]

    
    gls = Acronym(acronymString, description)

    return gls
    
    
def writeFile(glsList):
    print("+++ Writing File +++")
    glsFile = openOutputFile(outputFile)
    glsFile.write("%Converted by CSV2GLS from " + inputFile+"\n")
    glsFile.write("%Converted on " + str(datetime.datetime.today())+"\n" )

    for i in glsList:
        glsFile.write(i.getGLSLine())

    
    glsFile.close()


csvFile = openInputFile(inputFile)

glsList = processFile(csvFile)

writeFile(glsList)

csvFile.close()



print("+++ Done +++")
