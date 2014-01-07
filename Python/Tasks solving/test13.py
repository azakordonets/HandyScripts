#Your code here
#You can import some modules or create additional functions


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    template = data[0]
    grille = data[1]
    result = ""
    for i in range(0, 4):
        indexes = []
        for elIndex, el in enumerate(template):
            for index, value in enumerate(el):
                # print "%s %s" %(index,value)
                if value == "X":
                    indexes.append((elIndex, index))
        for i, j in indexes:
            result += grille[i][j]
        template = zip(*template[::-1])
    return result

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        ['X...',
         '..X.',
         'X..X',
         '....'],
        ['itdf',
         'gdce',
         'aton',
         'qrdi']]) == 'icantforgetiddqd', 'First example'

    assert checkio([
        ['....',
         'X..X',
         '.X..',
         '...X'],
        ['xhwc',
         'rsqx',
         'xqzz',
         'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'
