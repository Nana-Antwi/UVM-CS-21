#Nana Antwi
#CS 21 
#Assignment 7
#linenumber.py
#design a program that read an input file and create and out file

#define funtion
def main ():

	#user prompt 
	fil_creat = input('Enter a file name: sampleprogram.py')
	if fil_creat == 'sampleprogram.py':
		inputfile = open('sampleprogram.txt', 'r')
	else:
		print('Invalid response')
		while fil_creat == 'sampleproram.py':
			ln_sampleprogram == inputfile
			ln_sampleprogram.wirte(inputfile)

			#closefile
			inputfile.close()
			print('File write form sampleprogram text to ln_sampleprogram text is complete')
main()			
