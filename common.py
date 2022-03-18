import graphviz

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

    #declare initial response
    response = []

    for t in trans:
        transState, transSign, transFinalState  = t[0], t[1], t[2]
        if (
            (transState in states) and  
            (transSign == sign) and 
            (transFinalState not in response)  
        ):
            response.append(transFinalState)
    return response


'''
@e_closure

does the same as move but the main difference
is that it will jump between epsilons and give the next
state that jumps until it stop finding epsilons
'''
def e_closure(states, trans):

    #automatically copy the initial state 
    response = states

    sign = "E"

    for t in trans:
        transInitialState, transSign = t[0], t[1]
        if(transSign == sign and transInitialState in response):
            response2 = possible_ends(t, sign, trans)
            response = list(set(response + response2))


    return response


def graph_machine(df, filename):
    f = graphviz.Digraph('machine', filename=filename)
    f.attr(rankdir='LR', size='20')

    f.attr('node', shape='doublecircle')
    for i in df.finals:
        print(i)
        f.node(i)

    f.attr('node', shape='circle')
    for i in df.trans:
        f.edge(i[0], i[2], label=i[1])

    f.view()