'''
RecipeChoice
Makes a text file with "recipes".
Add pieces of the puzzle in in_types. Input files should be the string used in in_types + .txt
'''

import os,random

in_types = ["carbs","veg"]
resultfile = "result.txt"
weeks = 2

def retRandItem(lst=[]):
    return lst[random.randint(0,len(lst)-1)]

def readFile(file="in.txt"):
    with open(file,"r") as f:
        for l in f:
            line = l.strip("\n").strip()
            if line.startswith("#") or len(line)<2:
                continue
            else:
                yield line

def writeFile(file="",text=""):
    with open(file,"w") as f:
        f.write(text)
                
def retLst(file="in.txt"):
    return [line for line in readFile(file=file)]

def genResult(weeks=weeks,in_types=in_types):
    text = "Result:\n\n"

    for week in range(weeks):
        for day in range(7):
            for i in in_types:
                text += retRandItem(retLst(file=i+".txt")) + " - "
            text = text[:-3] + "\n"
        text += "\n"
    return text


writeFile(file=resultfile,text=genResult(weeks=weeks,in_types=in_types))
os.startfile(resultfile, 'open')
