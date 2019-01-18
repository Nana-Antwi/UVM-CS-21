#Nana Antwi
#CS 21
#decode.py
#Assignment 10


#design a program that alllows encrytion and decryption of input files by users

#define main function
def main():
	
	#declare varaible constants
    option = 0
    Encrypt = 1
    Decrypt = 2
    End = 3
    #condtion loop that validates user's option
    while option != End:
        #call menu function
        option = menu()
        #call encrypt function
        if option == Encrypt:
            print(encrypt())
        #call decrypt function
        elif option == Decrypt:
            print(decrypt())
        else:
            pass
    #statement if user quits
    print('Program has ended')

#define menu funtion
def menu():
    #define variable constants
    End = 3
    start = 1
    #menu option for user
    print('Would you like to:')
    print('---------------------------------')
    print('1. Encrypt a file?')
    print('2. Decrypt a file?')
    print('3. End')
    print()
    #condition loop to validate user's input
    exception = True
    while exception == True:
        #exception and error handling of condition
        try:
            option = int(input('Please select an option: '))
            #condtion loop 
            if start <= option <= End:
                #validation of loop
                exception = False
            else:
                print('Please enter a valid number')
        except ValueError:
            print('ERROR')
            print('Not a number')
        #return
    return option

#define encrypt function
def encrypt():
    #open inputfile
    codes = open('codes.txt', 'r')
    #empty dictionary to read information to
    code = {}
    #convertion of inputfile into a dictionary list
    for line in codes:
        (key, value) = line.split()
        code[key] = value
    #close inputfile
    codes.close()
    #exception and error handling with a condition loop
    exception = True
    while exception == True:
        #input file
        file = input('Please enter name of the file you wish to encrypt with (.txt): ')
        #exception and error handing of the for loop
        try:
            #read  opened file
            infile = open(file, 'r')
            #create an output file of encrypted data
            output = open('encrypted_' + file, 'w+')
            #validation of loop
            exception = False
        except FileNotFoundError:
            print('Please enter valid file')
    #condition loop with for to write output file
    for line in infile:
        for letter in line:
            #define varaible constants
            empty = ' '
            newline = '\n'
            #write to output file
            if letter == empty:
                output.write(empty)
            elif letter == newline:
                output.write(newline)
            else:
                output.write(code[letter])
    #display the encrytion
    print('The file you encryted reads:')
    print()
    #return output to start
    output.seek(0)
    #return output
    return output.read()
    #close all open input files 
    file.close()
    output.close()

#define decrypt function
def decrypt():
	#open inputfile
    codes = open('codes.txt', 'r')
    code = {}
    #condition loop
    for line in codes:
        (key, value) = line.split()
        code[key] = value
    codes.close()
    exception = True
    while exception == True:
        file = input('Please enter name of the file you wish to decrypt (with extension): ')
        try:
            infile = open(file, 'r')
            output = open('decrypted_' + file, 'w+')
            exception = False
        except FileNotFoundError:
            print('Please enter valid file')
    for line in infile:
        for letter in line:
            empty = ' '
            newline = '\n'
            if letter == empty:
                output.write(empty)
            elif letter == newline:
                output.write(newline)
            else:
                output.write(code[letter])
    #disply decryption results 
    print('The file you decryted reads:')
    print()
    output.seek(0)
    return output.read()
    #close all open inputfiles
    file.close()
    output.close()

#call main function
main()



