#project 
#all hands on deck
#musicdatabase.py

#Design a program that prompt users to create account of a collection of information to be stored and returned.

#define main function
def main():

        #output statements 
        print('The Music Legend Program!')

        #user prompt input statements 
        user_prompt = input('Do you wish to create a music legend database account yes/no: ')

        #condition loop statments
        if user_prompt == 'yes':
                print('Welcome to Music Legend!!!')
                print('Follow the steps to create your account.')
                print('Fill out with the correct information.')


                #account creation
                username = input('Enter the name you wish to use as username for your account:')
                print('Your username for this account is:', username)
                print('Thank you for creating an account.')


                #open the file to write information to
                myfile = open(username+'.txt', 'a')

                #Input prompt
                input_prompt = input('Do you wish to add information to your music legend database yes/no: ')

                #condtion loop state aoff adding new  information.
                if input_prompt == "yes":
                        print('Add information to your account')



                        #data base question to ask.
                        artist = input("Enter the name of your favorite artist: ")
                        genre = input("Enter the genre of music he performs: ")
                        albums = input('Enter the number of albums in his credit: ')
                        song = input('Enter your favorite song all time by your favorite artist: ')
                        quality = input('In a word describe your favorite artist: ')


                        #write database information to a file
                        myfile.write('artist:'+artist)
                        myfile.write('genre:'+genre+"\n")
                        myfile.write('albums:'+albums+"\n")
                        myfile.write('song:'+song+"\n")
                        myfile.write('quality:'+quality+"\n")





                        #Display all user information in account
                        print('You have successfully logged out of your account')
                        print('Your data saved to your account is:')

                        #display save information
                        print('Your information saved:')
                        print('Favorite artist:', artist)
                        print('Genre of music:', genre)
                        print('Number of albums:', albums)
                        print('Favorite song:', song)
                        print('Artist quality:', quality)
                        print('The above is all the data save on your music legeng account.')



                        #option of logging back or just quiting to save 
                        log_prompt = input('Do you wish to log back into your music legened account yes/no: ')


                        #codition loop 
                        if log_prompt == 'yes':
                                print('You have logged back into your account!')

                                #if yes 
                                add_prompt = input('Do you wish to to enter new information yes/no: ')
                                if add_prompt == 'yes':

                                        print('Add new information!')

                                        #add new information to work
                                        artist2 = input("Enter the name of another favorite artist: ")
                                        genre2 = input("Enter the genre of music he performs: ")
                                        albums2 = input('Enter the number of albums in his credit: ')
                                        song2 = input('Enter your favorite song all time by your favorite artist: ')
                                        quality2 = input('In a word describe your favorite artist: ')


                                        #write to file
                                        myfile.write('artist2:'+artist2+"\n")
                                        myfile.write('genre2:'+genre2+"\n")
                                        myfile.write('album2:'+albums2+"\n")
                                        myfile.write('song2:'+song2+"\n")
                                        myfile.write('quality2:'+quality2+"\n")

                                        #display new information
                                        print('New information has been successfully added:')
                                        print('The new added information:')

                                        #display new saved information
                                        print('Your information saved:')
                                        print('Second Favorite artist:', artist2)
                                        print('Genre of music:', genre2)
                                        print('Number of albums:', albums2)
                                        print('Favorite song:', song2)
                                        print('Artist quality:', quality2)
                                        print('The above is all the data save on your music legend account.')


                                        #all information on your account
                                        print('All the data information saved on your music legend account are:')

                                        #userdatabase
                                        print('Your total information saved:')
                                        print('first entry:')
                                        print('Favorite artist:', artist)
                                        print('Genre of music:', genre)
                                        print('Number of albums:', albums)
                                        print('Favorite song:', song)
                                        print('Artist quality:', quality)
                                        print('Second entry:')
                                        print('Second Favorite artist:', artist2)
                                        print('Genre of music:', genre2)
                                        print('Number of albums:', albums2)
                                        print('Favorite song:', song2)
                                        print('Artist quality:', quality2)
                                        print('The above is all information assocaited with your account')
                                        print('Log back in to allow database to process')


                                        #close file
                                        myfile.close()


                                #valdiation for second enrty
                                elif add_prompt == 'no':
                                        print('Thanks for using music legend')
                                        print('Music Legend has ended!')



                        #validation of codition
                        elif log_prompt == 'no':
                                print('You have successfully logged out!')
                                print('Music legend program has ended')

                    
                                    

	                    #prompt again to re-enter user name
	                    logname = input('Enter your username with (.txt): ')
	            

	                    #open save text
	                    account_file = open(logname, 'r')


	                            #condition loop to validate log information
	                            
	                    #read and output contents to program
	                    for line in account_file:
	                            print(line)


	                    #close file
	                    account_file.close()


	                    #open file
	                    user_file = open(logname, 'r')

	                    #search for an entry
	                    search = input('Do you wish to search for information in the database yes/no: ')

	                    #condition loop
	                    if search == 'yes':
	                            print('Database Search')
	                            print('To search for information in entry one the input format should be: (artist).')
	                            print('To search for information in entry two the input format should be: (artist2.')


	                            #user prompt input.
	                            search_entry = input('Enter the entry you wish to search for example (artist) or (artist2): ')

	                            #convert file into dictionary
	                            search_dict = {}
	                            for line in user_file:
	                                    spiltline = line.spilt(':')
	                                    search_dict[spiltline[0]] = spiltline[1]
	                                    print(search_dict[search_entry])

	                    #validation of codition loop
	                    elif search == 'no':
	                            print('No database search')
	                            print('Goodbye!')


	                            #close open input file
	                            user_file.close()


	                    #delete entry
	                    delete = input('Do you wish to delete your database yes/no: ')

	                    #conditon loop statement 
	                    if delete == 'yes':
	                            os.remove(user_file)
	                            print('Your Music Legend account has being deleted.')
	                            print('Thanks for being a valued user of the Music Legend!')

	                    elif delete == 'no':
	                            print('Your database was not deleted.')
	                            print('Your are still an authorized user of the Music Legend program.')

	                    #final display
	                    print('Music legend has finsehed all excutions')

	    #if no on userprompt
	    elif user_prompt == 'no':
	            print('Music Legend program is closed')
main()






































 



