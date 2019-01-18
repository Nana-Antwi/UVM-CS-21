#Nana Antwi
#CS 21
#Assignment 8
#charge_acc.py


#Design a program that prompts a user for an account number which it evalutes

#declare variables
myfile = 0.0
charge_account = 0.0
i = 0
search_myfile = 0.0


#define function
def main():
    #exception loops statments
    try:
    
        #open and read input file
        myfile = open('charge_accounts.txt', 'r')

        #user prompt input statement
        search_myfile = (input('Enter your charge account number: '))

        #read contents of input file to a list
        charge_account = myfile.readlines()

        #changing the contains into a list
        i = 0
        while 1 != len(charge_account):
            charge_account[i] == int(charge_account[i])
            i += 1

            #display converted list
            print(charge_account)

            #prompt user again for input statement
            search_myfile = (input('Enter your charge account number: '))

            #condition loop statements
            if search_myfile == charge_account:
                print('Your charge account number is valid!')

            else:
                print('Your charge account number is invalid!')


                #revalidiation of condition loop
        


            #close input file
            myfile.close()
    except IOError:
        print('Program Error')
    
   
#recall main fuction
main()
        
