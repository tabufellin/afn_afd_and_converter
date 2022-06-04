from common import *
from af import *

'''
@compile_afn

This functions will simulate an afn given a afn object and a string
it will return true if given string is valid and false if not
'''
def compile_nfa(afn, w):
    s = e_closure(afn.start,afn.trans)
    currentW = ""
    for i in w:
        currentW += i
        s = e_closure(possible_ends(s,i,afn.trans),afn.trans)

    for i in s:
        if i in afn.finals:
            #print(i[-1])
            return [True,int(i[-1])]
    return [False, 10000000]


