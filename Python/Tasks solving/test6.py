import sys, os
 
def main():
	argv = sys.argv[1:]
	#if not arguments passed
	if not argv:
		print "No arguments given"
	
	output = []
	for option in argv:
		if os.path.exists(option):
			if os.path.isdir(option):
				exist = "folder exist"
			else:
				exist = "path is correct, but it's a file" 
			
		else : 
			exist = "folder doesn't exist"
		output.append([option, exist])
	for i,output in enumerate(output):
		print "%d %s\t %s" %  (i, output[0], output[1])
 
if __name__ == '__main__':
	main()