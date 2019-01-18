#program that display your name 5 times

#define funtion.
def main():

	#open inputfile
	myfile = open(r'c:\Users\nana_sinatra\Desktop\alpha.txt', 'w')

	#use the file
	for i in range(5):
		print('Nana', 'cs')
		myfile.write('Nana'+'cs'+"\n")

		#close file
		myfile.close()