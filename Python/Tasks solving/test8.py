def Denary2Binary(list):
    '''convert denary integer n to binary string bStr'''
    result = []
    bStr = ''
    for n in list:
    	print "n is %s" %n
    	if n < 0:  raise ValueError, "must be a positive integer"
    	if n == 0: return '0'
    	while n > 0:
    		bStr = str(n % 2) + bStr
    		n = n >> 1
	print "bStr is %s" %bStr
	result.append(bStr)
	bStr = ''
	print result
	return result[0],result[1]

def checkio(data):
    a,b = Denary2Binary(data)
    difference = abs(len(a)-len(b)) 
    return a,b

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([117, 17]) == 3, "First example"
    # assert checkio([1, 2]) == 2, "Second example"
    # assert checkio([16, 15]) == 5, "Third example"
    list = 'CN IN AP VN AE SA RU BM VI IR MS A2 BS NC DM MY NP ID PK TK BD BZ EG TZ ZM CI SD MW AO GA ML BJ MG TD BW LY CV MZ GM LS MU CG BF SL SO ZW CD NE CF GN LR SC MA CM DZ RW MR NA KM SZ TG RE GQ TN PL SI EU AF BN ME NO TJ GE BY IQ AM LB MD FI OM KZ BA KW AX AL AG MK SM RS FK BH UZ AZ MC HT GU JM UM FM KY AN YE VG SY GD GT BB TT BV MH CK GI A1 WS KN FJ MP PW QA JO LK AS TC VC LC MO MN VA LA AW GY SR PG IM HR KP AI PM GP MF BI KG TM GG MM BT LI FO PS ET MQ JE AD AQ IO GL GW ER VU MV WF PF CU TO TL ST GF SB TV KI NU NF NR YT PN'.split(' ')
    print 'hello '+ str(len(list))
