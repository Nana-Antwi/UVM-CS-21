#project 
#all hands on deck
#musicdatabase.py

#Design a program that prompt users to create account of a collection of information to be stored and returned.

#define main function
def main():

	#output statements 
	print('The Music Legend Program')

	#user prompt input statements 
	user_prompt = input('Do you wish to create a music legend database account: yes/no')

	#condition loop statments
	if user_prompt == 'yes':
		print('Welcome to Music Legend')
		print('Follow the steps to create your account')
		print('Fill out with correct information')


		#account creation
		username = input('Enter the name you wish to use as username for your account:')
		print('Your username for this account is:', username)
		print('Thanks creating an account')


		#open the file to write information to
		myfile = open(username+'.txt', 'a')


		#assign user file
		userfile = myfile

		#open user file
		userfile = open(myfile, 'r') 

		#log information 
		logname = input('Enter your username:')


		#condition loop a for log in information 
		if logname == userfile:
			userinfo = userfile.read()
			print(userinfo)



			#Input prompt
			input_prompt = input('Do you wish to add information to your music legend database yes/no: ')

			#condtion loop state aoff adding new  information.
			if input_prompt == "yes":
				print('Add new information to your account')


				#open the user file for information to be written too
				infile = open(userfile, 'a')


				#data base question to ask.
				artist = input("Enter the name of your favorite artist: ")
				genre = input("Enter the genre of music he performs: ")
				albums = input('Enter the number of albums in his credit: ')
				song = input('Enter your favorite song all time by your favorite artist: ')
				quality = input('In a word describe your favorite artist: ')



				#write all user input information top the users account file.
				infile.write(artist)
				infile.write(genre)
				infile.write(albums)
				infile.write(song)
				infile.write(quality)


				#close file after adding new information 
				infile.close()


				#Display all user information in account
				print('Your data saved to your account is:')

				#open user file to read and display information
				accountinfo = open(infile, 'r')
				info = accountinfo.read()
				print(info)

				#program ends
				print('This all the information on your music legend account:')
				print('Program has completed its task re-run to use program again')


			
				





		#validation of condition loop for log in information
		elif logname != userfile:
			print('Your enter the worng username: ')

			#re log in agian 
			logname = input('Enter your username:')
		else:
			print('Program Error multiple entries of worng username')










	#if no on userprompt
	elif user_prompt == 'no':
		print('Music Legend program is closed')
main()
