from re import A
from cocol_functions import getCocolTokens
from nfa import *
from dfa import *
from sub import *
from thombson import *
from scanner import *

#some last changes to the real list of tokens
def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')

arrayTokens = [['ident', '(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)((A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)|(0|1|2|3|4|5|6|7|8|9))*'], ['number', '(0|1|2|3|4|5|6|7|8|9)((0|1|2|3|4|5|6|7|8|9))*']]
arrayTokensWithoutVocal =  list(map(getSecondValue, arrayTokens ))
arrayAFNs = list(map(thompson, arrayTokensWithoutVocal))
theAFN = joinArrayAFNs(arrayAFNs)

reservedWords = [['while', 'while'], ['do', 'do'], ['if', 'if'], ['switch', 'switch']]


with open('Archivo3.ATG') as f:
    lines = f.read()

    findFirst(lines, [], "", theAFN, reservedWords, arrayTokens)
    
    

