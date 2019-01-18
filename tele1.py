#Assignment 9
#telephonenumnber.py


#design a program that allows users to enter a alphanumeric telephone numbers to be returned all numeric.


#def main function
def main():

	#user prompt input statement
	user_input = input('Enter a 10-character telephone number in this format 800-XXX-XXXX\n')
	print('Your ten character telephone number is:',user_input)

	#declare varaibles
	phone_key = {2:'A,B,C', 3:'D,E,F', 4:'G,H,I', 5:'J,K,L', 6:'M,N,O', 7:'P,Q,R,S', 8:'T,U,V', 9:'W,X,Y,Z'}
	phonenumber = ''



	
	#condition loop statements
	for ch in user_input:
		if ch == 'A' or ch == 'B' or ch == 'C':
			ch = '2'
		elif ch == 'D' or ch == 'E' or ch == 'F':
			ch == '3'
		elif ch == 'G' or ch == 'H' or ch == 'I':
			ch = '4'
		elif ch == 'J' or ch == 'K' or ch == 'L':
			ch = '5'
		elif ch == 'M' or ch == 'N' or ch == 'O':
			ch = '6'
		elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
			ch = '7'
		elif ch == 'T' or ch == 'U' or ch == 'V':
			ch = '8'
		elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
			ch = '9'


			#validation
			phonenumber = phonenumber + ch

			#display results
			print('Your ten digit telepohone number is:',phonenumber)
main()



		
