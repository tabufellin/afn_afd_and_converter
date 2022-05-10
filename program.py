from re import A
from cocol_functions import getCocolTokens
from nfa import *
from dfa import *
from sub import *
from thombson import *

#some last changes to the real list of tokens
def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')

arrayTokens = [['ident', '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z+(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)+(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z))((a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z+(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)+(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z))|(0|1|2|3|4|5|6|7|8|9))*EXCEPTKEYWORDS'], ['hexnumber', '((0|1|2|3|4|5|6|7|8|9)+A|B|C|D|E|F)EXCEPTKEYWORDS']]
arrayTokensWithoutVocal =  list(map(getSecondValue, arrayTokens ))
arrayAFNs = list(map(thompson, arrayTokensWithoutVocal))
theAFN = joinArrayAFNs(arrayAFNs)

reservedWords = [['while', 'while'], ['do', 'do']]

flag  = True
while (flag):
    userInputs = input('Give me a value :')
    userInputsArray = userInputs.split(' ')
    tokens = []
    for inputU in userInputsArray:
        isReserved = False
        for rw in reservedWords:
            if (rw[1] == inputU):
                isReserved = True
            
        
        if (isReserved == False):
            token = compile_nfa(theAFN, inputU)
            tokens.append(token)
        else:
            token = ['RESERVED WORD: ', inputU]
            tokens.append(token)

    newStringWithTokens = []
    for token in tokens:
        if (token[0] == 'RESERVED WORD: '):
            newStringWithTokens.append('RESERVED WORD '+token[1]+ ',')
        else:
            newStringWithTokens.append(arrayTokens[token[1]][0])
        #print(arrayTokensWithoutVocal[token[1]])
        
    print(' '.join(newStringWithTokens))

