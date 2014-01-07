import string
import re

def count_words(text):
		words_ar = text.split(" ")
		words = 0
		for el in words_ar: 
			el = unicode(el)
			if not el.isnumeric():
				words +=1
		return words

def main():
	# text = raw_input("Please type yor text: ")
	text = "Hello Joe. How are you doing? My name is Andrew and i'm 27 years old. I was born on 9th December 1985"
	
	#example of count of big letters
	big_letters_amount = []
	for char in text:
		if char >= "A" and char <= "Z":
			big_letters_amount.append(char)

	print "amount of big letters in text is %s" % len(big_letters_amount)
	
	sentences = len(re.findall('[!?.;]',text)) #write code here
	words = count_words(text)
	numbers = len(re.findall('\d',text)) #write code here
 
	print "numbers: %s, words: %s, sentences: %s" % (numbers, words, sentences)
 
if __name__ == '__main__':
	main()