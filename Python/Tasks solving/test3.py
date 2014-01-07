# def main():
# 	text = raw_input("Please type yor text: ")
	
# 	#example of count of big letters
# 	big_letters_amount = []
# 	for char in text:
# 		if char >= "A" and char <= "Z":
# 			big_letters_amount.append(char)
	
# 	print "amount of big letters in text is %s" % len(big_letters_amount)
	
# 	sentences = 0 #write code here
# 	words = 0 #write code here
# 	numbers = 0 #write code here
 
# 	print "numbers: %s, words: %s, sentences: %s" % (numbers, words, sentences)
 
# if __name__ == '__main__':
# 	main()

# input = raw_input()


def define_value(array):
	for el in array: 
		if el[0].isalnum():
			return float(el)

def define_currency(array):
	for el in array: 
		if el == "USD":
			return el
			break
		if el == "EUR":
			return el
			break

def convert_value(x,currency):
	result = 0
	if currency == 'USD':
		result =  float(x*1.21)
		currency = "EUR"
	if currency == 'EUR':
		result =  float(x*0.81)
		currency = 'USD'
	else:
		print "Wrong currency"
		return 0
	leftover = round(float(result%1)*100,2)
	if leftover !=0.0:
		return "Result is %s %s %s cents" %(int(result),currency,int(leftover))
	else: 
		return "Result is %s %s " %(int(result),currency) 

def main():
	# input = raw_input("Please enter number and currency\n")
	input = "100 EUR"
	values_dict = input.split(" ")
	print convert_value(define_value(values_dict),define_currency(values_dict))
# 2857.1
print float((28571 * 100.0)/1000)


if __name__ == "__main__":
	main()



