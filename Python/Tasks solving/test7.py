import sys, os
 
def main():
	argv = sys.argv[1:]
	#if not arguments passed
	if not argv:
		print "No arguments given"

	argv = ["1", "2", "4", "5", "7", "2", "45", "2", "3", "50"]
	filtered = filter(lambda x: x.isdigit(),argv)
	mapped = map(int,filtered)
	print sorted(mapped)[-2:]
	print sorted(map(int,filter(lambda x: x.isdigit(),argv)))[-2:]
 
if __name__ == '__main__':
	main()