#Nana Antwi
#CS 21
#Assignment 8

#Design a program that prompts a user for an account number which it evalutes to identify if is part of a list of accounts



#define main function
def main():

        #declare variables
        myfile = 0.0
        t = 0
        f = 0
        charge_account = 0
        search_myfile = 0


        #user prompt input statement
        search_myfile = (int(input('Enter your charge account number: ')))

        #open and read of file
        myfile = open('charge_accounts.txt', 'r')

        #read contents in the inputfile
        charge_account = myfile.readline()

        #condition present
        t = 0

        #exception condition loops
        try:
        

                #converting contents of inputfile to output
                while charge_account != "":
                        charge_account = charge_account.rstrip("\n")
                        charge_account = int(charge_account)
                
                        


                        #condition loop statements
                        if charge_account == search_myfile:
                                t += 1
                                break
                        else:
                                charge_account = myfile.readline()
                               


                                
                        
                if t >= 1:
                        print('Your charge account', charge_account, 'is valid')
                else:
                        print('Your charge account entry is invalid')
                        
        except IOError:
                print('Program Error')

         

        #close file
        myfile.close()
    
    #recall main function
main()
                
        








