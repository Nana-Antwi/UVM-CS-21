#design a program that read a numbers in a file and sum it up

#define function
def main():

	#varaibles
	count = 0
	total = 0

	#open inputfile
	myfile = open(r'C:\Users\nana_sinatra\Desktop\numbers.txt', "r")

	#average valkue of the numbers
	for line in myfile:
		total += int(line)
		count += 1
		print('average', total, count)

		#close
		myfile.close()

main()