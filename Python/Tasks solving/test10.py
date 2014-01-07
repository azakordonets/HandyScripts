import sys
 
def parse_options():
	'''
	Parse options and make list of parsed options
	available to program
	'''
	args = args[0]
	options = {} # this should be variable to output data
	get_value = lambda a,x: a[a.index(x)+1] # write lambda expression to get value of option
	is_option = lambda x : x[:2] == "--" # write lambda expression to check option is start with --
	is_next_value = ... # write lambra expression to check if next value after option is not option again
	
	if args:
		for option in args:	
			# write code to handle options
			# check each option
			# check next value after option
			# if all is right then add option to 'options' variable
			# make sure you handle situation when no args are passed
			# or if invalid opiton are passed then it should be ignored
 
	return options
 
def main():
	args = parse_options(sys.argv[1:])
	print args
 
if __name__ == "__main__":
    main()