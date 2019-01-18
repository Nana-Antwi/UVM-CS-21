#Nana Antw+-i
#CS 21 
#Assignment 8
#baseball.py

#design a program that reads world series champion ship from an inputfile and display the results

#decalre my variables 
myfile = 0.0
user_prompt = 0.0
team = 0.0
num_winningseason = 0.0


#define main function
def main():

        #decalre my variables 
        myfile = 0.0
        user_prompt = 0.0
        team = 0.0
        num_winningseason = 0
#exception handling
        try:

                #open and read of inputfile
                myfile = open('WorldSeriesWinners.txt', 'r')

                #user prompt input statement
                user_prompt = str(input('Enter the name of a baseball time: '))

                #reading of contents in inputfile
                team =  myfile.readline()

                #exception loop statement
                

                
                        #condtion loop statements to test
                while team != "":
                        team = team.rstrip("\n")

                                #validtion of condition present
                        if user_prompt == team:
                                num_winningseason += 1
                        team = myfile.readline()
                print(user_prompt, 'in baseball history', num_winningseason, 'winning seasons in the MLB')


                                        
                                

                        
                                
#close inputfile
                myfile.close()
        except IOError:
              print('program error')
#recall main function
main()

