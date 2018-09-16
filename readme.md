# CSV2GLS

Matt Luckcuck <m.luckcuck@tutanota.com> 

14th of September 2018

CSV2GLS is a simple program that reads in a csv file and produces a tex file of acronyms compatible with the LaTeX glossary package. 

## Assumptions
 1. first line of csv is the title line (so it will be ignored)
 2. first column of csv is the acronym
 3. second colum of csv is description

## Usage

Run `csv2gls.py` providing the csv file as a parameter. You can also use the `-o` switch to, optionally, provide the outout file.
