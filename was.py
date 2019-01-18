#program that writes 1 to 2
#define function
def main():
#information to write to a file
        myfile = open('number.txt', 'w')
        for i in range(1,21):
                #write to file
                myfile.write(str(i)+'\n')
#close file
        myfile.close()
main()
