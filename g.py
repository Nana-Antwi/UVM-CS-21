#Nana Antwi
#CS 21A
#Assignment 7
#grades.py
#design a program that write an inputfile to an outfile with a different file name.

def main():
    # declare variables
    grades = ' '
    letters = ' '
    grade_value = ' '
    grade = 0
    letter_value = ' '
    a = 'A:'
    b = 'B:'
    c = 'C:'
    d = 'D:'
    f = 'F:'
    #exception loop to test condition
    try:
        #open inputfile grades.dat 
        grades = open('grades.dat', 'r')
        #write output file with letters
        letters = open('grades_out.dat', 'w')
        #condition loop statments
        while(grade_value != ''):
            
            grade_value = grades.readline()
            grade_value = grade_value.rstrip('\n')
            grade = grade_value
            if (grade == ''):
                grade = 0.0
 
            #revalidation of condition loop statements
            if (grade == ''):
                grade_value = ''
            if (float(grade) <=100 and float(grade) >=90):
                letter_value = 'A'
                a += '*'
                letters.write(str(letter_value) + '\n')
            elif (float(grade) >= 80):
                letter_value = 'B'
                b += '*'
                letters.write(str(letter_value) + '\n')
            elif (float(grade) >= 70):
                letter_value = 'C'
                c += '*'
                letters.write(str(letter_value) + '\n')
            elif (float(grade) >= 60):
                letter_value = 'D'
                d += '*'
                letters.write(str(letter_value) + '\n')
            elif (float(grade) > 0):
                letter_value = 'F'
                f += '*'
                letters.write(str(letter_value) + '\n')
            else:
                grade_value = ''
            
     
           
            
    except IOError:
        print("There was an error reading the file.")
    except ValueError:
        print("Incorrect values were entered.")
    except:
        print("An error occured.")
    #create new output file 
    letters.write(str(a)+ '\n')            
    letters.write(str(b)+ '\n')
    letters.write(str(c)+ '\n')
    letters.write(str(d)+ '\n')
    letters.write(str(f)+ '\n')
    print("Grades have been written to grades_out.dat as letter grades.")

        
 
    #close input file and outputfile
    grades.close()
    letters.close()
    
main()
