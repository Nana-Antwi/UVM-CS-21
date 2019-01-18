#Nana Antwi
#CS 21
#Assignment 7
#sampleprogram.py

#design a program that writes an inputfile to an output file

#declare varaiables 
name = "Nana Antwi"
course = "CS21"
program = "Sample program"
state_1 = print('This is a sample program')
state_2 = print('Do you remember when this seemed hard?')
state_3 = print('Python is cool!')
user_prompt = (input("Enter a file name called 'sampleprogram.py' : "))


#define fuction
def main():
	try:
		user_prompt == 'sampleprogram.py'
		myfile = open(ln_sampleprogram.txt, "a")
		myfile.write(name)
		myfile.write(course)
		myfile.write(program)
		myfile.write(state_1)
		myfile.write(state_2)
		myfile.write(state_3)

	except ValueError:
		user_prompt != 'sampleprogram.py'
		print("Invalid file name")
		user_prompt = (input("Enter a file name called 'sampleprogram.py' : "))
		user_prompt != "sampleprogram.py"
		print("Program close")
main()
