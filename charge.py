#Nana Antwi
#CS 21 
#Assignment 8
#charge_acc.py


#Design a program that prompts a user for an account number which it evalutes to identify if is part of a list of accounts


#declare varaibles
myfile = 0
charge_account = 0
i = 0
search_myfile = 0

#define function
def main():
		
	#user prompt input statements
	search_myfile = (raw_input('Enter your charge account number: '))

	#exception loops statements
	try:
	


		#open and read input file
		myfile = open('charge_accounts.txt', 'r')


		#read contains of the input file to a list
		charge_account = myfile.readlines()


		#Changing the contains into a list
		i = 0
		while i != len(charge_account):
			charge_account[i] = (int[charge_account])
			i += 1



			#display the converted list
			print(charge_account)

				#condition loop statements
                        while search_myfile == charge_account
                                print('Your charge account number is valid!')


                        else:
                                print('Your charge account number is invalid!')

	#revalidation of condition loop
		else:



			#close input file
			myfile.close()

	except IOError:
		print('Program Error')

#re call main function
main()






