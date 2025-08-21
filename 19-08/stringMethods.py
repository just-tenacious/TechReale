def capitalizeString(text):
    return text.capitalize()

def caseFold(text):
    return text.casefold()

def centerText(text):
    return text.center(5,'x')

def countValues(text,val):
    return text.count(val)

def endOfText(text,value):
    return text.endswith(value)

def findOccurence(text,search):
    return text.find(search)

def getIndex(text,character):
    return text.index(character)

def isCombo(text):
    return text.isalnum()

def characters(text):
    return text.isalpha()   

def numbers(text):
    return text.isdigit()

def decimals(text):
    return text.isdecimal()

def addText(oldText,newText):
    return oldText.join(newText)