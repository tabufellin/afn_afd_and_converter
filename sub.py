from common import *
from af import *

def subconjuntos(afn):

    #initial declaration of variables
    deterministicStates = [e_closure(afn.start, afn.trans)]
    deterministicTrans = []
    deterministicFinals = []

    #we will analyze the ones already procceced
    for state in deterministicStates:
        for sign in afn.sigma:
  
            #from where can i go right now to all possibles routes
            u = e_closure(possible_ends(state,sign,afn.trans),afn.trans)
            
            flag = True

            #here we will make a check that determines if 
            # we will make changes also in the Finals values
            for s in deterministicStates:
                if(set(u) == set(s)):
                    flag = False
                    index = deterministicStates.index(s)
            
            indexInState = str(deterministicStates.index(state))
            sizeState = str(len(deterministicStates))
            if(flag):
                
                deterministicStates.append(u)
                for value in u:
                    #in the case the length of the states is 
                    # not in the deterministic final states and value is not in finals
                    if ((value in afn.finals) and (sizeState not in deterministicFinals)):
                        deterministicFinals.append(sizeState)

                
                deterministicTrans.append([indexInState, sign, sizeState])
            else:
                deterministicTrans.append([indexInState, sign, str(index)])
    
    finalStates = []
    for i in range(len(deterministicStates)):
        finalStates.append(str(i))
    
    #initial state will always be "0"
    return(af(finalStates,afn.sigma,deterministicTrans,["0"],deterministicFinals))


'''
testAFN = af(["0","1","2","3","4","5","6","7","8","9","10"], ["a","b"], [
    ["0","E","1"],
    ["0","E","7"],
    ["1","E","2"],
    ["1","E","4"],
    ["2","a","3"],
    ["3","E","6"],
    ["4","b","5"],
    ["5","E","6"],
    ["6","E","1"],
    ["6","E","7"],
    ["7","a","8"],
    ["8","b","9"],
    ["9","b","10"],
    ], ["0"], ["10"])

result = subconjuntos(testAFN)

print(result.states)
print(result.sigma)
print(result.trans)
print(result.start)
print(result.finals)

graph_machine(result, "graphAFN")
'''
