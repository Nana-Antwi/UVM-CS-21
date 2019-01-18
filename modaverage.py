#design a program that read a numbers in a file and sum it up

#define function
def main():

	#varaibles
	count = 0
	total = 0

    #exceptions 
	try:


	#open inputfile
		myfile = open(r'C:\Users\nana_sinatra\Desktop\numbers.txt', "r")

	#average valkue of the numbers
		for line in myfile:
		try:

			total += int(line)
			count += 1
        
        #validation of tthe exception
		except ValueError
		print('line, is invalid')
		
		except IOError
		print('invalid file')

		#display results
	else:
		print('average', total/count)

		#close
		myfile.close()

main()