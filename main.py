from nfa import *
from dfa import *
from sub import *
# (a|b)*abb
exampleNFA = af(["0","1","2","3","4","5","6","7","8","9","10"], ["a","b"], [
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
    ["9","E","3"],
    ], ["0"], ["10"])

string = "babbabb"

result = compile_nfa(exampleNFA,string)

print('RESULT OF COMPILE NFA')

print(result)

exampleDFA = af(["1", "2", "3", "4", "5"], ["a", "b"], [
    ["1", "a", "2"],
    ["1", "b", "3"],
    ["2", "a", "2"],
    ["2", "b", "4"],
    ["3", "a", "2"],
    ["3", "b", "3"],
    ["4", "a", "2"],
    ["4", "b", "5"],
    ["5", "a", "2"],
    ["5", "b", "3"]
    ], ["1"], ["5"])

result = compile_dfa(exampleDFA,string)

print('RESULT OF COMPILE DFA')
print(result)



result = subconjuntos(exampleNFA)
print('RESULT OF CONVERTING NFA TO DFA')
print('states:')
print(result.states)
print('sigma:')
print(result.sigma)
print('trans:')
print(result.trans)
print('start:')
print(result.start)
print('finals:')
print(result.finals)


graph_machine(result, "graph")
