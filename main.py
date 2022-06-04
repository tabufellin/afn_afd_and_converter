from ctypes import sizeof
from distutils.command.clean import clean
from operator import invert
from sqlite3 import Row
from cocol_functions import getCocolTokens
from nfa import *
from dfa import *
from sub import *
from thombson import *
import re

#initial variables
listCharactersTokens = []
listRealTokens = []
validOperators = "|()*+?"
reservedWords = []
cocolTokens = getCocolTokens()
tokensConverted = cocolTokens
#patron CHR(any number between 1 to 3)
chrRegex = re.compile(r'(CHR)\(\d{1,3}\)')

rangeLetter =re.compile(r"(\w{1})(.*\..*\..*)((\w{1}))")

sumForm = re.compile(r'(CHR)\(\d{1,3}\)')

def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')


# Character range function
def range_char(start, stop):
    values=[]

    for n in range(ord(start), ord(stop) + 1):
        values.append(chr(n))
    values =  ''.join(values)

    return values


def replaceWithAlreadyTokens(listTokens, value):
    newListTokens = listTokens
    
    #prioritaze bigger over smaller ones doing a
    #  sort of tokens from bigger to smaller len
    newListTokens.sort(key=lambda x:len(x[0]), reverse=True)
    

    for token in newListTokens:
        
 
        position = value.find(token[0])

        if (position != -1):
            value = value.replace(token[0],('('+token[1]+')'))


    return value


for token in cocolTokens:

    typeToken, tokens = token[0], token[1] 

    if('CHARACTERS' in typeToken):

        for t in tokens:


            #only do one max split of = because it could contain that sign inside other parts
            vocal, value = t.replace(' ', '').split('=', 1)



            #probably this will fuck up things
            cleanValue = value.replace("'", "").replace('"', '')[::-1].replace('.'[::-1], '' , 1)[::-1]

            cleanValue = replaceWithAlreadyTokens(listCharactersTokens, cleanValue)
            
            #check for characters form
            chrObject = chrRegex.search(cleanValue)
            if (chrObject != None):
                chrForm = chrObject.group(0)
                chrNumber = int(chrForm.replace('CHR(', '').replace(')', ''))

                #if I find CHR pattern inside I will do the next thing
                if (chrForm):
          
                    value = chr(int(chrNumber))
                    #position of CHR              
                    cleanValue = cleanValue.replace(chrForm, chr(chrNumber))

           #check if "A..Z form"
            rlObject = rangeLetter.search(cleanValue)
            if (rlObject != None):

               firstLetter = rlObject.group(1)
               lastLetter = rlObject.group(3)
               asciiFirstLetter = list(firstLetter.encode('ascii'))
               asciiSecondLetter = list(lastLetter.encode('ascii'))

               allLetters = range_char(firstLetter, lastLetter)
               cleanValue = cleanValue.replace(rlObject.group(0), allLetters)
               #print(cleanValue)

            #IF IT WAS TOLD THEN...
            convertedValueArray = []
            index = 0

            for c in cleanValue:


                if (c in validOperators or len(cleanValue) - 1 == index or cleanValue[index + 1] in validOperators):
                    convertedValueArray.append(c)
                else:
                    convertedValueArray.append(c)
                    convertedValueArray.append('|')

                #manual index 
                index += 1

   
            convertedValue = ''.join(convertedValueArray)

            if (vocal == 'sign'):
              print('HERE COMES A NEW')
              print(vocal, convertedValue)




            listCharactersTokens.append([vocal, convertedValue])

        
    elif('KEYWORDS' in typeToken):

        for t in tokens:

            vocal, value = t.replace(' ', '').split('=')
            cleanValue = value.replace('"', '').replace('.', '')
            reservedWords.append([vocal, cleanValue])

    elif('TOKENS' in typeToken):
        #we will add to the tokens list and then clean the ones that are not here
        for t in tokens:
            if (t != '' and '=' in t):
                vocal, value = t.replace(' ', '').split('=', 1)
                cleanValue = value.replace('"', '').replace('.', '').replace('{', '(').replace('}', ')*').replace('[','(').replace(']', ')?')

                cleanValue = replaceWithAlreadyTokens(listCharactersTokens, cleanValue)
                
                #if there is sum in there
                cleanValue = cleanValue.replace('EXCEPTKEYWORDS', '')
            
                if ('+' in cleanValue and vocal == 'hexnumber' and cleanValue == None):
                    newCleanValue = cleanValue.split('+')

                    newCleanValueModified = []
                    for part in newCleanValue:
                        partChanged = '(' + part + ')'
                        newCleanValueModified.append(partChanged)

                    
                    cleanValue = ''.join(newCleanValueModified)
            
           

                listRealTokens.append([vocal, cleanValue])

        #now we clean the tokens that are

#some last changes to the real list of tokens
def getSecondValue(a):
    
    return a[1].replace('EXCEPTKEYWORDS', '')

arrayTokensWithoutVocal =  list(map(getSecondValue, listRealTokens ))
arrayAFNs = list(map(thompson, arrayTokensWithoutVocal))
theAFN = joinArrayAFNs(arrayAFNs)

#now we will create the file, we will use 
f = open('program.py', "w")

#default text
defaultText = """from re import A
from cocol_functions import getCocolTokens
from nfa import *
from dfa import *
from sub import *
from thombson import *
from scanner import *

#some last changes to the real list of tokens
def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')

arrayTokens = {}
arrayTokensWithoutVocal =  list(map(getSecondValue, arrayTokens ))
arrayAFNs = list(map(thompson, arrayTokensWithoutVocal))
theAFN = joinArrayAFNs(arrayAFNs)

reservedWords = {}


with open('Archivo.txt') as f:
    lines = f.read()

    findFirst(lines, [], "", theAFN, reservedWords, arrayTokens)
    
    

""".format(listRealTokens,reservedWords)

f.write(defaultText)



#print(listRealTokens)
#print(reservedWords)
#now we will create our afn
