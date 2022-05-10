'''
@possible_ends

give an array of @states 
and a sign and it will give you all possible 
final answers

!!!!
you can think is the same as e_closure but
it will be a better option in the DFA because
it doesnt have any Epsilon value
!!!!

'''
def possible_ends(states, sign, trans):
    response = []
    for i in trans:
        if((i[2] not in response) and (i[1] == sign) and (i[0] in states)):
            response.append(i[2])
    return response


'''
@e_closure

does the same as move but the main difference
is that it will jump between epsilons and give the next
state that jumps until it stop finding epsilons
'''
def e_closure(states, trans):
    response = states.copy()
    added = True
    while (added):
        added = False
        for i in trans:
            if((i[2] not in response) and (i[1] == "ε") and (i[0] in response)):
                response.append(i[2])
                added = True
    return response


def graph_machine(df, filename):
    f = graphviz.Digraph('machine', filename=filename)
    f.attr(rankdir='LR', size='20')

    f.attr('node', shape='doublecircle')
    for i in df.finals:
       
        f.node(i)

    f.attr('node', shape='circle')
    for i in df.trans:
        f.edge(i[0], i[2], label=i[1])

    f.view()