#Nana Antwi
#CS 21
#Assignment 7
#grades.py 

#design a the print out grades in numbers and letters.

#declare varaibles




#define function
def main():
	myfile = open('grades.dat', "r")
	                                                                  


	#decalare varaibles 
	new_txt = ("F, C, A, C, B, B, D, C, A", '\n') 
	ast_a = ("A: **") 
	ast_b = ("B: **") 
	ast_c = ("C: ***")
	ast_d = ("D: *") 
	ast_f = ("F: *")    

#writing of the new file.
	myfile = grades_out.dat
	grades_out.dat.wirte(new_txt)
	grades_out.dat.write(ast_a)
	grades_out.dat.write(ast_b)
	grades_out.dat.write(ast_c)
	grades_out.dat.write(ast_d)
	grades_out.dat.write(ast_f)
	grades_out.dat.close()
main()
