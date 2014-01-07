def checkio(text):
    symbols = {}
    for el in text:
        if el not in symbols:
        	symbols[el] = text.count(el)
    max_value = max(symbols.values())
    result = []
    for key,value in symbols.items():
        if value == max_value:
		    result.append(key)
    print result
    print "sorted %s" %sorted(result)
    # return result
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(u"BBBB cccc aaaa!") == "l", "Hello test"
    # print checkio(u"Hello World!") == "l", "Hello test"
    # assert checkio(u"How do you do?") == "o", "O is most wanted"
    # assert checkio(u"One") == "e", "All letter only once."
