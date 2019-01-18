#Nana Antwi
#CS 21
#assignment 9
#charateranalysis.py


#design a program that reads the contents of a file and display contents of the file.

#define main fuction
def main():

	#user prompt input statement
	read_file = input('Enter the filename you wish to display its contents:')

	#open an input file
	inputfile = open(read_file,'r')

	#read contents of inputfile
	inputfile = inputfile.readlines()

	#declare variables
	num_upper_count = 0
	num_lower_count = 0
	num_digit_count = 0
	num_space_count = 0

	#for loop iteration 
	for lines in inputfile:

		#condition loop statements
		for ch in lines:
			if ch.isupper():
				num_upper_count += 1
			elif ch.islower():
				num_lower_count += 1
			elif ch.isdigit():
				num_digit_count += 1
			elif ch.isspace():
				num_space_count += 1

	#display results
	print('The number of upper case letters in the file:',num_upper_count)
	print('The number of lower case letters in the file:', num_lower_count)
	print('The number of digits in the file:',num_digit_count)
	print('The number of white space:',num_space_count)

#recall main function
main()


