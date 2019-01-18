#Nana Antwi
#CS 21
#assignment 10
#sets.py

#design a program that compares two input files as sets.

#define main function
def main():



	#open files and convert them to sets 
	myset_1 = set(line.strip() for line in open('number1.txt', 'r'))
	myset_2= set(line.strip() for line in open('number2.txt', 'r'))

	#display all contents
	file_1 = len(myset_1)
	file_2 = len(myset_2)
	print('The total number of contents in both set:')
	print('Set one has: ', file_1)
	print('Set two has: ', file_2)

	#display set
	print('Sets are the  unique elements they contain')
	print('set one',myset_1)
	print('set two',myset_2)
	

	#disply intersection
	inter = myset_1.intersection(myset_2)
	print('Elements that can be found in both files are:')
	print(inter)

	#display difference betwwen the files
	diffe = myset_1.difference(myset_2)
	diffe_1 = myset_2.difference(myset_1)
	print('Elements that are unique to their set are:')
	print('The difference between set one and set two: ', diffe)
	print('The difference between set two and set one:', diffe_1)

	#display all the union
	union_1 = myset_1.union(myset_2)
	print('The union of both sets with all elements:')
	print('The union set:', union_1)

	#display unique elements
	super_set = myset_1.symmetric_difference(myset_2)
	print('Unique elements of both:', super_set)

	
	

#recall main function
main()
