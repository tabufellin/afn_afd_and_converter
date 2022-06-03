def getCocolTokens():

    with open('Aritmetica.txt') as f:
        lines = f.read().splitlines()
        bigWords = []
        end = 0
        i = 0
        for line in lines:
        
            if line == line.upper() and "(." not in line and ".)" not in line and line != '':
                bigWords.append([line, i])
            
            
            i += 1
            if ('END' in line):
                end = i
        i = 0
 
        cocolTokens = []
        for word in bigWords:
        
            if (len(bigWords) != i + 1):
                fromWhere = word[1]
                toWhere = bigWords[i+1][1]

                listOfLines = lines[fromWhere + 1 : toWhere]
                cleanListOfLines = list(filter(lambda x: x != "", listOfLines))
                cocolTokens.append([word[0], cleanListOfLines])
                #print(fromWhere, toWhere)
                i += 1
            else:
                fromWhere = word[1]
                toWhere = end - 1
                listOfLines = lines[fromWhere + 1 : toWhere]
                cleanListOfLines = list(filter(lambda x: x != "", listOfLines))
                cocolTokens.append([word[0], cleanListOfLines])

        return cocolTokens

