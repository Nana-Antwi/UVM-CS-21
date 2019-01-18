#a program that read a file and prints its contents out

#define function.
def main():

	#opening the input file
	myfile = open(r'c:\Users\nana_sinatra\Desktop\alphabet.txt', 'r')

	#print the information 
	for line in myfile:
		line = line.rstrip('\n')
		print(line)


		
main()
#close file
myfile.close()
