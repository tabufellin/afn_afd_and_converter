
from ast import Try
from lib2to3.pgen2.tokenize import tokenize
from re import A
from telnetlib import NEW_ENVIRON
from cocol_functions import getCocolTokens
from nfa import *
from dfa import *
from sub import *
from thombson import *

#some last changes to the real list of tokens
def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')


reservedWords = [['while', 'while'], ['do', 'do'], ['if', 'if'], ['switch', 'switch']]
["abscjsdkfljsdl jdflksdjf lsdjf lsdjf lsdkj "]

def findFirst(lines, arr , lastWord, theAFN, reservedWords, tokensNames ):
    #print(lines)
    #print(arr)
    #print(lastWord)

    newArray = arr
    c = lines[0]
 
    #first we will join last word and the character we are going for
    newValue = lastWord + c 

    
    #Check if new generated word is reserved

    isReserved = False
    for rw in reservedWords:
        if (rw[1] == newValue):
            
            
            isReserved = True

            newArray.pop()
            newArray.append(newValue)
            if (len(lines) == 1):
                
                arrayTokens = []
                for value in newArray:
                    tokenizer = compile_nfa(theAFN,value)
                    arrayTokens.append(tokensNames[tokenizer[1]][0])
                
                print(arrayTokens)
                #print (' '.join(arrayTokens))
                
                return [lines, newArray, ""]
            else:
                

                #print('RESERVED WORD FOUND')
                #print(lines[1:], newArray, newValue)

                findFirst(lines[1:], newArray, newValue, theAFN)


    #isReserved = False #temporaly 
    #if its not reserved we will check if its a token         
    if (isReserved != True):
        token = compile_nfa(theAFN, newValue)
        #if it is a token
        if (token[0] == True):
            #print('ENTER HERE')
            #print('FOUND ONE TOKEN')
            #print(newValue, newArray)
            if(len(newArray) > 0 and lastWord != ""):
                newArray.pop()
            newArray.append(newValue)      
            if (len(lines) == 1 ):
                arrayTokens = []
                for value in newArray:
                    tokenizer = compile_nfa(theAFN,value)
                    arrayTokens.append(tokensNames[tokenizer[1]][0])
                
                #print (' '.join(arrayTokens))
                print(arrayTokens)

                return [lines, newArray, ""]
                
            else:  

                findFirst(lines[1:], newArray, newValue, theAFN, reservedWords, tokensNames)
        else:
            #if doesnt find token that means
            
   
            if (len(lines) == 1):
                arrayTokens = []
                for value in newArray:
                    tokenizer = compile_nfa(theAFN,value)
                    
                    arrayTokens.append(tokensNames[tokenizer[1]][0])

                

                #print (' '.join(arrayTokens))
                print(arrayTokens)

                return [lines, newArray, ""]
            else:
                findFirst(lines[1:], arr, "", theAFN, reservedWords, tokensNames)





#findFirst("if HOLA QUE tal while", [], "")


