from nfa import compile_nfa
from thombson_m import *
from af import *

def thompson(er):
    afnList = []
    mainAFN = af([], [], [], [], [])

    getSigma(er, mainAFN)
    createLeafs(er, afnList)
    if ("." not in er):
        newEr = replaceConcat(er)
    else:
        newEr = er
    newEr = inToPos(newEr)
    afnCont = 0
    afnStack = []

    for i in newEr:
        if (i not in op):
            afnStack.append(afnList[afnCont])
            afnCont += 1
        else:
            if(i == "*"):
                afn = kleene(afnStack.pop())
                afnStack.append(afn)

            elif(i == "+"):
                afn = plus(afnStack.pop())
                afnStack.append(afn)

            elif(i == "."):
                afn2 = afnStack.pop()
                afn1 = afnStack.pop()

                afn = concat(afn1,afn2)
                afnStack.append(afn)

            elif(i == "|"):
                afn2 = afnStack.pop()
                afn1 = afnStack.pop()

                afn = opor(afn1,afn2)
                afnStack.append(afn)
            elif(i == "?"):
                afn = option(afnStack.pop())
                afnStack.append(afn)

    return afnStack[0]

      
def joinArrayAFNs (AFNs):
    joinedStates = []
    joinedSigma = []
    joinedAFNtrans = []
    joinedInitialState = 'masterI'
    joinedFinals = []
    
    indexAFNcount = 0
    for afn in AFNs:
        trans = afn.trans
        states = afn.states
        start = afn.start
        sigma = afn.sigma
        finals = afn.finals



        #we will give unique values to the actual values with a index
        #counting the afns used by this moment
        newStates = []
        for sta in states:
            sta = sta + str(indexAFNcount)
    
            newStates.append(sta)
        afn.states = newStates


        #sigma doesnt need to make changes

        #the same with trans
        newTrans = []
        for tra in trans:
            tra[0], tra[2] = tra[0] + str(indexAFNcount), tra[2] + str(indexAFNcount)
            newTrans.append(tra)
        
 

        #start need changes
        newStart = []
        for i in start:
            i = i + str(indexAFNcount)
            newStart.append(i)

          
        newFinals = []
        for i in finals:
            i = i + str(indexAFNcount)
            newFinals.append(i)
  

        #NOW WE WILL ENTER ALL THE NEW VALUES TO THE JOINED

        #add states to joined
        joinedStates.extend(newStates)

        #now add sigma and clear repeated values
        joinedSigma.extend(sigma)
        #clear repeated ones
        joinedSigma =  list(set(joinedSigma))

  
        #then we create the new initial state transition that goes to the afn with epsilon
        newInitialTrans = [joinedInitialState, 'ε', newStart[0]]
        #add it and then add trans of this afn
        joinedAFNtrans.append(newInitialTrans)
        joinedAFNtrans.extend(newTrans)


        #start is already declared, DONT TOUCH IT

        #finals values
        joinedFinals.extend(newFinals)

        #counter for id of afn's ++
        indexAFNcount += 1


    return (af(states= joinedStates, sigma= joinedSigma, trans= joinedAFNtrans, start=[joinedInitialState], finals=joinedFinals))




def getSecondValue(a):
    return a[1].replace('EXCEPTKEYWORDS', '')

arrayTokens = [['ident', '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z+(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)+(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z))((a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z+(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)+(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z))|(0|1|2|3|4|5|6|7|8|9))*EXCEPTKEYWORDS'], ['hexnumber', '((0|1|2|3|4|5|6|7|8|9)+A|B|C|D|E|F)EXCEPTKEYWORDS']]
arrayTokensWithoutVocal =  list(map(getSecondValue, arrayTokens ))
arrayAFNs = list(map(thompson, arrayTokensWithoutVocal))
theAFN = joinArrayAFNs(arrayAFNs)
print(compile_nfa(theAFN, 'hola'))