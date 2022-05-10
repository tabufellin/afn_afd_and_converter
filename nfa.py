from common import *
from af import *

'''
@compile_afn

This functions will simulate an afn given a afn object and a string
it will return true if given string is valid and false if not
'''
def compile_nfa(afn, string): 

    #first we will get all possible answers
    #for final state in this afn
    s = e_closure(afn.start,afn.trans)

    #then start going in string
    for i in string:

        #from final state to all possibles states
        #then putting this in e_closure to see all 
        # possibilities from this character  
             
        s = e_closure(possible_ends(s,i,afn.trans),afn.trans)

    print('s')
    print(s)
    #at the end check if your final value was in the final options of the afn
    for i in s:

    
        if i in afn.finals:
            #was found, return true
            return True, int(i[-1])
    
    #if not was find, return false
    return False

