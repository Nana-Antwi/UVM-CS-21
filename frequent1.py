#Nana Antwi
#CS 21
#assignment 9
#frequencycharacter.py

#design a program that display the most frequent appearing characters in a string that has been inputed by the user.

#define main function
def main():


	#user prompt input statement
	user_string = input('Enter a string:')

	#input string is converted into set
	charset = set(user_string)

	#decalre varaibles 
	maxcount = 0
	maxch = 0
	chcount = 0

	#for loop iteration over condition statement
	for ch in charset:
		 chcount = user_string.count(ch)
		 #condition loop statments
		 if chcount > maxcount:
		 	maxcount = chcount
		 	maxch = ch
    #display result
	print('frequent characters:', maxch, maxcount)

#recall main function
main()

			



