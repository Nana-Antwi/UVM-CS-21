#Nana Antwi
#CS 21
#Assignment 7
#sampleprogram.py

#design a program that writes an inputfile to an output file

#declare varaiables
count = 0

#define fuction
def main():
	user_prompt = (input("Enter a file name called: "))
	try:
		#read input file
		myfile = open(user_prompt, 'r')
		#write file
		outfile = open('ln_' + user_prompt, 'w')
		count = 0
		for line in myfile:
			count += 1
			outfile.write(str(count)+':'+line)
		#close file
		myfile.close()
	except IOError:
		print("Invalid file name")


		
#recall function
main()