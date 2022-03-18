from common import *


'''
@compile_dfa

This functions give the result of a simulation of a dfa
given an dfa and a string. If returns true it means that
the string is correct and viceversa.

'''
def compile_dfa(dfa, string):

    #get start values
    s = dfa.start

    #iterate in string based on beginning 
    #and given trans
    for sign in string:
        s = possible_ends(s, sign, dfa.trans)

    contained = [a in s for a in dfa.finals]
    for value in contained:
        if (value):
            return True
    '''
    if s[0] in dfa.finals:
        print('time to get out')
        print(s)
        return True
    '''
    return False

