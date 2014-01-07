workers = ["Joel","Ken","Pit"]
salary = ["Joel","Bob","Sam"]
contracts = ["Bob","Ken","Pit"]


main():
	person = raw_input("Please enter persons name")
	if (person not in workers) and (person not in contracts) and (person not in salary):  
		print "Sorry but we don't have this guy in our company"
	if (person in workers) and (person not in contracts) and (person in salary): 
		print "Yes salary to be paid"
	else: 
		print "No he shouldn't be paid salary"


if __name__ == "__main__":
	main()