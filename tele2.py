#Assignment 9
#telephonenumnber.py


#design a program that allows users to enter a alphanumeric telephone numbers to be returned all numeric.


#def main function
def main():

	#user prompt input statement
	user_input = input('Enter a 10-character telephone number in this format 800-XXX-XXXX\n')
	print('Your ten character telephone number is:',user_input)

	#declare varaibles
	phonenumber = ''
	ch = {'2':'A,B,C', '3':'D,E,F', '4':'G,H,I', '5':'J,K,L', '6':'M,N,O', '7':'P,Q,R,S', '8':'T,U,V', '9':'W,X,Y,Z'}
	



	
	#condition loop statements
	for ch in user_input:
		if ch == 'A':
			ch = '2'
		elif ch == 'B':
			ch = '2'
		elif ch == 'C':
			ch = '2'
		elif ch == 'D':
			ch = '3'
		elif ch == 'E':
			ch = '3'
		elif ch == 'F':
			ch = '3'
		elif ch == 'G':
			ch = '4'
		elif ch == 'H':
			ch = '4'
		elif ch == 'I':
			ch = '4'
		elif ch == 'J':
			ch = '5'
		elif ch == 'K':
			ch = '5'
		elif ch == 'L':
			ch = '5'
		elif ch == 'M':
			ch = '6'
		elif ch == 'N':
			ch = '6'
		elif ch == 'O':
			ch = '6'
		elif ch == 'P':
			ch = '7'
		elif ch == 'Q':
			ch = '7'
		elif ch == 'R':
			ch = '7'
		elif ch == 'S':
			ch = '7'
		elif ch == 'T':
			ch = '8'
		elif ch == 'U':
			ch = '8'
		elif ch == 'V':
			ch = '8'
		elif ch == 'W':
			ch = '9'
		elif ch == 'X':
			ch = '9'
		elif ch == 'Y':
			ch = '9'
		elif ch == 'Z':
			ch = '9'


		#validation
		phonenumber = phonenumber + ch

	#display results
	print('Your ten digit telepohone number is:',phonenumber)
main()



		
