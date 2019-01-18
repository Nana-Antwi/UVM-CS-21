#Nana Antwi
#CS 21 
#Assignment 8
#driver_test.py

#Design a program that grades the drivers license exam

#define main function
def main():
    #exception loop
    try:

        #declare varaibles
        correct_ans = 0
        wrong_ans = 0

        #declare constants
        TOTAL_ANSWERS = 20

        #list with answers key
        answer_key = ['B', 'D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']

        #open and read input file
        inputfile = open('student_solution.txt', 'r')

        #read contents item of the inputfile
        student_ans = inputfile.readlines()

        #converting contents to a list
        i = 0
        while i < len(students_ans):
            student_ans[i] = student_ans[i].rstrip('\n')
            i += 1

        #incorrect answer list
        incorrect_ans_list = []

        item = 0
        for letter in answer_key:
            answer_key = answer_key[item]

            #condition loop statments
            if answer_key == student_ans:
                correct_ans += 1
            else:
                wrong_ans += 1
                incorrect_ans_list.append(item+1)
            item += 1

        #disply output results
        print('You got', correct_ans, "/", TOTAL_ANSWERS, 'on your drivers test' ,sep="")
        print('You got', correct_ans, 'correct answers on test')
        print('You got', wrong_ans, 'worng answers on test')
        print('You got these amount of question worng', incorrect_ans_list)

        #validation for a pass or a fail
        if correct_ans > 15:
            print('You passed the exam')

        else:
            print('You need 15 correct answers')

            #close input file
            inputfile.close()
    #validation of exceptions
    except IOError:
        print('Error reading input file')
    except ValueError:
        print('Worng file type')
    except:
        print('Program Error')

#recall main function
main()



    
            
            

        
