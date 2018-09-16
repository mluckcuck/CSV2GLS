"""
CSV2GLS

Matt Luckcuck <m.luckcuck@tutanota.com>

Reads in a csv file and produces a tex file of acronyms compatible with the LaTeX glossary package
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inFile", help="The input file, should be a csv")
parser.add_argument("--outFile", help="The output file location")

args = parser.parse_args()

print("+++ CSV2GPL +++" )

#inputFile = args.inFile
#outputFile = args.outFile

inputFile = "Acronyms.csv"
outputFile = "Acronyms.tex"

print("+++ Converting " + inputFile + " to " + outputFile)

TEMP_FILE = "csv2gpl-"+inputFile.strip(".csv")+".temp"

def readInputFile(inputFile):
    print("+++ Reading Input File +++")
    csvFile = open(inputFile, "r")
    return csvFile

def processFile(csvFile):
    print("+++ Process File +++")

    tempFile = open(TEMP_FILE, "w")

    firstLine = True
    for line in csvFile:
        if firstLine:
            firstLine = False
        else:
            processRow(line, tempFile)

    tempFile.close()
    

def processRow(pair, outputFile):
    print("+++ Process Row +++")
    
    acronym = pair[0]
    description = pair[1]

    glsLine = "\newacronym{" + acronym.lower() + "}{" + acronym + "}{" + description + "}"

    outputFile.write(glsLine)

def writeOutputFile(outputFile):
    print("+++ Writing Output +++")
          
    glsFile = open(outputFile,"w")

    glsFile.write(TEMP_FILE)

    glsFile.close()

csvFile = readInputFile(inputFile)

processFile(csvFile)

writeOutputFile(outputFile)

print("+++ Done +++")
