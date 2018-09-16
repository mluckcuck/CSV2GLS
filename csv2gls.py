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
print("+++ Matt Luckcuck 2018 +++")

#inputFile = args.inFile
#outputFile = args.outFile

inputFile = "Acronyms.csv"
outputFile = "Acronyms.tex"

print("+++ Converting " + inputFile + " to " + outputFile)


def openInputFile(inputFile):
    print("+++ Opning Input File "+inputFile+" +++")
    try:
        csvFile = open(inputFile, "r")
        return csvFile
    except:
        print("exception opening file " + inputFile)
    

def openOutputFile(outputFile):
    print("+++ Opening Output File " + outputFile + " +++")
    try:
        file = open(outputFile, "w")
        return file
    except:
        print("exception opening file " + f)

def processFile(csvFile):
    print("+++ Processing CSV File +++")

    glsFile = openOutputFile(outputFile)
    
    firstLine = True
    
    with csvFile:
        for line in csvFile:
            if firstLine:
                firstLine = False
            else:
                processRow(line, glsFile)

    glsFile.close()
    

def processRow(pair, glsFile):
    print("+++ Process Row +++")
    pair = pair.split(",", maxsplit=1)
    acronym = pair[0].strip("\n").replace("&","and")    
    description = pair[1].strip("\n").strip('\"')
    
    glsLine = "\\newacronym{" + acronym.lower() + "}{" + acronym + "}{" + description + "}\n"

    writeLine(glsLine, glsFile)

def writeLine(glsLine, glsFile):
    print("+++ Writing " + glsLine + "+++")
    
    glsFile.write(glsLine)


csvFile = openInputFile(inputFile)

processFile(csvFile)


csvFile.close()



print("+++ Done +++")
